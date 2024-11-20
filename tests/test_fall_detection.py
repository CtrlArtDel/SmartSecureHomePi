import unittest
from fall_detection import FallDetection

class TestFallDetection(unittest.TestCase):
    def setUp(self):
        self.detector = FallDetection("models/fall_detection.tflite")

    def test_detect_fall(self):
        frame = "path/to/test_frame_with_fall.jpg"
        self.assertTrue(self.detector.detect_fall(frame), "Fall should be detected.")

    def test_no_fall(self):
        frame = "path/to/test_frame_without_fall.jpg"
        self.assertFalse(self.detector.detect_fall(frame), "No fall should be detected.")

if __name__ == "__main__":
    unittest.main()

