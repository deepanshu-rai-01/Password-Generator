import random
import string

def generate_password(length):
    # All possible characters
    characters = (
        string.ascii_letters +      # a-z A-Z
        string.digits +             # 0-9
        string.punctuation          # !@#$%^&*
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

while True:
    try:
        length = int(input("Enter password length (minimum 6): "))

        if length < 6:
            print("Password length should be at least 6.\n")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        choice = input("\nGenerate another password? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.\n")
