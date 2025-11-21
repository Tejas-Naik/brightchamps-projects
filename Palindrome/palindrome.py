# REVERSE THE STRING:
# # Step 1: Get user input
word = input("Enter a word: ")

# # Initialize an empty string to store the reversed word
result = ""

# # Step 2: Reverse the string using a for loop
for i in range(len(word) - 1, -1, -1):
  result += word[i]

# # Output the reversed string
print(f"Reversed word: {result}")

# PALINDROME
string = input("Enter your Name: ")
l = len(string)
rev = ""

for i in range(l - 1, -1, -1):
  rev += string[i]

print(f"The reverse of '{string.upper()}' is '{rev.upper()}'")

if rev.lower() == string.lower():
  print(f"The {string.capitalize()} is a palindrome")
else:
  print(f"The {string.capitalize()} is not a palindrome")
