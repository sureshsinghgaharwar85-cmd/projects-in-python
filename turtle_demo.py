import turtle

screen = turtle.Screen()
screen.setup(900, 700)
screen.title("My Beautiful House")
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(3)
t.pensize(3)

def rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def triangle(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()

# Ground
rectangle(-450, -300, 900, 180, "limegreen")

# House body
rectangle(-180, -120, 360, 280, "white")

# Roof
triangle([(-210, 160), (0, 330), (210, 160)], "red")

# Door
rectangle(-40, -120, 80, 140, "saddlebrown")

# Door knob
t.penup()
t.goto(25, -55)
t.dot(12, "yellow")

# Windows
for x in [-140, 80]:
    rectangle(x, 0, 65, 65, "deepskyblue")
    t.penup()
    t.goto(x + 32, 0)
    t.pendown()
    t.goto(x + 32, 65)
    t.penup()
    t.goto(x, 32)
    t.pendown()
    t.goto(x + 65, 32)

# Sun
t.penup()
t.goto(320, 220)
t.dot(90, "yellow")

# Tree trunk
rectangle(-350, -120, 35, 180, "saddlebrown")

# Tree leaves
t.penup()
t.goto(-330, 80)
t.dot(130, "green")

# Grass
for x in range(-400, 450, 80):
    t.penup()
    t.goto(x, -180)
    t.dot(25, "green")

t.hideturtle()
turtle.done()
