import flet as ft
import sqlite3
from datetime import datetime

from components.button import button

def criar_ficha(cpf):
    data_criacao = datetime.now().date()  # Data de criação da ficha (atual)

    # Conectar ao banco de dados e inserir a ficha
    conn = sqlite3.connect('../academia.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Ficha (cpf, data_criacao)
        VALUES (?, ?)
    ''', (cpf, data_criacao))

    conn.commit()
    conn.close()

    return f"Ficha criada com sucesso para o aluno com CPF {cpf}!"

def main(page: ft.Page):
    page.title = "Criar Ficha"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    cpf_field = ft.TextField(label="CPF (somente números)", width=300)
    result_text = ft.Text()

    def criar_ficha_click(e):
        cpf = cpf_field.value
        if not cpf.isdigit() or len(cpf) != 11:
            result_text.value = "CPF inválido. Ele deve ter 11 dígitos."
        else:
            result_text.value = criar_ficha(cpf)
        page.update()

    criar_ficha_button = button(text="Criar Ficha", on_click=criar_ficha_click)

    page.add(
        ft.Column(
            [
                cpf_field,
                criar_ficha_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=main)