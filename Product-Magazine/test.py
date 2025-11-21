
#hard level
a=int(input("Enter first number : "))
b=int(input("Enter second number: "))
print(" press 1 for addition \n press 2 for subraction \n press 3 for multiplication \n press 4 for division")
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