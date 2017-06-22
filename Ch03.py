#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

#Images
myLabel = ttk.Label(root,
                    text="Some really long text here with some spaces and... \nA new line and tabs \t to create more space and make it crazy long")
myLabel.config(wraplength=150)  # wraplength is in pixels
myLabel.config(justify=CENTER)
# myLabel.config(justify=LEFT)
# myLabel.config(justify=RIGHT)
myLabel.config(foreground="white", background="black")
myLabel.config(font=("Courier", 18, "italic"))  # pass in a list
myLabel.pack()

myImage = PhotoImage(file="python_logo.gif")
myLabel.config(image=myImage)
myLabel.config(compound="text")  # show text value of label
myLabel.config(compound="center")  # show both with image position
myLabel.config(compound="left")  # image on left

myLabel.img = myImage  # stores a reference to the image object within the tk element
# this will stop GC getting rid of the image, because TK will hold onto the label
myLabel.config(image=myLabel.img)

disabledButton = ttk.Button(root, text="I'm disabled!")
disabledButton.state(["disabled"])
disabledButton.pack()
print(disabledButton.instate(["disabled"]))  # check the state of a button
smallImage = myImage.subsample(3, 3)  # make images smaller (grabs every nth pixel)
disabledButton.config(image=smallImage, compound=LEFT)

##Choices
def uncheck(thing):
    #thing.state(["!selected"])
    print(spam.get())
checkbox = ttk.Checkbutton(root, text="try to check me", command=lambda: uncheck(checkbox))
checkbox.pack()
spam = StringVar()
spam.set("SPAM!")
checkbox.config(variable = spam, onvalue="SPAM please", offvalue="nospam") #hooks variable into the button
variableLabel = ttk.Label(root, textvariable=spam).pack() #ties label to the StringVar and updates it on change

##Entry elements
typedWords = StringVar()
entry = ttk.Entry(root, width=30, textvariable=typedWords).pack()
variableLabel = ttk.Label(root, textvariable=typedWords).pack() #ties label to the StringVar and updates it on change

##Progress bar
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progress.config(mode = "indeterminate")
progress.pack()
progress.start()

dProgress = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
dProgress.pack()
value = DoubleVar()
dProgress.config(mode = "determinate", maximum= 100, value = 52, variable = value)
scale = ttk.Scale(root, orient=HORIZONTAL, length=200, variable=value, from_=0, to=100).pack()
ttk.Label(root, textvariable=value).pack()



root.mainloop()
