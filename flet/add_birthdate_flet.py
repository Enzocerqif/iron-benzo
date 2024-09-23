import flet as ft
from datetime import datetime

from components.button import button

def verificar_data_nascimento(ano, mes, dia):
    ano_atual = datetime.now().year
    if ano > ano_atual:
        return f"Ano inválido. O ano não pode ser maior que {ano_atual}."
    elif ano < 1900:
        return "Ano inválido. O ano deve ser maior ou igual a 1900."

    if mes < 1 or mes > 12:
        return "Mês inválido. Por favor, insira um valor entre 1 e 12."

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

    if dia < 1 or dia > max_dias:
        return f"Dia inválido. Por favor, insira um valor entre 1 e {max_dias}."

    return "Data de nascimento válida!"

def main(page: ft.Page):
    page.title = "Verificar Data de Nascimento"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    ano_field = ft.TextField(label="Ano de nascimento (YYYY)", width=300)
    mes_field = ft.TextField(label="Mês de nascimento (MM)", width=300)
    dia_field = ft.TextField(label="Dia de nascimento (DD)", width=300)
    result_text = ft.Text()

    def verificar_click(e):
        try:
            ano = int(ano_field.value)
            mes = int(mes_field.value)
            dia = int(dia_field.value)
            result_text.value = verificar_data_nascimento(ano, mes, dia)
        except ValueError:
            result_text.value = "Por favor, insira valores numéricos válidos."
        page.update()

    verificar_button = button(text="Verificar Data de Nascimento", on_click=verificar_click)

    page.add(
        ft.Column(
            [
                ano_field,
                mes_field,
                dia_field,
                verificar_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=main)