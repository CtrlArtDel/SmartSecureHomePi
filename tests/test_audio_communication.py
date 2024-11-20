import unittest
from audio_communication import TwoWayAudio

class TestAudioCommunication(unittest.TestCase):
    def setUp(self):
        self.audio = TwoWayAudio("127.0.0.1", 5000)

    def test_start_audio_stream(self):
        self.assertTrue(self.audio.start_audio_stream(), "Audio stream should start successfully.")

    def test_stop_audio_stream(self):
        self.audio.start_audio_stream()
        self.assertTrue(self.audio.stop_audio_stream(), "Audio stream should stop successfully.")

if __name__ == "__main__":
    unittest.main()

