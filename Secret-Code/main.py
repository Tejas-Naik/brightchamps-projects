#while loops
# program to display numbers from 1 to 5
# initialize the variable
i = 1
n = 5
# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1
  
#infinite loop
#age=32
# the test condition is always True
#while age > 18:
 #   print('You can vote')

n= int(input("Enter the number"))
#initialize sum and counter
sum =0
i=1
while i<= n:
  sum =sum +i
  i=i+1        #update counter
#print the sum
print("The sum is", sum)

#while-else
counter = 0
while counter < 3:
    print('I am inside the While loop')
    counter = counter + 1
else:
    print('I am inside the else loop')

#Break statement
i=1
while i<6:
  print(i)
  if i==3:
    break
  i=i+1

#continue statement
i=0
while i<6:
  i=i+1
  if i==3:
    continue
  print(i)

#for loop

for i in range(10):   # print values from 0-9
  print(i)
  
for i in range(10):    # print hello 10 times
  print("hello")
  
  
# add start,stop and  step size(increment)

for i in range(10): 
  print(i)
  
for i in range(3,10):    
  print(i)
 
for i in range(2,20,2):    
  print(i)

# negative range from -1 to -10
for i in range(-1, -11, -1):
    print(i)

#iterating by index
list_fruits = ["apple", "orange", "banana"]
for index in range(len(list_fruits)):
    print(list_fruits[index])
    

#for with else
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break")

#with break statement
for i in range(20):   # loop to repeat 20 times
  print(i)
  if i==10:         
    break    # get out of loop when condition is true 


#with continue statement
for x in range(10):
  if(x==7):
    #print("i'm seven")
    continue     # after condition is true keep in loop 
  print(x)

#Using Nested for loop to print the range of tables
lower=int(input("Enter the lower limit "))
upper=int(input("Enter the upper limit "))
for i in range(lower,upper+1):          #Outer loop to the range of the tables to be printed
    for j in range(1,11):               #Inner loop to generate number from 1 to 10
        print(i*j,end=" ")
    print()                             #Inserts a newline character after each iteration of outer loop


# program to find the sum of first 10 numbers 
num=int(input("Enter the number to find the sum"))
sum=0
for i in range(num+1):
  sum=sum+i     # can use sum+=i  everytime add i value to sum
print("sum for first 10 natural numbers is ", sum)



# finding the sum of numbers by giving limits
sum=0
lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
for i in range(lower,upper+1):
  sum=sum+i     # can use sum+=i  everytime add i value to sum
print("sum of", lower,"to", upper, " natural numbers is ", sum)

# program to find the sum of  even number and odd numbers for  natural numbers 
num=int(input("Enter the number"))
total_even= 0
total_odd= 0
for x in range(num+1):
  if x % 2 == 0:
    total_even+=x   #or total_even=total_even+x
  else:
    total_odd+=x   #or total_odd=total_odd+x

print("sum of even numbers is ",total_even)
print("sum of odd numbers is ",total_odd)

