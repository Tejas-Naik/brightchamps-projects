def fibo(x):
  if x<=1:
    return x
  else:
    return(fibo(x-1)+fibo(x-2))
# numbers=10
numbers = int(input("Enter the number of terms: "))
if numbers<=0:
  print("please enter valid positive number")
else:
  print("Here is the Fibonacci series")
  for i in range(numbers):
    print(f"{i}: {fibo(i)}")
