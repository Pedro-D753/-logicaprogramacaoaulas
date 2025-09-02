nomes_lista =['Pedro', 'Davi', 'Martins', 'Nunes', 'Doris', 'Fernando', 'Lucas', 'João', 'Cleber']
nomes_lista2 =['Caio','José','Roberto', 'Arthur', 'Otávio', 'Geovane' , 'Gabriel', 'Amorim' , '']
nome = input('Informe o nome que deseja encontrar: ')
import time

if nome in nomes_lista:
    print(nome)
    time.sleep(2)

else:
    print(f'{nome} não foi encontrado')
    time.sleep(2)

if nome in nomes_lista2:
    print(nome)
    time.sleep(2)

else:
    print(f'{nome} não foi encontrado na lista 2')
    time.sleep(2)
 #alterando dados de uma lista


nome_listas3 = ['Davi', 'Pedro', "Martins", "João", "Nunes", "Doris"]
nome_listas3[0] = 'Edu'
for nome in nome_listas3:
    print(nome)

nomes_lista3 = ['Davi', 'Pedro', "Martins", "João", "Nunes", "Doris"]
nome_a_alterar = input('Informe o nome que deseja alterar: ')
nomes_lista3[nomes_lista3.index(nome_a_alterar)] = input('Informe o novo nome: ')

for nome in nomes_lista3:
    print(nome)
    
resposta = input("Deseja excluir algum nome da lista1 ou da lista2? (SIM ou NÃO): ").lower()

if resposta == "sim":
    nome_excluir = input("Informe o nome que deseja excluir da lista 1: ")
    if nome_excluir in nomes_lista:
        nomes_lista.remove(nome_excluir)
        print(f"{nome_excluir} foi removido da lista 1.")
        print(f"Lista final da lista 1:")
for n in nomes_lista:
    print(n)
else:
    exit()
        
