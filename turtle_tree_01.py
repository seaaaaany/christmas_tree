# Dependencies
import turtle

# Screen Size
screen = turtle.Screen()
screen.setup(800, 600)

# Circle for the part of the tree
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

# square for the part of the tree
square = turtle.Turtle()
square = shape('square')
square = shape('green')
square.speed('fastest')
square.up()

circle.goto(0, 280)
circle.stamp()

# set k value for the loop
k = 0

for i in range(1, 17):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
