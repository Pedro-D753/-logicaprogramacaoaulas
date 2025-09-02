'''
# revisao
nome = "Pedro"
idade = 16
print(type(nome)) # ver o tipo de dados da variavel

idade = float(idade)

print(40*'-','CALCULADORA DE IMC',40*'-')




while True:
       altura = float(input("Digite sua altura: ").replace(','',''.'))
       peso = input("Digte seu peso")
       imc = peso /(altura * altura)
       print()
       print(f'Seu IMC é: {imc:.2f}')
       
       if imc <= 18.5:
              print("Abaixo do normal")
       elif imc <= 24.9:
              print("Normal")
       elif imc <= 29.9:   
              print('Sobrepeso')
       elif imc <= 34.9:
              print("Obesidade grau I")
       elif imc <= 39.9:
              print("Obesidade grau II")
       else:
              print("Obesidade grau III")

       opcao = input("Deseja calcular novamente? S - Sim| N -Não").lower()

       if opcao == 's':
         continue
       elif opcao == 'n':
              print('Saindo do sistema!')
              break
       else:
        print("Opção inválida!")


cont  = 0

while cont <20:
      cont += 1
      if cont % 2 == 0:
         print(cont)
      elif cont < 5:
          pass
      elif cont >= 15:
            break
      else:
            continue
     

nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
telefone = input("Digite seu telefone: ")
dt_nascimento = int(input("Digite seu ano de nascimento: "))
print(80*'=')

while True:
    print(40*'-','Sistema console 2°DS',40* '-')
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Feliz Natal')
    print('6 - sair')

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        altura = float(input("Digite sua altura: ").replace(','',''.'))
        peso = input("Digte seu peso")
        imc = peso /(altura * altura)
        print()
        print(f'Seu IMC é: {imc:.2f}')
       
        if imc <= 18.5:
              print("Abaixo do normal")
        elif imc <= 24.9:
              print("Normal")
        elif imc <= 29.9:   
              print('Sobrepeso')
        elif imc <= 34.9:
              print("Obesidade grau I")
        elif imc <= 39.9:
              print("Obesidade grau II")
        else:
              print("Obesidade grau III")

    
    elif opcao == "2":
     ano_atual = 2025
     idade = ano_atual - dt_nascimento
     print(nome, 'é maior de idade.' if idade >=18 else 'é menor de idade.')
        
    elif opcao == "3":
        print("Calculadora")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        while True:
            print("1 - Soma")
            print("2 - Divisão")
            print("3 - Subtração")
            print("4 - Multiplicação")
            print("5 - Sair")

            opcao_calculo = input("Escolha uma operação matemática: ")

            if opcao_calculo == "1":
             print(f'Resultado da Soma é: {num1 + num2}')
            elif opcao_calculo == "2":
             print(f'Resultado da Divisão é: {num1 / num2}')
            elif opcao_calculo == "3":
             print(f'Resultado da Subtração é: {num1 - num2}')
            elif opcao_calculo == "4":
                print (f'Resultado da Multiplicação é: {num1 * num2}')
            elif opcao_calculo == "5":
                break
            
    elif opcao == "4":
        print(50*'_')
        print(f'|Nome: {nome}|Telefone: {telefone}')
        print(f'|CPF: {cpf}|Data de nascimento: {dt_nascimento}')
        print(50*'_')
        
    elif opcao == "5":
        linhas = 6
        j= 1

        while j<= linhas:
            espacos = linhas - j
            estrelas = 2 * j - 1

            print (" " *espacos + "*" * estrelas)
            j +=1 

    elif opcao == '6':
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida")
'''

nome = "Gomes"

for i in nome: #laço finito
      print(i.replace(i,'😂'))
