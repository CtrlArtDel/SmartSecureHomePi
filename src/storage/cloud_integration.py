import boto3
from googleapiclient.discovery import build
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import requests

class CloudIntegration:
    def __init__(self, config):
        self.config = config
        self.s3_client = None
        self.google_drive = None
        self.nextcloud_url = config.get('nextcloud_url')
        self.nextcloud_user = config.get('nextcloud_user')
        self.nextcloud_password = config.get('nextcloud_password')

        # AWS S3 Setup
        if 'aws' in config:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=config['aws']['access_key'],
                aws_secret_access_key=config['aws']['secret_key']
            )

        # Google Drive Setup
        if 'google' in config:
            gauth = GoogleAuth()
            gauth.LoadCredentialsFile(config['google']['credentials'])
            self.google_drive = GoogleDrive(gauth)

    def upload_to_s3(self, file_path, bucket_name):
        try:
            file_name = os.path.basename(file_path)
            self.s3_client.upload_file(file_path, bucket_name, file_name)
            print(f"Uploaded {file_name} to S3 bucket {bucket_name}")
        except Exception as e:
            print(f"Error uploading to S3: {e}")

    def upload_to_google_drive(self, file_path, folder_id):
        try:
            file_name = os.path.basename(file_path)
            file = self.google_drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
            file.SetContentFile(file_path)
            file.Upload()
            print(f"Uploaded {file_name} to Google Drive folder {folder_id}")
        except Exception as e:
            print(f"Error uploading to Google Drive: {e}")

    def upload_to_nextcloud(self, file_path):
        try:
            file_name = os.path.basename(file_path)
            with open(file_path, 'rb') as file:
                response = requests.put(
                    f"{self.nextcloud_url}/remote.php/dav/files/{self.nextcloud_user}/{file_name}",
                    auth=(self.nextcloud_user, self.nextcloud_password),
                    data=file
                )
            if response.status_code == 201:
                print(f"Uploaded {file_name} to Nextcloud")
            else:
                print(f"Error uploading to Nextcloud: {response.status_code}")
        except Exception as e:
            print(f"Error uploading to Nextcloud: {e}")

