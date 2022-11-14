import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Galão","Caixa","Saco","Unidade"]

janela = tk.Tk()

#titulo de janela

janela.title('ferramenta de cadastro de materiais')

label_descriçao = tk.Label(text='Descrição do material')
label_descriçao.grid(row=1,column=0,padx = 10, pady=10,sticky='nswe',columnspan =4)

entry_descriçao = tk.Entry()
entry_descriçao.grid(row=2,column=0,padx=10,pady=10,sticky='nswe',columnspan = 1)

label_tipo_unidade = tk.Label(text="Tipo da unidade do Material")
label_tipo_unidade.grid(row=3,column=0,padx = 10,pady=10,sticky='nswe',columnspan = 2 )

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3,column=1,padx=10,pady=10,sticky='nswe',columnspan = 2)




janela.mainloop()