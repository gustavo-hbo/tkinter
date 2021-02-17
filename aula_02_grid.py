from tkinter import *

root = Tk()

myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='My name is Gustavo')

# Pode ser assim tambem
# myLabel1 = Label(root, text='Hello World').grid(row=0, column=1)
# myLabel2 = Label(root, text='My name is Gustavo').grid(row=1, column=0)

# Posiciona os Widgets em em grid de posicoes relativa
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)

root.mainloop()
