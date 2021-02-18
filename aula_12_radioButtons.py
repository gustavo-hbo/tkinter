# Creating radio buttons
from tkinter import *

root = Tk()
root.title('Radio Buttons')

#r = IntVar()
#r.set('2')

# Name and Value
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set('Pepperoni')

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode, command=lambda: clicked(pizza.get())).pack(anchor=W)



# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()
root.mainloop()