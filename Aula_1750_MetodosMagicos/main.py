#https://rszalski.github.io/magicmethods/
#__init__ é um metodo magico
#Um design muito utilizado é o Singleton, ou seja, somente uma instacia para o projeto todo

class A:

    def __new__(cls, *args, **kwargs):       
        if not hasattr(cls,'_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste

    def __call__(self, *args, **kwds):
        #Faz se comportar como uma função
        resultado = 1
        for i in args:
            resultado *= i
        return resultado

    def __setattr__(self, name, value):
        if name == 'nome':
            self.__dict__[name] = 'You are not Allowed.'
        else:
            self.__dict__[name] = value

    def __del__(self):
        #Confirmação que o Garbage Colector do Python funcionou. Não é muito recomendado.
        print('Coletado a Sujeira.')

    def __str__(self):
        return "<class 'A'>"# Retorna informacao da Classe em Uso.
    
    def __len__(self):
        return 55
        #útil para usar como contador de metodos dentro de uma classe.
    
    def __init__(self):
        print('Eu sou o INIT')

a = A()
b = A()
c = A()
variavel = a(1,2,3,4,5,6,7,8,9,10)
print(variavel)

a.nome = 'Zezão da Esquina'
print(a.nome)
print(a)
print(len(a))