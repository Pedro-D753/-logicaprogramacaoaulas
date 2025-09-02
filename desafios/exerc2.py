lista =[]

sair = False

while sair == False:
    numeros = (input ('Digite alguns números aleatórios ou aperte enter para sair: '))
    if numeros != "":
        # append - adiciona o valor variavel dentro da lista
     lista.append(int(numeros))
     lista.sort()
    else:
       sair = True

print(f'Lista final ordenada:', lista)

