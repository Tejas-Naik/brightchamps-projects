colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "magenta"]

# Adds an element in the end of the list
colors.append("white")

# deletes the last element from the list
colors.pop()

# returns the index of the element
colors.index("blue")

# returns the element in that index
print(colors[4])

# returns the last element
print(colors[-1])

# mutable means you can add new values to it
# immutable means you cannot add new values to it

# A dictionary is a collection of key:value pairs. It is mutable, unordered and indexed.
contact_numbers = {
    "John": 1234567890,
    "Jane": 9876543210,
    "Alice": 1231231231,
}

# Returns the value of the key
print(contact_numbers["Jane"])
print(contact_numbers["Alice"])


# Adding a new key:value pair
contact_numbers["Kevin"] = 5555555555


print(contact_numbers)

# Deleting a key:value pair
del contact_numbers["John"]
print(contact_numbers)

# Updating an existing key:value pair
contact_numbers["Jane"] = 9999999999

# Getting Keys:
print(contact_numbers.keys())

# getting the values
print(contact_numbers.values())

# How we can loop over a dictionary
for contact in contact_numbers:
    print(f"{contact}: {contact_numbers[contact]}")

