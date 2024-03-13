import turtle


def draw_square(x, y):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

turtle.Screen().onclick(draw_square)
turtle.mainloop()


"""
##############################################################################################################
########################## to show the window just thats enough ##############################################
##############################################################################################################


import turtle
from turtle import *

window_width()
window_height()

screensize(canvwidth=400, canvheight=500)
turtle.Screen()
turtle.done()



"""
