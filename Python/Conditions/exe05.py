# Take the temperature in °C and print the advice. Temperature (°C) Print Below 10 10 to 25 26 to 35 Cold, wear a jacket Pleasant Warm Above 35 Very hot, stay hydrated


temp = int(input("Enter temperature :"))
if temp < 10 :
  print("Cold, wear a jacket")
elif temp >= 10 and temp <= 25 :
  print("Pleasant")
elif temp >= 25 and temp <= 35 :
  print("warm")
elif temp > 35 :
  print("Very hot, stay hydrated")