print(40* '-','CINEMA',40*'-')
nome = str(input ("Fale seu nome"))
idade =int(input('Fale sua idade'))

if idade >= 18:
    print(f'A entrada de {nome} está autorizada.')
else:
    print(f'A entrada de {nome} nao está autorizada para assitir o filme, entrada somente com pais ou responsáveis')
