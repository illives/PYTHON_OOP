class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} esta falando')

class Cliente(Pessoa):
    
    def comprar(self):
        print(f'{self.nomeclasse} comprando')
    
    def falar(self):
        print('Estou em Cliente')

class ClienteVip(Cliente):

    def falar(self):#Sobreposicao do metodo falar da classe superior
        super().falar()#Com o Super() chamamos o metodo da classe Cliente que é a Classe Pai desta classe
        Pessoa.falar(self)#Chamamos o Metodo falar da classe pessoa
        print('Falando educadamente!')

class Aluno(Pessoa):
    
    def estudar(self):
        print(f'{self.nomeclasse} estudando')
