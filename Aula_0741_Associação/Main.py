from Classes import Escritor, MaquinaEscrever, Caneta


escritor = Escritor ('João Antonio')
caneta = Caneta ('BIC')
maquina = MaquinaEscrever()

# O Atibuto ferramenta da classe Escritor vai receber um objeto da classe Caneta ou Maquina de escrever
#No caso abaixo irá receber o metodo escrever desta classe
escritor.ferramenta = maquina #escritor.ferramenta recebe objeto maquina
escritor.ferramenta.escrever()
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
