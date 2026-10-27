from cliente import Cliente
from clientedao import ClienteDAO

class UI:
    def main():
        op=0
        while op != 9:
            op=UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()

    def menu():
        print("1-Inserir, 2-Listar")
        return int(input("Informe a opção: "))

    def inserir():
        id=int(input("ID: "))
        nome=input("Nome: ")
        c=Cliente(id,nome)
        ClienteDAO().inserir(c)

    def listar()