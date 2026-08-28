#Entidade
class ContaBancaria:
    def __init__(self):
        self.titular="sem nome"
        self.numero="sem numero"
        self.__saldo=0                      #Encapsulamento

    def depositar(self,valor):
        if valor>0:
            self.__saldo+=valor
        else:
           # print("Valor deve ser positivo")
           raise ValueError("Valor deve ser positivo")

    def sacar(self,valor):
        if self.__saldo>=valor and valor>=0:
            self.__saldo-=valor
        else:
            #print("Saldo insuficiente")    
           raise ValueError("Valor deve ser positivo ou saldo insuficiente")

    def consultar_saldo(self):
      return self.saldo

#Interface com o usuário
x= ContaBancaria()
x.titular="Eduardo"
x.numero="123-0"

print(x.titular,x.numero,x.consultar_saldo())
x.depositar(1000)
print(x.titular,x.numero,x.consultar_saldo())
x.sacar(300)
print(x.titular,x.numero,x.consultar_saldo())
