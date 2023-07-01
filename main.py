import getpass
import myFunctions
choice = int(input('What would you like to do?\n1. Encrypt a file.\n2. Decrypt a file.\nChoice: '))
if choice == 1:
    # Example usage:
    password = getpass.getpass(prompt='Enter your password: ')
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")
    myFunctions.encrypt_file(password, input_file, output_file)
    print("File encrypted successfully.")
elif choice == 2:
    # To decrypt the file, use the same password:
    password = getpass.getpass(prompt='Enter your password: ')
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to save the decrypted file: ")
    myFunctions.decrypt_file(password, input_file, output_file)