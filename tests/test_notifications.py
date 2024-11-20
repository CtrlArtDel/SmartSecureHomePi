import unittest
from notifications import Notifier

class TestNotifications(unittest.TestCase):
    def setUp(self):
        self.notifier = Notifier({"email": {}, "telegram": {}})

    def test_send_email(self):
        result = self.notifier.send_email("Test Subject", "Test Body", ["test_attachment.txt"])
        self.assertTrue(result, "Email notification should be sent successfully.")

    def test_send_telegram(self):
        result = self.notifier.send_telegram("Test Message")
        self.assertTrue(result, "Telegram notification should be sent successfully.")

if __name__ == "__main__":
    unittest.main()

