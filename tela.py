# importando dependências do tkinter
from tkinter .ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import Image, ImageTk

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import datetime

# importando main
from main import *

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde


# criando janela
janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

Style = Style(janela)
Style.theme_use("clam")

# criando frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Trabalhando no frame logo -----------------------------------------
global imagem, imagem_string, l_imagem

app_lg = Image.open('mortarboard.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# abrindo a imagem

imagem = Image.open('mortarboard.png')
imagem = imagem.resize((130,150))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)

# ------------------------------------ Criando funções para CRUD --------------------------------------
# função adicionar
def adicionar():
    global imagem, imagem_string, l_imagem

    #obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo ,data, endereco, curso, img]

    # verificando se a lista contém valor vazio
    for i in lista:
        if i=='':
            messagebox.showerror('Erro', 'preencha todos os campos')
            return

    # registrando os valores
    sistema_de_registro.register_student(lista)

    # limpando os campos de entradas
    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_tel.delete(0,END)
    c_sexo.delete(0,END)
    data_nascimento.delete(0,END)
    e_endereco.delete(0,END)
    c_curso.delete(0,END)

    # mostrando os valores na tabela
    mostrar_alunos()

# função procurar
def procurar():
    global imagem, imagem_string, l_imagem

    # obtendo o id
    id_aluno = int(e_procurar.get())

    # procurando o aluno
    dados = sistema_de_registro.search_student(id_aluno)

    # limpando os campos de entradas
    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_tel.delete(0,END)
    c_sexo.delete(0,END)
    data_nascimento.delete(0,END)
    e_endereco.delete(0,END)
    c_curso.delete(0,END)

    # inserir valores nos campos de entrada
    e_nome.insert(END,dados[1])
    e_email.insert(END,dados[2])
    e_tel.insert(END,dados[3])
    c_sexo.insert(END,dados[4])
    data_nascimento.insert(END,dados[5])
    e_endereco.insert(END,dados[6])
    c_curso.insert(END,dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,150))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

# função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem

    #obtendo o id
    id_aluno = int(e_procurar.get())

    #obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista =  [nome, email, tel, sexo ,data, endereco, curso, img, id_aluno]

    # verificando se a lista contém valor vazio
    for i in lista:
        if i=='':
            messagebox.showerror('Erro', 'preencha todos os campos')
            return

    # registrando os valores
    sistema_de_registro.update_student(lista)

    # limpando os campos de entradas
    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_tel.delete(0,END)
    c_sexo.delete(0,END)
    data_nascimento.delete(0,END)
    e_endereco.delete(0,END)
    c_curso.delete(0,END)

    # abrindo a imagem
    imagem = Image.open('mortarboard.png')
    imagem = imagem.resize((130,150))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # mostrando os valores na tabela
    mostrar_alunos()

# função deletar
def deletar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())

    # deletando o aluno
    sistema_de_registro.delete_student(id_aluno)

    # limpando os campos de entradas
    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_tel.delete(0,END)
    c_sexo.delete(0,END)
    data_nascimento.delete(0,END)
    e_endereco.delete(0,END)
    c_curso.delete(0,END)

    e_procurar.delete(0,END)

    # abrindo a imagem
    imagem = Image.open('mortarboard.png')
    imagem = imagem.resize((130,150))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # mostrando os valores na tabela
    mostrar_alunos()






# criando os campos de entrada --------------------------------------
l_nome = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_sexo = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_details, width=7, font=('ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)

l_data_nascimento = Label(frame_details, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
data_nascimento.place(x=224, y=40)

l_endereco = Label(frame_details, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_details, width=15, justify='left', relief='solid')
e_endereco.place(x=224, y=100)

cursos = ['Engenharia', 'Medicina', 'Direito', 'Ciência da Computação', 'Arquitetura', 'Administração', 'Psicologia', 'Enfermagem', 'Fisioterapia', 'Farmácia']

l_curso = Label(frame_details, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_details, width=20, font=('ivy 8 bold'), justify='center')
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)


# função para escolher imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,150))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Alterar Foto'

botao_carregar = Button(frame_details, command=escolher_imagem, text="Carregar Foto" .upper(), width=20,compound=CENTER, anchor=CENTER, font=('Ivy 7 bold'), overrelief=RIDGE, bg=co1, fg=co0)
botao_carregar.place(x=391, y=162)


# Tabela Alunos
def mostrar_alunos():
    
    # creating a treeview with dual scrollbars
    list_header = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'Curso']

    #view all students
    df_list = sistema_de_registro.view_all_students()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "center", "center", "center", "center", "center"]
    h=[40, 150, 150, 70, 70, 70, 120, 100, 100]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        #adjust the column's width to the header string
        tree_aluno.column(col, width=h[n], anchor=hd[n])
        
        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)


# Procurar aluno --------------------------------
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text=" Procurar aluno [Entra ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar, command=procurar, text='Procurar', width=9, anchor=CENTER, font=('Ivy 7 bold'), overrelief=RIDGE, bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# botões ---------------------------------------
app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((25, 25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, font=('Ivy 11'), overrelief=RIDGE, bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('update.png')
app_img_atualizar = app_img_atualizar.resize((25, 25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, font=('Ivy 11'), overrelief=RIDGE, bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('delete.png')
app_img_deletar = app_img_deletar.resize((25, 25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar, relief=GROOVE, text=' Deletar', width=100, compound=LEFT, font=('Ivy 11'), overrelief=RIDGE, bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# linha separadora
l_linha = Label(frame_botoes, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co1)
l_linha.place(x=236, y=15)



# chamar a tabela
mostrar_alunos()


janela.mainloop()