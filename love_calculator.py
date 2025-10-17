print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")  
name2 = input("What is their name?")  
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = int(lower_case_string.count("t"))
print(f"t occur {t} times")
r = int(lower_case_string.count("r"))
print(f"r occur {r} times")
u = int(lower_case_string.count("u"))
print(f"u occur {u} times")
e = int(lower_case_string.count("e"))
print(f"e occur {e} times")
l = int(lower_case_string.count("l"))
print(f"l occur {l} times")
o = int(lower_case_string.count("o"))
print(f"o occur {o} times")
v = int(lower_case_string.count("v"))
print(f"v occur {v} times")
e = int(lower_case_string.count("e"))
print(f"e occur {e} times")

true_score = t + r + u + e
love_score = l + o + v + e

total_score = str(true_score) + str(love_score)
score = int(total_score)
print(score)

print(f"your total score is {total_score}")
if(score <= 10) or (score >= 90) :
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

#Pierre Curie
#Marie Curie