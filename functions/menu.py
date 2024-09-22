from functions.add_client import cadastrar_aluno
from functions.checar_prov import checar_informacoes

def exibir_menu():
    while True:
        print("\n--- Bem-vindo ao Sistema da Academia ---")
        print("1 - Cadastrar Aluno")
        print("2 - Checar Informações (Provisório)")
        print("0 - Fechar Programa")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            checar_informacoes()
        elif opcao == '0':
            print("Encerrando o programa... Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 0.")

if __name__ == '__main__':
    exibir_menu()