import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2.0) - 7


print("Con 10**-5")
x0 = 1.0
x1 = 2.0

Tolx = 10 ** -5
Tolf = Tolx

x2prev = x1

iter = 0
while 1:
    iter += 1
    x2 = x1 - (f1(x1) * (x1 - x0) / (f1(x1) - f1(x0)))
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break
    if f1(x2) * f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2
    x2prev = x2

print("Falsa posición - la raiz es: ", x2)
print("Falsa posición - Numero de iteraciones: ", iter)

print("Con 10**-10")

x0 = 1.0
x1 = 2.0

Tolx = 10 ** -10
Tolf = Tolx

x2prev = x1

iter = 0
while 1:
    iter += 1
    x2 = x1 - ((f1(x1) * (x1 - x0)) / (f1(x1) - f1(x0)))
    if np.abs(x2 * x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break
    if f1(x2) * f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2
    x2prev = x2

print("Falsa posición - la raiz es: ", x2)
print("Falsa posición - Numero de iteraciones: ", iter)

##
import numpy as np


def f2(x):
    return -(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5


print("Con 10**-5")
x0 = 1.0
x1 = 2.0

Tolx = 10 ** -5
Tolf = Tolx

x2prev = x1

iter = 0
while 1:
    iter += 1
    x2 = x1 - (f2(x1) * (x1 - x0) / (f2(x1) - f2(x0)))
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f2(x2)) <= Tolf:
        break
    if f2(x2) * f2(x0) < 0:
        x1 = x2
    else:
        x0 = x2
    x2prev = x2

print("Falsa posición - la raiz es: ", x2)
print("Falsa posición - Numero de iteraciones: ", iter)

print("Con 10**-10")

x0 = 1.0
x1 = 2.0

Tolx = 10 ** -10
Tolf = Tolx

x2prev = x1

iter = 0
while 1:
    iter += 1
    x2 = x1 - ((f2(x1) * (x1 - x0)) / (f2(x1) - f2(x0)))
    if np.abs(x2 * x2prev) <= Tolx:
        break
    if np.abs(f2(x2)) <= Tolf:
        break
    if f2(x2) * f2(x0) < 0:
        x1 = x2
    else:
        x0 = x2
    x2prev = x2

print("Falsa posición - la raiz es: ", x2)
print("Falsa posición - Numero de iteraciones: ", iter)
