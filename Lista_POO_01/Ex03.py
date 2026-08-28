class Conta:
    def __init__(self):
        self.nome = ""
        self.numero = 0
        self.saldo = 0

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if valor>=self.__saldo:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente")

    def verificar_saldo(self):
        return self.saldo


x = Conta()

x.nome = "Julia"
x.numero = 123
x.saldo = 100

print(x.nome)
print(x.numero)
print(x.verificar_saldo())

x.depositar(50)
print(x.verificar_saldo())

x.sacar(30)
print(x.verificar_saldo())