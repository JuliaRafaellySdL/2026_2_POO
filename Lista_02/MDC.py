x=int(input("Informe um valor inteiro:"))
y=int(input("Informe um valor inteiro:"))

m=x
while x%m != 0 or y%m !=0:
    m=m+1

d=x
while x%d !=0 or y%d !=0:
    d=d-1

print("MMC =", m)
print("MDC =", d)
