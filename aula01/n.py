# Tipos de variaveis



print(30*"-" ",",30* "-")
num1 = 10
num2 = 10
soma = num1 + num2
divi = num1 / num2
divi_inteira = num1 // num2 #divisão inteira
mult = num1 * num2
expo = num1 ** num2
sub = num1 - num2
resto = num1 %2
print("Resultado da soma", num1,"+", num2, "é", soma)
print("Resultado da divisao inteira", num1,"//", num2, "é", soma)
print("Resultado da multiplicacao", num1,"*", num2, "é", mult)
print("Resultado da subtracao", num1,"-", num2, "é", sub)
print("Resultado do resto", num1,"%2", num2, "é", resto)
print("Resultado da exponenciacao", num1 ** num2, "é", expo)

print()
print(30*"-""," "operadores de comparação" ,30*"-")
#operadores de comparação
num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print("ano atual",ano)
ano += 1
print("ano acrescido de +1" ,ano)
ano -=1
print("Ano decrecido de -1",ano)

#operadores lógicos
#AND, OR, NOT


print()
print(30*'-'',' "Entrada de dados",30*"-")

nome_usuario = input("Digite o seu nome: ")
print("Seja bem-vindo ao sistema python",nome_usuario)

numero1 = float(input ("Digite o primeiro número "))
numero2 = float(input ("Digite o segundo número "))
#tipos de dados
#float = numeros reais, ou seja, tem "," , exemploo 5.20
# int = numeros inteiros
#str =texto, conjunto de caracteres
# bool = valores logicos como True e False

soma = numero1 + numero2
divisao = numero1 / numero2
mult = numero1 * numero2
sub = numero1 - numero2





print("Resultado da soma", numero1,"+", numero2, "é", soma)
print("Resultado da multiplicacao", numero1,"*", numero2, "é", mult)
print("Resultado da subtracao", numero1,"-", numero2, "é", sub)
print("Resultado da divisao", numero1,"/", numero2, "é", divisao)

print ()
print(30*"-" "," "Convertendo tipos de dados",30* "-")
ano_nascimento = input(" Digite seu ano de nascimento: ")
print(type(ano_nascimento))
#convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))


saudacao = input ("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
telefone = input("Digite seu telefone")

print(20*'-',"Dados pessoais, 20*'-'")
print("Nome:", saudacao)
print("CPF:", cpf, '| Telefone:',telefone)
print(50*'-')
'''
'''