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
            f"Telefone: {self.__telefone}"
        )

class ClienteDAO:
    objetos=[]

    def Inserir(): #Inserir objeto na lista
        pass

    def Listar(): #Retornar os objetos na lista
        pass

    def Listar_Id(): #Retornar o objeto com um ID determinado
        pass

    def Atualizar(): #Atualizar dados de um objeto
        pass

    def Excluir(): #Excluir objeto da lista
        pass

    def Abrir(): #Recuperar a lista de objetos de um arquivo JSON
        pass

    def Salvar(): #Salvar a lisa de objetos em um arquivo JSON
        pass

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.Cliente_Listar()
            if op == 2: UI.Cliente_Inserir()
            if op == 3: UI.Atualizar()
            if op == 4: UI.Excluir()

    @staticmethod
    def menu():
        print("1-Listar, 2-Inserir, 3-Atualizar, 4-Excluir")
        return (int(input("Digite uma opção: ")))

    @classmethod
    def Cliente_Listar(): #Listar clientes cadastrados
        pass

    @classmethod
    def Cliente_Inserir(): #Inserir na lista de clientes
        pass

    @classmethod
    def Cliente_Atualizar(): #atualizar os dados de um cliente
        pass

    @classmethod
    def Cliente_Excluir(): #exluir cliente cadastrado
        pass