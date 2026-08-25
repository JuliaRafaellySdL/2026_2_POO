class Circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        return 3.14 * (self.raio ** 2)
    def circunferencia(self):
        return 2 * 3.14 * self.raio


x = Circulo()
print(x.raio)
x.raio = 3
print(x.raio)
print(x.area())
print(x.circunferencia())
