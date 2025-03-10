from colorama import Fore, Style
import re

def check_password_strength(password):
    strength_criteria = [
        len(password) >= 8,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    ]

    score = sum(strength_criteria)

    if score == 5:
        print(Fore.GREEN + "[✔] Strong Password! Great job!" + Style.RESET_ALL)
    elif score >= 3:
        print(Fore.YELLOW + "[⚠️] Medium Password. Consider improving it." + Style.RESET_ALL)
    else:
        print(Fore.RED + "[❌] Weak Password! Please make it stronger." + Style.RESET_ALL)

    print("Criteria for Strong Password:")
    print(Fore.GREEN if strength_criteria[0] else Fore.RED, "✔ Minimum 8 characters", Style.RESET_ALL)
    print(Fore.GREEN if strength_criteria[1] else Fore.RED, "✔ At least one uppercase letter", Style.RESET_ALL)
    print(Fore.GREEN if strength_criteria[2] else Fore.RED, "✔ At least one lowercase letter", Style.RESET_ALL)
    print(Fore.GREEN if strength_criteria[3] else Fore.RED, "✔ At least one number", Style.RESET_ALL)
    print(Fore.GREEN if strength_criteria[4] else Fore.RED, "✔ At least one special character", Style.RESET_ALL)

if __name__ == "__main__":
    from colorama import init
    init(autoreset=True)  # Ensures colors reset automatically

    password = input("Enter your password to check its strength: ")
    check_password_strength(password)