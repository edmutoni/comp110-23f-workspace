"""Turtle Tutorial"""
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

#to make the turtle do anything, use turtle_object_variable.method_name()

leo.color(99,204,250)
leo.penup()
leo.goto(-250,-100)
leo.pendown()

i: int = 0
leo.begin_fill()
leo.fillcolor(32,67,93)
while (i < 3):
    leo.forward(500)
    leo.left(120)
    i = i + 1
leo.end_fill()

done()