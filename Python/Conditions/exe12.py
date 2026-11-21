km = float(input("Distance traveled: "))
hours = int(input("Current Hours: "))
fare = 100 + (40 * km)
if hours >= 22 or hours < 6 :
  fare = fare + (fare * 0.2)
print(f"Fare is: {fare} Rs")