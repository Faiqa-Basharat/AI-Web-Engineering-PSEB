# Take a number from 1 to 7 and print the day (1 = Monday … 7 = Sunday). Any other number prints “Invalid day”.


num = int(input("Enter number :"))
if num > 7 and num < 1 :
 print("Invalid number")
elif num == 1:
 print("Monday")
elif num == 2:
 print("Tuesday")
elif num == 3:
 print("Wednesday")
elif num == 4:
 print("Thursday")
elif num == 5:
 print("Friday")
elif num == 6:
 print("Saturday")
elif num == 7:
 print("Sunday")