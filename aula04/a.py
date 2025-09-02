'''

#perccorrendo a lista com um contador
for i in range(len(nomes_lista)):
    print(f'{i+1}° nome da lista: {nomes_lista[i]}')
 # len (Conta a quantidade de elementos dentro da lista)

    lista_dados =  ['Alex', 39, 1.72]
    nomes_lista = ['Davi', 'Lucas', "Martins", "Fernando,", "Nunes", "Doris"]

    #ordena os dados da lista
    nomes_lista.sort
    '''

'''
Programa: Sorteio V.1.0
Importando biblitecas
Aula 04: 19/08/2025

Random: escolha aleatoria
Descrição: sisttema recebe o nome dos candidatos e realiza o sorteio

'''

#importando bibliotecas (lib)
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
nome5 = input('Digite o quinto nome: ')

lista_nomes= [nome1, nome2, nome3, nome4, nome5]
escolhido = random.choice(lista_nomes)
print(escolhido)
    
        
    