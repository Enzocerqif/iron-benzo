import sqlite3
from datetime import datetime


def criar_ficha(cpf):
    data_criacao = datetime.now().date()  # Data de criação da ficha (atual)

    # Conectar ao banco de dados e inserir a ficha
    conn = sqlite3.connect('academia_4.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Ficha (cpf, data_criacao)
        VALUES (?, ?)
    ''', (cpf, data_criacao))

    conn.commit()
    conn.close()

    print(f"Ficha criada com sucesso para o aluno com CPF {cpf}!")
