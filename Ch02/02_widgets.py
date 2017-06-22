#!/usr/bin/python3
# widgets.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk #ttk is THEMED tk widgets (change appearance to match OS)

#parent widget passed into widgets on creation
#parents are "graphical managers" of their children
#positions are probably relative?

def handleSecondButtonPress():
    button.config(text="you clicked me again!!", command=handleButtonPress)

def handleButtonPress():
    #keep handler code short and responsive
    print("Clicked")
    button.config(text = "you clicked me!", command = handleSecondButtonPress)

root = Tk()

#using ttk button widget, so its themed
button = ttk.Button(root, text = 'Click Me') #pass in the root as the parent
button.pack() #pack method tells TK to put it into its parent

print(button['text']) #accesses property "text"
button['text'] = 'Press Me' #assigns new value to prop
button.config(text = 'Push Me') #other way to set values
ttk.Label(root, text ='Hello, Tkinter!').pack()

#modify the command param
button.config(command = handleButtonPress)

myButton = ttk.Button(root, text = "My Button")
#place at specific location
myButton.place(x=250, y=250)

# mainloop() add
root.mainloop()