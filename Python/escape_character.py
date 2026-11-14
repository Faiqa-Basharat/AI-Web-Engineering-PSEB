# \r is a carriage return. It moves the cursor to the beginning of the line without advancing to the next line. In this case, "World" will overwrite "Hello" when printed.
a = "Hello \rWorld"
print(a)

# \n is a newlie character
a = "Hello \nWorld"
print(a)

# \t is a tab character. It adds a horizontal tab space in the string.
a = " Hello \tWorld"
print(a)

# \b is a backspace character. It removes the character before it in the string.
a = "Hellop\b World"
print(a)

# \f is a form feed character.It will create a new line after "Hello". Will give 4 spaces
a = "Hello \fMartha here!"
print(a)

