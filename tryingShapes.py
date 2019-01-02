from turtle import *
import random

s=Screen()
tom = Turtle()
tom.shape('turtle')
tom.speed(0)
s.tracer(0.0)
tom.color('white')
a=2
w=20
tom.hideturtle()
while True:
    for j in range(5):
        for i in range(320):
            tom.width(w)
            w=w-0.06
            tom.forward(10)
            tom.lt(a)
            a=a+0.02
        tom.pu()
        tom.goto(0,0)
        tom.pd()
        tom.left(360.0/5)
        a=2
        w=20
    tom.update()
    tom.clear()
    tom.goto(0,0)
    tom.lt(0.001)
