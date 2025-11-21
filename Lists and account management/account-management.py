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

