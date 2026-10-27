import json

class Cliente:
    def __int__(self, id, nome):
        self.id=id
        self.nome=nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

a=Cliente(1,"Douglas Crockford") # criador do json - dicionário com todas as chaves strings
b=Cliente(2,"Jon Bosak")         # criador do xml

print(a)
print(b)

print(a.__dict__)
print(vars(b))

#API = programa

lista=[a,b]
print(lista)
for c in lista:print(c)
 
arquivo=open("clientes.json", mode="w")
json.dump(lista, arquivo, default=vars)
arquivo.close()

