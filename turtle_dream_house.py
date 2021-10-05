import math
from turtle import *
import turtle


#set bakground color
turtle.bgcolor("skyblue")

#create turtle
obj = turtle.Turtle()
obj.pencolor("black")
obj.speed(10)

#def rectangle
def rectangle(obj, width, height, color):
    obj.fillcolor(color)
    obj.begin_fill()
    obj.forward(width)
    obj.left(90)
    obj.forward(height)
    obj.left(90)
    obj.forward(width)
    obj.left(90)
    obj.forward(height)
    obj.left(90)
    obj.end_fill()

#def triagle
def triagle(obj, width, color):
    obj.fillcolor(color)
    obj.begin_fill()
    obj.forward(width)
    obj.left(135)
    obj.forward(width / math.sqrt(2))
    obj.left(90)
    obj.forward(width / math.sqrt(2))
    obj.left(135)
    obj.end_fill()

#obj.penup()
#obj.goto(0,0)
#obj.pendown()
#triagle(obj,100, "red")

#def parallelogram
def parallelogram(obj, width, side, color):
    obj.fillcolor(color)
    obj.begin_fill()
    obj.left(30)
    obj.forward(width)
    obj.left(60)
    obj.forward(side)
    obj.left(120)
    obj.forward(width)
    obj.left(60)
    obj.forward(side)
    obj.left(120)
    obj.end_fill()

#def sun rays
def rays(obj, r, width, width2):
    for i in range(8):
      obj.penup()
      obj.forward(r)
      obj.pendown()
      obj.forward(width)
      obj.penup()
      obj.backward(r + width)
      obj.left(45)
      obj.penup()
      obj.forward(r)
      obj.pendown()
      obj.forward(width2)
      obj.penup()
      obj.backward(r + width2)

#in fornt of house
obj.penup()
obj.goto(-250,-200)
obj.pendown()
rectangle(obj, 130, 150, "pink")

#house side
obj.penup()
obj.goto(-120,-200)
obj.pendown()
parallelogram(obj, 130, 150, "pink")

#roof
obj.penup()
obj.goto(-250,-50)
obj.right(30)
obj.pendown()
obj.fillcolor("red")
obj.begin_fill()
for i in range(3):
    obj.forward(130)
    obj.left(120)
obj.end_fill()    

#roof side
obj.goto(-120,-50)
obj.left(30)
rectangle(obj, 130, 130, "orange")

#door
obj.penup()
obj.goto(-210, -200)
obj.right(30)
obj.pendown()
rectangle(obj, 50, 90, "yellow")

#window
obj.penup()
obj.goto(-70,-125)
obj.pendown()
parallelogram(obj, 50, 60, "blue")

#trunk
obj.penup()
obj.goto(150,-210)
obj.right(30)
obj.pendown()
rectangle(obj, 30, 60, "brown")

#leaves
obj.penup()
obj.goto(100,-150)
obj.pendown()
triagle(obj, 130, "green")
obj.penup()
obj.goto(110,-100)
obj.pendown()
triagle(obj, 110, "green")
obj.penup()
obj.goto(120,-55)
obj.pendown()
triagle(obj, 90, "green")

#sun
obj.penup()
obj.goto(120,150)
obj.pendown()
obj.fillcolor("yellow")
obj.begin_fill()
obj.circle(30)
obj.end_fill()


#rays
obj.penup()
obj.goto(120, 180)
obj.pendown()
rays(obj, 30, 30, 5)





 

        
 





turtle.done()