import unittest
from motion_detection import MotionDetector

class TestMotionDetection(unittest.TestCase):
    def setUp(self):
        self.detector = MotionDetector({"sensitivity": 0.5})

    def test_motion_detected(self):
        self.assertTrue(self.detector.detect_motion(), "Motion should be detected.")

    def test_no_motion_detected(self):
        # Simulate no motion case
        self.detector.reset()
        self.assertFalse(self.detector.detect_motion(), "No motion should be detected.")

if __name__ == "__main__":
    unittest.main()

