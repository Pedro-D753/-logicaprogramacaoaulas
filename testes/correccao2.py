contas = {}
proximo_numero = 1001
import random


def exibir_dados():
    numero = int(input('Digite o número da conta: '))
    if not contas:
        print('Nenhuma conta encontrada')
        return
    for numero, dados, in contas.item():
        print()
        print(f'Conta: {numero}')
        print(f'Saldo: {dados['saldo']}')
        print(f'Cliente: {dados['nome']} | CPF: {dados['cpf']}')
        print()

def criar_conta():
    global proximo_numero
    nome = input('Digite seu nome:').strip()
    cpf = input('Digite seu CPF:').strip()
    numero = random.randint(0,1001)
    print(f'O número da sua conta será {numero}')
    return numero
    
    
def depositar():
    numero = int(input('Digite o número da conta: '))
    if numero in contas:
       valor = float(input('Digite o valor que deseja depositar: '))
       contas[numero]['saldo'] += valor

def sacar():
    numero = input('digite o número da conta: ')
    if numero in  contas:
        valor = float(input('Digite o valor que deseja sacar: '))
        if valor <= contas[numero]['saldo']:
            contas[numero]['saldo'] -= valor
            print(f'Saque de {valor:.2f} realizado com sucesso')
        else:
            print('Saldo Insuficiente!')
    else:
        print('Conta não encontrada')

def encerrar_conta():
    numero = int(input('DIgite o número da conta'))
    if numero in  contas:
       del contas[numero]

def sair():
    print('Saindo...')
    exit()

while True:
    print('--- MENU BANCO ---')
    print('1 - Criar conta bancaria')
    print('2 - Mostrar dados da conta')
    print('3 - Depositar')
    print('4 - Sacar')
    print('5 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        exibir_dados(numero)
    elif opcao == '3':
        depositar()
    elif opcao == '4':
        sacar()
    elif opcao == '5':
        sair()
    else:
        print('Opção inválida!')    

    
    