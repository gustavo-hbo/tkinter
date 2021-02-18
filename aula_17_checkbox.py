# CheckBoxes
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('CheckBoxes')
root.geometry('400x400')

# var = IntVar()
var = StringVar()

def show():
    my_label = Label(root, text=var.get()).pack()

c = Checkbutton(root, text='check', variable=var, onvalue='ON', offvalue='OFF')
c.deselect()
c.pack()


mybutton = Button(root, text='Show selection', command=show)
mybutton.pack()
mainloop()