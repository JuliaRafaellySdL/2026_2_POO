print("Digite 4 valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = a
if (b > m): m = b
if (c > m): m = c
if (d > m): m = d
print("maior = ", m)

n = a
if (b < n): n = b
if (c < n): n = c
if (d < n): n = d
print("menor = ", n)

print(a + b + c + d - m - n)