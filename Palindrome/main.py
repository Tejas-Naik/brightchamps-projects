# # Activity 1:
# # Sample string
# s = "Python program"

# # Slicing examples
# # Example 1: Get the first character
# print(s[0])  # Output: 'P'

# # Example 2: Get a slice from index 7 to 13 (exclusive)
# print(s[7:13])  # Output: 'program'

# # Example 3: Get a slice from index 0 to 6 (exclusive)
# print(s[:6])  # Output: 'Python'

# # Example 4: Get a slice from index 7 to the end
# print(s[7:])  # Output: 'program'

# # Example 5: Get the last character
# print(s[-1])  # Output: 'm'

# # Example 6: Get a slice excluding the last character
# print(s[:-1])  # Output: 'Python progra'

# # Example 7: Get every second character from index 1 to 10 (exclusive)
# print(s[1:10:2])  # Output: 'yhnp'

# # Example 8: Reverse the string using slicing
# print(s[::-1])  # Output: 'margorp nohtyP'

# # Example 9: Get a slice from index 0 to the end, step size 3
# print(s[::3])  # Output: 'Ph o'

# # Example 10: Get a slice from index -5 to the end
# print(s[-5:])  # Output: 'ogram'

# # Example 11: Get a slice from index -8 to -3 (exclusive)
# print(s[-8:-3])  # Output: 'ython'

# # Example 12: Reversing of string
# print(s[::-1])

# # --------------------------------------------------
# # String repetition
# s = "Python"
# repeated_string = s * 3
# print(repeated_string)

# # String Concatenation
# s = "Python" + "Programming"
# print(s)

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hi " + name + " your age is " + age)

# # F-Strings
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hi {name} your age is {age}")

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

# # PALINDROME:
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

# Program using split() & join() method

#Get comma-separated names from the user
names_input = input("Enter comma-separated names: ")

# Split the input into individual names using split()
names_list = names_input.split(",")

# Display the individual names using range in the for loop
print("Individual names:")
for i in range(len(names_list)):
  print(names_list[i])

# Join the names_list using ', ' as a separator to display them as friends
friends = ', '.join(names_list)
print(f"These people are good friends: {friends}")

# EMAIL VALIDATION PROGRAM:
# while True:
#     email = input("Enter your Email ID: ")

#     if email[0].isalpha() or email[0].isdigit():
#         if email.endswith("@gmail.com"):
#             print("Your Email ID is valid")
#             break
#         else:
#             print("Invalid Gmail ID! Try again")
#     else:
#         print("Invalid Gmail ID! Try again")
