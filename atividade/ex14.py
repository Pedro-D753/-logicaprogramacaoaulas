# 14 Peça um número e exiba o quadrado dele.
num = int(input('Digite um número: '))
quadrado = num * num

print(f' O quadrado de {num} é {quadrado}')

# 15 Peça três números e exiba o produto deles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
produto = num1 * num2 * num3

print(f' O produto de {num1, num2, num3} é {produto}')

# 16 Peça o valor de um produto e exiba o valor após aplicar um desconto de 10%.

valor_do_produto = int(input('Digite o valor do produto: '))
valor_final = valor_do_produto * 0.10

print(f'O valor do desconto é {valor_final}')
print(f'O valor final do produto com o desconto aplicado é {valor_do_produto - valor_final}')

 # 17 Solicite um valor principal, a taxa de juros e o tempo, e exiba o valor dos juros simples.

valor_principal = int(input('Digite o valor principal: '))
tempo = int(input('Digite o tempo em dias, ou horas, ou minutos: '))
taxa_de_juros = float(input('Digite a taxa de juros: '))
formula_juros_simples = valor_principal * tempo * taxa_de_juros

print(f'O valor de juros simples aplicado no produto é {formula_juros_simples}')