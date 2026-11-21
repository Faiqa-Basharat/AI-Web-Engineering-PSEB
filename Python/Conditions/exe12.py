# Fare = Rs 100 base + Rs 40 per km. At night (hour 22 or later, or before 6), add 20%. Take the km and the hour (0–23) and print the final fare.

km = float(input("Distance traveled: "))
hours = int(input("Current Hours: "))
fare = 100 + (40 * km)
if hours >= 22 or hours < 6 :
  fare = fare + (fare * 0.2)
print(f"Fare is: {fare} Rs")