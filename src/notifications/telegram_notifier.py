import logging
from telegram import Bot

class TelegramNotifier:
    def __init__(self, api_token, chat_id):
        self.bot = Bot(token=api_token)
        self.chat_id = chat_id
        self.logger = logging.getLogger("TelegramNotifier")

    def send_message(self, message):
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
            self.logger.info("Telegram notification sent successfully.")
        except Exception as e:
            self.logger.error(f"Failed to send Telegram notification: {e}")

    def send_file(self, file_path, caption=""):
        try:
            with open(file_path, 'rb') as file:
                self.bot.send_document(chat_id=self.chat_id, document=file, caption=caption)
            self.logger.info(f"File sent to Telegram successfully: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to send file via Telegram: {e}")

