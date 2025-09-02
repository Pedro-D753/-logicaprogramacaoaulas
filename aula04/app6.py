'''
Programa: Advinhação V 2.0.0
Importando biblitecas
Aula 04: 19/08/2025

Random: escolha aleatoria
Descrição: sisttema recebe o nome dos candidatos e realiza o sorteio
'''

# importando lib
import random
import time
import os

numero_secreto = random.randint(1,100)

tentativas = 0
max_tentativas = 10
acertou = False

print(30*'-', 'Bem Vindo ao AdvinhaLogo',30* '-')
print(f'Você tem {max_tentativas} tentavias para advinhar o número secreto')
print('Vamos começar?')

while tentativas < max_tentativas:
    try:
        #palpite do usuário
        palpite = int(input("Digite seu palpite: "))

    except ValueError:
        print("Por Favor, digite um número válido.")
        continue
    tentativas +=1

    # verificar palpite
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um numero maior!')
        time.sleep(3)
        os.system('cls')
    else: 
        print('Tente um número menor!')
        time.sleep(3)
        os.system('cls')

if acertou:
    print(f'Parabens, você ganhou! Você acertou o número {numero_secreto} em {tentativas} tentativas')
else: print(f'Que pena! Você não conseguiu acertar, o número certo é {numero_secreto}')

#append - adicion o item na lista (sempre no final da lista)

nomes_lista =['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Mariana']

novo_nome = input('Informe o novo nome a ser inserido na lista')
posicao = int(input('Informe a posição que deseja inserir (de 1 a 6):'))

# corrige a posição para a contagem do computador
posicao -=1

# tenta inserir o nome na posição desejada
try:
    del(nomes_lista[posicao])
except:
    print('Não foi possível deletar.')

    for nome in nomes_lista:
     print(nome)