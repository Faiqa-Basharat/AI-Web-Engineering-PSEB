character = input("Enter value: ")
if len(character) != 1:
  print("Enter only one character")
elif character.isdigit():
  print("Digit")
elif character.isalpha():
  if character.lower() in "aeiou":
   print("Vowel")
  else:
    print("Consonant")
else:
  print("Special Character")