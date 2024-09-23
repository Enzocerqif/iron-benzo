import flet as ft
import sqlite3
from datetime import datetime

from components.button import button

def cadastrar_plano(cpf, plano_id):
    if plano_id == '1':
        nome_plano = "Anual"
        valor = 1000
    elif plano_id == '2':
        nome_plano = "Mensal"
        valor = 120
    elif plano_id == '3':
        nome_plano = "Diário"
        valor = 30
    else:
        return "Opção inválida. Por favor, escolha 1, 2 ou 3."

    # Data de adesão será a data atual
    data_adesao = datetime.now().date()
    status = "Ativo"

    # Conectar ao banco de dados e inserir o plano
    conn = sqlite3.connect('database/academia.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Plano_Aluno (cpf, id_plano, data_adesao, status)
        VALUES (?, ?, ?, ?)
    ''', (cpf, nome_plano, data_adesao, status))

    conn.commit()
    conn.close()

    return f"Plano ({nome_plano}) cadastrado com sucesso para o aluno com CPF {cpf}!"

def main(page: ft.Page):
    page.title = "Cadastrar Plano"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    cpf_field = ft.TextField(label="CPF)", width=300)
    plano_dropdown = ft.Dropdown(
        label="Escolha o plano",
        options=[
            ft.dropdown.Option("1", "Anual - R$ 1000"),
            ft.dropdown.Option("2", "Mensal - R$ 120"),
            ft.dropdown.Option("3", "Diário - R$ 30"),
        ],
        width=300
    )
    result_text = ft.Text()

    def cadastrar_plano_click(e):
        cpf = cpf_field.value
        plano_id = plano_dropdown.value
        if not cpf.isdigit() or len(cpf) != 11:
            result_text.value = "CPF inválido. Ele deve ter 11 dígitos."
        elif not plano_id:
            result_text.value = "Por favor, selecione um plano."
        else:
            result_text.value = cadastrar_plano(cpf, plano_id)
        page.update()

    cadastrar_plano_button = button(text="Cadastrar Plano", on_click=cadastrar_plano_click)

    page.add(
        ft.Column(
            [
                cpf_field,
                plano_dropdown,
                cadastrar_plano_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=main)