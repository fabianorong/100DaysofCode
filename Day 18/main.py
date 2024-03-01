from turtle import Turtle, Screen
import random

# DAY 18 TRAINING.

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# 170.
# def draw_polygon(turtle, sides, sides_lenght):
#     angle = 360/sides
#     for _ in range(sides):
#         turtle.forward(sides_lenght)
#         turtle.right(angle)

# all_polygons_sides = range(3,11)

# for sides in all_polygons_sides:
#     draw_polygon(timmy_the_turtle, sides, 100)

#171.randomwalk
# timmy_the_turtle.pensize(10)

# def dont_turn():
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(50)
    

# def turn_right():
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(50)

# def turn_left():
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.forward(50)

# def turn_back():
#     timmy_the_turtle.color(random.choice(colours))    
#     timmy_the_turtle.backward(50)
    

# steps = 0

# while steps < 100:
#     number = random.randrange(4)
#     if number == 0:
#         dont_turn()
#         steps += 1
#     if number == 1:
#         turn_left()
#         steps += 1
#     if number == 2:
#         turn_right()
#         steps += 1
#     if number == 3:
#         turn_back()
#         steps += 1

#172. 
# angle = 1   
# timmy_the_turtle.speed(0) 
# while angle != 360:
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.right(angle)
#     angle += 1

    



screen = Screen()
screen.exitonclick()