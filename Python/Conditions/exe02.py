# Take a person’s age. At 18 or above, print “Eligible to vote”. Otherwise, print how many years are left.


age = int(input("enter your age :"))
newAge = 0
if age >= 18:
  print("He is eligible")
elif age <18 : 
  newAge = 18 - age 
  print("Years to go:", newAge)
  if newAge == 1:
    print

