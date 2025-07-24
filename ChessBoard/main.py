import turtle

# Create a Screen & Turtle instance
turtle.title("Chess Board")
canvas = turtle.Screen()
artist = turtle.Turtle()
canvas.setup(400, 600)

# Set turtle object speed
artist.speed(10)


# Loop to draw each ROW on the board
for i in range(8):
  # Not ready to draw
  artist.up()
  # Set position for every row as the starting point (y-axis) of each row moves upwards
  artist.goto(-100, 30 * i)
  # Ready to draw
  artist.down()
  
  # Loop to draw 8 squares in each line (Single Row)
  for j in range(8):
    # Conditions for alternative color
    if (i + j) % 2 == 0:
        col = 'black'
    else:
        col = 'white'

    # Fill with given color and start filling with color
    artist.fillcolor(col)
    artist.begin_fill()

    # Draw one square
    for _ in range(4):
        artist.forward(30)
        artist.left(90)

    artist.forward(30)

    # Stop filling
    artist.end_fill()

artist.penup()
artist.goto(20, -50)
artist.pendown()
artist.write("CHESS BOARD", move=False, align="center", font=("Arial", 20, "bold"))

# After all the rows are printed, hide the turtle and end the code
artist.hideturtle()
turtle.done()


