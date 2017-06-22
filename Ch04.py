#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

def popup():
    popup = Toplevel(root)
    popup.title("Popup")
    #popup.state("iconic") #minimised
    #popup.state("withdrawn") #ninja window
    #geometry string is width, height, from left, from top
    popup.geometry("500x300+100+25")
    popup.resizable(False, False)
    #also can set max and min size
    popup.maxsize(640, 480)
    popup.minsize(200, 200)
    popup.resizable(True, True)
    ttk.Button(popup, text="Destroy", command=lambda: popup.destroy()).pack()


frame = ttk.Frame(root)
frame.pack()
frame.config(width=250, height=250)
frame.config(relief=RIDGE)

ttk.Button(frame, text="Button", command=popup).pack() #sets frame to use grid?
frame.config(padding=(30,15))

ttk.LabelFrame(root, height=250, width=250, text="This frame has a label").pack()


notebook = ttk.Notebook(root)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
notebook.add(frame1, text="This is frame 1")
notebook.add(frame2, text="This is frame 2")
notebook.insert(1, frame3, text="This is frame 3")
notebook.forget(0)
notebook.insert(1, frame1, text="This is frame 1")

ttk.Button(frame1, text="Button").pack()

#states for tabs exist
#disabled, hidden etc

root.mainloop()
