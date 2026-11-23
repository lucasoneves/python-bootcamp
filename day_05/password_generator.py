import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&']

print("Welcome to password generator!")

quantity_letters = int((input("Quantas letras quer na senha? \n")))
quantity_numbers = int((input("Quantos números? \n")))
quantity_symbols = int((input("Quantos símbolos? \n")))

final_password = []

for letter_password in range(0, quantity_letters):
    final_password.append(random.choice(letters))

for char in range(0, quantity_numbers):
    final_password.append(random.choice(numbers))
    
for char in range(0, quantity_numbers):
    final_password.append(random.choice(symbols))
    
random.shuffle(final_password)