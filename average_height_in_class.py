# my_list = [1, 2, 3, 4, 5]
# for number in my_list:
#   # print(number)
#   print(f'The number is {number}')

students_heights = input("Input a list of student heights ").split()

for n in range(0, len(students_heights)) :
  students_heights[n] = int(students_heights[n])
# print(students_heights)
total_height = 0
for height in students_heights:
  print(height)
  total_height += height 
# print(height)

number_of_student = len(students_heights)
average_height = int(total_height / number_of_student)

print(total_height)
print(number_of_student)
print(average_height)

