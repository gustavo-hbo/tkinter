from tkinter import *

root = Tk()
root.title('Radio Button')

MODES = [('Pepperoni', 'Pepperoni'),
         ('Cheese', 'Cheese'),
         ('Chedar', 'Chedar'),
         ('Ham', 'Ham'),
         ('Chicken', 'Chicken')]

def clicked(val):
    my_label = Label(root, text=val).pack()

pizza = StringVar()
pizza.set('Pepperoni')
for name, val in MODES:
    Radiobutton(root, variable=pizza, value=val, text=name).pack(anchor=W)

b = Button(root, text='Send', command=lambda: clicked(pizza.get())).pack()
root.mainloop()