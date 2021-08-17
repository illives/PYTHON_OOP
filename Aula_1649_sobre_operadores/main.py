"""
No Python os operadores podem tem seu comportamento alterado por métodos especiais.
"""

class Retangulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"
    
    def __add__(self, other):#Com esse método especial apontadmos duas variaveis, o x(self) e o y(other)
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo (novo_x, novo_y)
        #Se tornou um factore metodo, pois criou um novo objeto
    
    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 < a2:
            return True
        else:
            return False
    
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 > a2:
            return True
        else:
            return False

r1 = Retangulo(10,20)
r2 = Retangulo(10,10)
r3 = r1 + r2
print(r3)