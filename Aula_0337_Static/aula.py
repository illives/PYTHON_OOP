from random import randint

class Pessoas:
    ano_atual = 2021#Atributo da Classe

    def __init__(self, nome, idade):#Construtor Methodo
        self.nome = nome #Atributo do methodo
        self.idade = idade
    
    def get_idade(self):
        string = f'{self.nome} tem {self.idade} anos de vida!'
        return string
    
    @classmethod
    def ano_nascimento (cls, nome, idade):
        ano_nascimento = cls.ano_atual - idade
        return cls(nome, ano_nascimento)

    @staticmethod
    def get_id():
        id = randint(0,1000)
        return id

if __name__ == '__main__':
    p1 = Pessoas('Jucimar', 34)
    p2 = Pessoas.ano_nascimento('Zezao', 20)
    print(p1.get_idade())
    print(p2.nome)
    print(p2.idade)
    print(p2.get_id())
