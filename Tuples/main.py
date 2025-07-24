# a = 4
# tuple_a = (5, "One", a, 6.4)
# print(type(tuple_a))
# print(tuple_a)

# a = (5, )
# print(type(a))
# print(a)

# a = 4
# tuple_a = (5, "One", a, 6.4)
# print(tuple_a[0])
# print(tuple_a[1]) 
# print(tuple_a[2]) 
# print(tuple_a[3]) 

# tuple_a = (10, 20, 30, 50)
# tuple_a[3] = 40
# print(tuple_a)

# # String to Tuple
# color = "Red"
# tuple_a = tuple(color)
# print(tuple_a)
 
# # List to Tuple 
# list_a = [1, 2, 3]
# tuple_a = tuple(list_a)
# print(tuple_a)
 
# # Sequence to Tuple 
# tuple_a = tuple(range(4)) 
# print(tuple_a)

# # ----------------------------------------------------------
# # CONCATENATING TUPLES PROGRAM:

# names = ("Alice", "Bob", "Charlie")
# numbers = (10, 20, 30, 40)
# boolean = (True, False, True)
# floats = (3.14, 1.618, 2.718)

# combined_tuple = names + numbers + boolean + floats
# print(combined_tuple)

# # ----------------------------------------------------------
# # List Unpacking:
# list_a = [1, 2, 3, 4]
# result = 2 in list_a
# print(result)
# # Output: True

# result = 3 not in list_a
# print(result)


# # String Membership:
# word = 'Python'
# result = 'th' in word
# print(result)

# result = 'Py' not in word
# print(result)


# # Tuple Unpacking 
# my_tuple = (10, 20, 30)

# # Unpacking
# a, b, c = my_tuple
# print(a)  
# print(b)  
# print(c) 



# # ----------------------------------------------------------
# # Replace an Element 
# num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

# N = int(input("Enter the value of N: "))

# result_list = []

# # Iterate through each tuple in num_list
# for eachTuple in num_list:
#     temp_list = list(eachTuple)
#     temp_list.pop()
#     temp_list.append(N)
#     result_list.append(tuple(temp_list))

# # Print the final list of modified tuples
# print(f"\nInitial List: {num_list}")
# print(f"\nReplaced List: {result_list}")



# -------------------------------------------------------------
# Sum & Average of even numbers:

numbers_tuple = (10, 15, 20, 25, 30, 35, 40)

# Initialize an empty list to store even numbers
even_numbers_list = []

# Iterate through the tuple to find even numbers
for num in numbers_tuple:
    if num % 2 == 0:  
        even_numbers_list.append(num)

even_sum = sum(even_numbers_list)

# Calculate the average of even numbers (Avoid division by zero using max())
even_average = even_sum / max(len(even_numbers_list), 1)

print("Sum of even numbers:", even_sum)
print("\nAverage of even numbers:", even_average)