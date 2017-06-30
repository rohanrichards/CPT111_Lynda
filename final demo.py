#!/usr/bin/python3
# by Rohan Richards

from tkinter import *
from tkinter import ttk        

lineThickness = 2
mouseDown = False

class Palette:
    def __init__(self, master):
        # palette
        self.palette = ttk.Frame(master)
        self.palette.grid(row=0, column=0, ipadx=25, ipady=25, stick="nsew")
        self.palette.config(relief=SUNKEN)

        # ttk.Label(statusBar, text = 'Palette', background = 'Green').pack()
        ttk.Button(self.palette, text="Thickness 1", command=lambda: self.setThickness(1)).pack(padx=5, pady=5)
        ttk.Button(self.palette, text="Thickness 2", command=lambda: self.setThickness(2)).pack(padx=5, pady=5)
        ttk.Button(self.palette, text="Thickness 3", command=lambda: self.setThickness(3)).pack(padx=5, pady=5)

    def setThickness(self, size):
        global lineThickness
        lineThickness = 2 * size

class StatusBar:
    def __init__(self, master):
        # status bar
        self.statusBar = ttk.Frame(master)
        self.statusBar.grid(row=1, column=0, columnspan=2, stick='nsew')
        self.statusBar.config(relief=SUNKEN)

        ttk.Label(self.statusBar, text = "Thickness: 2").pack(anchor = "nw", padx=5, pady=5, side = LEFT)
        ttk.Label(self.statusBar, text="Colour: NA").pack(anchor="nw", padx=5, pady=5, side = LEFT)

root = Tk()
root.title("Simple Canvas Demo")
root.geometry('640x480+500+500')
root.resizable(False, False)

palette = Palette(root)
status = StatusBar(root)



# main frame
mainFrame = ttk.Frame(root)
mainFrame.grid(row = 0, column = 1, stick = 'nsew')

canvas = Canvas(mainFrame, bg = 'white')
canvas.pack(fill = BOTH, expand = YES)

def canvasClick(event):
    global mouseDown
    mouseDown = True

def canvasRelease(event):
    global mouseDown
    mouseDown = False

def mouseMove(event):
    # global mouseDown
    # if(mouseDown):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval((x-lineThickness, y-lineThickness, x+lineThickness, y+lineThickness), fill = 'green', width = 0)

# canvas.bind('<1>', canvasClick)
# canvas.bind('<ButtonRelease-1>', canvasRelease)
canvas.bind('<B1-Motion>', mouseMove)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 0, minsize = 25)
root.columnconfigure(0, weight = 0, minsize = 100)
root.columnconfigure(1, weight = 3)

root.mainloop()
