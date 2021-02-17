# Building a simple image viewer
# ---------------------------------------------------Rever a aula e terminar ------------------------------------------
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def forward(position):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[position+1])

    button_next = Button(root, text='>>', command=lambda: forward(position+1))
    my_label.grid(row=0, column=0, columnspan=3)

def back():
    global my_label
    global button_forward
    global button_backs

image1 = ImageTk.PhotoImage(Image.open('images/cloud.png'))
image2 = ImageTk.PhotoImage(Image.open('images/flyMan.png'))
image3 = ImageTk.PhotoImage(Image.open('images/spikeMan.png'))
image4 = ImageTk.PhotoImage(Image.open('images/sun.png'))
image5 = ImageTk.PhotoImage(Image.open('images/wingMan.png'))
image_list = [image1, image2, image3, image4, image5]

my_label = Label(image=image1)
my_label.grid(row=0, column=0, columnspan=3)

button_quit = Button(root, text='Exit Program', command=root.quit)
button_next = Button(root, text='>>', command=lambda: forward(2))
button_back = Button(root, text='<<', command=lambda: back())

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()