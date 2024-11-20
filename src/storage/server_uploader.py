import requests
import os

class ServerUploader:
    def __init__(self, server_config):
        self.url = server_config['url']
        self.api_key = server_config['api_key']

    def upload(self, file_path):
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return False

        with open(file_path, 'rb') as f:
            response = requests.post(
                self.url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                files={"file": f}
            )
        return response.status_code == 200

