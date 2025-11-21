# Using a string
name1 = "Ali"
name2 = "Tejas"
name3 = "John"

# using a list
names = ["Ali", "Tejas", "John", "Mark", "Harry", "Bill", "Steve"]
print(names)

# Indexing
print(names[0])
print(names[1])

# slicing
# lets print from index 0 to 2 
print(names[0:2])

# lets print from index 1 to end
print(names[1:])

# using a for loop to loop over the list
for name in names:
    print(name)

# greet the name in names list with a hello 
for name in names:
    print("Hello, ", name)
    print(f"Hello, {name}")
    