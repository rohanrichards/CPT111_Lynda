#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *

root = Tk()
Label(root, text="Hello, Tkinter!").pack()
Label(root, text="Another label, does it go under?").pack()
Label(root, text="").pack() #blank labels make whitespace...handy

#launches program?
root.mainloop()
#blocks the thread!
print("testing testing 123")