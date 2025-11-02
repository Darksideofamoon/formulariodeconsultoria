import tkinter as tk
from tkinter import Label, Frame, NW

co2 = "#008000"
co1 = "#FFFFFF"
co4 = "#000000"

janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry('600x400')
janela.configure(bg=co2)

frame_cima = Frame(janela, width=600, height=70, bg=co2)
frame_cima.pack(side='top', fill='x')

app_nome = Label(frame_cima, text='Formulario de Consultoria', anchor=NW,
                 font=('Ivy', 13, 'bold'), bg=co2, relief='flat', fg=co4)
app_nome.place(x=10, y=10)

frame_baixo = Frame(janela, width=600, height=330, bg=co1)
frame_baixo.pack(side='top', fill='both', expand=True)

I_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy', 10, 'bold'),
               bg=co1, fg=co4, relief='flat')
I_nome.place(x=10, y=10)
entry_nome = tk.Entry(frame_baixo, font=('Ivy', 10))
entry_nome.place(x=70, y=10, width=200, height=24)

I_email = Label(frame_baixo, text='Email', anchor=NW, font=('Ivy', 10, 'bold'),
                bg=co1, fg=co4, relief='flat')
I_email.place(x=10, y=50)
e_email = tk.Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=70, y=50, height=24)

I_telefone = Label(frame_baixo, text='Telefone', anchor=NW, font=('Ivy', 10, 'bold'),
                   bg=co1, fg=co4, relief='flat')
I_telefone.place(x=10, y=90)
e_telefone = tk.Entry(frame_baixo, width=25, justify='left', relief='solid')
e_telefone.place(x=70, y=90, height=24)

I_data = Label(frame_baixo, text='Data de Consulta', anchor=NW, font=('Ivy', 10, 'bold'),
               bg=co1, fg=co4, relief='flat')
I_data.place(x=10, y=130)
e_data = tk.Entry(frame_baixo, width=20, justify='left', relief='solid')
e_data.place(x=120, y=130, height=24)

janela.mainloop()
