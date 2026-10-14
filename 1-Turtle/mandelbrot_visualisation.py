import turtle
t=turtle.Turtle()
turtle.tracer(0, 0)   # turn off per move redraw 
t.hideturtle()
t.penup()
t.speed(0)
acorn = -0.75
bcorn = -0.1
size = 0.02

for j in range(1000):
    for k in range(1000):
        count = 0
        ca = acorn + j*size/1000
        cb = bcorn + k*size/1000
        zx=0
        zy=0

        while count < 100 and (zx**2 + zy**2) <4:
            count +=1
            xtemp = zx**2 - zy**2
            zy = 2*zx*zy +cb
            zx= xtemp + ca
        if count == 100:
            t.goto(j-100,k-100)
            t.dot(2,"black")

turtle.update()
turtle.done()