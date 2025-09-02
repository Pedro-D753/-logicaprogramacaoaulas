'''
Programa: Advinhação V 1.0.0
Importando biblitecas
Aula 04: 19/08/2025

Random: escolha aleatoria
Descrição: sisttema recebe o nome dos candidatos e realiza o sorteio
'''

# import lib
from random import randint

print('Tente advinhar o número')
num1 = int(input("Digite um número: "))

num_secreto = randint(1,10)

if num1 == num_secreto:
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu')
    print(f'O número correto é {num_secreto}')