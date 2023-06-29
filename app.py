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
        print("Invalid password. Decryption failed.")
        return

    with open(output_file, 'wb') as file:
        file.write(decrypted_text)
        print("File decrypted successfully.")


choice = int(input('What would you like to do?\n1. Encrypt a file.\n2. Decrypt a file.\nChoice: '))
if choice == 1:
    # Example usage:
    password = input("Enter the password: ")
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")
    encrypt_file(password, input_file, output_file)
    print("File encrypted successfully.")
elif choice == 2:
    # To decrypt the file, use the same password:
    password = input("Enter the password to decrypt the file: ")
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to save the decrypted file: ")
    decrypt_file(password, input_file, output_file)
    
