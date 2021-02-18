# Using sliders
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
# Controla o tamanho da tela
root.geometry('400x400')
def divide():
    root.geometry(str(horizontal.get())+'x'+str(vertical.get()))

vertical = Scale(root, from_=1, to=400)
vertical.pack()

horizontal = Scale(root, from_=1, to=400, orient=HORIZONTAL
horizontal.pack()

my_btn = Button(root, text='DIVIDE', command=divide).pack()
root.mainloop()