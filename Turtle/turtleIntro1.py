# Rainier Hasbrouck
# Created 3/3/2021
# Last modified 3/3/2021
# First Turtle Intro

import turtle

canvas = turtle.Screen()
canvas.setup(600, 500)

k = turtle.Turtle()
k.shape("turtle")
k.setheading(90)
k.width(4)
k.fillcolor("yellow")
k.penup()
k.goto(50,0)
k.pendown()
k.begin_fill()
k.circle(100)
k.end_fill()

canvas.exitonclick()
