# try this either as a .py file or in the python shell
# import turtle
# window = turtle.Screen()
# liz = turtle.Turtle()
# liz.pensize(2)
# liz.color("red", "blue")
# # the distance we want the pointer to travel each time
# DIST = 100
# for x in range(0,6):
#     print "x", x
#     for y in range(1,5):
#         print "y", y
#         # turn the pointer 90 degrees to the right
#         liz.right(90)
#         # advance according to set distance
#         liz.forward(DIST)
#     # add to set distance
#     DIST += 20

import turtle        # allows us to use the turtles library
import time
wn = turtle.Screen()       # creates a graphics window
alex = turtle.Turtle()     # create a turtle named alex
alex.speed(10)
alex.pensize(2)
alex.color("purple", "blue")
for x in range(1, 300):
    alex.forward(x*2)           # tell alex to move forward by 150 units
    alex.left(90)               # turn by 90 degrees
time.sleep(2)
