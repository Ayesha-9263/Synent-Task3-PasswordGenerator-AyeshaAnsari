# ================================
# Synent Technologies Internship
# Name: Ayesha Ansari
# Task: Task 3 - Password Generator
# ================================

import random
import string

print("\n🔐 Welcome to Secure Password Generator 🔐")


def check_strength(password):
    """Check password strength based on multiple conditions"""
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    elif any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        return "Strong"
    else:
        return "Moderate"


def generate_secure_password():
    """Generate a secure password based on user input"""
    try:
        while True:
            length = int(input("\nEnter password length (min 4): "))
            if length < 4:
                print("❌ Please enter at least 4 characters.")
                continue
            break

        include_symbols = input("Include special characters? (yes/no): ").strip().lower()

        if include_symbols == "yes":
            char_pool = string.ascii_letters + string.digits + string.punctuation
        else:
            char_pool = string.ascii_letters + string.digits

        password_list = [random.choice(char_pool) for _ in range(length)]
        random.shuffle(password_list)
        password = ''.join(password_list)

        print(f"\n✅ Generated Password: {password}")
        print(f"💪 Strength: {check_strength(password)}")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")


def main():
    while True:
        generate_secure_password()
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Exiting Password Generator")
            break


if __name__ == "__main__":
    main()