# Criando quit button, icone de programa e adicionando imagem 
from tkinter import *
root = Tk()
root.title('Simple program')

# Adicionando icone, a imagem deve ter formato .ico
# root.iconbitmap('image.ico')

# Add image#
from PIL import ImageTk, Image
my_img = ImageTk.PhotoImage(Image.open('images/space-invaders.png'))
myLabel = Label(image=my_img)
myLabel.pack()

# Botão com a função sair
button_quit = Button(root, text="Exit program", command=root.quit, bg='red')
button_quit.pack()

root.mainloop()