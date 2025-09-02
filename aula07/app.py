'''


def exibir_msg():
    print('-'20*, 'Bem vindo ao SENAI', '-'20*)
    print('Você está fazendo o CURSO DESENVOLVEDOR PYTHON')
'''
def exibir_msg(nome):
        print(f'{'-'*20} Olá {nome}, seja bem vindo ao SENAI {'-'*20}')

nome = input('Informe o seu nome: ')

exibir_msg(nome)

def calcular_equacao_primeiro_grau(a,b):
        x = -b/a
        return x

a = int(input('Informe o valor de a'))
b = int(input('Informe o valor de b'))

def matricular_aluno(nome, validação):
    if validação == True:
           return f'{nome}'
    

def verificar_matricula(nome):
       yield f'{nome} está com a documentação pendente.'
       yield f'{nome} está com a documentação em verificação.'
       yield f'{nome} está com a documentação aprovada com a matrícula pendente.'
       yield f'{nome} está com a matrícula aprovada e efetivada.'
       #yield = vários retornos, um return que não sai da função
       print = input('Informe o seu nome: ')

       situacao = verificar_matricula(nome)

# função recursiva

'''
def calcular_fatorial(n):
    if n == 0
    return 1
'''

soma = lambda x, y: x + y

x = int(input('Informe um número: '))
y = int(input('Informe outro número: '))

print(f'O resultado da soma é')


calcular_pg = lambda x: x* 2

numeros = [1, 2, 3, 4, 5]
print(list(map(calcular_pg, numeros)))

#exercicio 1 com função

def exibir_msg(nome):
        print(f'{'-'*20} Olá {nome}, seja bem vindo ao SENAI {'-'*20}')

nome = input('Informe o seu nome: ')





