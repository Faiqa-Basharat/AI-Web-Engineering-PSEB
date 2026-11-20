#Exercise 1: City list cities = ["Lahore", "Karachi", "Multan", "Quetta", "Peshawar"] Print the first city, the last city, the middle three cities (using slicing) and the whole list reversed. Expected: 

cities = ["Lahore", "Karachi", "Multan", "Quetta", "Peshawar"]
print(cities[0])
print(cities[-1])
print(cities[1:4])
print(cities[::-1])

#Exercise 2: Marks report marks = [78, 92, 65, 88, 54] Print the total, the average, the highest, the lowest, and how many marks are above 70 (use a loop). 
marks = [78, 92, 65, 88, 54]
print(sum(marks))
print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))

newMarks = []

for mark in marks:
  if mark >= 70:
    newMarks.append(mark)
print(len(newMarks))


#Exercise 3: Shopping list Start with ["bread", "milk", "eggs"]. Then: ● append "rice" ● insert "sugar" at index 1 ● remove "milk" ● pop() the last item and print what was popped 
shopping_list = ["bread", "milk", "eggs"]
print(shopping_list)
shopping_list.append("suger")
shopping_list.insert(1, "butter")
shopping_list.remove("milk")
shopping_list.pop()
print(shopping_list)

#Exercise 4: Remove duplicates nums = [3, 1, 3, 2, 1, 5] Make a new list without duplicates, keeping the original order. Use a loop and not in, not set(). 
number = [3, 1, 3, 2, 1, 5]
unique_num = []
for num in number:
  if num not in unique_num:
    unique_num.append(num)
print(unique_num)

#Exercise 5: Even and odd Using list comprehension, make two lists from the numbers 1 to 15: one with the even numbers and one with the odd numbers. 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = []
odd_num = []
for num in nums:
  if num % 2 == 0:
    even_num.append(num)
  else:
    odd_num.append(num)
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)

# Exercise 6: rotate
r = [1, 2, 3, 4, 5] 
rotate = r[2:] + r[:2]
print(rotate)

# Exercise 7:append
a = [1, 2, 3]
b  = a
c = a.copy()
a.append(4)
print(a, b, c)
# b change because it is a shallow copy that points to same value as a like a shared memory or space but c is a deep copy that has same value but not memory location

# Tuple
# Exercise 8: Student record student = ("BSIT-12", "Sara", 88) 1. Unpack it into roll_no, name, marks and print each one with an f-string. 2. Try student[2] = 95 and write down the error you get. 3. Now update the marks the correct way: convert the tuple to a list, change the marks, then convert it back to a tuple. 
student = ("BSIT-12", "Sara", 88) 
rollno, name, marks = student
print(f"Name is:", name)
print(f"Roll no is:", rollno)
print(f"Marks are:", marks)
# converting tuple to list
students = list(student)
students[2] = 95
student = tuple(students)
print(student) 

# student[2] = [95]  got a type error 
# print(student)

#Exercise 9: Vote counter votes = ("A", "B", "A", "C", "A", "B") Use count() to count the votes for A, B and C, and index() to find the position of the first "C". 
votes = ("A", "B", "A", "C", "A", "B") 
print(votes.count("A"))
print(votes.count("B"))
print(votes.count("C"))
first_c = votes.index("C")
print(first_c)

# list of tuples
#Exercise 10: List of tuples students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)] 1. Loop through the list and print each student as Ali scored 85. 2. Find the topper. 3. Make a list of the names of students who passed (marks 70 or above). 
students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)] 
topper = students [0]
for name, marks in students:
      print(f"Name:", name, "Marks:", marks)
      if marks > topper[1]:
          topper = (name, marks)
print(topper)

passed_students = []
for name, marks in students:
    if marks >= 70 :
      passed_students.append(name)
print(passed_students)


# finding second highest
# Exercise 11: Second highest scores = [45, 82, 67, 91, 73] Find the second highest score with a loop only. Don't use sort() or max().
scores = [45, 82, 67, 91, 73] 
second_highest = scores[0]
for marks in scores:
    if marks < len(scores):
     second_highest.append(marks)
print(second_highest)
