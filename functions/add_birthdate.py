import sqlite3
from datetime import datetime

def verificar_data_nascimento():
    # Coletar o ano de nascimento
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (YYYY): "))
            ano_atual = datetime.now().year
            if ano > ano_atual:
                print(f"Ano inválido. O ano não pode ser maior que {ano_atual}.")
            elif ano < 1900:
                print("Ano inválido. O ano deve ser maior ou igual a 1900.")
            else:
                break
        except ValueError:
            print("Ano inválido. Por favor, insira um ano válido.")

    # Coletar o mês de nascimento
    while True:
        try:
            mes = int(input("Digite o mês de nascimento (MM): "))
            if mes < 1 or mes > 12:
                print("Mês inválido. Por favor, insira um valor entre 1 e 12.")
            else:
                break
        except ValueError:
            print("Mês inválido. Por favor, insira um valor numérico válido.")

    # Coletar o dia de nascimento com base no mês e ano
    while True:
        try:
            # Definir o número máximo de dias com base no mês e ano
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                max_dias = 31
            elif mes in [4, 6, 9, 11]:
                max_dias = 30
            elif mes == 2:
                # Verificar se o ano é bissexto
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    max_dias = 29
                else:
                    max_dias = 28

            dia = int(input(f"Digite o dia de nascimento (1-{max_dias}): "))
            if dia < 1 or dia > max_dias:
                print(f"Dia inválido. Por favor, insira um valor entre 1 e {max_dias}.")
            else:
                break
        except ValueError:
            print("Dia inválido. Por favor, insira um valor numérico válido.")

    # Retornar a data de nascimento formatada
    return datetime(ano, mes, dia).date()