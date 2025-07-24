# Draw a Panda using Turtle Graphics
##################### Things to remember ########################
# pen.up			 --> move turtle to air
# pen.down		 --> move turtle to ground
# pen.setpos		 --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
#################################################################

import turtle as t

t.title("Panda")

# Configure Turtle & Screen 
turtle = t.Turtle()
screen = t.Screen()
screen.setup(width=400, height=400)
screen.bgcolor("lightgray")

def draw_circle(col="white", rad=50):
  turtle.fillcolor(col)
  turtle.begin_fill()
  turtle.circle(rad)
  turtle.end_fill()

# draw_circle("red")
# draw_circle("orange", 40)
# draw_circle("blue", 30)
# draw_circle("yellow", 20)
# draw_circle("green", 10)

def draw_face():
  # Draw face
  turtle.up()
  turtle.setpos(0, 35)
  turtle.down()
  draw_circle('white', 40)

def draw_ears():
  # Draw first ear
  turtle.up()
  turtle.setpos(-35, 95)
  turtle.down()
  draw_circle('black', 15)
  # Draw second ear
  turtle.up()
  turtle.setpos(35, 95)
  turtle.down()
  draw_circle('black', 15)

def draw_eyes_black():
  # Draw first eye (black)
  turtle.up()
  turtle.setpos(-18, 75)
  turtle.down()
  draw_circle('black', 8)

  # Draw second eye (black)
  turtle.up()
  turtle.setpos(18, 75)
  turtle.down()
  draw_circle('black', 8)

def draw_eyes_white():
  # Draw first eye (white)
  turtle.up()
  turtle.setpos(-18, 77)
  turtle.down()
  draw_circle('white', 4)

  # Draw second eye (white)
  turtle.up()
  turtle.setpos(18, 77)
  turtle.down()
  draw_circle('white', 4)

def draw_nose():
  # Draw nose
  turtle.up()
  turtle.setpos(0, 55)
  turtle.down()
  draw_circle('black', 5)

def draw_mouth():
  # Draw mouth
  turtle.up()
  turtle.setpos(0, 55)
  turtle.down()
  turtle.right(90)
  turtle.circle(5, 180)
  turtle.up()
  turtle.setpos(0, 55)
  turtle.down()
  turtle.left(360)
  turtle.circle(5, -180)

def draw_panda():
  draw_face()
  draw_ears()
  draw_eyes_black()
  draw_eyes_white()
  draw_nose()
  draw_mouth()

  turtle.penup()
  turtle.goto(5, -20)
  turtle.pendown()
  turtle.write("Panda", move=False, align="center", font=("Arial", 20, "bold"))
  turtle.hideturtle()

# Call the function to draw the panda
draw_panda()
t.done()

