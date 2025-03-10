import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

# User input
if __name__ == "__main__":
    while True:
        clear_screen()
        mode = input("Do you want to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
            input("Press Enter to continue...")
            continue

        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Please enter a valid integer for the shift value.")
            input("Press Enter to continue...")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"{mode.capitalize()}ed text: {result}\n")

        again = input("Do you want to try again? (yes/no): ").strip().lower()
        if again != 'yes':
            break
