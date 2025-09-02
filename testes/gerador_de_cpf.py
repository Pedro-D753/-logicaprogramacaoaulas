# Tentativa de fazer um código que gere um cpf

print(40* '-','GERADOR DE CPF',40*'-')

import random

cpf = random.randint(0,123456789)
print('O CPF gerado foi:', cpf)
print(input(f'Deseja gerar outro CPF? '))(s/n).strip().lower()
if s:
    print('O CPF gerado foi:', cpf)
