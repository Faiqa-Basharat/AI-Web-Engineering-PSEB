# Take a student’s marks out of 100. 40 or above is Pass; below 40 is Fail.


marks = int(input("Enter your marks :"))
if marks < 0 or marks > 100 :
  print("Invalid marks")
elif marks >= 40:
  print("Passed")
elif marks < 40:
  print("Failed")
