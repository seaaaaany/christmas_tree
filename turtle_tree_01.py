# Dependencies
import turtle

# Screen Size
screen = turtle.Screen()
screen.setup(1200, 900)

# Circle for the part of the tree
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fast')
circle.up()

# square for the part of the tree
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fast')
square.up()

circle.goto(0, 280)
circle.stamp()

# set k value for the loop
k = 0

# loop for the shape of the tree
for i in range(1, 17):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)  # coordination
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

    # Red Lights
    if i % 4 == 0:
        x = 30 * (j + 1)
        circle.color('red')
        circle.goto(-x, -y + 280)  # coordination
        circle.goto(x, -y + 280)
        circle.stamp()

    # Yellow lights
    if i % 4 == 3:
        x = 30 * (j + 1)
        circle.color('yellow')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()

# Trunk of the tree
square.color('brown')
for i in range(17, 20):
    y = 30 * i
    for j in range(3):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

turtle.exitonclick()
