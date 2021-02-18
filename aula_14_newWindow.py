from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Main window')

def open_win():
    global my_img
    top = Toplevel()
    top.title('New window')
    # Label(top, text='This is in the new window').pack()
    my_img = ImageTk.PhotoImage(Image.open('images/spikeMan.png'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close', command=top.destroy).pack()

btn = Button(root, text='Open new window', command=open_win).pack()

root.mainloop()