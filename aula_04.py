# Input boxes
from tkinter import *

root = Tk()


def click():
    message = 'Hello ' + e.get()
    myLabel = Label(root, text=message).pack()


# 'Input class'
e = Entry(root, width=50, borderwidth=10)
e.insert(0, 'Enter your name: ')
e.pack()

myButton = Button(root, text='Click Me', command=click)
myButton.pack()
root.mainloop()