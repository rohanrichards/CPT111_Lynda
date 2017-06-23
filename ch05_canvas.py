#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

root = Tk()
canvas = Canvas(root)
canvas.pack()

canvas.config(width = 500, height = 500)
line = canvas.create_line(160, 360, 480, 120, fill = "blue", width = 5)
#get or set coordinates of canvas elements
print(canvas.coords(line))
canvas.coords(line,0,0,250,499,500,0) #3 pairs of coodinates to make multiple points in the line
#canvas.coords(line, range(0,500, 50), range(0,500, 50)) #doesn't work
#can smooth lines
#canvas.itemconfigure(line, splinesteps = 5)
# canvas.itemconfigure(line, smooth = True)

#clear the canvas
#canvas.delete("all")

rect = canvas.create_rectangle(160,120,480, 360)
canvas.itemconfigure(rect, fill = "yellow")
oval = canvas.create_oval(50, 50, 100, 100)
oval2 = canvas.create_oval(160,120,480, 360)
arc = canvas.create_arc(50,100,100, 150)
canvas.itemconfigure(arc, start = 0, extent = 180, fill = "green")
poly = canvas.create_polygon(160,360, 320, 480, 480, 360, fill="blue")
text = canvas.create_text(320, 240, text = "Python!", font = ("Courier", 32, "bold"))
logo = PhotoImage(file = "python_logo.gif")
image = canvas.create_image(320,240, image = logo)
#lift an lower method for display order / zindex
canvas.lift(text)
canvas.lower(image)
#can move it to positions based on other elements
canvas.lower(image, text) #place image just below text

#can add UI elements on the canvas
button = Button(canvas, text = "im a button on a canvas")
canvas.create_window(320, 60, window = button)

#tags are good for grouping items
canvas.itemconfigure(rect, tag = ("shape"))
canvas.itemconfigure(oval, tag = ("shape", "round"))
#now configure all shapes easily
canvas.itemconfigure("shape", fill = "grey")

root.mainloop()