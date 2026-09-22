class Financeamento:
    def __init__(self,veiculo,valor,entrada,num_parcelas):
        self.set_veiculo(veiculo)
        self.set_valor(valor)
        self.set_entrada(entrada)
        self.set_num_parcelas(num_parcelas)

    def get_veiculo(self):
        return self.__veiculo
    def set_veiculo(self, veiculo):
        if veiculo=="": raise ValueError("Veículo deve ser informado")
        self.__veiculo=veiculo

    def get_valor(self):
        return self.__valor
    def set_valor(self,valor):
        if valor<0: raise ValueError("Valor deve ser positivo")
        self.__valor=valor

    def get_entrada(self):
        return self.__entrada
    def set_entrada(self,entrada):
        if entrada<0: raise ValueError("Entrada deve ser positiva")
        self.__entrada=entrada

    def get_num_parcelas(self):
        return self.__num_parcelas
    def set_num_parcelas(self,num_parcelas):
        if num_parcelas<1 or num_parcelas>36: raise ValueError("Número de parcelas deve estar entre 1 e 36")
        self.__num_parcelas=num_parcelas

    def valor_a_vista(self):
        return 0.95*self.__valor

    def valor_da_parcela(self):
        return(self.__valor - self.__entrada)/self.__num_parcelas

    def __str__(self):
        return f"{self.__veiculo}-{self.__valor:.2f}-{self.__entrada:.2f}-{self.__num_parcelas}"

class UI:
    @staticmethod
    def main():
        op=0
        while op != 2:
            op=UI.menu()
            if op==1:UI.calculo()

    @staticmethod
    def menu():
        print("1 - Financeamento, 2 - Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def calculo():
        veiculo=input("Nome do veículo: ")
        valor=float(input("Valor do veículo: "))
        entrada=float(input("Valor da entrada: "))
        num_parcelas=int(input("Número de parcelas: "))

        x=Financeamento(veiculo,entrada,valor,num_parcelas)
        print(f"Valor a vista: {x.valor_a_vista()}")
        print(f"Valor da parcela: {x.valor_da_parcela()}")

UI.main()
            