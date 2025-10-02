import json
import os

JSON_FILE = "poo.json"

# garante que o arquivo existe e está com um JSON válido (lista)
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

try:
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()
        if conteudo == "":
            livros = []
        else:
            livros = json.loads(conteudo)
            if not isinstance(livros, list):
                livros = []
except (json.JSONDecodeError, FileNotFoundError):
    print("Aviso: arquivo JSON inválido — recriando arquivo vazio.")
    livros = []
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(livros, f, ensure_ascii=False, indent=4)

def salvar():
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(livros, f, ensure_ascii=False, indent=4)

class Livro:
    def __init__(self, id_livro: int, titulo: str, autor: str, ano: int):
        self.__id_in = id_livro
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

    def __str__(self):
        return f"[{self.__id_in}] {self.__titulo} {self.__ano} — {self.__autor}"

while True:
    print('\n--- SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ---')
    print('1 - Cadastrar livro.')
    print('2 - Listar.')
    print('3 - Atualizar.')
    print('4 - Excluir livro.')
    print('5 - Encerrar programa.')

    opcao = input('Digite a opção que deseja selecionar: ').strip()

    class Biblioteca:
     def __init__(self, arquivo_json="biblioteca.json"):
        self.__arquivo = arquivo_json
        self.__livros = []
        self.carregar_dados()

    if opcao == '1':  # cadastrar
        nome = input('Digite o nome do livro: ').strip()
        autor = input('Digite o nome do autor do livro: ').strip()
        id_in = input('Digite o número do ID: ').strip()
        ano = input('Digite o ano que o livro foi publicado: ')

        # checagem simples de ID duplicado 
        if any(str(l.get('ID')) == id_in for l in livros):
            print("ID já existe. Escolha outro ou atualize o livro existente.")
        else:
            livro = {'nome': nome, 'autor': autor, 'ID': id_in, 'ano': ano}
            livros.append(livro)
            salvar()
            print("Livro cadastrado!")

    elif opcao == '2':  # listar
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            for l in livros:
                nome = l.get('nome', '')
                autor = l.get('autor', '')
                id_in = l.get('ID', '')
                ano = l.get('ano', '')
                dados = Livro(nome, autor, id_in, ano)
                print(dados)

    elif opcao == '3':  # atualizar
        id_alvo = input("Digite o ID do livro a atualizar: ").strip()
        encontrado = False
        for i, l in enumerate(livros):
            if str(l.get('ID')) == id_alvo:
                novo_nome = input(f"Novo nome ({l.get('nome')}): ").strip() or l.get('nome')
                novo_autor = input(f"Novo autor ({l.get('autor')}): ").strip() or l.get('autor')
                novo_ano = input(f"Novo ano ({l.get('ano')}): ").strip() or l.get('ano')
                livros[i]['nome'] = novo_nome
                livros[i]['autor'] = novo_autor
                livros[i]['ano'] = novo_ano
                salvar()
                print("Livro atualizado!")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == '4':  # excluir
        id_alvo = input("Digite o ID do livro a excluir: ").strip()
        encontrado = False
        for i, l in enumerate(livros):
            if str(l.get('ID')) == id_alvo:
                conf = input(f"Confirmar exclusão de [{l.get('ID')}] {l.get('nome')} (s/N)? ").strip().lower()
                if conf == 's':
                    livros.pop(i)
                    salvar()
                    print("Livro excluído!")
                else:
                    print("Exclusão cancelada.")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == '5':  # sair
        print('Programa encerrado. Até logo!')
        break

    else:
        print("Opção inválida, tente novamente.")