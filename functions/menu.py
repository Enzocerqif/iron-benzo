from add_client import cadastrar_aluno
from checar_prov import checar_informacoes
from atualizarDados import atualizar_dados
from atualizarPlano import atualizar_plano

def exibir_menu():
    while True:
        print("\n--- Bem-vindo ao Sistema da Academia ---")
        print("1 - Cadastrar Aluno")
        print("2 - Checar Informações (Provisório)")
        print("3 - Atualizar Dados(1 por vez)")
        print("4 - Atualizar Plano")
        print("0 - Fechar Programa")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            checar_informacoes()
        elif opcao == '3':
            atualizar_dados()
        elif opcao == '4':
            atualizar_Plano()
        elif opcao == '0':
            print("Encerrando o programa... Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3, 4 ou 0.")

if __name__ == '__main__':
    exibir_menu()