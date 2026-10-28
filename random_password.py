
import random
import string

print("WELCOME TO RANDOM PASSWORD GENERATOR")

length = int(input("Enter password length: "))
if length <= 0:
    print("Password length should be greater than 0.")
    exit()
else:
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    symbol = random.choice(string.punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = uppercase + lowercase + number + symbol

for i in range(length - 4):
    password = password + random.choice(characters)

print("Your generated password is:", password)
