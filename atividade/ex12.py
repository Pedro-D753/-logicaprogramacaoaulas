 # 12 Crie um sistema que receba um número e mostre o seu dobro, triplo, e raiz quadrada
num = int(input('Digite um número:'))
dobro = int(num) * 2
triplo = int (num) * 3
raiz = num ** (1/2)

print(f'O dobro de {num} é {dobro}')
print(f'O triplo de {num} é {triplo}')
print(f'A raiz de {num} é {raiz:.2f}')