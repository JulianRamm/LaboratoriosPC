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
    acal = N + 2**n -1
    while acal >= 1:
        res = str(acal % 2) + res
        acal = compl // 2
    res = "0"*(n-len(res)) + res
    print("El valor de {} en complemento a 2 es: {}".format(N, res))
##

