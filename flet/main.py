import flet as ft
from components.button import button
from register.register_student import cadastrar_aluno
from search.search_training_sheets import ver_fichas
from search.search_students import checar_informacoes
from update.update_student_data import atualizar_dados
from update.update_plan import atualizar_plano
from register.register_plan_db import cadastrar_plano
from register.register_training_sheet import cadastrar_ficha_treino

def main(page: ft.Page):
    page.title = "Sistema da Academia Iron Benzo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def show_menu():
        page.controls.clear()
        page.add(
            ft.Container(
                content= ft.Container(
                    content = ft.Column(
                    [
                        ft.Text("Bem-vindo ao Sistema Iron Benzo", size=40),
                        button("Todos os alunos", on_click=checar_informacoes_click, icon=ft.icons.GROUP),
                        button("Adicionar aluno", on_click=cadastrar_aluno_click, icon=ft.icons.PERSON_ADD),
                        button("Adicionar fichas", on_click=show_cadastrar_ficha, icon=ft.icons.FITNESS_CENTER),
                        button("Fichas de treino", on_click=show_ver_fichas, icon=ft.icons.DESCRIPTION),
                        button("Adicionar plano", on_click=cadastrar_plano_click, icon=ft.icons.PLAYLIST_ADD),
                        button("Atualizar plano", on_click=atualizar_plano_click, icon=ft.icons.EDIT),
                        button("Atualizar dados", on_click=atualizar_dados_click, icon=ft.icons.UPDATE),
                        button("Sair", on_click=fechar_programa_click, icon=ft.icons.EXIT_TO_APP),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=ft.colors.BLACK87,
                padding=100,
                border_radius=10,
            ),
            expand=True,
            alignment=ft.alignment.center,
            image_src="https://img.freepik.com/fotos-premium/academia-moderna-e-totalmente-equipada-localizada-no-andar-superior-de-uma-torre-comercial-generative-ai_1000174-4419.jpg",
            image_fit=ft.ImageFit.COVER,
            )
        )
        page.update()

    def cadastrar_aluno_click(e):
        page.controls.clear()
        cadastrar_aluno(page)
        add_back_button()
        page.update()

    def checar_informacoes_click(e):
        page.controls.clear()
        checar_informacoes(page)
        add_back_button()
        page.update()

    def atualizar_dados_click(e):
        page.controls.clear()
        atualizar_dados(page)
        add_back_button()
        page.update()

    def atualizar_plano_click(e):
        page.controls.clear()
        atualizar_plano(page)
        add_back_button()
        page.update()

    def cadastrar_plano_click(e):
        page.controls.clear()
        cadastrar_plano(page)
        add_back_button()
        page.update()

    def show_cadastrar_ficha(e):
        page.controls.clear()
        cadastrar_ficha_treino(page)
        add_back_button()
        page.update()

    def show_ver_fichas(e):
        page.controls.clear()
        ver_fichas(page)
        add_back_button()
        page.update()

    def fechar_programa_click(e):
        page.window_close()

    def add_back_button():
        back_button = button("Voltar", on_click=lambda e: show_menu())
        page.controls.append(back_button)

    show_menu()

if __name__ == '__main__':
    ft.app(target=main)
