
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Simple image viwer')

# Váriavel que controla a foto que será exibida
i = 0
def next_image():
    # Importando as variáveis globais
    global i
    global my_label
    # Incrementando a variavel posicional e atualizando o botão
    if i < 4:
        i += 1
        button_back = Button(root, text='<<', command=back_image)
        button_back.grid(row=1, column=0)
    if i == 4:
        button_next = Button(root, text='>>', command=next_image, state=DISABLED)
        button_next.grid(row=1, column=2)

    # Trocando a imagem para a próxima
    my_label.grid_forget()
    my_label = Label(image=images[i])
    my_label.grid(row=0, column=0, columnspan=3)

    # Atualizando a barra de progressão
    status = Label(root, text=f'Image {i+1} of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back_image():
    global i
    global my_label
    if i > 0:
        i -= 1
        button_next = Button(root, text='>>', command=next_image)
        button_next.grid(row=1, column=2)
    if i == 0:
        button_back = Button(root, text='<<', command=back_image, state=DISABLED)
        button_back.grid(row=1, column=0)
    status = Label(root, text=f'Image {i+1} of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    my_label.grid_forget()
    my_label = Label(image=images[i])
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text=f'Image {i+1} of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Criando as imagens
my_image1 = ImageTk.PhotoImage(Image.open('images/cloud.png'))
my_image2 = ImageTk.PhotoImage(Image.open('images/flyMan.png'))
my_image3 = ImageTk.PhotoImage(Image.open('images/spikeMan.png'))
my_image4 = ImageTk.PhotoImage(Image.open('images/sun.png'))
my_image5 = ImageTk.PhotoImage(Image.open('images/wingMan.png'))
images = [my_image1, my_image2,my_image3, my_image4, my_image5]
cont = len(images)

status = Label(root, text='Image 1 of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
# Displaying uma das imagens na tela
my_label = Label(image=images[0])
my_label.grid(row=0, column=0, columnspan=3)

# Criando os botões 
button_quit = Button(root, text='Exit Program', command=root.quit)
button_next = Button(root, text='>>', command=next_image)
button_back = Button(root, text='<<', state=DISABLED, command=back_image)

# Posicionando os botões na tela
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()
