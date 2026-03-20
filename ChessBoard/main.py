import turtle

# Create a Screen & Turtle instance
turtle.title("Chess Board")
canvas = turtle.Screen()
artist = turtle.Turtle()
canvas.setup(400, 600)
artist.speed(10)


# Loop to draw each ROW on the board
for i in range(8):
  artist.up()
  artist.goto(-100, 30 * i)
  artist.down()
  for j in range(8):
    if (i + j) % 2 == 0:
        col = 'black'
    else:
        col = 'white'

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


