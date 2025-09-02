import os

while True:
    try:
        novo_texto=input('Digite o texto: \n')
        nome_arquivo = input('Digite o nome do arquivo (sem extensão):').strip().lower()

        with open(fr'C:\Users\PedroDomiensedosSant\Documents\LogicaProgramaca_oAulas\aula05/{nome_arquivo}.txt', 'w', encoding= 'utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{nome_arquivo}.txt gravado com sucesso.')

        while True:
            prosseguir = input('Deseja abrir outro arquivo? (S/N): ').strip().lower()
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('Opção inválida!')
                continue
        match prosseguir:
            case 's':
                continue
            case 'n':
                 break
            
    except Exception as e :
        print(f'Não foi ler o arquivo. {e}')
        continue

