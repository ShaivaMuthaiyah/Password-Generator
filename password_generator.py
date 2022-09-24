
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random.seed(nr_letters )

first_part = ""
second_part = ""
third_part = ""

for l in range(1,nr_letters+1) :
	
	first_part += random.choice(letters)
		
for s in range(1,nr_symbols+1) :
	
	second_part += random.choice(symbols)

for n in range(1,nr_numbers+1) :
	
	third_part += random.choice(numbers)

password = first_part+second_part+third_part

shuffled_password = list(password)

random.shuffle(shuffled_password)

print("Your password is: "+''.join(shuffled_password))


