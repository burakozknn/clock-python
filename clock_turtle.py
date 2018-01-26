import turtle
screen=turtle.Screen()
pen = turtle.Turtle()
screen.bgcolor("lightgreen")
pen .pensize(3)
pen .shape("turtle")


height=150
angle=20

for i in range(12):
   for j in range(1):
    pen .stamp()
    pen .penup()
    pen .forward(height)
    pen .stamp()
    pen .left(180)
    pen .forward(height)
    pen .left(180)



   pen .right(angle+10)
   pen .forward(height)
   pen .stamp()
   pen .left(180)
   pen .forward(height)
   pen .left(180)








screen.mainloop()
