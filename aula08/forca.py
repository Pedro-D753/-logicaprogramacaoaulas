import random
import os

def escolher_palavras():
    palavras = ['python','developer', 'programação', 'inteligência artificial',
            'algoritmo', 'computador', 'java', 'linguagens de programação',
            'software', 'mouse', 'teclado', 'garoto de programa', 'gabinete']

    return random.choice(palavras)


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
           print('Você perdeu! A palavra era:',palavra)
         break

    letra_usuario = input('Digite uma letra: ').lower()

    if letra_usuario in palavra:
        print('Letra correta!')
        letras_corretas.append(letra_usuario)
    else:
        print('Letra incorreta')
        letras_erradas.append(letra_usuario)
        tentativas

if __name__ == '__main__':
    os.system('cls')
    print('Bem vindo ao jogo da forca')
    jogar_forca()
        
