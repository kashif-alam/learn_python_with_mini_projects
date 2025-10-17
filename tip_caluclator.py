#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#input("Welcome to the tip calculator!")
bill = input(" Welcome to the tip calculator!\n What was the total bill?" +
             "  ")
tip_percentage = input("How much would you like to tip? 10, 12, or 15? " + " ")
total_num_people = input("How many people to split the bill? " + " ")
tip_percentage_as_float = (float(tip_percentage) / 100) * float(bill)
total_bill = float(bill) + tip_percentage_as_float
bill_each_person =format( total_bill / int(total_num_people) , '.2f')
print(f"Each person should pay: ${bill_each_person}")


