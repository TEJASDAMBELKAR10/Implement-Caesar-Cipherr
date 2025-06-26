def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'E':
        result = caesar_cipher_encrypt(message, shift)
        print(f"\nEncrypted message: {result}")
    else:
        result = caesar_cipher_decrypt(message, shift)
        print(f"\nDecrypted message: {result}")

if __name__ == "__main__":
    main()
