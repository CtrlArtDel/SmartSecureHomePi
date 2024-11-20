import smtplib
from email.mime.text import MIMEText

class Notifier:
    def __init__(self, notification_config):
        self.method = notification_config['method']
        self.email_config = notification_config['email']

    def send_alert(self, video_path):
        if self.method == "email":
            self.send_email(video_path)

    def send_email(self, video_path):
        msg = MIMEText(f"Motion detected. Video saved at: {video_path}")
        msg['Subject'] = 'Security Alert'
        msg['From'] = self.email_config['sender']
        msg['To'] = self.email_config['recipient']

        with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['port']) as server:
            server.starttls()
            server.login(self.email_config['sender'], self.email_config['password'])
            server.send_message(msg)

