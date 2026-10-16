class Circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        return 3.14 * (self.raio ** 2)
    def circunferencia(self):
        return 2 * 3.14 * self.raio


x = Circulo()
x.raio = 3
y = Circulo()
y.raio = 3
z=x
z.raio=20

print(x,x.raio,x.area(),x.circunferencia())
print(y,y.raio,y.area(),y.circunferencia())