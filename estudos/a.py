#classe = mesma coisa que objeto
# atributos = características do objeto
#metodos = ações
#intancias = objetos

class ControleRemoto:
 def __init__(self, cor, altura, profundidade, largura):
# inicializa a classe, todas as coisas que ja tem que existir
  self.cor = cor 
#self nesse caso faz uma referência a uma característica do controle
# o cor é uma característica do controle remoto
  self.altura = altura
  self.profundidade = profundidade
  self.largura = largura

def passar_canal(self, botao):
 if botao == '+':
  print('Aumentar o canal')
 elif botao == '-':
  print('Diminuir o canal')
#metodos do controle remoto:
# passar de canal
#mexer no volume
#abrir algum aplicativo
#desligar a TV


controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm',)
#exemplo de instancia
#aqui vai rodar o init
print(controle_remoto.cor)


controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')
#exemplo de instancia
