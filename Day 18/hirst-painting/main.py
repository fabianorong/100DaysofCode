import colorgram
from turtle import Turtle, Screen
import random

# Extract 6 colors from an image.
colors = colorgram.extract('Day 18/hirst-painting/image.jpg', 30)
screen = Screen()
screen.colormode(255)

rgb_colors =[]
colours = [(254, 254, 253), (219, 254, 237),
           (84, 254, 155), (173, 146, 118),
           (254, 250, 254), (245, 39, 191),
           (158, 107, 56), (2, 1, 176), (151, 54, 251),
           (221, 254, 101), (253, 146, 193), (3, 87, 176),
           (249, 1, 246), (35, 34, 253), (1, 213, 212),
           (249, 0, 0), (254, 147, 146), (253, 71, 70),
           (244, 248, 254), (39, 249, 42), (85, 249, 253),
           (240, 1, 13), (5, 210, 216), (230, 126, 190),
           (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

timmy_the_turtle.pensize(25)
timmy_the_turtle.speed(0)

def one_dot():
    timmy_the_turtle.pendown()
    timmy_the_turtle.pencolor(random.choice(colours))
    timmy_the_turtle.forward(1)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(50)
    timmy_the_turtle.pendown()

def turn():
    timmy_the_turtle.penup()
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)


score = 0
end_board = False
change_row_value = 50
row = 0

while end_board == False:
    while score < 10:
        one_dot()
        score += 1
    if score == 10:
        row += 1
        timmy_the_turtle.penup()
        timmy_the_turtle.goto(0, change_row_value)   
        score = 0
        change_row_value += 50
    if row == 10:
        end_board = True









screen.exitonclick()