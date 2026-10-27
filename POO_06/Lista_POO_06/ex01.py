import json
from pathlib import Path

class Cliente:
    def __init__(self,id,nome,email,fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self,id):
        if id <=0: raise ValueError("O ID deve ser um número positivo.")
        self.__id=id

    def set_nome(self,nome):
        if nome == "": raise ValueError("O nome deve ser informado.")
        self.__nome=nome

    def set_email(self, email):
        if email == "": raise ValueError("O email deve ser informado.")
        self.__email=email

    def set_fone(self, fone):
        if fone == "": raise ValueError("O telefone deve ser informado.")
        self.__fone=fone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def __str__(self):
        return (
            f"ID: {self.__id} "
            f"Nome: {self.__nome} "
            f"Email: {self.__email} "
            f"Telefone: {self.__fone}"
        )

class ClienteDAO:
    objetos=[]
    arquivo = Path(__file__).with_name("clientes.json")

    @classmethod
    def Inserir(cls, cliente): #Inserir objeto na lista
        if cls.Listar_Id(cliente.get_id()) is not None:
            raise ValueError("ID já utilizado.")
        cls.objetos.append(cliente)

    @classmethod
    def Listar(cls): #Retornar os objetos na lista
        return cls.objetos.copy()

    @classmethod
    def Listar_Id(cls, id): #Retornar o objeto com um ID determinado
        for cliente in cls.objetos:
            if cliente.get_id() == id:
                return cliente
        return None

    @classmethod
    def Atualizar(cls,id,nome,email,fone): #Atualizar dados de um objeto
        cliente=cls.Listar_Id(id)
        if cliente is None: return False

        cliente.set_nome(nome)
        cliente.set_email(email)
        cliente.set_fone(fone)
        return True

    @classmethod
    def Excluir(cls,id): #Excluir objeto da lista
        cliente=cls.Listar_Id(id)
        if cliente is None: return False

        cls.objetos.remove(cliente)
        return True

    @classmethod
    def Abrir(cls): #Recuperar a lista de objetos de um arquivo JSON
        if not cls.arquivo.exists():
            cls.objetos=[]
            return

        try:
            with cls.arquivo.open("r", encoding="utf-8") as arquivo:
                dados=json.load(arquivo)

            cls.objetos=[
                Cliente(
                    int(item["id"]), item["nome"], item["email"], item["fone"]
                )
                for item in dados
            ]

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as erro:
            cls.objetos=[]
            print(f"Não foi possível carregar os clientes: {erro}")

    @classmethod
    def Salvar(cls): #Salvar a lisa de objetos em um arquivo JSON
        dados=[
            {
                "id": cliente.get_id(),
                "nome": cliente.get_nome(),
                "email": cliente.get_email(),
                "fone": cliente.get_fone()
            }
            for cliente in cls.objetos
        ]

        with cls.arquivo.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

class UI:
    @staticmethod
    def main():

        ClienteDAO.Abrir()

        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.Cliente_Listar()
            elif op == 2: UI.Cliente_Inserir()
            elif op == 3: UI.Cliente_Atualizar()
            elif op == 4: UI.Cliente_Excluir()
            elif op == 5: print("Aplicação finalizada")

    @staticmethod
    def menu():
        print("1-Listar, 2-Inserir, 3-Atualizar, 4-Excluir, 5-Finalizar")
        return (int(input("Digite uma opção: ")))

    @staticmethod
    def Cliente_Listar(): #Listar clientes cadastrados
        clientes = ClienteDAO.Listar()

        if not clientes:
            print("Nenhum cliente cadastrado")
            return

        for cliente in clientes:
            print(cliente)

    @staticmethod
    def Cliente_Inserir(): #Inserir na lista de clientes
        id=int(input("ID: "))
        nome=input("Nome: ")
        email=input("Email: ")
        fone=input("Telefone: ")

        cliente=Cliente(id,nome,email,fone)
        ClienteDAO.Inserir(cliente)
        ClienteDAO.Salvar()

    @staticmethod
    def Cliente_Atualizar(): #atualizar os dados de um cliente
        id=int(input("ID: "))
        cliente=ClienteDAO.Listar_Id(id)

        if cliente is None:
            print("Não encontrado")
            return

        nome=input("Nome: ")
        email=input("Email: ")
        fone=input("Telefone: ")

        ClienteDAO.Atualizar(id,nome,email,fone)
        ClienteDAO.Salvar()

    @staticmethod
    def Cliente_Excluir(): #exluir cliente cadastrado
        id=int(input("ID: "))

        if ClienteDAO.Excluir(id):
            ClienteDAO.Salvar()
            print("Excluido")
        else:
            print("Não encontrado")

UI.main()
