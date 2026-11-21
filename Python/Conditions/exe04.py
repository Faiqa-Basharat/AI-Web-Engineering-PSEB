# Check whether a number is divisible by both 5 and 11. Use % and and.


num = int(input("Enter a number :"))
if num % 5 and num % 11:
  print("It is divisible")
else:
  print("Not divisible by 5 and 11")
