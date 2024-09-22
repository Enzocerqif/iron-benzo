import verify_cpf
import add_ficha
import add_plan
import sqlite3
from datetime import datetime


def cadastrar_aluno():
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

        # Validação de data com datetime
        data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD) (opcional, pressione Enter para pular): ")
        if data_nascimento:
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            except ValueError:
                print("Data de nascimento inválida. Use o formato YYYY-MM-DD.")
                return
        else:
            data_nascimento = None

        # Conectar ao banco de dados
        conn = sqlite3.connect('academia_3.db')
        cursor = conn.cursor()

        # Inserir os dados na tabela Aluno
        cursor.execute(''' 
            INSERT INTO Aluno (nome_aluno, cpf, email, numero_telefone, genero, data_de_nascimento)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, cpf, email, telefone, genero, data_nascimento))

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
        if conn:
            conn.close()
