import flet as ft
import sqlite3

def atualizar_dados(page: ft.Page):
    page.title = "Atualizar Dados"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    tabela_field = ft.TextField(label="Nome da tabela", width=300)
    coluna_field = ft.TextField(label="Nome da coluna a atualizar", width=300)
    novo_valor_field = ft.TextField(label="Novo valor para a coluna", width=300)
    condicao_coluna_field = ft.TextField(label="Nome da coluna da condição", width=300)
    condicao_valor_field = ft.TextField(label="Valor para a condição", width=300)
    result_text = ft.Text()

    def atualizar_click(e):
        tabela = tabela_field.value
        coluna = coluna_field.value
        novo_valor = novo_valor_field.value
        condicao_coluna = condicao_coluna_field.value
        condicao_valor = condicao_valor_field.value

        try:
            banco = sqlite3.connect('../academia.db')
            cursor = banco.cursor()

            query = f"UPDATE {tabela} SET {coluna} = ? WHERE {condicao_coluna} = ?"
            valores = (novo_valor, condicao_valor)

            cursor.execute(query, valores)
            banco.commit()

            result_text.value = f"Registro atualizado com sucesso na tabela '{tabela}'!"
        
        except sqlite3.Error as erro:
            result_text.value = f"Erro ao tentar atualizar dados: {erro}"
        
        finally:
            if banco:
                cursor.close()
                banco.close()
                result_text.value += "\nConexão com o banco de dados encerrada."
        
        page.update()

    atualizar_button = ft.ElevatedButton(text="Atualizar Dados", on_click=atualizar_click)

    page.add(
        ft.Column(
            [
                tabela_field,
                coluna_field,
                novo_valor_field,
                condicao_coluna_field,
                condicao_valor_field,
                atualizar_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=atualizar_dados)