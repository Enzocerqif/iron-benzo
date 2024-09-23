import sqlite3
from datetime import datetime


def cadastrar_plano(cpf):
    # Loop para garantir entrada correta do plano (armazenando strings)
    while True:
        plano_id = input("Escolha o plano (1 = Anual - R$ 1000, 2 = Mensal - R$ 120, 3 = Diário - R$ 30): ")
        if plano_id == '1':
            nome_plano = "Anual"
            valor = 1000
            break
        elif plano_id == '2':
            nome_plano = "Mensal"
            valor = 120
            break
        elif plano_id == '3':
            nome_plano = "Diário"
            valor = 30
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

    # Data de adesão será a data atual
    data_adesao = datetime.now().date()
    status = "Ativo"

    # Conectar ao banco de dados e inserir o plano
    conn = sqlite3.connect('.database/academia.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Plano_Aluno (cpf, id_plano, data_adesao, status)
        VALUES (?, ?, ?, ?)
    ''', (cpf, nome_plano, data_adesao, status))

    conn.commit()
    conn.close()

    print(f"Plano ({nome_plano}) cadastrado com sucesso para o aluno com CPF {cpf}!")
