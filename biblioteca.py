livros = [
    {"titulo": "1984", "autor": "george orwell", "disponivel": True},
    {"titulo": "dom casmurro", "autor": "machado de assis", "disponivel": True}
         ]

def encontrar_livro(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return livro
    
    return None


def cadastrar_livros():

    novo_livro = {"titulo": input("Digite o título: ").lower(),
                  "autor": input("Digite o nome do autor: ").lower(),
                  "disponivel": True}
        
    for livro in livros:
        if livro["titulo"] == novo_livro["titulo"]:
            print("O livro já está cadastrado")
            return
        
    livros.append(novo_livro)
    print("Livro cadastrado.")

    
def listar_livros():

    for livro in livros:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f'{livro["titulo"].title()} - {livro["autor"].title()} | {status}')

def buscar_livros():
    buscar = input("Digite o título que deseja procurar: ").lower()
    for livro in livros:
        if livro["titulo"].lower() == buscar:
            print(f"O livro {buscar} foi encontrado.")
            return
            
    print("Não encontrado.")

def emprestrar_livro():
    emprestar = input('Digite o título do livro que deseja pegar emprestado: ').lower()
    livro = encontrar_livro(emprestar)
    if livro is None:
        print("Livro não encontrado.")
        return
    
    if livro["disponivel"]:
        livro["disponivel"] = False
        print(f'Livro {emprestar} emprestado com sucesso!')
    else:
        print('O livro já foi emprestado.')

def devolver_livro():
    titulo = input('Digite o título do livro que deseja devolver: ').lower()
    livro = encontrar_livro(titulo)
    if livro is None:
        print('Não encontrado.')
        return
    
    if livro["disponivel"] == False:
        livro["disponivel"] = True
        print("Livro devolvido com sucesso, muito obrigado pela preferência!!")
    else:
        print("Livro já disponível na biblioteca.")

def livros_emprestados():
    emprestados = [livro for livro in livros if not livro["disponivel"]]

    if not emprestados:
        print("Nenhum livro emprestado")
        return
    
    print("Livros emprestados:")

    for livro in emprestados:
        print(f'{livro["titulo"]} - {livro["autor"]}')


def livros_disponiveis():
    disponiveis =  [livro for livro in livros if livro["disponivel"]]

    if not disponiveis:
        print("Nenhum livro disponível")
        return
    
    print("Livros disponíveis:")

    for livro in disponiveis:
        print(f'{livro["titulo"]} - {livro["autor"]}')
    

