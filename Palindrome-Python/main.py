### ACTIVITY 1: PRINT THE LAST DIGIT OF A NUMBER
num = int(input("Enter an integer: "))

last_digit = num % 10
print("Last digit:", last_digit)


### ACTIVITY 1: PRINT THE FIRST DIGIT OF A NUMBER
num = int(input("Enter an integer: "))
while num >= 10:
  num = num // 10
print("First digit:", num)



## ACTIVITY 2: PALINDROME NUMBER FINDER
def check_palindrome(num):
  original_num = num
  reversed_num = 0
  
  while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num = num // 10

  return original_num == reversed_num


number = int(input("Enter a number: "))
result = check_palindrome(number)

if result:
  print(f"{number} is a palindrome.")
else:
  print(f"{number} is not a palindrome.")



### ACTIVITY 3: DENOMINATION CALCULATOR
amount = int(input("Enter the amount: "))

num_100 = amount // 100
amount %= 100

num_50 = amount // 50
amount %= 50

num_10 = amount // 10
amount %= 10

num_1 = amount

print(f"100:{num_100}")
print(f"50:{num_50}")
print(f"10:{num_10}")
print(f"1:{num_1}")





