# ### SOME COMMONLY USED MATH FUNCTIONS
# import math

# x = 25
# square_root = math.sqrt(x)
# print(square_root) 

# base = 2
# exponent = 3
# result = math.pow(base, exponent)
# print(result)

# number = 3.7
# ceiling = math.ceil(number)
# floor = math.floor(number)
# print(ceiling, floor) 

# x = -10
# absolute_value = math.fabs(x)
# print(absolute_value)  

# n = 5
# factorial = math.factorial(n)
# print(factorial)  

# x = 100
# natural_log = math.log(x)
# logarithm_base_10 = math.log10(x)
# print(natural_log, logarithm_base_10)  



### FUNCTION ARGUMENTS using a greet function:
# def greet(word):
#     msg = "Hello " + word
#     print(msg)

# name = input("Enter your name: ")
# greet(word=name)

# Function variables can be used only within the function
# def greet(word):
#     msg = "Hello " + word

# name = input()
# greet(word=name)
# print(msg)

# ### WEATHER REPORTER:
# def get_weather_report(temperature):
#   if temperature < 22:
#     return "It's quite chilly out there."
#   elif temperature >= 22 and temperature < 65:
#     return "Enjoy the pleasant weather!"
#   elif temperature >= 65 and temperature < 85:
#     return "It's getting warm. Stay hydrated!"
#   else:
#     return "It's hot outside. Be cautious and stay cool."

# temperature = int(input("Enter the temperature: "))
# result = get_weather_report(temperature)
# print(result)




# ### COUNT THE VOWELS:
# def count_the_vowels(sen):
#   vowels = ['a', 'e', 'i', 'o', 'u']
#   count = 0
#   for char in sen:
#     if char.lower() in vowels:  # To make the comparison case-insensitive
#       count += 1
#   return count

# sentence = input("Enter any sentence: ")
# vowel_count = count_the_vowels(sentence)
# print(f"\nThe word '{sentence}' contains {vowel_count} vowel(s).")



### Functions for add, sub, mul, div:
def addition(a, b):
  print(f"\nThe result is: {a} + {b} = {a+b}")

def subtraction(a, b):
  print(f"\nThe result is: {a} - {b} = {a-b}")

def multiply(a, b):
  print(f"\nThe result is: {a} * {b} = {a*b}")

def division(a, b):
  print(f"\nThe result is: {a} / {b} = {a/b}")

num1 = int(input("Enter the first number: "))
op = input("Enter the operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

# Call the function using conditionals
if op == "+":
  addition(num1, num2)
elif op == "-":
  subtraction(num1, num2)
elif op == "*":
  multiply(num1, num2)
elif op == "/":
  division(num1, num2)
else:
  print("Invalid Input given...")

