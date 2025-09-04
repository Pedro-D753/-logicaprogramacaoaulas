import random
import string

def gerar_senha(comprimento=12, incluir_maiusculo=True, incluir_minusculo=True,
                incluir_numeros=True, incluirr_caracter=True):
    
    caracteres=''
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase

    if incluir_minusculo:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres +=string.digits

    if incluirr_caracter:
        caracteres += string.punctuation

    if not caracteres:
        return ValueError('Deve ter pelo menos um tipo de caracteres')
    
    senha= ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'Senha:{senha}')
    return senha




def main():
    print('Gerador de Senhas fortes')
    comprimento = int(input('Digite o comprimento da senha (padrão é 12): ')or 12)
    incluir_maiuscula = input('Incluir maiúscula: (s/n, padrão = sim): ').lower()!='n'
    incluir_minuscula = input('Incluir minúscula: (s/n, padrão = sim): ').lower()!='n'
    incluir_numeros = input('Incluir números: (s/n, padrão = sim): ').lower()!='n'
    incluir_caracteres_esp = input('Incluir caractere especial (s/n, padrão = sim): ').lower()!='n'

    senha = gerar_senha(comprimento, incluir_maiuscula, incluir_minuscula, incluir_numeros, incluir_caracteres_esp)
    
    print(f'A senha gerada foi: {senha}')

    with open('senhas.txt', 'a') as s:
        s.write(f'\n{senha}')


if __name__ == '__main__':
    main()