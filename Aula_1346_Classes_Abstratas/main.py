from Aula_1346_Classes_Abstratas.conta_corrente import ContaCorrente
from conta_popupanca import ContaPoupanca
from conta_corrente import ContaCorrente

cp = ContaPoupanca(1125, 45685, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(10)


cc = ContaCorrente(1125, 45685, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)

#Uma Classe Absrata é quando criamos uma classe e não queremos que ela seja instanciada.
#Ela pode ter metodos concretos e metodos abstratos
#Metodos Concretos == Metodos normais que tem funcionalidades
#Metodos abstratos == so se cria o metodo (def com pass) obrigando as classes filhas a sobreescreverem o metodo.
#A ideia...Se cria uma classe 'conceito' e as classes filhas se especializam em cima do conceito...para isso se usa o decorador @abstractmethod nos metodos