import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    if length > 4:
        password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]
num_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the length of the passwords: "))
if password_length < 4:
    print("Password length should be at least 4 to ensure security.")
else:
    passwords = generate_passwords(num_passwords, password_length)
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")
