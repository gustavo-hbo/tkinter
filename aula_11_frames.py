from tkinter import *

root = Tk()
root.title('Frame')

# Cria padding dentro do frame
frame = LabelFrame(root, padx=5, pady=5)
# Cria padding fora do frame
frame.pack(padx=10, pady=10)

# Para colocar o botão dentro do frame devo usar o frame no primeiro argumento
button = Button(frame, text='Dont Click')
button.pack()
root.mainloop()

# Com a utilizacao de frames eh possivel utilizar grid e pack no código,
# Um deles para posicionar dentro do frame e outro para posicionar o frame