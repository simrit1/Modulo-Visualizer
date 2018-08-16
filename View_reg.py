
from turtle import *
import Tkinter as tk
from tkColorChooser import askcolor
from mingus.midi import fluidsynth
fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2',"alsa")

def getDots(n, Link, view, dotColorNode):
    scale = 6 #increses / decreases the size of the patterns to a factor of scale
    t.tracer(0) if view else t.tracer(2)
    for x in range(n):
        t.dot(5, dotColorNode)
        Link[x] = t.position()
        t.forward(scale * 360.0/n) #I want all of the shapes to be to same relative size
        t.left(360.0/n) #After simpliying (n-2) * 180 given that I need to find the complimentary angle
    return Link

def createPoly(tTable, n, view,lineColor, dotColorNode, dotColorDest):
    Link = [0] * int(n) #Creating list to connect nodes, rounds any floats
    t.color(lineColor)
    t.speed(0)
    t.penup()
    Link = getDots(n, Link, view, dotColorNode)
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
        t.dot(5, dotColorDest)# before it goes back change the color of the targeted node
        t.goto(Link[x])
    t.penup()
    t.goto(Link[0]) #The pen needs to go back to the start so the next pattern can be drawn
    done()

def changeLineColor():
    color = askcolor()[1]
    f4.set(color)
    canvas.itemconfig(Line, fill = color)

def changeBackColor():
    t.screen.bgcolor(askcolor()[1])

def changeNodeColor():
    f5.set(askcolor()[1])

def changeHitNodeColor():
    f6.set(askcolor()[1])


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


f = tk.IntVar()
e2 = tk.Scale(master = root, from_=50, to=1000, variable=f, length=700, orient=tk.HORIZONTAL, label="# of Nodes").pack(side = tk.BOTTOM)
f.set(0)

f2 = tk.StringVar()
f2.set("2")
e2 = tk.Entry(master = root, textvariable=f2).pack(side = tk.TOP)

f4 = tk.StringVar()
f4.set("red")
f5 = tk.StringVar()
f5.set("red")
f6 = tk.StringVar()
f6.set("red")

View = tk.Button(master = root, text = "View", command = lambda: createPoly(float(f2.get()), int(f.get()), True ,f4.get(), f5.get(), f6.get())).pack(side = tk.RIGHT)
Draw = tk.Button(master = root, text = "Draw", command = lambda: createPoly(float(f2.get()), int(f.get()), False ,f4.get(), f5.get(), f6.get())).pack(side = tk.RIGHT)
Clear = tk.Button(master = root, text = "Clear", command = t.clear).pack(side = tk.RIGHT)
BackColor = tk.Button(master = root, text = "Background Color", command = changeBackColor).pack(side = tk.RIGHT)
LineColor = tk.Button(master = root, text = "Line Color", command = changeLineColor).pack(side = tk.RIGHT)
NodeColor = tk.Button(master = root, text = "Node Color", command = changeNodeColor).pack(side = tk.RIGHT)
HitNodeColor = tk.Button(master = root, text = "Hit Node Color", command = changeHitNodeColor).pack(side = tk.RIGHT)
#Line = canvas.create_line(300, 380 , 350, 380, fill=f4.get(), width=10)
#Node = canvas.create_oval(300, 300 , 350, 350, fill=f4.get())


#init()

root.mainloop()
