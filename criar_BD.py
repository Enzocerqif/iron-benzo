import sqlite3

conn = sqlite3.connect('academia.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Aluno (
        cpf VARCHAR(11) PRIMARY KEY NOT NULL,
        nome_aluno VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        numero_telefone INTEGER(16) NOT NULL,
        genero VARCHAR(50),
        data_de_nascimento DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Plano (
        id_plano INTEGER(8) PRIMARY KEY AUTOINCREMENT,
        nome_plano VARCHAR(40) NOT NULL,
        valor FLOAT(8) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Plano_Aluno (
        id_plano_aluno INTEGER(8) PRIMARY KEY AUTOINCREMENT,
        cpf VARCHAR(11) NOT NULL,
        id_plano INTEGER(4) NOT NULL,
        data_adesao DATE NOT NULL,
        data_encerramento DATE,
        status VARCHAR(50) NOT NULL,
        FOREIGN KEY (cpf) REFERENCES Aluno(cpf),
        FOREIGN KEY (id_plano) REFERENCES Plano(id_plano)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ficha (
        id_ficha INTEGER(8) PRIMARY KEY AUTOINCREMENT,
        cpf VARCHAR(11) NOT NULL,
        data_criacao DATE NOT NULL,
        FOREIGN KEY (cpf) REFERENCES Aluno(cpf)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ficha_Treino (
        id_ficha_treino INTEGER(4) PRIMARY KEY NOT NULL,
        id_ficha INTEGER(4) NOT NULL,
        nome_exercicio INTEGER(4) NOT NULL,
        series INTEGER(4) NOT NULL,
        repeticoes INTEGER(4) NOT NULL,
        dia_da_semana VARCHAR(40) NOT NULL,
        FOREIGN KEY (id_ficha) REFERENCES Ficha(id_ficha)
    )
''')

conn.commit()
conn.close()