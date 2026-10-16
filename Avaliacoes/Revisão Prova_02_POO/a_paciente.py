from datetime import datetime, timedelta

class Paciente:
    def __init__(self,nome,cpf,telefone,nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_nome(self,nome):
        if nome == "": raise ValueError ("O nome deve ser informado.")
        self.__nome=nome
    def set_cpf(self,cpf):
        if cpf == "": raise ValueError ("CPF deve ser informado.")
        self.__cpf=cpf
    def set_telefone(self,telefone):
        if telefone == "": raise ValueError ("Telefone deve ser informado.")
        self.__telefone=telefone
    def set_nascimento(self, nascimento):
        try:
            self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        except (TypeError, ValueError):
            raise ValueError("Nascimento inválido. Use o formato dd/mm/aaaa.")
        
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento

    def Idade(self):
        nascimento=datetime.strptime(self.__nascimento, "%d,%m,%Y")
        agora=datetime.now()

        tempo=agora-nascimento
        anos=tempo.days//365
        meses=tempo.days % 365 //30

        return (f"Anos: {anos} Meses: {meses}")

    def __str__(self):
        self.__nascimento.strftime("%d/%m/%Y")
        return(
            f"Nome: {self.__nome}"
            f"CPF: {self.__cpf}"
            f"Telefone: {self.__telefone}"
            f"Nascimento: {self.__nascimento}"
        )

class UI:
    pacientes=[]

    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.Inserir()
            if op == 2: UI.Listar_alfabeto()
            if op == 3: UI.Listar_idade()
        

    @staticmethod
    def menu():
        print(f"1 - Inserir Paciente, 2 - Listar paciente em ordem alfabética, 3 - Listar paciente pela idade")
        return int(input("Escolha uma opção: "))

    @classmethod
    def Inserir(cls):
        nome=input("Nome: ")
        cpf=input("CPF: ")
        telefone=input("Telefone: ")
        nascimento=input("Nascimento (dd/mm/aaaa): ")

        x=Paciente(nome,cpf,telefone,nascimento)
        cls.pacientes.append(x)
        print("Paciente inserido")

    @classmethod
    def Listar_alfabeto(cls):
        pacientes_ordenados=sorted(
            cls.pacientes, 
            key= lambda paciente: paciente.get_nome().lower()
        )

        for paciente in pacientes_ordenados:
            print(paciente)

    @classmethod
    def Listar_idade(cls):
        pacientes_ordenados=sorted(
            cls.pacientes,
            key=lambda paciente: paciente.get_nascimento()
        )

        for paciente in pacientes_ordenados:
            print(paciente)
            print(paciente.Idade())

UI.main()
