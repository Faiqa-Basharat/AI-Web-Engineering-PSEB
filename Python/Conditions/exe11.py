matric = int(input("Enter matric percentaage: "))
intermediate = int(input("Enter FSc. percentaage: "))
entry_test_marks = int(input("Enter entry test marks: "))
if matric >= 60 or intermediate >= 50 or entry_test_marks >= 70:
  print("Student is eligible")
else:
  print("Ineligible for admission")