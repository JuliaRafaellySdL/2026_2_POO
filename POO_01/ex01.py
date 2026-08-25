class Triangulo:
    def __init__(self): #definir os dados
        self.b=0
        self.h=0
    def calcular_area(self): #operações
        return self.b*self.h/2

x=Triangulo() #Triangulo.__init__(x)
print(x.b, x.h)
x.b=10
x.h=10
print(x.b,x.h)
print(x.calcular_area())
