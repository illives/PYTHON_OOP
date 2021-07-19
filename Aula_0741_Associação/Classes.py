class Escritor:
    def __init__(self,nome):
        self.__nome = nome
        self.__ferrmanta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferrmanta
    #setter
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferrmanta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta esta escrevendo...')

class MaquinaEscrever:
    
    def escrever(self):
        print('Maquina esta escrevendo...')