# atividade forca
# bibliotecas
import random
# importa a biblitoeca pra "sortear" no arquivo
import os
import json
# importa o json que está armazenando as palavras do json

with open("temas.json", "r", encoding="utf-8") as f: 
    # abre o arquivo json
    temas = json.load(f) 
    # lê o arquivo json

while True:
    print('--- FORCA - TEMAS ---')
    # menu 
    print('1 - Animais')
    print('2 - Times de Futebol')
    print('3 - Objetos de casa')
    print('Digite ''4'' para encerrar o programa.')
    
    tema = input('Escolha um tema: ')
    if tema == '1':
        def escolher_palavras():
            return random.choice(temas["Animais"]).lower()
            #escolhe palavra de forma aleat´roia de acordo com o tema dentro da lista json

    elif tema == '2':
        def escolher_palavras():
            return random.choice(temas["Times"]).lower()

    elif tema == '3':
        def escolher_palavras():
            return random.choice(temas["Objetos"]).lower()
        
    elif tema == "4":
         print('Programa encerrado. Até logo!')
         #Fim no programa
         break

    else:
        print('Opção inválida!')
        continue

    def jogar_forca():
        palavra = escolher_palavras()
        letras_corretas = []
        letras_erradas = []
        tentativas = 6
        # lógica do karython
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
                # append adiciona um elemento ao final da lista
            else:
                print('Letra incorreta!')
                letras_erradas.append(letra_usuario)
                tentativas -= 1

    if __name__ == '__main__':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Bem vindo ao jogo da forca')
        jogar_forca()
