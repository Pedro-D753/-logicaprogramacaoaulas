# correção da atividade da aula passada (depois, lembrar de corrigir aquele código)

sala1 ="Vingadores" 
min1= 14
sala2 = "Avatar"
min2 = 14
sala3 = "Batman"
min3 = 16
sala4 = "Super Man"
min4 = 18
sala5 = "Homem Aranha"
min5 = "16"

while True:
    print(30*'-','CineClub',30*'-')
    print('Escolha uma opção de Filme que deseja assisitr!')
    print(f'1. Sala01 - {sala1} idade mínima {min1}')
    print(f'2. Sala02 - {sala2} idade mínima {min2}')
    print(f'3. Sala03 - {sala3} idade mínima {min3}')
    print(f'1. Sala04 - {sala4} idade mínima {min4}')
    print(f'1. Sala05 - {sala5} idade mínima {min5}')
    print(f'6. Sair')

    opcao = int(input("Digite a opção desejada: "))
    idade = input('Digite a sua idade: ')

    if opcao == 1:
        if idade >= min1:
            print(f'Bem Vindo ao CineClub')
            print(f'Ingresso para: {sala1}')
            print(f'Sala: 01')
        else:
            print('Você não possui idade mínima para assistir o filme')
    elif opcao == 2:
            print(f'Bem Vindo ao CineClub')
            print(f'Ingresso para: {sala1}')
            print(f'Sala: 01')
    else:
            print('Você não possui idade mínima para assistir o filme')
    elif opcao == 2:
    elif opcao == 3:
        ...
    elif opcao == 4:
        ...
    elif opcao == 5:
        ...
    elif opcao == 6:
        print("Saindo do sistema")
        break
    else:
        print('Opção Inválida')
    
