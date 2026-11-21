bill = int(input("Enter bill amount :"))
discount = 0
if bill >= 5000:
  discount = bill % 10
  print("Your bill is :")
elif bill > 2000 and bill < 5000:
  discount = bill % 5
  print("Your bill is :")
elif bill < 2000:
  print("Your amount is :", bill)