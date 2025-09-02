import json
import os

usuarios = []
novo_arquivo = ''

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
    usuario = {}
    print('1 - Cadastrar novo usario.')
    print('2 - Salvar arquivo json.')
    print('3 - Ler arquivo json.')
    print('4- Sair.')

    opcao = (input('Informe a opcao desejada: '))
    limpar()

    match opcao:
        case '1':
            usuario['nome'] = input('Informe o nome do usario: ').strip().title()
            usuario['idade'] = int(input('Informe a idade do usario: '))
            usuario['email'] = input('Informe o email do usario: ').strip().lower()

            usuarios.append(usuario)
            limpar()
            print('Usário cadastrado com sucesso!')
            continue
        case '2': 
            novo_arquivo = input('Informe o nome do arquivo: ').strip().lower()
            if novo_arquivo:
             with open(f'aula06/{novo_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print('Arquivo salvo com sucesso!')
            continue
        case '3':
            if not novo_arquivo:
                novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()
            with open(f'aula06/{novo_arquivo}.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
            print(f'{'-'*20}USUARIOS {'-'*20}\n')
            for usuario in dados:
                for chave in usuario:
                    print(f'{chave.capitalize()}: {usuario.get(chave)}')
                print('-'*40)
            continue
        case '4':
            print('Saindo do sistema!')
            break
        case _:
            print('Opcao invalida.')
            continue

                