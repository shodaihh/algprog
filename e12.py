#usr/bin/env python3
#-*-coding:utf-8-*-
import turtle

def desenheSprite(tartaruga, num_pernas, comp_pernas):
    angulo = 360 / num_pernas
    for i in range(num_pernas):
        tartaruga.forward(comp_pernas)
        tartaruga.backward(comp_pernas)
        tartaruga.right(angulo)

tartaruga = turtle.Turtle()
desenheSprite(tartaruga, 15, 120)
exit(0)
