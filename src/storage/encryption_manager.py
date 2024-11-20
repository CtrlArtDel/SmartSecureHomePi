from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = self.fernet.encrypt(file.read())
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        with open(file_path, 'wb') as file:
            file.write(self.fernet.decrypt(encrypted_data))

