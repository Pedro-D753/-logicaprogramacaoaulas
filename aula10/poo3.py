class Jedi:
    # construtor 
    def __init__(self, nome, vida,):
        # encapsulalamento = o '__' para deixar privado
        self.__nome = nome 
        self.__vida = vida

# para acessar os atributos já que eles estão privados

        # definindo GET para chamar o nome (ler)
    @property
    def nome(self):
        return self.__nome
        
        # definindo SET para mudar o nome do personagem
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @ property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 30
        print(f'{self.nome} atacou {personagem.nome} e tirou 30 pontos de vida.')
        print(f'Agora {personagem.nome} está com {personagem.vida} pontos de vida')
            

class Sith(Jedi):
    def __init__(self, nome, vida,):
        self.__nome = nome 
        self.__vida = vida


    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @ property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 70
        print(f'{self.nome} usou o estrangulamento da força em {personagem.nome} e tirou 70 pontos de vida.')
        print(f'Agora {personagem.nome} está com {personagem.vida} pontos de vida')
            

class Comum (Jedi):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, personagem):
        personagem.vida -= 25
        print(f'{self.nome} atirou em {personagem.nome}')
        print(f'Agora {personagem.nome} está com {personagem.vida} pontos de vida')

class Suporte(Jedi):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self, personagem):
        personagem.vida += 15
        print(f'{self.nome} usou poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida} pontos de vida')

class Verificar_vida:
    ...
    # implementar novas funções no código


darth_vader = Sith('Darth Vader', 100)
dindjarin = Comum('DinDjarin', 100) 
luke_skywalker = Jedi('Luke Skywalker', 100)
suporte_imperial = Suporte('Suporte', 100)    



if darth_vader.vida <= 0:
     print('Fim de jogo para Darth Vader')

if suporte_imperial.vida <= 0:
     print('Fim de jogo para Suporte Imperial')


dindjarin.atacar(darth_vader)
luke_skywalker.atacar(darth_vader)
suporte_imperial.curar(darth_vader)
darth_vader.atacar(luke_skywalker)
dindjarin.atacar(darth_vader)
luke_skywalker.atacar(darth_vader)
dindjarin.atacar(darth_vader)
