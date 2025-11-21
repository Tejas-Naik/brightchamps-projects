print("------------------------------------")
print("~~ Welcome to the bmi Calculator! ~~")
print("------------------------------------")
print()

print("Please enter your details to calculate your bmi.")
print()

# Get user input for weight and height
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cms): "))

# Calculate BMI
bmi = weight / ((height/100)**2)
# print("Your Body Mass Index is", bmi)
print("Your BMI is:", round(bmi, 2))

if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi <= 34.9:
    print("You are severely over weight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

