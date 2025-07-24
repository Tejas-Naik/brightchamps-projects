# Example 1: Basic Input and Output
# Taking input from user and printing it
name = input("Enter your name: ")
print("My name is", name)

print("\n" + "="*50 + "\n")

# Example 2: Class with Instance Variables
class Student:
    # Constructor method - called when creating new object
    def __init__(self, name):    # self refers to the current object instance
        self.name = name         # Creating instance variable 'name'
    
    # Method to print greeting
    def printHi(self):
        print('Hi, name is', self.name)

# Creating two different student objects
student1 = Student('Shikha')
student2 = Student('Shishir')

# Calling method for both objects
student1.printHi()  # Each object has its own name value
student2.printHi()

print("\n" + "="*50 + "\n")

# Example 3: Class with Class Variable
class Student:
    # Class variable - shared by all instances
    age = 12
    
    def __init__(self, name):
        # Instance variable - unique to each instance
        self.name = name
    
    def printHi(self):
        print('Hi, name is', self.name)

# Creating student objects
student1 = Student("Shikha")
student2 = Student("Shishir")

# Printing greetings
student1.printHi()
student2.printHi()

# Accessing class variable - both objects share the same age
print(student1.age)  # Prints 12
print(student2.age)  # Prints 12

print("\n" + "="*50 + "\n")

# Example 4: Inheritance with Animals
class Animal:
    def __init__(self, name, age):
        self.name = name    # Name of the animal
        self.age = age      # Age of the animal
    
    def make_sound(self):
        print("Some generic animal sound")
    
    def info(self):
        print(f"I am a {self.name} and I am {self.age} years old")

# Tiger inherits from Animal
class Tiger(Animal):
    def make_sound(self):
        print("ROAR! The tiger roars loudly!")
    
    def hunt(self):
        print(f"{self.name} is hunting in the jungle")

# Lion inherits from Animal
class Lion(Animal):
    def make_sound(self):
        print("ROAR! The lion roars majestically!")
    
    def sleep(self):
        print(f"{self.name} is sleeping in the savanna")

# Cat inherits from Animal
class Cat(Animal):
    def make_sound(self):
        print("Meow! The cat meows softly")
    
    def play(self):
        print(f"{self.name} is playing with a ball of yarn")

# Creating animal objects
tiger = Tiger("Shere Khan", 5)
lion = Lion("Simba", 3)
cat = Cat("Whiskers", 2)

# Using inherited and overridden methods
print("\nTiger:")
tiger.info()      # Inherited from Animal
tiger.make_sound() # Overridden method
tiger.hunt()      # Tiger-specific method

print("\nLion:")
lion.info()       # Inherited from Animal
lion.make_sound() # Overridden method
lion.sleep()      # Lion-specific method

print("\nCat:")
cat.info()        # Inherited from Animal
cat.make_sound()  # Overridden method
cat.play()        # Cat-specific method
