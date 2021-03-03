##############################################################
#
# Example file to create a graphic object in Python
#
# turtleIntro3.py - incorporated draggable turtle to give coords
#
##############################################################

import turtle

#Create the screen
wn  = turtle.Screen()
wn.setup(800,600)


#Create two turtles to drag and track position
runner = turtle.Turtle("triangle")
runner.color("red")
runner.speed("fastest")
runner.penup()
runner.setposition(200, 200)

marker = turtle.Turtle(visible=False)  # our virtual magic marker
marker.penup()
marker.color("black")
FONT = ('Arial', 24, 'normal')
marker.write(runner.position(), align='center', font=FONT)  # so we can undo it

#Create an event handler to track the coordinateson the screen
def drag_handler(x, y):
    runner.ondrag(None)  # disable handler while in handler
    marker.undo()  # erase previous position
    marker.write((x, y), align='center', font=FONT)
    runner.setheading(runner.towards(x, y))  # head towards new location
    runner.setposition(x, y)
    runner.ondrag(drag_handler)

#Attach the handler to an action
runner.ondrag(drag_handler)

wn.mainloop()
