def exibir_msg(nome):
        
        print(f'{'-'*20} Olá {nome}, seja bem vindo ao banco, você possui no momento um saldo de R$ {saldo}  {'-'*20}')

nome = input('Informe o seu nome: ')
idade = input('Informe a sua idade: ')
cpf = input('Informe o seu CPF: ')
numero_de_telefone = input('informe o seu número de telefone: ')
email = input('Informe o seu email: ')
saldo = (0,00)

exibir_msg(nome)

print(f'{'-'*20} Olá novamente {nome}, escolha alguma opcão {'-'*20}')

while True: 
        print(f'1 - Criar conta')
        print(f'2 - Exibir dados da conta')
        print(f'3 - Depositar valor')
        print(f'4 - Sacar valor')
        print(f'5 - Encerrar conta')
        print(f'6 - Sair do programa')

        opcao = input('Digite a opção que deseja escolher: ') 

        if opcao == '1':
           print(f'1 - Criar conta')
           nome_novo = input('Informe o seu nome: ')
           idade_novo = (input('Informe a sua idade: '))
           cpf_novo = (input('Informe o seu CPF: '))
           numero_de_telefone_novo = (input('informe o seu número de telefone: '))
           email_novo = ('Informe o seu email: ')

           print(f'{'-'*20} Olá {nome_novo}, seja bem vindo ao banco, você possui no momento um saldo de R$ {saldo}  {'-'*20}')

        elif opcao == '2':
            print(f'2 - Exibir dados da conta')
            print ()
            print(f'Nome: {nome} ')
            print(f'Idade: {idade} ')
            print(f'CPF: {cpf} ')
            print(f'Número de Telefone: {numero_de_telefone}')
            print(f'Email: {email} ')
            print(f'Saldo: {saldo} ')
            exit()

        elif opcao == '3':
              print(f'3 - Depositar Valor ')
              valor = float(input('Digite um valor para depositar: R$ '))
              if valor >= 0:
                    saldo+= valor
                    print(f'Depósito realizado, novo saldo R$ {saldo:.2f}')
              else:
                    print('Valor inválido')

        elif opcao == '4':
              print(f'4 - Sacar valor')
              input('Informe o valor que deseja sacar: ')
              if 0 < valor <= saldo:
                    saldo -= valor
                    print(f'Saque realizado, novo saldo R$ {saldo:.2f}')
       
        else:
              break
              
            
              
           


