
from turtle import *
import Tkinter as tk

def createPoly(tTable, n):
    scale = 6 #increses / decreases the size of the patterns to a factor of scale
    Link = [0] * n #Creating list to connect nodes
    t.color('red', 'yellow')
    t.speed(0)
    t.penup()
    for x in range(n):
        t.dot(500/n if n >10 else 5, 'blue')
        Link[x] = t.position()
        t.forward(scale * 360.0/n) #I want all of the shapes to be to same relative size
        t.left(360.0/n) #After simpliying (n-2) * 180 given that I need to find the complimentary angle
    for x in range(n):
        t.penup()
        t.goto(Link[x])
        t.pendown()
        value = x * tTable
        if (value >= n):
            t.goto(Link[value % n])
        else:
           t.goto(Link[value])
        t.goto(Link[x])
    t.penup()
    t.goto(Link[0]) #The pen needs to go back to the start so the next pattern can be drawn
    print(t.pos())
    t.clear()
    done()

'''
def init():
    t.color('red', 'yellow')
    for x in range(100):
        t.dot(5, 'blue')
        t.forward(6 * 360.0/100)
        t.left(360.0/100)
    done()
'''

root = tk.Tk()
root.title('Mulitplication Visualizer')
canvas = tk.Canvas(master = root, width = 800, height = 800)
root.resizable(False, False)
canvas.pack()

t = RawTurtle(canvas)
t.ht() #Hides curser
t.screen.bgcolor('black')
t.penup()
t.sety(-325)

f = tk.StringVar()
e2 = tk.Entry(master = root, textvariable=f).pack(side = tk.TOP)
f.set("2")


f2 = tk.StringVar()
f2.set("2")
e2 = tk.Entry(master = root, textvariable=f2).pack(side = tk.TOP)

tk.Button(master = root, text = "View", command = lambda: createPoly(int(f2.get()), int(f.get()))).pack(side = tk.TOP)
tk.Button(master = root, text = "Draw", comman = lambda: createPoly(3,100)).pack(side = tk.BOTTOM)
tk.Button(master = root, text = "Draw", comman = lambda: createPoly(4,100)).pack(side = tk.BOTTOM)

#init()

root.mainloop()
