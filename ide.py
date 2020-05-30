from tkinter import *
import os

def save():
    name = Entry(root).grid(row=2, column=2)
    
root = Tk()
text = Text(font="Calibri 18").grid(row=1, column=1)
save = Button(text="Save as", font="Calibri 18" command=save).grid(row=0, column=0)
root.mainloop()

