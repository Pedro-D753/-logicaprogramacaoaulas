nome_usuario = input("Digite seu nome: ") # padrao string

peso = float(input("Digite seu peso").replace(','',''.'))

if peso >= 50:
    print("Acima de 5o kilos")
else: #se nao for verdadeiro
    print("Abaixo de 50 kilos")

    if peso >= 50:
        print("Acima de 50 kilos")
    elif peso>= 80:
        print("Acima de 80 kilos")
    elif peso>= 90:
        print("Acima de 90 kilos")
    else:
        print("Abaixo do peso")