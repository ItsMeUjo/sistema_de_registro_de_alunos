import sqlite3
from tkinter import messagebox

class SistemaDeRegistro: 
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            tel TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data_nascimento TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            curso TEXT NOT NULL,
                            imagem TEXT NOT NULL) ''')
    
    def register_student(self, estudantes,):
        self.c.execute("INSERT INTO estudantes (nome, email, tel, sexo, data_nascimento, endereco, curso, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (estudantes))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro com sucesso!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        return dados

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        
        return dados

    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, imagem=? WHERE id=?"
        self.c.execute(query, novos_valores)
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID: {novos_valores[8]} foi atualizado!')
    
    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID: {id} foi deletado!')

# criando uma instância do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# informações
#estudante = ('Elena', 'elena@gmail.com', '987654321', 'F', '15/08/2005', 'Ceará, Fortaleza', 'Medicina', 'imagem.jpg')
#sistema_de_registro.register_student(estudante)



#procurar alunos
#aluno = sistema_de_registro.search_student(2)

#atualizar aluno
#estudante = ('Elena', 'elena@gmail.com', '987654321', 'F', '15/08/2005', 'Ceará, Fortaleza', 'Medicina', 'imagem.jpg', 2)
#aluno = sistema_de_registro.update_student(estudante)

#sistema_de_registro.delete_student(1)

# ver estudantes
#todos_alunos = sistema_de_registro.view_all_students()