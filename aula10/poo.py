# metodos - que são as ações desse objeto
#nome e vida - atacar
# self quando quero me referir a algum atributo da classe
# construtor - quando quero criar um novo objeto, chamo o construtor para acessar os atributos
# setter - novo valor
# get - adicionar um novo valor

class Personagem:
    # construtor
    def __init__(self, nome, vida):
     # encapsulamento
     self.nome = nome
     self.vida = vida

    # definindo GET e SET
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_nome):
       self.__nome = novo_nome

    @ property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
     personagem.vida -= 20
    print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
    print(f'Agora está com {personagem.vida}')
            

personagem1= Personagem('Gandof', 100)
personagem2 = Personagem('Legolas', 100)

personagem1.atacar(personagem2)
personagem2.atacar(personagem1)


class Guerreiro:
    ...

class Mago:
    ...