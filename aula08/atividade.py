# atividade forca

import random
import os
import json

with open("temas.json", "r", encoding="utf-8") as f:
    temas = json.load(f)

while True:
    print('--- FORCA - TEMAS ---')
    print('1 - Animais')
    print('2 - Times de Futebol')
    print('3 - Objetos de casa')

    tema = input('Escolha um tema: ')
    if tema == '1':
        def escolher_palavras():
            return random.choice(temas["Animais"]).lower()

    elif tema == '2':
        def escolher_palavras():
            return random.choice(temas["Times"]).lower()

    elif tema == '3':
        def escolher_palavras():
            return random.choice(temas["Objetos"]).lower()

    else:
        print('Opção inválida!')
        continue

    def jogar_forca():
        palavra = escolher_palavras()
        letras_corretas = []
        letras_erradas = []
        tentativas = 6

        while True:
            palavra_escondida = ''
            for letra in palavra:
                if letra in letras_corretas:
                    palavra_escondida += letra
                else:
                    palavra_escondida += '_'

            print('Palavra:', palavra_escondida)
            print('Letras erradas:', letras_erradas)
            print('Tentativas restantes:', tentativas)

            if palavra_escondida == palavra:
                print('Parabéns, você ganhou!!')
                break
            elif tentativas == 0:
                print('Você perdeu! A palavra era:', palavra)
                break

            letra_usuario = input('Digite uma letra: ').lower()

            if letra_usuario in palavra:
                print('Letra correta!')
                letras_corretas.append(letra_usuario)
            else:
                print('Letra incorreta!')
                letras_erradas.append(letra_usuario)
                tentativas -= 1

    if __name__ == '__main__':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Bem vindo ao jogo da forca')
        jogar_forca()

        

     

