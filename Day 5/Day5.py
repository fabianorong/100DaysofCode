import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
qnty_letters = int(input("How many letters would you like in your password?\n"))
qnty_symbols = int(input("How many symbols would you like?\n"))
qnty_numbers = int(input("How many numbers would you like?\n"))

password = []
q_letters = 0
q_numbers = 0
q_symbols = 0

while q_letters < qnty_letters:
    q_letters += 1
    password.append(random.choice(letters))

while q_numbers < qnty_numbers:
    q_numbers += 1
    password.append(random.choice(numbers))

while q_symbols < qnty_symbols:
    q_symbols += 1
    password.append(random.choice(symbols))
    
random.shuffle(password)
separator =''
passwordresult = separator.join(password)
print (f"Here is your password: {passwordresult}")
