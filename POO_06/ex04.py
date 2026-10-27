import json

class Cliente:
    def __int__(self, id, nome):
        self.id=id
        self.nome=nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

lista=[]
arquivo= open("clientes.json", mode="r")
clientes_json=json.load(arquivo)        #lista de dicionários
for obj in clientes_json:               #cada objeto é um dicionário
    lista.append(Cliente(obj["id"], obj["nome"]))
arquivo.close()

for c in lista: print(c)

