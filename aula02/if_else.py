# concatenação
# quebra de linha
# formatando decimais
# alterando vírgula e ponto
# if else
# operador ternario


#cd - abrir uma pasta
#cd .. 'volta na pasta anterior'
#ctrl + s "salva o código"
#ls "listar"
#dim "listar diretorio"
#ctrl + j "abrir o terminal"
#cls 'limpa o terminal'

import this


nome = "Pedro"
idade = 16
altura = 1.70
#FIXME - concatenação com +
#print('Olá, meu nome é ' + nome + 'tenho' +  (idade) + 'anos de idade')
#FIXME - concatenação com ,
#print ('Olá, meu nome é,', nome ', tenho ' , (idade) ,'anos de idade')
#FIXME - concatenação com format
print #('Olá, meu nome é,'{} ', tenho {} anos de idade'.format(nome,idade))

#FIXME - concatenação com f-string
print(f'Olá, meu nome é {nome} e tenho {idade} anos de idade')
#O mais usado "print(f)"

#eliminado quebra de linha
print('O sábio sabia', end= '')
print(' que sabiá sabia assobiar')

valor = 1.23456789

# exibindo o valor com duas casas depois da vírgula
print(f' {valor:,.3f}')

print(30* '=')
peso = input('Digite seu peso: ').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}')

#Atividade 1

numero1 = float(input ("Digite o primeiro número: "))
print("O número float é:", numero1)
numero2 = int(input ("Digite o segundo número: "))
print("O número int é: ", numero2)
caracteres = str(input ("Digite algum texto ou caracter que não seja número: "))
print("O caracter str é: ",caracteres)
porta_aberta = bool(input(" A porta está aberta?(True/False)"))
print("A porta está aberta?", porta_aberta)
porta_fechada = bool(input("A porta está fechada?(True/False)"))
print("A porta está fechada?", porta_fechada)

nome = "Pedro"
idade = 16

#estrutura de decisão

nome = str(input('Digite seu nome'))
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print(f'Você é maior de idade!')
    print('Você esta dentro do bloco IF')
else:
    print('Você é menor de idade')
    print("Você está dentro do bloco ELSE")
    print('Você está fora da estrutura condicional if else')

    num1 = 10
if num1 %2 ==0:
    print('Numero par')
else: print('Numero impar')


print(40* '-','CINEMA',40*'-')
nome = str(input ("Fale seu nome"))
idade =int(input('Fale sua idade'))

if idade >= 18:
    print(f'A entrada de {nome} está autorizada.')
else:
    print(f'A entrada de {nome} nao está autorizada para assitir o filme, entrada somente com pais ou responsáveis')

#variaveis
nome = 'Alex'
idade = 39

#operador ternário
print(nome, 'é maior de idade.' if idade >=18 else 'é menor de idade.')