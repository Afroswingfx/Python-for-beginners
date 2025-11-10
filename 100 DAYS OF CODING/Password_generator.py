#Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# passl=random.sample(letters,nr_letters)
# pass_s=random.sample(symbols,nr_symbols)
# pass_n=random.sample(numbers,nr_numbers)
# lp=nr_numbers+nr_symbols+nr_letters
# print(lp)
# new_list=letters+numbers+symbols
# #print(new_list)
# #
# Password=(passl+pass_n+pass_s)
# random.shuffle(Password)
# #print(Password)
# password_string = ''.join(Password)
# print(f"Password is {password_string}")
#EASY LEVEL
password_list=[]
for char_n in range (1,nr_numbers +1):
    random_char_n=random.choice(numbers)
    password_list+=random_char_n
for char_s in range(1,nr_symbols+1):
    random_char_s=random.choice(symbols)
    password_list+=random_char_s
for char_l in range (1, nr_letters+1):
    random_char_l=random.choice(letters)
    password_list+=random_char_l
print(password_list)
random.shuffle(password_list)
print(password_list)
Passkey= ""
for char in password_list:
    Passkey+=char
print(f"Your Passkey is: {Passkey}")





