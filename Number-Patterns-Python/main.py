### Multiplication Tables 
# n = int(input("Enter any number: "))
# for i in range(1, 11):
#   print(f"{n} x {i} = {n*i}")




### Number Triangle Pattern-1
# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#   for j in range(1, i + 1):
#     print(j, end=' ')
#   print()



# ### Number Triangle Pattern-2
# n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         print(n, end=" ")
#     print()



# ### Odd Number Triangle
# rows = int(input("Enter the number of rows: "))
# i = 1

# while i <= rows:
#   j = 1
#   while j <= i:
#     print(2 * i - 1, end=" ")
#     j += 1
#   print()
#   i += 1



# ### Number Staircase
# rows = int(input("Enter the number of rows: "))
# current_number = 1

# for i in range(1, rows + 1):
#   for j in range(i):
#     print(current_number, end=" ")
#     current_number += 1
#   print()



# ### Decreasing Number Pyramid
# rows = int(input("Enter the number of rows: "))

# for i in range(rows, 0, -1):
#   for j in range(1, i + 1):
#     print(i, end=" ")
#   print()



### Fibonacci Series
# Initialize the first two numbers
firstNumber = 0
secondNumber = 1

# Specify how many terms you want or can take userinput here
numTerms = 100  # You can change this to get more terms

# Print the first two numbers
print(firstNumber)
print(secondNumber)

# Generate the rest of the series
for i in range(2, numTerms):
  # Calculate the next number in the series
  nextNumber = firstNumber + secondNumber
  
  # Print the next number
  print(nextNumber)
  
  # Update the variables for the next iteration
  firstNumber = secondNumber
  secondNumber = nextNumber





