#mesmo objeto duas referências
x={"RN":"Natal","PB":"João Pessoa","PE":"Recife"}
y=x
y["AM"] = "Manaus"

print(x)

#dois objetos duas referências
x={"RN":"Natal","PB":"João Pessoa","PE":"Recife"}
y=x.copy()
y["AM"] = "Manaus"

print(x)
print(y)


x=[1,2,3]
y=x
y.append(4)
print(x)

x=[1,2,3]
y=x.copy() #x[:]
y.append(4)
print(x)