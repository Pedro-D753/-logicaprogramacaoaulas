while True:
    try:
        #entrada de dados
     etanol = float(input('Digite o preço do etanol: ').replace(',','.'))
     gasolina = float(input('Digite o preço da gasolina: ').replace(',','.'))
     calculo = (etanol/gasolina)*100
     resultado = 'Gasolina' if calculo > 70 else 'Etanol'

     print(f'Resultado = {calculo:.2f}%. Compensa abastecer com {resultado}.')

     opcao = input('Deseja refazer o cálculo? (s/n)'). lower().strip()
     match opcao:
        case 's':
           continue
        case 'n':
           break
        case _:
           print(f'Opção inválida!')
           continue
    except Exception as e:
        print(f'Não foi possível executar a operação {e}')
        continue
