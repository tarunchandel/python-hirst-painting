import random

import colorgram
from turtle import Turtle, Screen


def get_colors(num):
    colors = colorgram.extract('hirst.jpg', num)
    colors_list = []
    for i in range(num):
        first_color = colors[i]
        rgb = first_color.rgb # e.g. (255, 151, 210)
        colors_list.append((rgb.r, rgb.g, rgb.b))
    return colors_list

colors_list = get_colors(30)

kittu = Turtle()
kittu.shape("turtle")
kittu.color("DodgerBlue", "LightSlateBlue")
kittu.hideturtle()
screen = Screen()

screen.colormode(255)
kittu.speed(0)
kittu.pensize(2)


def draw_hirst_painting(rows, columns, radius):
    kittu.penup()
    kittu.setheading(225)
    kittu.forward(360)
    kittu.setheading(0)

    for i in range(rows):
        for j in range(columns):
            kittu.pendown()
            clr = random.choice(colors_list)
            kittu.pencolor(clr)
            kittu.dot(radius)
            kittu.penup()
            kittu.forward(radius*3)

        kittu.penup()
        kittu.setheading(90)
        kittu.forward(radius * 3)
        kittu.setheading(180)
        kittu.forward(radius*3*columns)
        kittu.setheading(0)

draw_hirst_painting(10, 10, 20)

screen.exitonclick()