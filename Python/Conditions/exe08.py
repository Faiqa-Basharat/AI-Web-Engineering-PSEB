# Take one character and print whether it is a Vowel, Consonant, Digit or Special character. Hint: .isdigit(), .isalpha(), and .lower() in "aeiou".

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