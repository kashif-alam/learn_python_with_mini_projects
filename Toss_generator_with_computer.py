import random
# random_number = random.randint(10, 20)
# print(f"Random number: {random_number}")

# random_float= random.random()
# random_float_num = random_float *5
# print(f"Random float number: {random_float_num}")
# num = 0.9999999 * 5
# print(num)


head_tail=input("head or tail?" + " ").lower()
print(f"You choose {head_tail}")

random_num = random.randint(0,1)
print(random_num)

if(random_num == 0) & (head_tail == "tail"):
  print("You won")
elif(random_num == 1) & (head_tail == "head"):
  print("You won")
else:
  print("You lose")