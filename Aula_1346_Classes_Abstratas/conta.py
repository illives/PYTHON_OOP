
from abc import ABC, abstractmethod

class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    #getter
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor tem não é numerico.')
        self._saldo = valor
    
    def depositar (self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do Deposito precisa ser numerico')
        self.saldo += valor
    
    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Agência: {self.conta}', end=' ')
        print(f'Agência: {self.saldo}')
    
    @abstractmethod
    #Dependendo do tipo de conta 'sacar' algum dinheiro pode ter limite, por isso, esse metodo será abstrato. Forçando a classe filha sobreescrever o metodo.
    def sacar(self,valor):
        pass