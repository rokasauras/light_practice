import random
import string

def random_password(length, use_punctuation=True):
    """Generates a random password of specified length."""
    characters = string.ascii_letters + string.digits
    if use_punctuation:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    password_length = int(input("Enter the password length: "))
    include_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == 'yes'
    print("Generated password:", random_password(password_length, include_punctuation))
