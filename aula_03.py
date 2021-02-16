# Creating buttons
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='I clicked')
    myLabel.pack()

myButton = Button(root, text='Click me', padx = 50, command=myClick)

myButton.pack()

root.mainloop()


# Variáveis que podem ser setadas em Button()
# state=DISABLED ---> Deixa o butão desativado
# padx=50        ---> Cria um espaçamento HORIZONTAL no botão
# pady=50        ---> Cria um espaçamento VERTICAL no botão
# fg='color'     ---> Seta a cor do texto
# bg='color'     ---> Seta a cor do fundo