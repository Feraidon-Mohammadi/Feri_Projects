from turtle import *

speed(10) #geschwindigkeit
shape("turtle")
begin_fill()
bgcolor("purple")
goto(0, 75)  
forward(400)          
right(90)             
forward(400)          
right(90)             
forward(400)          
right(90)             
forward(400) 
right(90)  
end_fill()

#dach 
goto(0,75)
begin_fill()
left(35)
forward(240)
right(70)
forward(240)
fillcolor("red")
end_fill()

# link fenster
goto(90, -35)
begin_fill()
fillcolor("red")
forward(75)
right(90)
forward(75)
right(90)
forward(75)
right(90)
forward(75)
right(90)
end_fill()
# recht fenster
goto(300, -35)
begin_fill()
fillcolor("red")
forward(75)
right(90)
forward(75)
right(90)
forward(75)
right(90)
forward(75)
right(90)
end_fill()

#door
goto(190, -190)
begin_fill()
fillcolor()
left(35)
forward(50),
right(90)
forward(100)
right(90)
forward(50)
end_fill()









# (forward(400) , right(90))*4    
# f = forward(400)
# r = right(90)
# print(("f"+"r")*4)


# speed(1)
# shape("circle")
# pencolor("red")
# bgcolor("green")
# forward(100)
# right(90)
# forward(100)
input("Press any key to exit ...")
# # Press any key to exit ...
# home() #bewegt die Turtle zur Ausgangsposition (0, 0)

# fillcolor(252, 148, 3)  #ermöglicht z.B. das die Füllfarbe nun orange ist RGB steht für rot, grün, blau
# fillcolor("#ff0000")





