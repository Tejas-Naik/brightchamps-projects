### TURTLE METHODS:

# import turtle

# # Create a screen & turtle instance
# canvas = turtle.Screen()

# # Create a turtle instance
# turtle = turtle.Turtle()

# # Setup the turtle graphics window with width & height
# canvas.setup(width=500, height=500)

# # Move the turtle forward by 200 units
# turtle.forward(200)

# # Move the turtle backward by 150 units
# turtle.backward(150)

# # Turn the turtle left by 90 degrees
# turtle.left(90)

# # Move the turtle forward by 100 units without drawing
# turtle.penup()
# turtle.forward(100)

# # Put the turtle's pen back on the screen to start drawing again
# turtle.pendown()

# # Adjust the turtle's drawing speed to fastest (10)
# turtle.speed(10)

# turtle.forward(100)

# # Move the turtle to the coordinates (50, 50) without drawing
# turtle.penup()
# turtle.goto(50, 50)

# --------------------------------------------------------

# ACTIVITY 1: DRAW A SQUARE & TRIANGLE

import turtle
import time

# Create a Screen & Turtle instance
canvas = turtle.Screen()
turtle = turtle.Turtle()

canvas.setup(500, 500)

# Draw a square
for i in range(4):
  turtle.forward(100)
  turtle.left(90)

# Set the pen color to green
turtle.pencolor("green")

# Set the fill color to blue
turtle.fillcolor("blue")

# Begin filling the shape
turtle.begin_fill()

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

# Draw a triangle
for i in range(3):
  turtle.forward(80)
  turtle.left(120)

# End filling the shape
turtle.end_fill()

time.sleep(4)
turtle.reset()

# -------------------------------------------------------------
# ACTIVITY 2: POLYGON GENERATOR
# import turtle

# Create a Screen & Turtle instance

canvas.setup(500, 400)
canvas.title("Polygon Generator")

# Take user inputs
length = int(input("Enter the length/size of the polygon: "))
num_sides = int(input("Enter the number of sides of the polygon: "))
fill_color = input(
    "Enter the color to fill the polygon (e.g., 'red', 'blue', '#FF0000'): ")

# Calculate the angle based on the number of sides
angle = 360 / num_sides

# Set the fill color
turtle.fillcolor(fill_color)

# Begin filling the shape
turtle.begin_fill()

# Draw the polygon using a loop
for i in range(num_sides):
  turtle.forward(length)
  turtle.left(angle)

# End filling the shape
turtle.end_fill()
turtle.reset()


# -------------------------------------------------------------
# ACTIVITY 3: DRAW A HEART

import turtle

# Create a Screen & Turtle instance
turtle.title("Heart")
canvas = turtle.Screen()
turtle = turtle.Turtle()
canvas.setup(width=400, height=400)
turtle.speed(0)

turtle.fillcolor('red')
turtle.begin_fill()

# Left line
turtle.left(140)
turtle.forward(113)

# Left Curve
for i in range(200):
  turtle.right(1)
  turtle.forward(1)

turtle.left(120)

# Right Curve
for i in range(200):
  turtle.right(1)
  turtle.forward(1)

# Right line
turtle.forward(112)
turtle.end_fill()

# Hiding the turtle
turtle.hideturtle()
