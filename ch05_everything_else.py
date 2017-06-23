#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import messagebox
from tkinter import ttk        
    
root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

textWidget = Text(root, width = 40, height = 10)
textWidget.pack()

def callback():
    #has to actually be a "2nd" or "4th" line to insert at that position
    #e.g doesn't insert empty lines to put them in the right place
    #so if there's no text it'll just go in the first line
    # textWidget.insert("1.0 + 2 lines", "inserted text here")
    # textWidget.insert("1.0 + 4 lines", "inserted text with \n multiple lines here")
    # textWidget.tag_add("yellow", "1.0", "1.0 wordend")
    # textWidget.tag_configure("yellow", background="yellow")
    #tags stay attached to text and can be moved around by typing
    # textWidget.tag_remove("yellow", "1.1", "1.3")

    textWidget.insert("insert", "__")

button.config(command = callback)
button.invoke()

#control word wrapping with the wrap config option
textWidget.config(wrap = "word")

#getting text
textWidget.get("1.0", "end")
#this will get all the text in the input

textWidget.get("1.0", "1.end")
#gets the first line

#inserting text takes index as first parameter as the position of the insert
textWidget.insert("1.0 + 2 lines", "inserted text here")
textWidget.insert("1.0 + 4 lines", "inserted text with \n multiple lines here")

#deletion is non inclusive by default
textWidget.delete("1.0", "1.0 lineend")
#wont delete the last character (newline)
#to fix that just modify again
#textWidget.delete("1.0", "1.0 lineend + 1 chars")

#text can be enabled and disabled with state like other elements

##### 5.2 - Adding tags, marks, images and widgets to the text widget #####
#tags are defined with a name and a range
textWidget.tag_add("yellow", "1.0", "1.0 wordend")
textWidget.tag_configure("yellow", background = "yellow")
#sets the first word of the first line to have a yellow background
#remove tags with tag_remove
textWidget.tag_remove("yellow", "1.1", "1.3")
#get info on tags
textWidget.insert("1.0", textWidget.tag_ranges("yellow"))
textWidget.tag_names()
textWidget.replace("yellow.first", "yellow.last", "otherTag")

#tracked marks, insert and current.
#insert is cursor position
#current is character under the cursor
textWidget.insert("insert", "__")
#custom marks
textWidget.mark_set("myMark", "end")
#gravity attribute determines what side of the cursor becomes the mark
textWidget.mark_gravity("myMark", "right")
#remove marks with unset
textWidget.mark_unset("myMark")

#####tree view item
tree = ttk.Treeview(root)
tree.pack()
#default root node is an empty string
#           root, position, id, text
tree.insert('', '0', 'item1', text = "First Item")
tree.insert('', '1', 'item2', text = "Second Item")
tree.insert('', 'end', 'item3', text = "Third Item")
#can add images to the tree
logo = PhotoImage(file="python_logo.gif").subsample(10,10)
tree.insert('item2', 'end', 'python', text="Python", image = logo) #change root to item2
tree.config(height = 5)
#can move items, just can move a parent item to be a child
# item to move, location, position
tree.move("item2", "item1", "end")
#set default view of node (expanded or not)
tree.item("item1", open=True)
textWidget.insert("insert", "\nItem is open? " + str(tree.item("item1", "open")))
#remove an item from the tree with detach
#doesn't destroy the element, can be added back in
tree.detach("item3")
tree.move("item3", "item2", "0")
#to completely remove an item so that it cannot be reused later
tree.delete("item3")

#add new columns to the tree
tree.config(columns=("version"))
tree.column("version", width = 50, anchor = "center")
#access "main" column with special character #0
tree.column("#0", width = 150)
tree.heading("#0", text="Main")
tree.heading("version", text = "Version")
#set data for items
tree.set("python", "version", "3.4.1") #find python row, set its version column to 3.4.1
tree.item("python", tags = ("software")) #not sure what a tag is but thats how we add one
tree.tag_configure("software", background = "yellow") #oooh they're like for text, its kinda like CSS
#no callback action for treeviews but you can use virtual events to list for changes

def treeCallback(event):
    print(tree.selection());

tree.bind("<<TreeviewSelect>>", treeCallback)

##### Menus #####
root.option_add("*tearOff", False) # do not create a "tearable" menu (like in java, yucky!)
menu = Menu(root)
root.config(menu = menu)
file = Menu(menu)
edit = Menu(menu)
help_ = Menu(menu)
menu.add_cascade(menu = file, label = "File")
menu.add_cascade(menu = edit, label = "Edit")
menu.add_cascade(menu = help_, label = "Help")
file.add_command(label = "new", command = lambda: print("new option pressed"))
file.entryconfig("new", accelerator = "Ctrl + N")
file.add_separator()
file.add_command(label = "open...", command = lambda: print("opening file"))
file.add_command(label = "save", command = lambda: print("save file"))
file.add_separator()
file.add_command(label = "quit", command = lambda: print("quit program"))
file.entryconfig("open...", image = logo, compound = "left")
#can set state like buttons
#can delete with delete method

#create popup menu with the post method
#file.post(300,300) # draw file menu at 300,300

#####scroll bars#####
grid = Tk()
text = Text(grid, width = 40, height = 10, wrap = "word")
text.grid(row = 0, column = 0)
scrollbar = ttk.Scrollbar(grid, orient = VERTICAL, command = text.yview)
scrollbar.grid(row = 0, column = 1, sticky="ns")
text.config(yscrollcommand = scrollbar.set)

from tkinter import colorchooser
chosenColour = "#FFFFFF"
def getColour():
    #it returns RGB and hex in a list, have to use the hex to set colour of elements
    chosenColour = colorchooser.askcolor(initialcolor="#FFFFFF")[1]
    print(chosenColour)
    setColour(chosenColour)

def setColour(col_):
    style.configure("TButton", foreground = col_)

#####widget styling#####
button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2', command = getColour)
button1.pack()
button2.pack()

#style object
style = ttk.Style()
print(style.theme_names())
print(style.theme_use())
style.theme_use("classic") #ewwww
style.theme_use("winnative")
print(button1.winfo_class())
style.configure("TButton", foreground = "green")
#customize existing styles
style.configure("Alarm.TButton", foreground = "orange", font =("Arial", 24, "bold"))
#inherits everytrhing from TButton
button2.config(style = "Alarm.TButton")
#list of pairs
style.map("Alarm.TButton", foreground = [("pressed", "pink"), ("disabled", "grey")])
button1.state(["disabled"])
#element children, button element, focus element, padding element, label element
print(style.layout("TButton"))
#see whgat options are available to an element
print(style.element_options("Button.label"))

#####POPUPS#####
# messagebox.showinfo(title = "Messagebox", message="Hello")
#modal, must respond to move forward
#showinfo, showwarning, showerror
# result = messagebox.askyesno(title = "hungry?", message = "Do you want SPAM?")
# print(result)

if messagebox.askyesno(title = "hungry?", message = "Do you want SPAM?"):
    messagebox.showinfo(title="Messagebox", message="Here you go")
else:
    messagebox.showinfo(title="Messagebox", message="Awwww...ok")

root.mainloop()
