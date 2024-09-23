import flet as ft
import sqlite3
from datetime import date

def atualizar_plano(page: ft.Page):
    page.title = "Atualizar Plano"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    cpf_field = ft.TextField(label="CPF (somente números)", width=300)
    escolha_dropdown = ft.Dropdown(
        label="Escolha uma ação",
        options=[
            ft.dropdown.Option("alterar", "Alterar Plano"),
            ft.dropdown.Option("encerrar", "Encerrar Plano"),
        ],
        width=300
    )
    novo_id_plano_field = ft.TextField(label="Novo ID do Plano", width=300, visible=False)
    result_text = ft.Text()

    def escolha_changed(e):
        if escolha_dropdown.value == "alterar":
            novo_id_plano_field.visible = True
        else:
            novo_id_plano_field.visible = False
        page.update()

    escolha_dropdown.on_change = escolha_changed

    def atualizar_click(e):
        cpf = cpf_field.value
        escolha = escolha_dropdown.value
        novo_id_plano = novo_id_plano_field.value
        data_atual = date.today().strftime('%Y-%m-%d')

        try:
            banco = sqlite3.connect('../academia_4.db')
            cursor = banco.cursor()

            if escolha == "encerrar":
                cursor.execute("""
                    UPDATE Plano_Aluno
                    SET status = 'Inativo', data_encerramento = ?
                    WHERE cpf = ? AND status = 'Ativo'
                """, (data_atual, cpf))
                banco.commit()
                result_text.value = f"Plano do aluno com CPF {cpf} foi encerrado com sucesso."

            elif escolha == "alterar":
                cursor.execute("""
                    UPDATE Plano_Aluno
                    SET status = 'Inativo', data_encerramento = ?
                    WHERE cpf = ? AND status = 'Ativo'
                """, (data_atual, cpf))
                cursor.execute("""
                    INSERT INTO Plano_Aluno (cpf, id_plano, data_adesao, status)
                    VALUES (?, ?, ?, 'Ativo')
                """, (cpf, novo_id_plano, data_atual))
                banco.commit()
                result_text.value = f"Plano do aluno com CPF {cpf} foi alterado com sucesso."

        except sqlite3.Error as erro:
            result_text.value = f"Erro ao tentar atualizar plano: {erro}"

        finally:
            if banco:
                cursor.close()
                banco.close()
                result_text.value += "\nConexão com o banco de dados encerrada."

        page.update()

    atualizar_button = ft.ElevatedButton(text="Atualizar Plano", on_click=atualizar_click)

    page.add(
        ft.Column(
            [
                cpf_field,
                escolha_dropdown,
                novo_id_plano_field,
                atualizar_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=atualizar_plano)