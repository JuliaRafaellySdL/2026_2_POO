def MMC(x, y):
    m = x
    while m % x != 0 or m % y != 0:
        m = m + 1
    return m

def MDC(x, y):
    d = x
    while x % d != 0 or y % d != 0:
        d = d - 1
    return d

def MDC2(x, y):  # Algotimo de Euclides
    if x % y == 0: return y
    return MDC2(y, x % y)

def MMC2(x , y):
    return x * y / MDC2(x, y)

# MMC * MDC = x * y  -> MMC = x * y / MDC

x = int(input("Informe um valor inteiro: "))
y = int(input("Informe um valor inteiro: "))

print("MMC =", MMC(x, y))
print("MDC =", MDC2(x, y))
print("Prod = ", x * y)
print("MMC * MDC = ", MMC(x, y) * MDC(x, y))