while True:  
    # Inicia um loop infinito para mostrar o menu do cinema
    print(40*'-','CINEMA',40* '-') 
     # Mostra o cabeçalho do cinema
    print('1 - Sala 1') 
     # Opção de Sala 1
    print('2 - Sala 2')  
    # Opção de Sala 2
    print('3 - Sala 3')  
    # Opção de Sala 3
    print('4 - Sala 4') 
     # Opção de Sala 4
    print('5 - Sala 5') 
     # Opção de Sala 5
    print('6 - Sala 6')  
    # Opção de Sala 6

    opcao = input("Digite uma opção: ")  
    # Pede para o usuário escolher uma sala

    if opcao == "1":  
        # Verifica se a escolha foi Sala 1
        print('Sala 1') 
         # Mostra que o usuário entrou na Sala 1
        while True:  
            # Inicia loop interno para mostrar filmes da Sala 1
            print("1 - Quinteto Fantástico") 
             # Filme 1
            print("2 - Star Wars X O Recomeço") 
             # Filme 2
            print("3 - Vingadores Guerras Secretas")  
            # Filme 3
            print("4 - Superman Legacy")  
            # Filme 4

            escolha_filme = input("Escolha algum filme: ")  
            # Pede para escolher um filme
            if escolha_filme == "1":  
                # Filme 1
                print(f'"Quinteto Fantástico"') 
                 # Mostra filme
                idade = int(input('Fale sua idade: '))  
                # Pede idade
                if idade >=14:  
                    # Verifica idade mínima
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme') 
                     # Ingresso liberado
                    exit() 
                     # Encerra o programa
                else:  
                    # Caso não tenha idade mínima
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')  # Aviso

            if escolha_filme == "2":  
                # Filme 2
                print(f'"Star Wars X O Recomeço"') 
                 # Mostra filme
                idade = int(input('Fale sua idade: ')) 
                 # Pede idade
                if idade >=12: 
                     # Verifica idade mínima
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme') 
                     # Ingresso liberado
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')  # Aviso

            if escolha_filme == "3":  
                # Filme 3
                print(f'"Vingadores Guerras Secretas"')  
                # Mostra filme
                idade = int(input('Fale sua idade: ')) 
                 # Pede idade
                if idade >=16: 
                     # Verifica idade mínima
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme') 
                     # Ingresso liberado
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')  # Aviso

            if escolha_filme == "4": 
                 # Filme 4
                print(f'"Superman Legacy"')  
                # Mostra filme
                idade = int(input('Fale sua idade: '))  
                # Pede idade
                if idade >=14:  
                    # Verifica idade mínima
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme') 
                     # Ingresso liberado
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')  # Aviso

    if opcao == "2":  
        # Sala 2
        print('Sala 2')  
        # Mostra Sala 2
        while True: 
             # Loop interno para filmes da Sala 2
            print("5 - Carros 4")  
            # Filme 5
            print("6 - Toy Story 5")  
            # Filme 6
            print("7 - Aviões 3") 
             # Filme 7
            print("8 - Angry Birds 3") 
             # Filme 8

            escolha_filme = input("Escolha algum filme: ")  
            # Escolher filme
            if escolha_filme == "5": 
                 # Filme 5
                print(f'"Carros 4"')  
                # Mostra filme
                idade = int(input('Fale sua idade: ')) 
                 # Pede idade
                if idade >=1: 
                     # Verifica idade mínima
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')  
                    # Ingresso liberado
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')  # Aviso

            if escolha_filme == "6": 
                 # Filme 6
                print(f'"Toy Story 5"')
                idade = int(input('Fale sua idade: '))
                if idade >=10:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "7":  
                # Filme 7
                print(f'"Aviões 3"')
                idade = int(input('Fale sua idade: '))
                if idade >=10:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "8": 
                 # Filme 8
                print(f'"Angry Birds 3"')
                idade = int(input('Fale sua idade: '))
                if idade >=1:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

    if opcao == "3": 
         # Sala 3
        print('Sala 3')
        while True:  
            # Loop interno para filmes da Sala 3
            print("9 - Tropa de Elite")
            print("10 - Cidade de Deus")
            print("11 - O Auto da Compadecida")
            print("12 - Ainda estou aqui")

            escolha_filme = input("Escolha algum filme: ")
            if escolha_filme == "9":
                print(f'"Tropa de Elite"')
                idade = int(input('Fale sua idade: '))
                if idade >=16:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "10":
                print(f'"Cidade de Deus"')
                idade = int(input('Fale sua idade: '))
                if idade >=16:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "11":
                print(f'O Auto da Compadecida"')
                idade = int(input('Fale sua idade: '))
                if idade >=12:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "12":
                print(f'"Ainda estou aqui "')
                idade = int(input('Fale sua idade: '))
                if idade >=14:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')
                break 
             # Sai do loop da Sala 3

    if opcao == "4": 
         # Sala 4
        print('Sala 4')
        while True:  
            # Loop interno para filmes da Sala 4
            print("13 - 1917")
            print("14 - O Resgate do Soldado Ryan")
            print("15 - Oppenheimer")
            print("16 - Napoleão Bonaparte")

            escolha_filme = input("Escolha algum filme: ")
            if escolha_filme == "13":
                print(f'"1917"')
                idade = int(input('Fale sua idade: '))
                if idade >=16:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "14":
                print(f'"O Resgate do Soldado Ryan"')
                idade = int(input('Fale sua idade: '))
                if idade >=16:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "15":
                print(f'Oppenheimer"')
                idade = int(input('Fale sua idade: '))
                if idade >=14:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "16":
                print(f'"Napoleão Bonaparte"')
                idade = int(input('Fale sua idade: '))
                if idade >=14:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

    if opcao == "5":  
        # Sala 5
        print('Sala 5')
        while True:  
            # Loop interno para filmes da Sala 5
            print("17 - Titanic")
            print("18 - O Cavaleiro das Trevas")
            print("19 - Coringa")
            print("20 - Avatar")

            escolha_filme = input("Escolha algum filme: ")
            if escolha_filme == "17":
                print(f'"Titanic"')
                idade = int(input('Fale sua idade: '))
                if idade >=12:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "18":
                print(f'"O Cavaleiro das Trevas"')
                idade = int(input('Fale sua idade: '))
                if idade >=14:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "19":
                print(f'Coringa"')
                idade = int(input('Fale sua idade: '))
                if idade >=16:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')

            if escolha_filme == "20":
                print(f'"Avatar"')
                idade = int(input('Fale sua idade: '))
                if idade >=12:
                    print(f'Está aqui o seu ingresso, tenha um ótimo filme')
                    exit()
                else:
                    print(f'Você não possui a idade mínima para assistir o filme, não irá receber o ingresso')