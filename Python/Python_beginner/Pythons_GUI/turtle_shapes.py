import turtle

# wn = turtle.Screen()
#
#
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")
# t.speed(12)  # Slow speed for better visibility
# list_ff = [1, 2, 3, 4, 5, 6, 7 ,3, 4, 4, 5, 6, 7]
#
# for f in list_ff:
#
# 	looop = [t.forward(10), t.right(5), t.right(50), t.right(5), t.forward(10), t.right(50),
# 	t.forward(10), t.right(5), t.forward(10), t.right(90)]
# 	for i in list_ff:
# 		looop1 = [t.right(5), t.forward(10)]
# 		for o in list_ff:
# 			loop2 = [t.right(2), t.forward(5), t.color("green")]


# wn = turtle.Screen()
#
#
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")
# t.speed(12)  # Slow speed for better visibility
# list_ff = [1, 2, 3, 4, 5, 6, 7 ,3, 4, 4, 5, 6, 7]
#
# for f in list_ff:
#
# 	looop = [t.forward(101), t.right(15), t.right(510), t.right(51), t.forward(101),
# 	t.right(510), t.forward(110), t.right(51), t.forward(110), t.right(910)]
# 	for i in list_ff:
# 		looop1 = [t.right(115), t.forward(110)]
# 		for o in list_ff:
# 			loop2 = [t.right(12), t.forward(51), t.color("green")]


import turtle
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Special Turtle Shape")
wn.bgcolor("black")

# Create a turtle named "artist"
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.color("cyan")
t.width(5)

# Hide the turtle initially
t.hideturtle()

colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta",]


# Function to draw the shape


def draw_shape():
    for i in range(1000):
        color = random.choice(colors)  # Choose a random color
        t.color(color)
        t.forward(1000)  # Adjust the distance to fit the screen
        t.right(222)  # Adjust the angle to get interesting patterns


# Function to slowly hide the oldest lines
def hide_old_lines():
    for _ in range(360):
        t.undo()  # Undo the last turtle action (draw)
        time.sleep(0.8)  # Adjust the sleep time for smoother animation


# Main loop
while True:
    t.penup()
    t.goto(-500, -200)  # Start from the center
    t.pendown()
    draw_shape()
    hide_old_lines()

wn.mainloop()
