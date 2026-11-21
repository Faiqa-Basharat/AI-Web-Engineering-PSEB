# Take the bill amount and print the discount and the final amount. Bill (Rs) Discount 5000 or more 10% 2000 to 4999 5% Below 2000 None


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