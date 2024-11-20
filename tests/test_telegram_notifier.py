import unittest
from notifiers.telegram_notifier import TelegramNotifier

class TestTelegramNotifier(unittest.TestCase):
    def setUp(self):
        self.notifier = TelegramNotifier(api_token="TEST_TOKEN", chat_id="TEST_CHAT_ID")

    def test_send_message(self):
        try:
            self.notifier.send_message("Test message")
        except Exception as e:
            self.fail(f"send_message raised an exception: {e}")

    def test_send_file(self):
        try:
            self.notifier.send_file("path/to/test_file.jpg", caption="Test file")
        except Exception as e:
            self.fail(f"send_file raised an exception: {e}")

