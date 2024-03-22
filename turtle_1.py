from turtle import Turtle
t=Turtle()
t.width(5) # For bolder lines
t.left(90) # Turn to face north
t.forward(50) # Draw a vertical line in black
t.left(90) # Turn to face west
t.up() # Prepare to move without drawing
t.forward(20) # Move to beginning of horizontal line
t.setheading(0) # Turn to face east
t.pencolor("red")
t.down() # Prepare to draw
t.forward(40) # Draw a horizontal line in red
t.hideturtle() # Make the turtle invisible

import turtle
s=turtle.getscreen()
t=turtle.Turtle()
t.forward(100) 
t.right(90) 
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)


import turtle
s=turtle.getscreen()
t=turtle.Turtle()
t.forward(100) 
t.left(120) 
t.forward(100)
t.left(120)
t.forward(100)