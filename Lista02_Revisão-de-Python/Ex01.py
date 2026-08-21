numeros=list(map(int, input("Digite quatro valores inteiros:").split()))
pares=[]
impares=[]
for i in numeros:
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)

spares=sum(pares)
simpares=sum(impares)
print("Soma dos pares =", spares)
print("Soma dos ímpares =", simpares)