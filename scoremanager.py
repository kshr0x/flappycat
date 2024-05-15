from cryptography.fernet import Fernet
import os

class ScoreManager:
    def __init__(self, result_dir='result', score_file='high_score.enc', key_file='encryption_key.key'):
        self.result_dir = result_dir
        os.makedirs(self.result_dir, exist_ok=True)
        self.score_file = os.path.join(self.result_dir, score_file)
        self.key_file = os.path.join(self.result_dir, key_file)
        self.encryption_key = self.load_encryption_key()

    def load_encryption_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        else:
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        return key

    def encrypt_high_score(self, score):
        fernet = Fernet(self.encryption_key)
        return fernet.encrypt(str(score).encode())

    def decrypt_high_score(self, encrypted_score):
        fernet = Fernet(self.encryption_key)
        try:
            return int(fernet.decrypt(encrypted_score).decode())
        except:
            return 0

    def load_high_score(self):
        if os.path.exists(self.score_file):
            with open(self.score_file, 'rb') as file:
                encrypted_score = file.read()
                return self.decrypt_high_score(encrypted_score)
        return 0

    def save_high_score(self, score):
        encrypted_score = self.encrypt_high_score(score)
        with open(self.score_file, 'wb') as file:
            file.write(encrypted_score)
