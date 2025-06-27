import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
easy_or_hard=int(input(f"Enter 0 for Easy and 1 for hard password: "))

password = ""
if easy_or_hard == 0:
#Easy Level
    for l in range(0, nr_letters):
        password += random.choice(letters)
    for s in range(0, nr_symbols):
        password += random.choice(symbols)
    for n in range(0, nr_numbers):
        password += random.choice(numbers)
else:
#Hard Level
    pass_keys = []
    for l in range(0, nr_letters):
        pass_keys.append(random.choice(letters))
    for s in range(0, nr_symbols):
        pass_keys.append(random.choice(symbols))
    for n in range(0, nr_numbers):
        pass_keys.append(random.choice(numbers))
    random.shuffle(pass_keys)
    for keys in pass_keys:
        password += keys

print(f"Here is your password: {password}")
