#Polimorfismo é quando um metodo derivado de uma classe superior é sobreescrito, porém, com um comportamento diferente.

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg): print(f'B esta faland{msg}')

class C(A): 
    def fala (self, msg): print(f'C está falando {msg}')


if __name__=='__main__':
    b = B()
    c = C()
    b.fala()
    c.fala()