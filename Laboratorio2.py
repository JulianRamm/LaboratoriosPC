## Punto 1
n = float(input("ingrese el número  a convertir"))
res = ""
if n / 1 > n // 1 or n < 0:
    print("Error garrafal: el número es racional o menor a 0")
else:
    n = int(n)
    aux = n
    while aux >= 1:
        res = str(aux % 2) + res
        aux = aux // 2
    print("El valor de {} en binario es: {}".format(n, res))
## Punto 2
N = float(input("ingrese el número  a convertir"))
n = int(input("Ingrese el número de bits a utilizar"))
res = ""
if n / 1 > n // 1 or not(-2**(n-1) <= N <= (2**(n-1))-1):
    print("Error garrafal: el número es racional o el número de bits no es suficiente")
else:
    N = int(N)
    compl = N
    if N < 0:
        compl = 2 ** n + N
    print(compl)
    while compl >= 1:
        res = str(compl % 2) + res
        compl = compl // 2
    res = "0"*(n-len(res)) + res
    print("El valor de {} en complemento a 2 es: {}".format(N, res))
## Punto 3
N = float(input("ingrese el número  a convertir"))
n = int(input("Ingrese el número de bits a utilizar"))
res = ""
if n / 1 > n // 1 or not(-2**(n-1) <= N <= (2**(n-1))-1):
    print("Error garrafal: el número es racional o el número de bits no es suficiente")
else:
    acal = int(N) + 2**(n-1)
    while acal >= 1:
        res = str(acal % 2) + res
        acal = acal // 2
    res = "0"*(n-len(res)) + res
    print("El valor de {} en complemento a 2 es: {}".format(int(N), res))
## Punto 4
N = float(input("ingrese el número  a convertir"))
res = ""
ent = int(N)
rac = N - int(N)
entm = ""
potencia = ""
mantissa = ""
if N > 0:
    res += "0"
else:
    res += "1"
while ent >= 1:
    entm = str(ent % 2) + entm
    ent = ent // 2
for i in range(24 - len(entm)):
    rac = rac*2
    mantissa = mantissa + str(int((rac//1) % 2))
    if rac > 1:
        rac = rac - 1
potencian = len(entm) + 126
while potencian >= 1:
    potencia = str(potencian % 2) + potencia
    potencian = potencian // 2
print(res, potencia, entm[1:] + mantissa)
print("El número {} en formato IEE 754 es: {}".format(N, res + potencia + entm[1:] + mantissa))
## Punto 5
N = float(input("ingrese el número  a convertir"))
res = ""
ent = int(N)
rac = N - int(N)
entm = ""
potencia = ""
mantissa = ""
if N > 0:
    res += "0"
else:
    res += "1"
while ent >= 1:
    entm = str(ent % 2) + entm
    ent = ent // 2
for i in range(53 - len(entm)):
    rac = rac*2
    mantissa = mantissa + str(int((rac//1) % 2))
    if rac > 1:
        rac = rac - 1
potencian = len(entm) + 1022
while potencian >= 1:
    potencia = str(potencian % 2) + potencia
    potencian = potencian // 2
print("El número {} en formato IEE 754 es: {}".format(N, res + potencia + entm[1:] + mantissa))
##

