'''
Programa: Sorteio V.3.0
Importando biblitecas
Aula 04: 19/08/2025

Random: escolha aleatoria
Descrição: sisttema recebe o nome dos candidatos e realiza o sorteio
'''

#importando lib
import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input('Digite o nome para o sorteio: ')
    if nome:
        lista_nomes.append(nome)
    else:
        break

while True:
    if lista_nomes:
     os.system('cls')
     escolhido = random.choice(lista_nomes)
     lista_sorteados.append(escolhido)
     #exclui o sorteado da lista original
     '''
     pop - função, remove pelo indice
        pop () - remover o ultimo indice
        pop(0) - remove o indice 0
     del - instrução, remover item pelo indice, mais de um item
          del[escolhido]
    remove - remove a partir de uma variavel
        lista.remove(variavel)
     '''

     print(f'O escolhido foi: ')
     lista_nomes.remove(escolhido)
    
    opcao = input('Deseja sortear outro nome? S - Sim\n| N - Não\n: ').lower()
    os.system('cls')

    if opcao != 's':
        break
else:
   print('Não há nomes para serem sorteados')
   exit()
   print('Programa finalizado!')
   print(f'Os sorteados foram {lista_sorteados}')