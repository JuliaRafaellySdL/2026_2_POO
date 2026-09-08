print("Olá")
print()
x = print    # x é o print
x = print()  # x é o retorno do print = None
print(x)
print(type(x))
#x("Tudo bem?")

def quadrado(n):
    return n ** 2

print(quadrado(4))

x = quadrado
print(x(4))

x = lambda n : n ** 2
print(x(4))

x = lambda a, b : a + b
print(x(4, 6))