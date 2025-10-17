#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letter = ""
for i in range(0, nr_letters):
  letter_index  = random.randint(0, len(letters)-1)
  random_letter += letters[letter_index] 
# print(random_letter)
random_symbol = ""
for i in range(0,nr_symbols):
  symbol_index = random.randint(0, len(symbols)-1)
  random_symbol += symbols[symbol_index]
# print(random_symbol)
random_number = ""
for i in range(0, nr_numbers):
  number_index = random.randint(0, len(numbers)-1)
  random_number += numbers[number_index]
# print(random_number)

final_password = random_letter + random_symbol + random_number
print(final_password)

num_words_in_final = int(len(final_password))
print(num_words_in_final)

strong_password = ""
for i in range(0, num_words_in_final):
  random_word = random.randint(0, num_words_in_final-1)
  strong_password += final_password[random_word]
print(strong_password)
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P