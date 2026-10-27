import json
from cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.__objetos=[]

    def inserir(self, obj):
        self.__abrir()
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def __abrir(self):
        lista=[]
        arquivo=open("clientes.json", mode="r")
        clientes_json=json.load(arquivo)
        for obj in clientes_json:
            self.__objetos.append(Cliente(obj["id"],obj["nome"]))
        arquivo.close()

    def __salvar(self):
        arquivo=open("clientes.json", mode="w")
        json.dump(self.__objetos)