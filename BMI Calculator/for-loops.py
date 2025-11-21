# in range (printing numbers 0 to 5)
for i in range(1, 6):  # start counting from 0 and end at 5 (exclusive)
    print(i)
    
# using it with a list
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print(fruits)
# printing each fruit in the list using range
print(len(fruits))  # length of the list

for i in range(len(fruits)):
    print(fruits[i]) 

for fruit in fruits:
    print(fruit)
