# File Encryption and Decryption App

This Python application allows you to encrypt and decrypt files using the Fernet encryption algorithm from the `cryptography` library. It provides a simple command-line interface for encrypting and decrypting files.

## Prerequisites

Before using this application, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- The `cryptography` library installed. You can install it using the following command:

  ```shell
  pip install cryptography
  ```

## Usage

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the application files are located.

3. Run the `app.py` script using the following command:

   ```shell
   python app.py
   ```

4. The application will prompt you to choose an operation:

   ```shell
   What would you like to do?
   1. Encrypt a file.
   2. Decrypt a file.
   Choice:
   ```

   Enter `1` to encrypt a file or `2` to decrypt a file.

5. If you choose to encrypt a file:

   - Enter a password when prompted. This password will be used to generate an encryption key.
   - Enter the path to the input file that you want to encrypt.
   - Enter the path where you want to save the encrypted output file.

   ```shell
   Enter the password: [password]
   Enter the path to the input file: [input_file_path]
   Enter the path to the output file: [output_file_path]
   ```

   The application will encrypt the file and save the encrypted version to the specified output file path.

6. If you choose to decrypt a file:

   - Enter the password that was used to encrypt the file.
   - Enter the path to the input file that you want to decrypt.
   - Enter the path where you want to save the decrypted output file.

   ```shell
   Enter the password to decrypt the file: [password]
   Enter the path to the input file: [input_file_path]
   Enter the path to save the decrypted file: [output_file_path]
   ```

   The application will decrypt the file and save the decrypted version to the specified output file path.

## Example

Here's an example usage of the application:

```shell
What would you like to do?
1. Encrypt a file.
2. Decrypt a file.
Choice: 1

Enter the password: mypassword
Enter the path to the input file: /path/to/input/file.txt
Enter the path to the output file: /path/to/output/encrypted_file.txt

File encrypted successfully.
```

```shell
What would you like to do?
1. Encrypt a file.
2. Decrypt a file.
Choice: 2

Enter the password to decrypt the file: mypassword
Enter the path to the input file: /path/to/input/encrypted_file.txt
Enter the path to save the decrypted file: /path/to/output/decrypted_file.txt

File decrypted successfully.
```

## Security Considerations

- It's important to remember and protect the password used for encryption and decryption. Losing the password will result in permanent data loss.
- Ensure that the encrypted files and the password are stored securely to prevent unauthorized access.

## License

This application is released under the [MIT License](LICENSE).

## Acknowledgments

This application uses the [cryptography](https://cryptography.io/en/latest/) library for file encryption and decryption.
