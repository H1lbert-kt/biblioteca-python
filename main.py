import biblioteca

def mostrar_menu():
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Livros emprestados")
    print("7 - Livros disponíveis")
    print("0 - Sair")

def main():

    while True:
        mostrar_menu()

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao == 1:
                biblioteca.cadastrar_livros()
            elif opcao == 2:
                biblioteca.listar_livros()
            elif opcao == 3:
                biblioteca.buscar_livros()
            elif opcao == 4:
                biblioteca.emprestrar_livro()
            elif opcao == 5:
                biblioteca.devolver_livro()
            elif opcao == 6:
                biblioteca.livros_emprestados()
            elif opcao == 7:
                biblioteca.livros_disponiveis()
            elif opcao == 0:
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite apenas números.")

if __name__ == "__main__":
    main()
    

    
