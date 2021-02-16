# Creating a Simple Calculator with Tkinter
from tkinter import *
from time import sleep
root = Tk()
root.title('Simple Calculator')

# Coloca o numero clicado no input
def myClick(num):
    e.insert(END, num)

def action(tipo):
    global first_num
    global action_type
    action_type = tipo
    first_num = e.get()
    e.delete(0, END)

def equal():
    second_num = e.get()
    e.delete(0, END)
    if action_type == 'add':
        e.insert(0, float(first_num) + float(second_num))
    elif action_type == 'sub':
        e.insert(0, float(first_num) - float(second_num))
    elif action_type == 'mult':
        e.insert(0, float(first_num) * float(second_num))
    elif action_type == 'div':
        if second_num != 0 or second_num !='0':
            e.insert(0, float(first_num) / float(second_num))

def clear():
    e.delete(0, END)

def backspace():
    num = str(e.get())
    pos = len(num)-1
    e.delete(0, END)
    e.insert(0, num[:pos])

# Coloca o ponto se nao tiver algum, caso contrario faz nada
def dot():
    number = e.get()
    for char in str(number):
        if char == '.':
            e.delete(0, END)
            e.insert(0, number)
        else:
            e.insert(END, '.')

# Entrada de dados
e = Entry(root, width=60)
e.grid(row=0, column=0,columnspan=5, padx=10, pady=10)

# Botões numéricos
button_1 = Button(root, padx=40, pady=20, text='1', command=lambda: myClick(1))
button_2 = Button(root, padx=40, pady=20, text='2', command=lambda: myClick(2))
button_3 = Button(root, padx=40, pady=20, text='3', command=lambda: myClick(3))
button_4 = Button(root, padx=40, pady=20, text='4', command=lambda: myClick(4))
button_5 = Button(root, padx=40, pady=20, text='5', command=lambda: myClick(5))
button_6 = Button(root, padx=40, pady=20, text='6', command=lambda: myClick(6))
button_7 = Button(root, padx=40, pady=20, text='7', command=lambda: myClick(7))
button_8 = Button(root, padx=40, pady=20, text='8', command=lambda: myClick(8))
button_9 = Button(root, padx=40, pady=20, text='9', command=lambda: myClick(9))
button_0 = Button(root, padx=40, pady=20, text='0', command=lambda: myClick(0))

# Botões de ações (soma, subtração, multiplicação e divisão)
button_add = Button(root, padx=37, pady=50, text='+', command=lambda: action('add'))
button_subtract = Button(root, padx=41, pady=21, text='-', command=lambda: action('sub'))
button_multiply = Button(root, padx=39, pady=19, text='*', command=lambda: action('mult'))
button_divide = Button(root, padx=40, pady=20, text='/', command=lambda: action('div'))

# Botões de ações (ponto, igual, apagar e limpar)
button_dot = Button(root, padx=40, pady=20, text='.', command=dot)
button_equal = Button(root, padx=90, pady=20, text='=', command=equal)
button_clear = Button(root, padx=25, pady=20, text='clear', command=clear)
button_backspace = Button(root, padx=33, pady=20, text='<-', command=backspace)

# Colocando os botões na tela com grid
# OBS: row=0 é a do input
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)
button_dot.grid(row=1, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)
button_divide.grid(row=2, column=4)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=3, column=3, rowspan=2)
button_clear.grid(row=3, column=4)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)
button_backspace.grid(row=4, column=4)

root.mainloop()
