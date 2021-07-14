#Criando uma Classe
class Pessoas:
    #Definindo Metodos == funcoes...primeiro o construtor
    def __init__(self, nome, idade, comendo = False, falando = False):
        #Colocando os atributos
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} ja esta comendo {comida}.')
            return
        print(f'{self.nome} esta comendo {comida}')
    
    def falar(self):
        if self.falando:
            print(f'{self.nome} esta falando')
            return
        print('{self.nome} comecou a falar')
        self.falando = True

if __name__ == '__main__':
#Acima impede que alguem execute o seu script de outro script.
    p1 = Pessoas('Jose', 35)#Instanciando o objeto pessoa 1
    p2 = Pessoas('Maria', 32)
    p1.comer('pizza')
    p2.falar()



