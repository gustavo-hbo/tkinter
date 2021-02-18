# Creating Message Boxes
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('Message Boxes')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

# showinfo    -> ok = 'ok'
# showwarning -> ok = 'ok'
# showerror   -> ok ='ok'
# askquestion -> yes ='yes', no ='no'
# askokcancel -> ok = 1, cancel = 0
# askyesno    -> yes = 1, no = 0

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    if response == 1:
        Label(root, text='You clicked yes').pack()
    if response == 0:
        Label(root, text='You clicked no').pack()

button = Button(root, text='pop-up', command=popup).pack()


root.mainloop()