import flet as ft
import sqlite3
from datetime import datetime

from components.button import button
from components.text_field import text_field
from components.dropdown import dropdown

def cadastrar_ficha_treino(page: ft.Page):
    def submit(e):
        cpf = cpf_field.value
        id_ficha = id_ficha_dropdown.value
        nome_exercicio = nome_exercicio_field.value
        series = series_field.value
        repeticoes = repeticoes_field.value
        dia_da_semana = dia_da_semana_dropdown.value

        if not cpf or not id_ficha or not nome_exercicio or not series or not repeticoes or not dia_da_semana:
            dialog = ft.AlertDialog(title=ft.Text("Todos os campos são obrigatórios."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        conn = None
        try:
            conn = sqlite3.connect('database/academia.db')
            cursor = conn.cursor()

            if id_ficha == "nova_ficha":
                cursor.execute('''
                    INSERT INTO Ficha (cpf, data_criacao)
                    VALUES (?, ?)
                ''', (cpf, datetime.now().strftime("%Y-%m-%d")))

                id_ficha = cursor.lastrowid
            else:
                id_ficha = int(id_ficha)

            cursor.execute('''
                INSERT INTO Ficha_Treino (id_ficha, nome_exercicio, series, repeticoes, dia_da_semana)
                VALUES (?, ?, ?, ?, ?)
            ''', (id_ficha, nome_exercicio, series, repeticoes, dia_da_semana))

            conn.commit()

            dialog = ft.AlertDialog(title=ft.Text(f"Ficha de treino cadastrada com sucesso!"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        except sqlite3.Error as error:
            dialog = ft.AlertDialog(title=ft.Text(f"Erro ao cadastrar ficha de treino: {error}"))
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
            conn = sqlite3.connect('database/academia.db')
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id_ficha, data_criacao
                FROM Ficha
                WHERE cpf = ?
            ''', (cpf,))

            fichas = cursor.fetchall()

            id_ficha_dropdown.options = [ft.dropdown.Option("nova_ficha", "Criar Nova Ficha")] + [
                ft.dropdown.Option(str(ficha[0]), f"Ficha ID: {ficha[0]}, Data: {ficha[1]}") for ficha in fichas
            ]
            id_ficha_dropdown.value = "nova_ficha"
            page.update()

        except sqlite3.Error as error:
            dialog = ft.AlertDialog(title=ft.Text(f"Erro ao carregar fichas: {error}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        finally:
            if conn:
                conn.close()

    cpf_field = text_field(label="CPF do Aluno", on_change=carregar_fichas)
    id_ficha_dropdown = dropdown(label="Selecione a Ficha", options=[])
    nome_exercicio_field = text_field(label="Nome do Exercício")
    series_field = text_field(label="Séries")
    repeticoes_field = text_field(label="Repetições")
    dia_da_semana_dropdown = dropdown(
        label="Dia da Semana",
        options=[
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
            "Domingo",
        ],
    )
    submit_button = button(text="Cadastrar", on_click=submit)

    page.add(
        ft.Column(
            [
                cpf_field,
                id_ficha_dropdown,
                nome_exercicio_field,
                series_field,
                repeticoes_field,
                dia_da_semana_dropdown,
                submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )