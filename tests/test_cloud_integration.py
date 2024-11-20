import unittest
from cloud_integration import CloudIntegration

class TestCloudIntegration(unittest.TestCase):
    def setUp(self):
        self.cloud = CloudIntegration({"aws": {}, "google": {}, "nextcloud": {}})

    def test_upload_to_s3(self):
        result = self.cloud.upload_to_s3("path/to/test_file.mp4", "test_bucket")
        self.assertTrue(result, "File should be uploaded to S3.")

    def test_upload_to_google_drive(self):
        result = self.cloud.upload_to_google_drive("path/to/test_file.mp4", "test_folder_id")
        self.assertTrue(result, "File should be uploaded to Google Drive.")

    def test_upload_to_nextcloud(self):
        result = self.cloud.upload_to_nextcloud("path/to/test_file.mp4")
        self.assertTrue(result, "File should be uploaded to Nextcloud.")

if __name__ == "__main__":
    unittest.main()

