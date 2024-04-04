from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings

class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passwords')
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    encrypted_password = models.BinaryField(null = True)
    decrypted_password = models.CharField(max_length=255, null=True, blank=True)  # New field for decrypted password

    @property
    def password(self):
        key = settings.ENCRYPTION_KEY.encode()
        cipher_suite = Fernet(key)
        try:
            return cipher_suite.decrypt(self.encrypted_password).decode()
        except Exception as e:
            print(f"Error decrypting password: {e}")
            return "Decryption failed"

    @password.setter
    def password(self, value):
        key = settings.ENCRYPTION_KEY.encode()
        cipher_suite = Fernet(key)
        self.encrypted_password = cipher_suite.encrypt(value.encode())

     
    def save(self, *args, **kwargs):
        key = settings.ENCRYPTION_KEY.encode()
        cipher_suite = Fernet(key)
        try:
            self.decrypted_password = cipher_suite.decrypt(self.encrypted_password).decode()
            self.encrypted_password = cipher_suite.encrypt(self.encrypted_password.encode())
        except Exception as e:
            print(f"Error decrypting password: {e}")
            self.encrypted_password = "Encryption failed"
            self.decrypted_password = "Decryption failed"
        
        super(Password, self).save(*args, **kwargs)