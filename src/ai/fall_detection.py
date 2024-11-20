import cv2
import numpy as np
from tensorflow.keras.models import load_model

class FallDetection:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def detect_fall(self, frame):
        # Preprocess frame for fall detection model
        resized_frame = cv2.resize(frame, (224, 224))  # Adjust to your model's input size
        normalized_frame = resized_frame / 255.0
        input_data = np.expand_dims(normalized_frame, axis=0)

        # Predict fall
        predictions = self.model.predict(input_data)
        if predictions[0][0] > 0.5:  # Assuming binary classification (0 = no fall, 1 = fall)
            return True
        return False


