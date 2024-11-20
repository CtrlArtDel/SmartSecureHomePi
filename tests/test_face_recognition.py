import unittest
from face_recognition_module import FaceRecognition

class TestFaceRecognition(unittest.TestCase):
    def setUp(self):
        self.recognizer = FaceRecognition({"model_path": "path/to/model"})

    def test_recognize_known_face(self):
        frame = "path/to/test_frame_with_known_face.jpg"
        self.assertTrue(self.recognizer.recognize_face(frame), "Known face should be recognized.")

    def test_recognize_unknown_face(self):
        frame = "path/to/test_frame_with_unknown_face.jpg"
        self.assertFalse(self.recognizer.recognize_face(frame), "Unknown face should not be recognized.")

if __name__ == "__main__":
    unittest.main()

