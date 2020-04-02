##
import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2.0) - 7


def g1(x):
    return ((1.0 / 4.0) * (np.sqrt(3.0 * x) ** (2.0 / 5.0) - (x ** 3.0) * np.cos(3.0 * x) + 7)) ** 0.5

x1 = 2.0
Tolx = 10**-5
Tolf = Tolx
x2prev = x1
iter = 0

while 1:
    iter +=1
    x2 = g1(x1)
    if np.abs(x2 - x2prev)<=Tolx:
        break
    if np.abs(f1(x2)) <=Tolf:
        break
    x1 = x2
    x2prev = x2

print("Punto fijo - la raiz es: ", x2)
print("Punto fijo - Numero de iteraciones: ", iter)