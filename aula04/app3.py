'''
Programa: Sorteio V.2.0
Importando biblitecas
Aula 04: 19/08/2025

Random: escolha aleatoria
Descrição: sisttema recebe o nome dos candidatos e realiza o sorteio

'''

import random

lista =[]

sair = False

while sair == False:
    nome_candidato = input ('Digite os nomes para o sorteio ou aperte enter para sair: ')
    if nome_candidato != "":
        # append - adiciona o valor variavel dentro da lista
     lista.append(nome_candidato)
    else:
       sair = True
escolhido = random.choice(lista)

print('Escolhido foi: ', escolhido)