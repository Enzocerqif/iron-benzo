import flet as ft
import sqlite3

from components.button import button

def verificar_cpf_existente(cpf):
    conn = None
    try:
        conn = sqlite3.connect('../academia.db')
        cursor = conn.cursor()

        cursor.execute('SELECT cpf FROM Aluno WHERE cpf = ?', (cpf,))
        resultado = cursor.fetchone()

        return resultado is not None

    except sqlite3.Error as error:
        return f"Erro ao verificar CPF: {error}"
    
    finally:
        if conn:
            conn.close()

def main(page: ft.Page):
    page.title = "Verificar CPF"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    cpf_field = ft.TextField(label="CPF (somente números)", width=300)
    result_text = ft.Text()

    def verificar_cpf_click(e):
        cpf = cpf_field.value
        if not cpf.isdigit() or len(cpf) != 11:
            result_text.value = "CPF inválido. Ele deve ter 11 dígitos."
        else:
            resultado = verificar_cpf_existente(cpf)
            if isinstance(resultado, str):
                result_text.value = resultado
            elif resultado:
                result_text.value = "CPF já cadastrado no sistema."
            else:
                result_text.value = "CPF não encontrado no sistema."
        page.update()

    verificar_cpf_button = button(text="Verificar CPF", on_click=verificar_cpf_click)

    page.add(
        ft.Column(
            [
                cpf_field,
                verificar_cpf_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=main)