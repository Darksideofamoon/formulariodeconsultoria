import tkinter as tk
from tkinter import Label, Frame, NW

# Cores
co2 = "#008000"  # verde padrão

# Janela principal
janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry('600x400')
janela.configure(bg=co2)

# Frame superior
frame_cima = Frame(janela, width=600, height=50, bg=co2)
frame_cima.pack(side='top', fill='x')

# Label dentro do frame_cima
app_nome = Label(frame_cima, text='Formulario de Consultoria', anchor=NW,
                 font=('Ivy', 13, 'bold'), bg=co2, relief='flat')
app_nome.grid(row=0, column=0, padx=10, pady=10)
app_nome.place( x=10,y=20)

# Loop da interface
janela.mainloop()