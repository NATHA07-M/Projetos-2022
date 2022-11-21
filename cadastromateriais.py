import tkinter as tk
from tkinter import ttk
import datetime as dt
import pandas as pd

materiais = pd.read_excel('materiais.xlsx', engine = 'openpyxl')

lista_tipos = ["Galão","Caixa","Saco","Unidade"]
lista_codigos = []

janela = tk.Tk()

#criaçao da funçao 

def inserir_codigo():
    descriçao = entry_descriçao.get()
    tipo = combobox_selecionar_tipo.get
    quant = entry_quant.get()
    data_criaçao = dt.datetime 
    data_criaçao = dt .datetime.now()
    data_criaçao = data_criaçao.strftime("%d/%m/%Y %H:%M")
    codigo = materiais.shape[0] + len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str,descriçao,tipo,quant,data_criaçao))
    

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

label_quant = tk.Label(text="Quantidade na unidade de material")
label_quant.grid(row=4, column =0,padx=10,pady=10,sticky='nswe',columnspan =2)

entry_quant = tk.Entry()
entry_quant.grid(row=4,column=2,padx=10,pady=10,sticky='nswe',columnspan =2)

botao_criar_codigo = tk.Button(text="Criar codigo",command=inserir_codigo)
botao_criar_codigo.grid(row=5,column=0,padx= 10,pady=10,sticky='nswe',columnspan=4) 
  



janela.mainloop()

novo_material = pd.DataFrame(lista_codigos, columns=('codigo_str','descriçao','tipo','quant','data_criaçao'))
materiais = materiais.append(novo_material, ignore_index=True)
materiais.to_excel('materiais.xlsx',index=False)


print(lista_codigos) 