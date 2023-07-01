from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    # Use the provided password to generate a 32-byte key
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(password, input_file, output_file):
    key = generate_key(password)
    cipher_suite = Fernet(key)

    with open(input_file, 'rb') as file:
        plaintext = file.read()

    encrypted_text = cipher_suite.encrypt(plaintext)

    with open(output_file, 'wb') as file:
        file.write(encrypted_text)

def decrypt_file(password, input_file, output_file):
    key = generate_key(password)
    cipher_suite = Fernet(key)

    with open(input_file, 'rb') as file:
        encrypted_text = file.read()

    try:
        decrypted_text = cipher_suite.decrypt(encrypted_text)
    except:
        print("An error occurred during decryption. The provided password is invalid or the file has been compromised.")
        return
    with open(output_file, 'wb') as file:
        file.write(decrypted_text)
        print("File decrypted successfully.")