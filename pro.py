import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','(',')','*','+','@',]

print("Welcome to the pypassword Generator!")
nr_letters = int(input("How many letters would you like to generate?\n"))
nr_numbers = int(input(f"How many numbers would you like to generate?\n"))
nr_symbols = int(input(f"How many symbols would you like to generate?\n"))

#password= ""
#for char in range(0, nr_letters):
    #password += random.choice(letters)

#for num in range(0, nr_numbers):
    #password += random.choice(numbers)

#for symbol in range(0, nr_symbols):
    #password += random.choice(symbols)

#print(password)

#hardlevel

password_list = []
for char in range(0, nr_letters):
     password_list.append(random.choice(letters))

for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your final password:  {password}")