class Pais:
    def __init__(self, nome, populacao, area):
        self.nome=nome
        self.populacao=populacao
        self.area=area

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if valor.strip()=="":
            raise ValueError("O nome não pode estar vazio")
        self.__nome=valor

    @property
    def populacao(self):
        return self.__populacao
    @populacao.setter
    def populacao(self, valor):
        if valor<=0:
            raise ValueError("O número de habitantes deve ser maior que zero")
        self.__populacao=valor

    @property
    def area(self):
        return self.__area
    @area.setter
    def area(self,valor):
        if valor<=0:
            raise ValueError("A área deve ser um número maior que zero")
        self.__area=valor

    def densidade(self):
        return self.populacao/self.area

class PaisUI:
    @staticmethod
    def menu():
        print("1-Calcular")
        print("2-Fim")
        return int(input("Selecione uma das opções: "))

    @staticmethod
    def calculo():
        nome=input("Nome: ")
        populacao=float(input("Número de habitantes: "))
        area=float(input("Área total: "))

        pais=Pais(nome,populacao,area)

        print(f"Nome: {pais.nome}")
        print(f"Número de habitantes: {pais.populacao}")
        print(f"Área total: {pais.area} km2")
        print(f"Densidade: {pais.densidade()} habitantes/km2")

    @staticmethod
    def main():
        opcao=PaisUI.menu()
        while opcao!=2:
            if opcao==1:
                try:
                    PaisUI.calculo()
                except ValueError as error:
                    print(f"Erro: {error}")
            else:
                print("Opção inválida.")

            opcao=PaisUI.menu()
        print("Programa finalizado!")

PaisUI.main()