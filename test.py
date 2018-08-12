
from turtle import *
def createPoly(tTable, n):
    s = Screen()
    s.setup(300, 300)
    Link = [0] * n #Creating list to connect nodes
    color('red', 'yellow')
    speed(0)
    penup()
    for x in range(n):
        pendown()
        dot(1, 'blue')
        penup()
        Link[x] = position()
        forward(720.0/n) #I want all of the shapes to be to same relative size
        left(360.0/n) #After simpliying (n-2) * 180 given that I need to find the complimentary angle
    for x in range(n):
        penup()
        goto(Link[x])
        pendown()
        value = x * tTable
        if (value >= n):
            goto(Link[value % n])
        else:
           goto(Link[value])
        goto(Link[x])
    done()
createPoly(7, 148)
