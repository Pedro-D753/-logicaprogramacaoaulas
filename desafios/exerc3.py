
print(40*'-','Código para calcular a média',40*'-')
lista =[]
sair = False

while sair == False:
    notas = (input ('Digite algumas notas ou aperte enter para sair: '))
    if notas != "":
        # append - adiciona o valor variavel dentro da lista
     lista.append(float(notas))
     lista.sort()
    else:
       sair = True

if lista:
    media = sum(lista)/len(lista)
    print(f'Média das notas: {media:.2f}')
else:
    print('Nenhuma nota foi digitada.')

if media >= 7:
  print(f'Aprovação')
else:
    print(f'Reprovação')