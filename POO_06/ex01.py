x={"RN":"Natal","PB":"João Pessoa","PE":"Recife"}
print(x, type(x))
print(x["RN"])
x["PB"]="JP"
x["AM"]="Manaus"

print(x)
#print(x("PA"))

for item in x.items():
    print(item,item[0],item[1],item[2])