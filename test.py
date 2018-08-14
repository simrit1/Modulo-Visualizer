
from turtle import *
import Tkinter as tk
from mingus.midi import fluidsynth
fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2',"alsa")

def getDots(n, Link, view):
    scale = 6 #increses / decreases the size of the patterns to a factor of scale
    t.tracer(0) if view else t.tracer(2)
    for x in range(n):
        t.dot(5, 'red')
        Link[x] = t.position()
        t.forward(scale * 360.0/n) #I want all of the shapes to be to same relative size
        t.left(360.0/n) #After simpliying (n-2) * 180 given that I need to find the complimentary angle
    return Link

def createPoly(tTable, n, view):
    Link = [0] * int(n) #Creating list to connect nodes, rounds any floats
    t.color('red', 'yellow')
    t.speed(0)
    t.penup()
    Link = getDots(n, Link, view)
    if view:
        t.tracer(0)
    else:
        t.tracer(1)
    for x in range(n):
        t.penup()
        t.goto(Link[x])
        t.pendown()
        value = int(x * tTable)
        fluidsynth.play_Note(value % 100,100)
        print(value % 100)
        if (value >= n):
            t.goto(Link[value % n])
        else:
           t.goto(Link[value])
        t.goto(Link[x])
        t.dot(5, 'red')# before it goes back change the color of the targeted node
    t.penup()
    t.goto(Link[0]) #The pen needs to go back to the start so the next pattern can be drawn
    done()

root = tk.Tk()
root.title('Mulitplication Visualizer')
canvas = tk.Canvas(master = root, width = 800, height = 800)
root.resizable(False, False)
canvas.pack()
fluidsynth.init("soundfont.SF2")

t = RawTurtle(canvas)
t.ht() #Hides curser
t.screen.bgcolor('black')
t.penup()
t.sety(-325)
t.pensize(2)

f = tk.StringVar()
e2 = tk.Entry(master = root, textvariable=f).pack(side = tk.TOP)
f.set("200")

f2 = tk.StringVar()
f2.set("2")
e2 = tk.Entry(master = root, textvariable=f2).pack(side = tk.TOP)

View = tk.Button(master = root, text = "View", command = lambda: createPoly(float(f2.get()), int(f.get()), True)).pack(side = tk.TOP)
Draw = tk.Button(master = root, text = "Draw", command = lambda: createPoly(float(f2.get()), int(f.get()), False)).pack(side = tk.TOP)
Clear = tk.Button(master = root, text = "Clear", command = t.clear).pack(side = tk.BOTTOM)


#init()

root.mainloop()
