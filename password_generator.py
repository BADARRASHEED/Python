import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "<", ">", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "?"]

print("\n\tWelcome to the Password Generator!\n")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = set({})

for char in range(1, nr_letters + 1):
    password.add(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password.add(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password.add(random.choice(numbers))

password_string = ""

for i in password:
    password_string += i

print(f"Your password is: {password_string}\n")
