from turtle import Turtle, Screen
from random import Random, randint


def random_walk(direction):
    kittu.setheading(90 * direction)
    kittu.pencolor(random_color())
    kittu.forward(30)


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def draw_dashes(length):
    for _ in range(length):
        kittu.forward(length+10)
        kittu.penup()
        kittu.forward(length+10)
        kittu.pendown()

def draw_geometric_shapes(count):
    for i in range(3, count+1):
        kittu.pencolor(random_color())
        kittu.fillcolor(random_color())
        sides = count + 3 - i
        kittu.begin_fill()
        for _ in range(sides):
            kittu.forward(100)
            kittu.left(360 / sides)
        kittu.end_fill()



def draw_spirograph(circles, radius):
    for _ in range(circles):
        kittu.circle(radius)
        kittu.left(int(abs(360/circles)))

def draw_srispirograph(circles, radius):
    for i in range(circles):
        kittu.pencolor(random_color())
        draw_spirograph(circles, radius)
        kittu.penup()
        kittu.left(abs(360/circles))
        kittu.forward(circles*5)
        kittu.pendown()



kittu = Turtle()
kittu.shape("turtle")
kittu.color("DodgerBlue", "LightSlateBlue")
screen = Screen()
screen.colormode(255)
kittu.speed(0)
kittu.pensize(10)

draw_geometric_shapes(10)
draw_dashes(10)

for _ in range(150):
    random_walk(randint(0, 3))

kittu.home()
kittu.clear()
kittu.pensize(1)

draw_spirograph(120, 100)
kittu.home()
kittu.clear()

draw_srispirograph(15, 100)
screen.exitonclick()
