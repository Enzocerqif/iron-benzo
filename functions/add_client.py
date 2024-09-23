import sqlite3
from datetime import datetime
import verify_cpf
import add_ficha
import add_plan
from add_birthdate import verificar_data_nascimento

def cadastrar_aluno():
    conn = None  # Inicializa a variável como None
    try:
        # Coletando os dados do aluno via terminal
        cpf = input("Digite o CPF (somente números): ")
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido. Ele deve ter 11 dígitos.")
            return

        # Verificar se o CPF já está cadastrado
        if verify_cpf.verificar_cpf_existente(cpf):
            print("Erro: CPF já cadastrado no sistema.")
            return

        nome = input("Digite o nome do aluno: ")
        if not nome:
            print("Nome é obrigatório.")
            return

        email = input("Digite o email: ")
        if not email or "@" not in email:
            print("Email inválido.")
            return

        telefone = input("Digite o número de telefone (somente números): ")
        if not telefone.isdigit() or len(telefone) > 16:
            print("Número de telefone inválido.")
            return

        while True:
            genero = input("Escolha o gênero (1 = Masculino, 2 = Feminino, 3 = Indefinido): ")
            if genero == '1':
                genero = "Masculino"
                break
            elif genero == '2':
                genero = "Feminino"
                break
            elif genero == '3':
                genero = "Indefinido"
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

        # Inicializar a variável data_nascimento fora do laço while
        data_nascimento = None

        # Coletar e validar a data de nascimento
        while True:
            opcao_data = input("Deseja informar a data de nascimento? (S/N): ").upper()
            if opcao_data == 'S':
                data_nascimento = verificar_data_nascimento()  # Chama a função de verificação
                break
            elif opcao_data == 'N':
                data_nascimento = None  # O usuário escolheu não informar a data
                break
            else:
                print("Opção inválida. Escolha S ou N.")

        # Conectar ao banco de dados
        conn = sqlite3.connect('../academia_4.db')
        cursor = conn.cursor()

        # Inserir os dados na tabela Aluno
        cursor.execute(''' 
            INSERT INTO Aluno (cpf, nome_aluno, email, numero_telefone, genero, data_de_nascimento)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (cpf, nome, email, telefone, genero, data_nascimento))

        # Salvar (commit) as mudanças
        conn.commit()

        print(f"Aluno cadastrado com sucesso! CPF: {cpf}")

        # Chamar a função para cadastrar o plano
        add_plan.cadastrar_plano(cpf)

        # Chamar a função para criar a ficha do aluno
        add_ficha.criar_ficha(cpf)

    except sqlite3.Error as error:
        print(f"Erro ao cadastrar aluno: {error}")

    finally:
        # Fechar a conexão com o banco de dados, se ela foi criada
        if conn:
            conn.close()
