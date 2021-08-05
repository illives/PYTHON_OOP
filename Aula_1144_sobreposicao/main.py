from classe import *

p1 = Pessoa('Josemar', 90)
p1.falar()

c1 = Cliente('Frederico', 60)
c1.falar()
c1.comprar()

a1 = Aluno('Pedrinho', 11)
a1.falar()
a1.estudar()

#Sobreposicao significa reescrever um metodo de uma classe filha dentro de uma outra classe
c2 = ClienteVip('Josefina', 21)
c2.falar()

