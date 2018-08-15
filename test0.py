
from turtle import *
import Tkinter as tk
from tkColorChooser import askcolor
from mingus.midi import fluidsynth
fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2',"alsa")

def getDots(Link, view):
    scale = 6 #increses / decreases the size of the patterns to a factor of scale
    t.tracer(0)
    for x in range(numONodes.get()):
        t.dot(5, nodeColor.get())
        Link[x] = t.position()
        t.forward(scale * 360.0/numONodes.get()) #I want all of the shapes to be to same relative size
        t.left(360.0/numONodes.get()) #After simpliying (n-2) * 180 given that I need to find the complimentary angle
    return Link

def createPoly(view):
    colors = ["#660000", "#990000", "#CC0000", "#FF0000", "#CC3333", "#FF6666", "#FF9999", "#FFCCCC", "#663300", "#993300",
              "#CC3300", "#FF3300", "#FF6600", "#FF6633", "#FF9966", "#FFCC99", "#996633", "#CC9900", "#FFCC00", "#FFFF00",
               "#FFFF33", "#FFFF66", "#FFFF99", "#FFFFCC", "#003300", "#006600", "#009900", "#00CC00", "#00FF00", "#66FF66",
               "#CCFFCC", "#003333", "#336666", "#009999", "#00CCCC", "#66CCCC", "#66FFCC", "#99FFCC", "#003399", "#0033FF",
               "#0066FF", "#00CCFF", "#00FFFF", "#99FFFF", "#CCFFFF", "#000066", "#000099", "#0000CC", "#0000FF", "#3366FF",
               "#3399FF", "#66CCFF", "#99CCFF", "#330066", "#660099", "#663399", "#9900CC", "#9933FF", "#9966FF", "#9999FF",
               "#CCCCFF", "#660066", "#990066", "#CC0099", "#FF0099", "#FF00FF", "#FF66FF", "#FF99FF", "#FFCCFF"]
    Link = [0] * int(numONodes.get()) #Creating list to connect nodes, rounds any floats
    t.color(lineColor.get())
    t.speed(0)
    t.penup()
    Link = getDots(Link, view)
    if view:
        t.tracer(0)
    else:
        t.tracer(1)
    for x in range(numONodes.get()):
        t.color(colors[x % 69])
        t.penup()
        t.goto(Link[x])
        t.pendown()
        value = int(x * float(degree.get()))
        fluidsynth.play_Note(value % 100,100)
        if (value >= numONodes.get()):
            t.goto(Link[value % numONodes.get()])
        else:
           t.goto(Link[value])
        t.dot(5, hitNodeColor.get())# before it goes back change the color of the targeted node
        t.goto(Link[x])
    t.penup()
    t.goto(Link[0]) #The pen needs to go back to the start so the next pattern can be drawn
    done()

def changeLineColor():
    color = askcolor()[1]
    lineColor.set(color)
    canvas.itemconfig(Line, fill = color)

def changeBackColor():
    t.screen.bgcolor(askcolor()[1])

def changeNodeColor():
    nodeColor.set(askcolor()[1])

def changeHitNodeColor():
    hitNodeColor.set(askcolor()[1])

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
t.pensize(1)

numONodes = tk.IntVar()
e2 = tk.Scale(master = root, from_=50, to=1000, variable=numONodes, length=700, orient=tk.HORIZONTAL, label="# of Nodes").pack(side = tk.BOTTOM)
numONodes.set(0)

degree = tk.StringVar()
degree.set("2")
e2 = tk.Entry(master = root, textvariable=degree).pack(side = tk.TOP)

lineColor = tk.StringVar()
lineColor.set("red")
nodeColor = tk.StringVar()
nodeColor.set("red")
hitNodeColor = tk.StringVar()
hitNodeColor.set("red")

View = tk.Button(master = root, text = "View", command = lambda: createPoly(True)).pack(side = tk.RIGHT)
Draw = tk.Button(master = root, text = "Draw", command = lambda: createPoly(False)).pack(side = tk.RIGHT)
Clear = tk.Button(master = root, text = "Clear", command = t.clear).pack(side = tk.RIGHT)
BackColor = tk.Button(master = root, text = "Background Color", command = changeBackColor).pack(side = tk.RIGHT)
LineColor = tk.Button(master = root, text = "Line Color", command = changeLineColor).pack(side = tk.RIGHT)
NodeColor = tk.Button(master = root, text = "Node Color", command = changeNodeColor).pack(side = tk.RIGHT)
HitNodeColor = tk.Button(master = root, text = "Hit Node Color", command = changeHitNodeColor).pack(side = tk.RIGHT)
#Line = canvas.create_line(300, 380 , 350, 380, fill=lineColor.get(), width=10)
#Node = canvas.create_oval(300, 300 , 350, 350, fill=lineColor.get())

#init()

root.mainloop()
