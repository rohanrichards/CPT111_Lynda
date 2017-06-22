#!/usr/bin/python3
# hello_local.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)

        #changed to actually store the reference
        self.texasButton = ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)
        # changed to actually store the reference
        self.hawaiiButton = ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)

        self.movingLabel = ttk.Label(master, text="[]")
        self.movingLabel.grid(row=2, column = 0)

    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')
        self.toggleLabel()

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')
        self.toggleLabel()

    #toggles the position of the moving label
    def toggleLabel(self):
        #what does grid info do?
        #print(self.movingLabel.grid_info().get("column"))
        if self.movingLabel.grid_info().get("column") == 0:
            self.movingLabel.grid(column = 1)
        else:
            self.movingLabel.grid(column=0)

            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()
