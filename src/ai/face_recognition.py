import cv2
import os

class FaceRecognition:
    def __init__(self, face_data_path):
        self.face_data_path = face_data_path
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.known_faces = self.load_known_faces()

    def load_known_faces(self):
        # Load face encodings from the training dataset
        known_faces = {}
        for file in os.listdir(self.face_data_path):
            if file.endswith(".jpg") or file.endswith(".png"):
                img = cv2.imread(os.path.join(self.face_data_path, file))
                encoding = self.encode_face(img)
                known_faces[file] = encoding
        return known_faces

    def encode_face(self, img):
        # Convert to grayscale and encode
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.Laplacian(gray, cv2.CV_64F).var()

    def detect_faces(self):
        # Capture a frame and detect unknown faces
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if not ret:
            return False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face = frame[y:y + h, x:x + w]
            encoding = self.encode_face(face)
            if not self.is_known_face(encoding):
                return True  # Unknown face detected
        return False

    def is_known_face(self, encoding):
        for known_encoding in self.known_faces.values():
            if abs(known_encoding - encoding) < 10:  # Threshold for matching
                return True
        return False

