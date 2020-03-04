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


def calcTaylor(x, n):
    if x == 0 or n == 0:
        return 1
    else:
        return ((x ** n) / fact(n)) + calcTaylor(x, n-1)


print(calcTaylor(2.78, 6))
## Punto 4


