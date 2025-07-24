# Examples of List accessing, slicing, length
a = 2
list_a = [5, "One", a, 8.2]
print(list_a)
print(type(list_a))
print(len(list_a))
print(list_a[1])
print(list_a[-1])

# Loops with Lists
a = 2
list_a = [5, "One", a, 8.2]
for item in list_a:
    print(item)

# List Concatenation
list_a = [10, 20, 30]
list_b = ["a", "b", "c"]
list_c = list_a + list_b
print(list_c)

# List Repetition
list_d = list_a * 3
print(list_d)
print(list_d[:2])
print(list_d[0:5:3])

# Converting to a List -
color = "Green"
list_a = list(color)
print(list_a) # Output: ['G', 'r', 'e', 'e', 'n']


# Print the list in the Reverse Order
my_list = ["Bright","Champs",1,2,3,20.1]

# Using a for loop to print the list in reverse order
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])


# Print the list in the Reverse Order using negative step List Slicing
my_list = ["Bright","Champs",1,2,3,20.1]
reverse_list = my_list[::-1]
for item in reverse_list:
    print(item)

# -------------------------------------------------
# LIST OPERATIONS:
list_a = ["Bright","Champs", 1, 2, 3, 20.1]
list_a.append("Student")

print(list_a)

'''
Output: ['Bright','Champs', 1, 2, 3, 20.1, 'Student']
'''

list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_a.extend(list_b)
print(list_a) 
# Output: [1, 2, 3, 4, 5, 6]

list_a.insert(1,4)
print(list_a) 
# Output: [1, 4, 2, 3]

list_a.pop()
print(list_a) 
# Output: [1, 4, 2]

nums = "1 2 3 4"
nums_list = nums.split()
print(nums_list)
# Output: ['1', '2', '3', '4']


# ---------------------------------------------


# User Account Management
user_accounts = []

# Get user credentials as space-separated input
credentials_input = input("Enter username and password (separated by space): ")
username, password = credentials_input.split()

# Add the username and password to the list of user accounts
user_accounts.append(username)
user_accounts.append(password)

print("User account created successfully!")
print("User accounts:", user_accounts)

# Ask if the user wants to modify the password
modify_password = input("\nDo you want to modify the password? (yes/no): ")

if modify_password.lower() == "yes":
    new_password = input("Enter the new password: ")
    
    # Update the password
    user_accounts.pop()
    user_accounts.append(new_password)
    
    print("Password updated successfully!")
    print("Updated user accounts:", user_accounts)
else:
    print("Thank you for using User Account Management.")

