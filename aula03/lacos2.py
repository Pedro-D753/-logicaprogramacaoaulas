print(40*'-','ELEVADOR DE CARGA',40*'-')
elevador_de_carga = 200

peso = float(input("Digte seu peso: "))
peso_carga =float (input("Digite o peso da carga: "))

if (peso + peso_carga <=199):
    print("O elevador está habil a transportar você e a carga")
else:
    print("O elevador não está habil a transportar você e a carga")


numero = 10

while numero >= 0:
       print(numero)
       numero -= 1


cont = 0
while cont < 10:
     cont += 1
     if cont %2 ==0:
          print(cont)
     else:
       continue
     print("Contando...")

cont = 0
while cont < 15:
     cont += 1
     if cont %2 ==0:
          print(cont)
     elif cont >=7:
          break
     else:
          continue
     print("Contando...")




