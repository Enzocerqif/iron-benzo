import flet as ft
import sqlite3

def cadastrar_plano(page: ft.Page):
    page.title = "Cadastrar Novo Plano"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campos para o formulário de cadastro
    nome_plano_field = ft.TextField(label="Nome do Plano", width=300)
    valor_plano_field = ft.TextField(label="Valor do Plano", width=300)
    result_text = ft.Text()

    # Função para cadastrar o plano no banco de dados
    def cadastrar_click(e):
        nome_plano = nome_plano_field.value
        valor_plano = valor_plano_field.value

        try:
            # Conectando ao banco de dados
            banco = sqlite3.connect('../academia.db')
            cursor = banco.cursor()

            # Comando SQL para inserir um novo plano
            query = "INSERT INTO Plano (nome_plano, valor) VALUES (?, ?)"
            valores = (nome_plano, valor_plano)

            cursor.execute(query, valores)
            banco.commit()

            # Atualizando mensagem de sucesso
            result_text.value = f"Plano '{nome_plano}' cadastrado com sucesso!"
        
        except sqlite3.Error as erro:
            result_text.value = f"Erro ao tentar cadastrar plano: {erro}"
        
        finally:
            if banco:
                cursor.close()
                banco.close()
                result_text.value += "\nConexão com o banco de dados encerrada."

        # Atualizando a página
        page.update()

    # Botão para realizar o cadastro
    cadastrar_button = ft.ElevatedButton(text="Cadastrar Plano", on_click=cadastrar_click)

    # Layout da página
    page.add(
        ft.Column(
            [
                nome_plano_field,
                valor_plano_field,
                cadastrar_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=cadastrar_plano)
