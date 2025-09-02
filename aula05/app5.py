# importação
import json
'''

Dicionario = {}

estrutura:
{
'Nome': "Maria"
'idade':16

variavel:  

'''
try:
    arquivo = input('Digite o nome do arquivo: ').strip().lower()

    with open(f'{arquivo}.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)

        print(f'{'-'*20} DADOS {'-'*20}\n ')
        for dado in dados:
            for chave in dado:
             print(f'{chave.capitalize()}: {dado.get[chave]}')
             print('-'*40)
except Exception as e:
    print(f'Não foi possível ler o arquivo. {e}')