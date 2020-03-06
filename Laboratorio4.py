## Punto 1
def pertFib(n, a=1, b=1):
    if n == 1 or n == 0:
        return True
    next = a + b
    if next > n:
        return False
    elif next == n:
        return True
    else:
        return pertFib(n, b, next)


print(pertFib(14))
## Punto 2
import math as ma


def pertSerieC(n, a=2):
    if n == 1:
        return True
    p = a * a
    if n < p:
        return False
    elif p == n:
        return True
    else:
        return pertSerieC(n, a + 1)


print(pertSerieC(30))


## Punto 3
def fact(n):
    if n == 0 or n == 1:  # por defincición factorial(0 V 1) =1
        return 1
    else:
        return n * fact(n - 1)


def exponencial(x, n, i=0, f=1):

    if i != 0:
        f *= i
    if i == n:
        return (x ** n) / f
    else:
        return  ((x ** i) / f) + exponencial(x, n, i+1, f)

print(exponencial(1, 1000))


## Punto 4
def fact(n):
    if n == 0 or n == 1:  # por defincición factorial(0 V 1) =1
        return 1
    else:
        return n * fact(n - 1)


def sen(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return x
    else:
        return (((-1) ** n) * (x ** (2 * n + 1)) / fact(2 * n + 1)) + sen(x, n - 1)


print(sen(1, 4))


## Punto 5
def fact(n):
    if n == 0 or n == 1:  # por defincición factorial(0 V 1) =1
        return 1
    else:
        return n * fact(n - 1)


def cos(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (((-1) ** n) * (x ** (2 * n)) / fact(2 * n)) + cos(x, n - 1)


print(cos(1, 4))

## Punto 6
import numpy as np
import matplotlib.pyplot as plt

def fact(n):
    if n == 0 or n == 1:  # por defincición factorial(0 V 1) =1
        return 1
    else:
        return n * fact(n - 1)

def exponencial(x, inicio, fin, f,arr):
    print(f)
    if inicio != 0:
        f *= inicio
        arr.append(f)
    if inicio == fin:
        return (x ** fin) / f
    else:
        return [((x ** inicio) / f) + exponencial(x, inicio + 1, fin, f, arr)[0], arr]
arr = []
print(exponencial(1, 0, 10, 1,arr ))


def graficarEX():
    exponentes = np.array([], dtype=float)
    valores = np.arange(10, 1000, 10)
    print(valores)
    for i in valores:
        print(exponencial(3, i))
        exponentes = np.append(exponentes, exponencial(3, i))
    plt.plot(valores, exponentes)
    plt.title("Valor de e^3 con n de diferentes valores")
    plt.xlabel("N")
    plt.ylabel("e^3 con N")
    plt.show()


## Punto 7
