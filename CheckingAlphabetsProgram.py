# Asks a input from the user for a chracter
character = input("Enter a character to check if it's an alphabet: ")

# Determines whether it's a single character and an alphabet
if len(character) == 1 and character.isalpha():
   print(character, "is an alphabet.")
else:
   print(character, "is not an alphabet.")
