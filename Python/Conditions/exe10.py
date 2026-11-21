# Take the balance and the package price. If the balance is enough, print “Package activated” and the remaining balance. Otherwise, print how much more is needed.

balance = int(input("Enter mobile balance: "))
price = int(input("Enter price: "))

if balance < price:
  needed = price - balance
  print(f"Balance is insufficient, need Rs {needed} more.")
else:
  remaining = balance - price 
  print(f"Balance activated,\nRemaining balance is: {remaining} ")