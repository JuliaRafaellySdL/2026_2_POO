class Viagem:
    def __init__(self):
        self.distancia=0
        self.tempo=0

    def velocidade_media(self):
        return self.distancia/self.tempo

x=Viagem()
print(x.distancia,x.tempo)
x.distancia=46
x.tempo=12
print(x.distancia,x.tempo)
print(x.velocidade_media())