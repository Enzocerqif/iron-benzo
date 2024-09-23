import flet as ft
from components.button import button
from add_client_flet import cadastrar_aluno
from search_info_flet import checar_informacoes
from update_data_flet import atualizar_dados
from update_plan_flet import atualizar_plano
from add_ficha_treino_flet import cadastrar_ficha_treino, ver_fichas

def main(page: ft.Page):
    page.title = "Sistema da Academia Iron Benzo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def show_menu():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Bem-vindo ao Sistema da Iron Benzo", size=40),
                    button("Cadastrar aluno", on_click=cadastrar_aluno_click),
                    button("Cadastrar ficha de treino", on_click=show_cadastrar_ficha),
                    button("Ver fichas de treino", on_click=show_ver_fichas),
                    button("Todos os alunos", on_click=checar_informacoes_click),
                    button("Atualizar dados", on_click=atualizar_dados_click),
                    button("Atualizar plano", on_click=atualizar_plano_click),
                    button("Sair", on_click=fechar_programa_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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