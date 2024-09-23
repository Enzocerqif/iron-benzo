import sqlite3
from datetime import date

def atualizar_plano():
    # Conectar ao banco de dados SQLite
    try:
        banco = sqlite3.connect('.database/academia.db')  # Conecte ao banco de dados
        cursor = banco.cursor()

        # Perguntar o CPF do aluno
        cpf = input("Informe o CPF do aluno (somente números): ")

        # Perguntar se o usuário deseja alterar ou encerrar o plano
        escolha = input("Deseja alterar o plano ou encerrar o plano atual? (alterar/encerrar): ").strip().lower()

        # Data atual
        data_atual = date.today().strftime('%Y-%m-%d')

        if escolha == "encerrar":
            # Encerrar o plano atual: atualiza o status para 'inativo' e a data de encerramento para hoje
            cursor.execute("""
                UPDATE Plano_Aluno
                SET status = 'Inativo', data_encerramento = ?
                WHERE cpf = ? AND status = 'Ativo'
            """, (data_atual, cpf))

            banco.commit()

            print(f"Plano do aluno com CPF {cpf} foi encerrado com sucesso.")

        elif escolha == "alterar":
            # Primeiro, encerrar o plano atual: atualiza o status para 'inativo' e a data de encerramento
            cursor.execute("""
                UPDATE Plano_Aluno
                SET status = 'Inativo', data_encerramento = ?
                WHERE cpf = ? AND status = 'Ativo'
            """, (data_atual, cpf))

            # Perguntar o novo ID do plano
            novo_id_plano = input("Informe o novo ID do plano: ")

            # Recuperar os dados do plano atual do aluno (exceto o id_plano e status)
            cursor.execute("""
                SELECT id_plano, data_adesao FROM Plano_Aluno
                WHERE cpf = ? AND status = 'Inativo'
                ORDER BY data_adesao DESC LIMIT 1
            """, (cpf,))
            plano_atual = cursor.fetchone()

            if plano_atual:
                data_adesao = plano_atual[1]

                # Inserir nova linha com o novo plano e status "ativo", sem data de encerramento
                cursor.execute("""
                    INSERT INTO Plano_Aluno (cpf, id_plano, data_adesao, status)
                    VALUES (?, ?, ?, 'Ativo')
                """, (cpf, novo_id_plano, data_atual))

                banco.commit()
                print(f"Plano do aluno com CPF {cpf} foi alterado com sucesso para o plano {novo_id_plano}.")
            else:
                print("Erro: Não foi possível encontrar um plano ativo para alterar.")
        else:
            print("Opção inválida! Escolha 'alterar' ou 'encerrar'.")
    
    except sqlite3.Error as erro:
        print(f"Erro ao acessar o banco de dados: {erro}")
    
    finally:
        # Fechar a conexão com o banco de dados
        if banco:
            cursor.close()
            banco.close()
            print("Conexão com o banco de dados encerrada.")
