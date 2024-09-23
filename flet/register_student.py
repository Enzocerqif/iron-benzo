import flet as ft
import sqlite3
from components.button import button
import functions.verify_cpf as verify_cpf
import register_student_plan as add_plan
from functions.verify_birthdate import verificar_data_nascimento

def cadastrar_aluno(page: ft.Page):
    def submit(e):
        cpf = cpf_field.value
        nome = nome_field.value
        email = email_field.value
        telefone = telefone_field.value
        genero = genero_dropdown.value
        data_nascimento = data_nascimento_field.value

        if not cpf.isdigit() or len(cpf) != 11:
            dialog = ft.AlertDialog(title=ft.Text("CPF inválido. Ele deve ter 11 dígitos."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        if verify_cpf.verificar_cpf_existente(cpf):
            dialog = ft.AlertDialog(title=ft.Text("Erro: CPF já cadastrado no sistema."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        if not nome:
            dialog = ft.AlertDialog(title=ft.Text("Nome é obrigatório."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        if not email or "@" not in email:
            dialog = ft.AlertDialog(title=ft.Text("Email inválido."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        if not telefone.isdigit() or len(telefone) > 16:
            dialog = ft.AlertDialog(title=ft.Text("Número de telefone inválido."))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()
            return

        conn = None
        try:
            conn = sqlite3.connect('database/academia.db') 
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Aluno (cpf, nome_aluno, email, numero_telefone, genero, data_de_nascimento)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (cpf, nome, email, telefone, genero, data_nascimento))

            conn.commit()

            dialog = ft.AlertDialog(title=ft.Text(f"Aluno cadastrado com sucesso! CPF: {cpf}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

            add_plan.main(page)

        except sqlite3.Error as error:
            dialog = ft.AlertDialog(title=ft.Text(f"Erro ao cadastrar aluno: {error}"))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        finally:
            if conn:
                conn.close()

    cpf_field = ft.TextField(label="CPF", width=300)
    nome_field = ft.TextField(label="Nome completo", width=300)
    email_field = ft.TextField(label="Email", width=300)
    telefone_field = ft.TextField(label="Número de telefone", width=300)
    genero_dropdown = ft.Dropdown(
        label="Gênero",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
            ft.dropdown.Option("Indefinido"),
        ],
        width=300
    )
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)", width=300)
    submit_button = button(text="Cadastrar", on_click=submit)

    page.add(
        ft.Column(
            [
                cpf_field,
                nome_field,
                email_field,
                telefone_field,
                genero_dropdown,
                data_nascimento_field,
                submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )