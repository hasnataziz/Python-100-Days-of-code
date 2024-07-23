import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pasword = ""

print("Welcome to the easy PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
for num in range(0,nr_letters):
    pasword += random.choice(letters)
nr_symbols = int(input(f"How many symbols would you like?\n"))
for num in range(0,nr_symbols):
    pasword+=random.choice(symbols)
nr_numbers = int(input(f"How many numbers would you like?\n"))
for num in range(0,nr_numbers):
    pasword += random.choice(numbers)
print(pasword)
pasword = []

print("Welcome to the hard PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
for num in range(0,nr_letters):
    pasword += random.choice(letters)
nr_symbols = int(input(f"How many symbols would you like?\n"))
for num in range(0,nr_symbols):
    pasword+=random.choice(symbols)
nr_numbers = int(input(f"How many numbers would you like?\n"))
for num in range(0,nr_numbers):
    pasword += random.choice(numbers)
random.shuffle(pasword)
password_string = ""
for char in pasword:
    password_string+=char
print(f"Your password is {password_string}")
