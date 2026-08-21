x=[4,5,6]
y=x                 #x e y são a mesma lista
y=x[:]              #x e y são listas diferentes
y.append(7)
print(x, id(x))
print(y, id(y))

a=5
b=a
b=6

print(a, id(a))
print(b, id(b))

'C'
"C"
