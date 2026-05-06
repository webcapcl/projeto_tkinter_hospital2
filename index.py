
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
    data_nascimento = entry_Data_Nascimento.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio_sus = entry_convenio_sus.get()
    contato = entry_contato_emergencia.get()    
    
    if nome == '' or cpf == '' or data_nascimento == '' or telefone == '' or email == '' or convenio_sus == '' or contato == '':
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos!!!')
    else:    
        tabela.insert('', 'end', values=(nome, cpf, data_nascimento, telefone, email, convenio_sus, contrato))
        entry_Nome_Completo.delete(0, END)
        entry_Cpf.delete(0, END)
        entry_Data_Nascimento.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_convenio_sus.delete(0, END)
        entry_contrato_emergencia.delete(0, END)    
        
        messagebox.showinfo('Sucesso', 'Paciente cadastrado com sucesso!')
        
        
def eliminar():
    item_selecionado = tabela.selection()
    if item_selecionado:
        tabela.delete(item_selecionado)
    else:
        messagebox.showwarning("Aviso", "Selecione um paciente para eliminar.")
        
        # aba de cadastro
        
Label(aba1, text='Nome Completo:').pack(pady=5)
entry_Nome_Completo = Entry(aba1, width=40)
entry_Nome_Completo.pack()
        
Label(aba1, text='CPF:').pack(pady=5)
entry_Cpf = Entry(aba1, width=40)   
entry_Cpf.pack()
        
Label(aba1, text='Data de Nascimento:').pack(pady=5)
entry_Data_Nascimento = Entry(aba1, width=40)
entry_Data_Nascimento.pack()
        
Label(aba1, text='Telefone:').pack(pady=5)
entry_telefone = Entry(aba1, width=40)  
entry_telefone.pack()
        
  
Label(aba1, text='Email:').pack(pady=5)
entry_email = Entry(aba1, width=40)
entry_email.pack()
        
Label(aba1, text='Convênio/SUS:').pack(pady=5)
entry_convenio_sus = Entry(aba1, width=40)  
entry_convenio_sus.pack()
        
Label(aba1, text='Contato de Emergência:').pack(pady=5)
entry_contato_emergencia = Entry(aba1, width=40)
entry_contato_emergencia.pack()
        
Button(
            aba1,
            text='Cadastrar',
            bg='blue',
            fg='white',
            width=20,
            command=cadastrar
        ).pack(pady=20)

Button(aba2, text="Eliminar Selecionado", bg="#4c67ee", fg="white", command=eliminar).pack(pady=10)
        
        # aba de tabela

colunas = ('Nome Completo', 'CPF', 'Data de Nascimento', 'Telefone', 'Email', 'Convênio/SUS', 'Contato de Emergência')     
        
tabela = ttk.Treeview(
            aba2,
            columns=colunas,
            show='headings'
        )
        
for col in colunas:
            tabela.heading(col, text=col)
            tabela.column(col, width=150)
            
tabela.pack(fill='both', expand=True, pady=20)
            

    






janela.mainloop()#sempre ultimo comando