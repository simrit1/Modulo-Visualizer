from Tkinter import *
from math import *

master = Tk()

def placeCoordinates():
    x=0.0
    y=0.0
    for z in range(360):
        x = 500 + scale.get() * sin((z*pi)/180)
        y = 430 + scale.get() * cos((z*pi)/180)
        corrdinates[z] = (x, y)

def draw():
    for x in range(360):
        value = (x * degree.get()) % 360
        w.create_line(corrdinates[x][0], corrdinates[x][1], corrdinates[int(value)][0], corrdinates[int(value)][1], fill = colors[x % 69])

def animate():
    degree.set(degree.get() + 0.01)
    master.after(0, draw)
    master.after(0, updateCounter)
    master.after(10, w.delete("all"))
    master.after(10, animate)

def updateCounter():
    w.create_text(500,950, text=("Factor =%s" % str(degree.get())), fill='#EFEFEF', font=("arial", 60))

colors = ["#660000", "#990000", "#CC0000", "#FF0000", "#CC3333", "#FF6666", "#FF9999", "#FFCCCC", "#663300", "#993300",
        "#CC3300", "#FF3300", "#FF6600", "#FF6633", "#FF9966", "#FFCC99", "#996633", "#CC9900", "#FFCC00", "#FFFF00",
        "#FFFF33", "#FFFF66", "#FFFF99", "#FFFFCC", "#003300", "#006600", "#009900", "#00CC00", "#00FF00", "#66FF66",
        "#CCFFCC", "#003333", "#336666", "#009999", "#00CCCC", "#66CCCC", "#66FFCC", "#99FFCC", "#003399", "#0033FF",
        "#0066FF", "#00CCFF", "#00FFFF", "#99FFFF", "#CCFFFF", "#000066", "#000099", "#0000CC", "#0000FF", "#3366FF",
        "#3399FF", "#66CCFF", "#99CCFF", "#330066", "#660099", "#663399", "#9900CC", "#9933FF", "#9966FF", "#9999FF",
        "#CCCCFF", "#660066", "#990066", "#CC0099", "#FF0099", "#FF00FF", "#FF66FF", "#FF99FF", "#FFCCFF"]

w = Canvas(master, width=1000, height=1000)
w.pack()

w.configure(background='black')

scale = IntVar()
scale.set(420)

degree = DoubleVar()
degree.set(0) #Start Value

x,y = [],[]
for i in range(360):
        xcorrdinate = DoubleVar()
        x.append(xcorrdinate)
        ycorrdinate = DoubleVar()
        y.append(ycorrdinate)
corrdinates = list(zip(x, y))

placeCoordinates()

master.after(0, animate)


master.mainloop()
