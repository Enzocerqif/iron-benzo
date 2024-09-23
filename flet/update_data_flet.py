import flet as ft
import sqlite3

def atualizar_dados(page: ft.Page):
    page.title = "Atualizar Dados"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    result_text = ft.Text()

    # Conectar ao banco de dados e carregar as tabelas
    def carregar_tabelas():
        try:
            banco = sqlite3.connect('../academia.db')
            cursor = banco.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tabelas = [row[0] for row in cursor.fetchall()]
            return tabelas
        except sqlite3.Error as erro:
            result_text.value = f"Erro ao carregar tabelas: {erro}"
            page.update()
        finally:
            if banco:
                cursor.close()
                banco.close()

    # Função para carregar colunas da tabela selecionada
    def carregar_colunas(tabela):
        try:
            banco = sqlite3.connect('../academia.db')
            cursor = banco.cursor()
            cursor.execute(f"PRAGMA table_info({tabela})")
            colunas = [row[1] for row in cursor.fetchall()]  # Segunda coluna é o nome da coluna
            return colunas
        except sqlite3.Error as erro:
            result_text.value = f"Erro ao carregar colunas: {erro}"
            page.update()
        finally:
            if banco:
                cursor.close()
                banco.close()

    # Função para atualizar campos de acordo com a tabela selecionada
    def tabela_selecionada(e):
        colunas = carregar_colunas(tabela_dropdown.value)
        coluna_dropdown.options = [ft.dropdown.Option(coluna) for coluna in colunas]
        condicao_coluna_dropdown.options = [ft.dropdown.Option(coluna) for coluna in colunas]
        page.update()

    # Dropdown para selecionar a tabela
    tabelas = carregar_tabelas()
    tabela_dropdown = ft.Dropdown(
        label="Selecione a tabela",
        options=[ft.dropdown.Option(tabela) for tabela in tabelas],
        on_change=tabela_selecionada,
        width=300
    )

    # Dropdown para selecionar a coluna a ser atualizada
    coluna_dropdown = ft.Dropdown(label="Selecione a coluna a atualizar", width=300)

    # Campo para o novo valor
    novo_valor_field = ft.TextField(label="Novo valor para a coluna", width=300)

    # Dropdown para selecionar a coluna da condição
    condicao_coluna_dropdown = ft.Dropdown(label="Selecione a coluna da condição", width=300)

    # Campo para o valor da condição
    condicao_valor_field = ft.TextField(label="Valor para a condição", width=300)

    # Função para atualizar os dados no banco de dados
    def atualizar_click(e):
        tabela = tabela_dropdown.value
        coluna = coluna_dropdown.value
        novo_valor = novo_valor_field.value
        condicao_coluna = condicao_coluna_dropdown.value
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

    # Botão de atualização
    atualizar_button = ft.ElevatedButton(text="Atualizar Dados", on_click=atualizar_click)

    # Layout da página
    page.add(
        ft.Column(
            [
                tabela_dropdown,
                coluna_dropdown,
                novo_valor_field,
                condicao_coluna_dropdown,
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
