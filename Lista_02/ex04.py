"""for i in range(1, 11):
    print(i, end = "   ")
print()
i = 1
while i < 11:
    print(i, end = " ")
    i += 1

"""
def mostrar(x):
    if x == 11: return
    print(x, end = " ")
    mostrar(x + 1)

#mostrar(1)