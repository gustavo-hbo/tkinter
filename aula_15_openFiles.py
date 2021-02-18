# Abrir o explorador de arquivos

from tkinter import *
from PIL import ImageTk, Image
# Importando o módulo para abrir o explorador de arquivos
from tkinter import filedialog
root = Tk()
root.title('Dialog box')
def open_image():
    global myImage
    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(root, image=myImage).pack()

def open_explorer():
    # A variavel deve chamar root.filename
    # A função retorna o endereço do arquivo 
    # filetypes deve ter no mínimo duas opções, uma de sua escolha e a outra ('All Files', '*.*')
    root.filename = filedialog.askopenfilename(title='Select a file', filetypes=(("Png Files", "*.png"), ("all files", "*.*")))
    button = Button(root, text='Open File', command=open_image).pack()

button = Button(root, text='Open File', command=open_image, state=DISABLED).pack()
button = Button(root, text='Open Explorer', command=open_explorer).pack()
root.mainloop()