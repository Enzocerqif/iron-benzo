import sqlite3


def checar_informacoes():
    # SELECT ALL PROVISORIO
    try:
        conn = sqlite3.connect('academia_4.db')
        cursor = conn.cursor()

        # Executar consulta para obter todos os alunos
        cursor.execute('''
            SELECT Aluno.cpf, Aluno.nome_aluno, Aluno.email, Aluno.numero_telefone, 
                   Aluno.genero, Aluno.data_de_nascimento, Plano_Aluno.id_plano, Plano_Aluno.data_adesao, 
                   Plano_Aluno.status 
            FROM Aluno
            LEFT JOIN Plano_Aluno ON Aluno.cpf = Plano_Aluno.cpf
        ''')

        alunos = cursor.fetchall()

        if alunos:
            print("\n--- Informações dos Alunos Cadastrados ---")
            for aluno in alunos:
                cpf, nome, email, telefone, genero, data_nascimento, plano, data_adesao, status = aluno
                print(f"\nCPF: {cpf}")
                print(f"Nome: {nome}")
                print(f"Email: {email}")
                print(f"Telefone: {telefone}")
                print(f"Gênero: {genero}")
                print(f"Data de Nascimento: {data_nascimento}")
                print(f"Plano: {plano}")
                print(f"Data de Adesão ao Plano: {data_adesao}")
                print(f"Status do Plano: {status}")
        else:
            print("Nenhum aluno cadastrado no sistema.")

    except sqlite3.Error as error:
        print(f"Erro ao checar as informações: {error}")

    finally:
        if conn:
            conn.close()
