from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):# Herança multipla de LogMixin..vai herdar todos os metodos da classe
    
    def __init__(self, nome):
        super().__init__(nome)#Com o SUPER() chamamos o construtor da classe Eletronico
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado'
            self.log_info(info)
            print(info)
            return
        if self._conectado:
            error = f'{self._nome} JA ESTA CONECTADO'
            self.log_erro(error)
            print(error)
            return
        print(f'{self._nome} esta Conectado.')
        self._conectado = True
    
    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} Não esta conectado.'
            self.log_erro(error)
            print(error)
            return
        info = f'{self._nome} foi desligado.'
        self.log_info(info)
        print(info)
        self._conectado = False