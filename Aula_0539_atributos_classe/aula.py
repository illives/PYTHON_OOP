class A:
    valor = 123


if __name__=='__main__':
    
    print(A.valor)
    A.valor = 4321#Atributo da Classe foi alterado
    p1= A()
    p2 = A()
    print(p1.valor)
    print(p2.valor)