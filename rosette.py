#rosette.py
import turtle
import math
t = turtle.Pen()
t.speed(0)
t.hideturtle()
t.pencolor("light blue")
turtle.bgcolor("papayawhip")
# Ask the number of sides the user would like
circles = int( turtle.numinput("Number of circles","How many circles do you want?"))
# Draw a colorful spiral with the user-specified number of sides
for x in range (circles):
	t.pensize(5)
	t.pencolor("royalblue")
	t.circle(100)
	t.left(360/circles)
for x in range (circles):
	t.pensize(3)
	t.pencolor("blue")
	t.circle(50)
	t.left(360/circles)
for x in range (circles):
	t.pensize(2)
	t.pencolor("deepskyblue")
	t.pendown()
	t.circle(25)
	t.left(360/circles)
	t.penup()


