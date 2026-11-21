# A student is eligible if (Matric 60% or above and Inter 50% or above), or Entry test 70 or above. Take all three and print Eligible or Not eligible.

matric = int(input("Enter matric percentaage: "))
intermediate = int(input("Enter FSc. percentaage: "))
entry_test_marks = int(input("Enter entry test marks: "))
if matric >= 60 or intermediate >= 50 or entry_test_marks >= 70:
  print("Student is eligible")
else:
  print("Ineligible for admission")