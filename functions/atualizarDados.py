import sqlite3

def atualizar_dados():
    # Conectar ao banco de dados SQLite
    try:
        banco = sqlite3.connect('../academia_4.db')
        cursor = banco.cursor()

        # Perguntar ao usuário sobre os detalhes da atualização
        tabela = input("Informe o nome da tabela: ")
        coluna = input("Informe o nome da coluna que deseja atualizar: ")
        novo_valor = input(f"Informe o novo valor para a coluna '{coluna}': ")
        condicao_coluna = input("Informe o nome da coluna da condição (para identificar o registro): ")
        condicao_valor = input(f"Informe o valor para a condição (para a coluna '{condicao_coluna}'): ")

        # Formatar a query SQL de atualização
        query = f"UPDATE {tabela} SET {coluna} = ? WHERE {condicao_coluna} = ?"
        valores = (novo_valor, condicao_valor)

        # Executar a query de atualização
        cursor.execute(query, valores)
        banco.commit()

        print(f"Registro atualizado com sucesso na tabela '{tabela}'!")
    
    except sqlite3.Error as erro:
        print(f"Erro ao tentar atualizar dados: {erro}")
    
    finally:
        # Fechar a conexão com o banco de dados
        if banco:
            cursor.close()
            banco.close()
            print("Conexão com o banco de dados encerrada.")
