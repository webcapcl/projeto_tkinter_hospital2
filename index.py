
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 

janela = Tk()
janela.title('Formulário de Cadastro de Pacientes')
janela.geometry('800x600')

# Construção de abas //////

abas = ttk.Notebook(janela)
abas.pack(fill='both', expand=True)

# aba1 Cadastro

aba1 = Frame (abas)
abas.add(aba1, text='Cadastro de Pacientes')

# aba2- tabela

aba2= Frame (abas)
abas.add(aba2,text='Pacientes Cadastrados')

# Função Cadastrar

def cadastrar():
    nome = entry_Nome_Completo.get()
    cpf = entry_Cpf.get()
    data_nascimento = entry_Data_Nascimento.get(
    telefone =     
    )

    



















janela.mainloop()#sempre ultimo comando