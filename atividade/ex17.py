 # 17 Solicite um valor principal, a taxa de juros e o tempo, e exiba o valor dos juros simples.

valor_principal = int(input('Digite o valor principal: '))
tempo = int(input('Digite o tempo em dias, ou horas, ou minutos: '))
taxa_de_juros = float(input('Digite a taxa de juros: '))
formula_juros_simples = valor_principal * tempo * taxa_de_juros

print(f'O valor de juros simples aplicado no produto é {formula_juros_simples}')