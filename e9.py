#usr/bin/env python
#-*-coding:utf-8-*-
import turtle

def Estrela(t, comprimento):
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    
    for i in range(5):
        t.forward(comprimento)
        t.right(144)
        t.forward(comprimento)
        t.right(144)
    
    t.hideturtle()
    turtle.done()

tartaruga = turtle.Turtle()
Estrela(tartaruga, 100)
exit(0)
