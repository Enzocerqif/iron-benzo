import flet as ft
import sqlite3

def checar_informacoes(page: ft.Page):
    page.title = "Informações dos Alunos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    alunos_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("CPF", size=16)),
            ft.DataColumn(ft.Text("Nome", size=16)),
            ft.DataColumn(ft.Text("Email", size=16)),
            ft.DataColumn(ft.Text("Telefone", size=16)),
            ft.DataColumn(ft.Text("Gênero", size=16)),
            ft.DataColumn(ft.Text("Data de Nascimento", size=16)),
            ft.DataColumn(ft.Text("Plano", size=16)),
            ft.DataColumn(ft.Text("Data de Adesão", size=16)),
            ft.DataColumn(ft.Text("Status", size=16)),
        ],
        rows=[]
    )

    def carregar_informacoes():
        conn = None  
        try:
            conn = sqlite3.connect('./academia_4.db')  
            cursor = conn.cursor()

            cursor.execute('''
                SELECT Aluno.cpf, Aluno.nome_aluno, Aluno.email, Aluno.numero_telefone, 
                       Aluno.genero, Aluno.data_de_nascimento, Plano_Aluno.id_plano, Plano_Aluno.data_adesao, 
                       Plano_Aluno.status 
                FROM Aluno
                LEFT JOIN Plano_Aluno ON Aluno.cpf = Plano_Aluno.cpf
            ''')

            alunos = cursor.fetchall()

            if alunos:
                alunos_table.rows.clear()
                for aluno in alunos:
                    cpf, nome, email, telefone, genero, data_nascimento, plano, data_adesao, status = aluno
                    alunos_table.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(cpf, size=14)),
                                ft.DataCell(ft.Text(nome, size=14)),
                                ft.DataCell(ft.Text(email, size=14)),
                                ft.DataCell(ft.Text(telefone, size=14)),
                                ft.DataCell(ft.Text(genero, size=14)),
                                ft.DataCell(ft.Text(data_nascimento, size=14)),
                                ft.DataCell(ft.Text(plano, size=14)),
                                ft.DataCell(ft.Text(data_adesao, size=14)),
                                ft.DataCell(ft.Text(status, size=14)),
                            ]
                        )
                    )
                page.update()
            else:
                dialog = ft.AlertDialog(title=ft.Text("Nenhum aluno cadastrado no sistema.", size=16))
                page.overlay.append(dialog)
                dialog.open = True
                page.update()

        except sqlite3.Error as error:
            dialog = ft.AlertDialog(title=ft.Text(f"Erro ao checar as informações: {error}", size=16))
            page.overlay.append(dialog)
            dialog.open = True
            page.update()

        finally:
            if conn:
                conn.close()

    carregar_informacoes()  

    page.add(
        ft.Column(
            [
                alunos_table,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )