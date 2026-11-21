bill = int(input("Enter bill amount :"))
discount = 0
if bill >= 5000:
  discount = bill * 0.10
  print(f"Your bill is: {bill}")
elif bill > 2000 and bill < 5000:
  discount = bill * 0.05
  print("Your bill is :", discount)
else:
  print("Your amount is :", bill)