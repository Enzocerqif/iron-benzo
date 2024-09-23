import flet as ft
import sqlite3
from datetime import datetime

from components.button import button

def cadastrar_ficha_treino(page: ft.Page):
    def submit(e):
        cpf = cpf_field.value
        nome_exercicio = nome_exercicio_field.value
        series = series_field.value
        repeticoes = repeticoes_field.value
        dia_da_semana = dia_da_semana_field.value

        if not cpf or not nome_exercicio or not series or not repeticoes or not dia_da_semana:
            dialog = ft.AlertDialog(title=ft.Text("Todos os campos são obrigatórios."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        conn = None
        try:
            conn = sqlite3.connect('../academia.db')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Ficha (cpf, data_criacao)
                VALUES (?, ?)
            ''', (cpf, datetime.now().strftime("%Y-%m-%d")))

            id_ficha = cursor.lastrowid

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

    cpf_field = ft.TextField(label="CPF do Aluno", width=300)
    nome_exercicio_field = ft.TextField(label="Nome do Exercício", width=300)
    series_field = ft.TextField(label="Séries", width=300)
    repeticoes_field = ft.TextField(label="Repetições", width=300)
    dia_da_semana_field = ft.TextField(label="Dia da Semana", width=300)
    submit_button = button(text="Cadastrar", on_click=submit)

    page.add(
        ft.Column(
            [
                cpf_field,
                nome_exercicio_field,
                series_field,
                repeticoes_field,
                dia_da_semana_field,
                submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

def ver_fichas(page: ft.Page):
    def submit(e):
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
                SELECT Ficha.id_ficha, Ficha.data_criacao, Ficha_Treino.nome_exercicio, Ficha_Treino.series, Ficha_Treino.repeticoes, Ficha_Treino.dia_da_semana
                FROM Ficha
                JOIN Ficha_Treino ON Ficha.id_ficha = Ficha_Treino.id_ficha
                WHERE Ficha.cpf = ?
            ''', (cpf,))

            fichas = cursor.fetchall()

            if not fichas:
                dialog = ft.AlertDialog(title=ft.Text("Nenhuma ficha encontrada para este CPF."))
                page.overlay.append(dialog)
                dialog.open = True
                page.update()
                return

            fichas_text = "\n".join([f"Ficha ID: {ficha[0]}, Data: {ficha[1]}, Exercício: {ficha[2]}, Séries: {ficha[3]}, Repetições: {ficha[4]}, Dia: {ficha[5]}" for ficha in fichas])
            dialog = ft.AlertDialog(title=ft.Text(f"Fichas do Aluno:\n{fichas_text}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        except sqlite3.Error as error:
            dialog = ft.AlertDialog(title=ft.Text(f"Erro ao buscar fichas: {error}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        finally:
            if conn:
                conn.close()

    cpf_field = ft.TextField(label="CPF do Aluno", width=300)
    submit_button = button(text="Ver Fichas", on_click=submit)

    page.add(
        ft.Column(
            [
                cpf_field,
                submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )