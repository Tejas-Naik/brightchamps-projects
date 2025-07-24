# Creating & Accessing from Dictionary
dict_a = {
  'name': 'Champ',
  'age': 16
}

print(dict_a['name']) # Output: Champ
print(dict_a['city']) # Output: KeyError: 'city' 
print(dict_a.get('city')) # Output: None


# Membership Check
result = 'name' in dict_a
print(result) 

# No Duplicates allowed
dictEx={
    1:'one',
    2:'two',
    3:'third',
    3:'three',
    4:'one' 
}
print(dictEx) 
# Output: {1: 'one', 2: 'two', 3: 'three', 4: 'one'}
# Only the 3 with value updated at last is considered. 


# LENGTH & TYPE OF DICTIONARY
countries = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}
print(len(countries)) 
print(type(countries)) 

'''
Output: 
3
<class 'dict'>
'''

# DICTIONARY OPERATIONS
# ADDING A KEY-VALUE PAIR
dict_a = {
  'name': 'Champ',
  'age': 16
}

dict_a['city'] = 'Delhi'
print(dict_a) 
 
# Modifying the age key
dict_a['age'] = 30
print(dict_a)

# Deleting the age key
del dict_a['age']
print(dict_a)


# DICTIONARY METHODS:
dict_a = {
  'name': 'Champ',
  'age': 16
}

# Getting Keys:
print(dict_a.keys())

# Getting Values:
print(dict_a.values())

# Getting Items:
print(dict_a.items())



# ITERATING OVER DICTIONARY
countries = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# print dictionary keys one by one
for country in countries:
    print(country)

print("----------")

# print dictionary values one by one
for country in countries:
    capital = countries[country]
    print(capital)





# ITERATING USING DICTIONARY METHODS:
countries = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

keys_list = list(countries.keys())
print(keys_list) 

# Example 1: Using dict.keys() method
for key in countries.keys():
   print(key)


# Example 2: Using dict.values() method
for value in countries.values():
   print(value)


# Example 3: Using dict.items() method
for key, value in countries.items():
  pair = f"{key} {value}"
  print(pair)