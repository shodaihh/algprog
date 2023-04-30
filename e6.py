#usr/bin/env python
#-*-coding:utf-8-*-
import turtle

def desenhaPoli(t, n, tamanho):
    for i in range(n):
        t.forward(tamanho)
        t.left(360/n)

def desenhaTrianguloEqui(t, tamanho):
    desenhaPoli(t, 3, tamanho)

tartaruga = turtle.Turtle()
desenhaTrianguloEqui(tartaruga, 100)
turtle.done()
exit(0)
