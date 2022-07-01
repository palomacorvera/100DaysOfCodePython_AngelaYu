#import colorgram

#rgb_colors = []
#colors = colorgram.extract('img.jpg', 30)

#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b

    #rgb_colors.append((r, g, b))

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

my_turtle = Turtle()

my_turtle.speed("fastest")

color_list = [(123, 8, 40), (5, 115, 139), (103, 154, 6), (121, 223, 100), (159, 198, 8), (57, 100, 6), (121, 99, 8)]

for i in range (10):
    for i in range (10):
        my_turtle.color(random.choice(color_list))
        my_turtle.dot(size=20)
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()
    
    my_turtle.penup()
    my_turtle.backward(500)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.pendown()

screen.exitonclick()