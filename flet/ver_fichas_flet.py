import flet as ft
import sqlite3

from components.button import button

def ver_fichas(page: ft.Page):
    def submit(e):
        cpf = cpf_field.value
        id_ficha = id_ficha_dropdown.value

        if not cpf or not id_ficha:
            dialog = ft.AlertDialog(title=ft.Text("CPF e Ficha são obrigatórios."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        conn = None
        try:
            conn = sqlite3.connect('../academia.db')
            cursor = conn.cursor()

            cursor.execute('''
                SELECT nome_exercicio, series, repeticoes, dia_da_semana
                FROM Ficha_Treino
                WHERE id_ficha = ?
            ''', (id_ficha,))

            exercicios = cursor.fetchall()

            if not exercicios:
                dialog = ft.AlertDialog(title=ft.Text("Nenhum exercício encontrado para esta ficha."))
                page.overlay.append(dialog)
                dialog.open = True
                page.update()
                return

            dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
            exercicios_por_dia = {dia: [] for dia in dias_da_semana}

            for exercicio in exercicios:
                nome_exercicio, series, repeticoes, dia_da_semana = exercicio
                exercicios_por_dia[dia_da_semana].append(f"{nome_exercicio} - {series} séries de {repeticoes} repetições")

            exercicios_text = "\n\n".join([f"{dia}:\n" + "\n".join(exercicios_por_dia[dia]) for dia in dias_da_semana if exercicios_por_dia[dia]])

            dialog = ft.AlertDialog(title=ft.Text(f"Exercícios da Ficha:\n\n{exercicios_text}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        except sqlite3.Error as error:
            dialog = ft.AlertDialog(title=ft.Text(f"Erro ao buscar exercícios: {error}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        finally:
            if conn:
                conn.close()

    def carregar_fichas(e):
        cpf = cpf_field.value
        if not cpf:
            dialog = ft.AlertDialog(title=ft.Text("CPF é obrigatório."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        conn = None
        try:
            conn = sqlite3.connect('../academia.db')
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id_ficha, data_criacao
                FROM Ficha
                WHERE cpf = ?
            ''', (cpf,))

            fichas = cursor.fetchall()

            id_ficha_dropdown.options = [
                ft.dropdown.Option(str(ficha[0]), f"Ficha ID: {ficha[0]}, Data: {ficha[1]}") for ficha in fichas
            ]
            id_ficha_dropdown.value = None
            page.update()

        except sqlite3.Error as error:
            dialog = ft.AlertDialog(title=ft.Text(f"Erro ao carregar fichas: {error}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        finally:
            if conn:
                conn.close()

    cpf_field = ft.TextField(label="CPF do Aluno", width=300, on_change=carregar_fichas)
    id_ficha_dropdown = ft.Dropdown(label="Selecione a Ficha", width=300)
    submit_button = button(text="Ver ficha", on_click=submit)

    page.add(
        ft.Column(
            [
                cpf_field,
                id_ficha_dropdown,
                submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )