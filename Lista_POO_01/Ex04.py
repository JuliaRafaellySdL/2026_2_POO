class Entrada:
    def __init__(self):
        self.dia = ""
        self.hora = 0

    def valor(self):
        if self.dia == "Segunda" or self.dia == "Terça" or self.dia == "Quinta":
            if self.hora < 17 and self.hora > 0:
                preco = 16
            else:
                preco = 16 + (16 * 0.50)

        if self.dia == "Quarta":
            preco = 8

        if self.dia == "Sexta" or self.dia == "Sábado" or self.dia == "Domingo":
            if self.hora < 17 and self.hora > 0:
                preco = 20
            else:
                preco = 20 + (20 * 0.50)

        return preco


x = Entrada()

x.dia = input("Dia da semana: ")
x.hora = int(input("Hora do filme: "))

if x.dia != "Quarta":
    meia = input("Meia entrada? (S/N) ")

    if meia == "S":
        print(x.valor() / 2)
    else:
        print(x.valor())

if x.dia == "Quarta":
    print(x.valor())