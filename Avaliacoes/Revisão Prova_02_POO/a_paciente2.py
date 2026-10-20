from datetime import datetime, timedelta

class Paciente:
    def __init__(self,nome,cpf,telefone,nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_nome(self,nome):
        if nome == "": raise ValueError("O nome deve ser informado")
        self.__nome=nome
    def set_cpf(self,cpf):
        if cpf == "": raise ValueError("O cpf deve ser informado")
        self.__cpf=cpf
    def set_telefone(self,telefone):
        if telefone == "": raise ValueError("O telefone deve ser informado")
        self.__telefone=telefone
    def set_nascimento(self,nascimento):
        try:
            self.__nascimento=datetime.strptime(nascimento, "%d/%m/%Y")
        except (TypeError, ValueError):
            raise ValueError("Data de nascimento no formato incorreto")

    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento

    def Idade(self):
        nascimento=self.__nascimento
        agora=datetime.now()

        tempo=agora-nascimento
        anos=tempo.days//365
        meses=tempo.days % 365 //30

        return (f"Anos: {anos} Meses: {meses}")

    def __str__(self):
        return(
            f"Nome: {self.__nome}"
            f"CPF: {self.__cpf}"
            f"Telefone: {self.__telefone}"
            f"Idade: {self.__nascimento.strftime("%d/%m/%Y")}"
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
        print("1-Inserir paciente, 2-Listar por ordem alfabética, 3-Listar por idade, 4-Sair")
        return(int(input("Escolha uma opção: ")))

    @classmethod
    def Inserir(cls):
        nome=input("Nome: ")
        cpf=input("CPF: ")
        telefone=input("Telefone: ")
        nascimento=input("Nascimento: ")

        x=Paciente(nome,cpf,telefone,nascimento)

        cls.pacientes.append(x)
        print("Inserido")

    @classmethod
    def Listar_alfabeto(cls):
        pacientes_ord=sorted(
            cls.pacientes, key=lambda paciente:paciente.get_nome().lower()
        )
        for paciente in pacientes_ord:
            print(paciente)

    @classmethod
    def Listar_idade(cls):
        pacientes_ord=sorted(
            cls.pacientes, key=lambda paciente:paciente.get_nascimento()
        )
        for paciente in pacientes_ord:
            print(f"{paciente} - {paciente.Idade()}")

UI.main()