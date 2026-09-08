x = [4, 5, 6]
#y = x     # x e y são a mesma lista
y = x[:]   # x e y são listas diferentes
y.append(7)
print(x, id(x))
print(y, id(y))

a = 5
b = a
b = 6
print(a, id(a))
print(b, id(b))

# nas linguagens C++, C#, Java
#'C' - char
#"C" - string
# no python
#'C' - string
#"C" - string

s = "Tecnologia"
print(s[0:5])

x = 5
y = x == 5
print(y)
print(type(y))

x = 5
y = 6.0
z = x + y
print(z, type(z))

print(1/4)
print(1//4)

x = 1/4
y = 1.0/4
y = 1/4.0

"""
print(5 * "TADS") 
#print(5 + "5")
"""

print("A" > "B")
print("A" > "a")
print("2" > "10")
print(2 > 10)
#print("2" > 10)

print(1 > False)
print(1 > True)
print(2 > True)