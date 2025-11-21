from turtle import Turtle, Screen
import random 
painter = Turtle()
screen = Screen()
painter.speed(100)
# for i in range(120):
#     painter.circle(100)
#     painter.right(3)

colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']

for i in range(120):
    painter.color(random.choice(colors))
    for i in range(4):
        painter.forward(100)
        painter.right(90)
    painter.right(3)

screen.exitonclick()