# first step need to install --> pip install cryptography
import os

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode

def encrypt(plaintext, password):
    # Derive a key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=b'salt_value',  # You should use a random and unique salt
        iterations=100000,
        length=32  # Length of the derived key in bytes
    )
    key = urlsafe_b64encode(kdf.derive(password.encode()))

    # Generate a random IV (Initialization Vector)
    iv = urlsafe_b64encode(os.urandom(16))

    # Encrypt the message using AES in GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()

    # Concatenate IV and ciphertext
    return iv + ciphertext

def decrypt(ciphertext, password):
    # Extract IV and ciphertext from the input
    iv = ciphertext[:24]  # 16 bytes for IV + 8 bytes for GCM tag
    ciphertext = ciphertext[24:]

    # Derive the key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=b'salt_value',  # Use the same salt as in the encryption process
        iterations=100000,
        length=32
    )
    key = urlsafe_b64encode(kdf.derive(password.encode()))

    # Decrypt the message using AES in GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext.decode()

# Example usage
plaintext_message = "Hello, cryptography!"
password = "super_secure_password"

encrypted_message = encrypt(plaintext_message, password)
decrypted_message = decrypt(encrypted_message, password)

print(f"Original Message: {plaintext_message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")