##############################################################
#
# Example file to create a graphic object in Python
#
# turtleIntro1.py
#
##############################################################

import turtle               # import the turtle module


canvas = turtle.Screen()    # get a canvas/screen to draw on
canvas.setup(600,500)       # set the canvas width and height


mike = turtle.Turtle()      # create a new turtle named mike

# Draw a big yellow circle and fill it
mike.setheading(90)
mike.width(4)
mike.fillcolor("yellow")
mike.penup()
mike.goto(50,0)
mike.pendown()
mike.begin_fill()
mike.circle(100)
mike.end_fill()

canvas.exitonclick()        # wait for a user click on the canvas
