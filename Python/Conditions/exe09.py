a = int(input("Enter first side of triangle:"))
b = int(input("Enter second side of triangle:"))
c = int(input("Enter third side of triangle:"))
if a + b <= c or a+c <= b or b+c <= a :
  print("Invalid triangle")
elif a == b == c:
  print("Equiletral Triangle")
elif a == b or a == c or b == c:
  print("Isoceles Triangle")
else:
  print("Scalene")