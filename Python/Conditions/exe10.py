balance = int(input("Enter mobile balance: "))
price = int(input("Enter price: "))

if balance < price:
  needed = price - balance
  print(f"Balance is insufficient, need Rs {needed} more.")
else:
  remaining = balance - price 
  print(f"Balance activated,\nRemaining balance is: {remaining} ")