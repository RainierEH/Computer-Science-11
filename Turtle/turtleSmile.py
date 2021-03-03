##############################################################
#
# Example file to create a graphic object in Python
# Adds in multiple shapes and text
#
# turtleIntro2.py
#
##############################################################

import turtle               # import the turtle module


canvas = turtle.Screen()    # get a canvas/screen to draw on
canvas.setup(600,500)       # set the canvas width and height


mike = turtle.Turtle()      # create a new turtle named mike
mike.shape("turtle")        # set mike's shape
mike.color("black")         # set mike's color to green

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

# Draw eyes and a smile
#first eye
mike.penup()
mike.goto(-90,40)
mike.seth(-135)
mike.pendown()
mike.fillcolor("black")
mike.begin_fill()
for i in range(2): 
    mike.circle(20,90) 
    mike.circle(10,90)
mike.end_fill()

#second eye
mike.penup()
mike.goto(-30,40)
mike.seth(-135)
mike.pendown()
mike.fillcolor("black")
mike.begin_fill()
for i in range(2): 
    mike.circle(20,90) 
    mike.circle(10,90)
mike.end_fill()

#smile
mike.penup()
mike.goto(-100,-25)
mike.seth(-90)
mike.pendown()
mike.fillcolor("black")
mike.begin_fill()
mike.circle(50,180) 
mike.end_fill()


#add text
mike.penup()
mike.goto(-30,-200)
mike.write("Smile", align = "center", font = ("Bradley Hand ITC", 40, "bold"))


canvas.exitonclick()        # wait for a user click on the canvas
