# listas, tuplas e dicionários - aula04 dia 19/08/2025
'''


nomes_lista = ['Davi', 'Lucas', "Martins", "Fernando,", "Nunes", "Doris"]
#listas

print(nomes_lista)
#imprime lista na tela

print(nomes_lista[0]) #exibe o primeiro nome da lista
print(nomes_lista[3]) #exibe o quarto nome da lista
print(nomes_lista[5]) #exibe o sexto nome da lista

#percorrendo a lista

for nome in nomes_lista:
    print(nome)

# lista
nomes_lista = ['Davi', 'Lucas', "Martins", "Fernando,", "Nunes", "Doris"]
nomes_lista2 = ['Davi', 'Pedro', "Martins", "João,", "Nunes", "Doris"]
nome = input('Informe o nome que deseja encontrar: ')

if nome in nomes_lista2:
    print(nome)
else:
    print(f' {nome} não encontrado')

nomes_lista =  ['Davi', 'Pedro', "Martins", "João,", "Nunes", "Doris"]
nome = input("Informe o nome que deseja encontrar")

#procura pelo índice através do valor
indice = nomes_lista.index(nome)

#retorna o resultado
try:
    print(f'{nome} encontrado no índice {indice}.')
except:
    print(f'{nome} não encontrado.')


nomes_lista =  ['Davi', 'Pedro', "Martins", "João,", "Nunes", "Doris"]
nome = input("Informe o nome que deseja encontrar")

#conta a quantidade de vezes que o valor foi encontrado
quantidade = nomes_lista.count(nome)

#retorna resultado
try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes.')
except:
    print(f'{nome} não foi encontrado')
    #range (Gera números, uma lista de números)


#alterando dados de uma lista
nome_listas3 = ['Davi', 'Pedro', "Martins", "João,", "Nunes", "Doris"]
nome_listas3[0] = 'Edu'

for nome in nome_listas3:
    print(nome)

nomes_lista = ['Davi', 'Pedro', "Martins", "João,", "Nunes", "Doris"]
nome_a_alterar = input('Informe o nome que deseja alterar: ')
nomes_lista[nomes_lista.index(nome_a_alterar)] = input('Informe o novo nome: ')

for nome in nomes_lista:
    print(nome)
'''

 # tabuada
numero = int(input('Digite o primeiro número: '))

for i in range (1,11):
    resultado = numero * i
    print(f'{i} X {numero} ={resultado}')

#Algumas bibliotecas:
#OS - Sistema Operacional
#Time 
#Random

'''
Programa: Contagem regressiva
Importando bibliotecas
Aula 04: 19/082025
'''
#importando bibliotecas

import os
from time import sleep 

cont = input('Digite um número inteiro: ')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'Contagem regressiva: {cont_int}...')
        sleep(1)
        cont_int -= 1
        os.system('cls')

except:
    print('Digite um número válido')

print('Fim da contagem!')