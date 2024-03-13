import another_module

#print(another_module.another_variable)
# object and class
# object and attribute
# object and methods
#

from turtle import Turtle, Screen

timmy =Turtle() # an object of the class Turtle
print(timmy)
timmy.shape("turtle")
timmy.color("red")


for i in range(10):
    timmy.forward(100)

    for j in range(1):
        timmy.right(100)

        for f in range(3):
            timmy.right(100)




my_screen = Screen() # create object (my_screen) from the class Screen
print(my_screen.canvwidth)
my_screen.exitonclick()
