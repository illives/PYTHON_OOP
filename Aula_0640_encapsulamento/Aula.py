
class BaseDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados

    def insert_into(self, id , nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})

if __name__ == '__main__':
    bd = BaseDados()
    lista = ['Maria', 'Joao', 'Jose']
    for v, n in enumerate(lista):
        bd.insert_into(v,n)
    print(bd._BaseDados__dados)
    print(f'Acessando BD com getter == {bd.dados}')