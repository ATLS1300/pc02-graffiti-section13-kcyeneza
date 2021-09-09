#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use


# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.colormode(255)

turtle.forward(100)

turtle.right(90)

turtle.forward(100)

turtle.begin_fill()

turtle.right(90)

turtle.forward(100)

turtle.right(90)

turtle.forward(100)

turtle.right(45)

turtle.forward(100)

turtle.right(90)

turtle.forward(100)

turtle.begin_fill()

turtle.right(90)

turtle.forward(100)

turtle.right(90)

turtle.forward(100)

turtle.up()

turtle.forward(100)

turtle.goto(90,50)

turtle.goto(45,90)

turtle.down()

turtle.circle(9)

turtle.circle(108)

turtle.up()

turtle.left(45)

turtle.left(90)

turtle.left(90)

turtle.left(90)

turtle.forward(100)

turtle.down()

turtle.forward(100)

turtle.pencolor("blue")

turtle.up()

turtle.goto(-30,-40)

turtle.left(90)

turtle.left(90)

turtle.forward(100)

turtle.down()

turtle.left(45)

turtle.begin_fill()

turtle.forward(45)

turtle.left(45)

turtle.right(45)

turtle.right(45)

turtle.forward(45)

turtle.left(45)

turtle.left(45)

turtle.left(22.5)

turtle.forward(45)

turtle.right(90)

turtle.forward(45)

turtle.undo()

turtle.left(22.5)

turtle.forward(45)

turtle.right(67.5)

turtle.undo()

turtle.left(67.5)

turtle.undo()

turtle.left(90)

turtle.left(22.5)

turtle.forward(45)

turtle.undo()

turtle.left(22.5)

turtle.forward(45)

turtle.left(45)

turtle.undo()

turtle.right(45)

turtle.forward(45)

turtle.undo()

turtle.right(22.5)

turtle.forward(45)

turtle.right(45)

turtle.undo()

turtle.left(45)

turtle.left(22.5)

turtle.left(45)

turtle.forward(45)

turtle.undo()

turtle.left(22.5)

turtle.forward(45)

turtle.right(45)

turtle.forward(45)

turtle.right(165)

turtle.right(90)

turtle.left(22.5)

turtle.forward(45)

turtle.right(45)

turtle.forward(45)

turtle.undo()

turtle.right(22.5)

turtle.forward(45)

turtle.forward(10)

turtle.forward(5)

turtle.end_fill()

turtle.pensize(5)

turtle.pencolor("pink")

turtle.pensize(30)

turtle.circle(30)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
