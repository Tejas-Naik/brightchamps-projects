# #arithmetic operators
# a=10
# b=20 
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)
# print(a // b)

# #comparison operators
# a=10
# b=20 
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)

# #logical operators
# a=True
# b=False 
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)

# #bitwise operators
# a=60
# b=13 
# print(a & b)
# print(a | b)
# print(~a)
# print(a<<2)
# print(a>>2)

# #membership operators
# a="hello world"
# b={1:"steve",2:"Shika"} 
# print("w" in a)
# print("r" not in a )
# print (3 in b)
# print (1 in b)


# #identity operator
# m = 70
# n = 70
# if ( m is n ):
#    print("Result: m and n have same identity")
# else:
#    print("Result: m and n do not have same identity")

# m = 70
# n = 30
# if ( m is not n ):
#    print("Result: m and n do not have same identity")
# else:
#    print("Result: m and n have same identity")



#Write a program to find the denomination of the amount(in 100,50,10 and 5 rupee notes )

#amt = int(input("Enter the Amount to be Withdrawn :"))
# hundred = amt//100
# amt = amt%100
# fifty = amt//50
# amt = amt%50
# ten = amt//10
# amt =amt%10
# five = amt//5
# amt = amt%5
# print("No of Hundred Notes :",hundred)
# print("No of Fifty Notes :",fifty)
# print("No of Ten Notes :",ten)
# print("No of five Notes :",five)



#using if else
#write a program to find the largest of two numbers 

a = int(input("Enter a: "))

b = int(input("Enter b: ")) 

if a>b:  
    print("a is the largest")
else:
    print("b is the largest")

#make a program to give access to only who has secret code

secret_code="charlie345"
name=input(" Enter your name")
user_code=input("please enter secret code ")
if (user_code==secret_code):
  print("Hello "+name+ "welcome to our secret society")
  print("you have access to our VIP programs")
else :
  print("you are not allowed to access the program ")

#extra programs for fast learners
number = int(input("Enter a number: ")) 
  # check if number is positive or negative 
if number > 0:
    print('Number is positive.')
else:
    print('Number is negative.')

# Simple Python Program to check whether a number is even or not.  
num = int(input("Enter the number:"))         
if num%2 == 0:      
    print("The Given number is an even number")    
else:    
    print("The Given Number is an odd number")    


#if-elif-else
print("welcome to Driving License Program")
print("Enter your name")
name=str(input())
print("please enter your age to check if you are eligible to get Driving License")
age=int(input())
if(age>=18):
    print("Hi", name," you are eligible to get the Driving License")
elif(age<18):
    print("Hi", name,"  you are not eligible to get Driving License")
else:
    print("Hi", name," please enter the correct age")


#nested if
name = input("Enter your name: ")
email = input("Enter your email address: ")
password = input("Enter your password: ")
if name == "":
    print("Name cannot be empty.")
else:
    if "@" not in email:
        print("Invalid email address.")
    else:
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        else:
            print("Registration successful.")

#calculator
#Easy level
a=int(input("Enter first number : "))
b=int(input("Enter second number: "))
print(" press 1 for addition \n press 2 for subraction \n press 3 to multiply \n press 4 for division")

choice=int(input("enter your choice "))
add=a+b
sub=a-b
mul=a*b
div=a/b
if (choice==1):
   print("addition = ",add)
if (choice==2):
   print("subtraction = ",sub)
if (choice==3):
   print("Multiplication = ",mul)
if (choice==4):
   print("division = ",div)

#medium level
a=int(input("Enter first number : "))
b=int(input("Enter second number: "))
print(" press 1 for addition \n press 2 for subraction \n press 3 to multiply \n press 4 for division")
choice=int(input("enter your choice "))
add=a+b
sub=a-b
mul=a*b
div=a/b
if (choice==1):
  print("addition = ",add)
elif (choice==2):
  print("subtraction = ",sub)
elif (choice==3):
  print("Multiplication = ",mul)
elif (choice==4):
  print("division = ",div)
else:
  print("enter a valid option ")


#hard level
a=int(input("Enter first number : "))
b=int(input("Enter second number: "))
print(" press 1 for addition \n press 2 for subraction \n press 3 to multiply \n press 4 for division")
while True:
  choice=int(input("enter your choice "))
  add=a+b
  sub=a-b
  mul=a*b
  div=a/b
  if (choice==1):
   print("addition = ",add)
  elif (choice==2):
   print("subtraction = ",sub)
  elif (choice==3):
   print("Multiplication = ",mul)
  elif (choice==4):
   print("division = ",div)
  else:
   print("enter a valid option ")
    # check if user wants another calculation
   # break the while loop if answer is no
  next_calculation = input("Let's do next calculation? (yes/no): ")
  if (next_calculation == "no"):
    break