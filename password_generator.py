import random
import string

def generate_password(length, use_digits=True, use_punctuation=True, use_uppercase=True):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = input("How long would you like your password to be? (Please enter a whole numerical value): ")
password = generate_password(int(password_length))
print(password)