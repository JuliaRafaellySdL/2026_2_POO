class Viagem: #cria a classe viagem
    def __init__(self, destino, distancia, combustivel): #função
        self.destino=destino
        self.distancia=distancia
        self.combustivel=combustivel

    @property #get
    def destino (self):
        return self.__destino

    @destino.setter
    def destino(self, valor):
        if valor.strip()=="":
            raise ValueError("O destino não pode estar vazio")
        self.__destino=valor

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, valor):
        if valor <=0:
            raise ValueError("A distância deve ser um número positivo")
        self.__distancia=valor

    @property
    def combustivel(self):
        return self.__combustivel

    @combustivel.setter
    def combustivel(self, valor):
        if valor <=0:
            raise ValueError("O combustível deve ser um número maior que zero")
        self.__combustivel=valor

    def consumo(self):
        return self.distancia / self.combustivel

class ViagemUI:
    @staticmethod
    def menu():
        print("1 - Calcular")
        print("2 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def calculo():
        destino=input("Destino de viagem: ")
        distancia=float(input("Distância percorrida (km): "))
        combustivel=float(input("Combustível gasto (litros): "))

        viagem= Viagem (destino, distancia, combustivel)

        print("Dados da viagem")
        print(f"Destino: {viagem.destino}")
        print(f"Distância: {viagem.distancia} km")
        print(f"Combustível: {viagem.combustivel} L")
        print(f"Consumo médio: {viagem.consumo()} km/L")

    @staticmethod
    def main():
        opcao=ViagemUI.menu()

        while opcao !=2:
            if opcao ==1:
                try:
                    ViagemUI.calculo()
                except ValueError as erro:
                    print(f"Erro: {erro}")
            else:
                print("Opção inválida.")

            opcao=ViagemUI.menu()

        print("Programa encerrado")

ViagemUI.main()
    
 