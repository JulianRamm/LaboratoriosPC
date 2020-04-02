# Estas funciones no son lineales debido a que el exponente de la x es mayor a 1. En la primer función,
# El exponente es mayor a 1. En el segundo caso, la función es curva debido a que el exponente es igual a la
# inversa de un exponente mayor a 1

##
import numpy as np
import matplotlib.pyplot as plt


def f2(x):
    return -(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5

print("Con 0.001")
x = np.arange(0.0, 2.0, 0.001)
plt.figure()
plt.plot(x, f2(x))
plt.grid(1)
plt.xlabel("x")
plt.ylabel("f2(x)")
plt.show()

indmin = np.argmin(np.abs(f2(x)))
print("Una posible raíz se encuentra alrededor de:", x[indmin])


print("Con 0.00001")
x = np.arange(0.0, 2.0, 0.00001)
plt.figure()
plt.plot(x, f2(x))
plt.grid(1)
plt.xlabel("x")
plt.ylabel("f2(x)")
plt.show()

indmin = np.argmin(np.abs(f2(x)))
print("Una posible raíz se encuentra alrededor de:", x[indmin])

##
import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return -(np.sqrt(3 * x) ** 2.0 / 5.0) + ((x ** 3) * np.cos(3.0 * x)) + 4.0 * (x ** 2) - 7

print("Con 10^-5")
x0 = 1.0
x1 = 2.0
Tolx = 10 ** -5
Tolf = Tolx
x2prev = x1
iter = 0
while 1:
    iter += 1
    x2 = (x0 + x1) / 2.0
    if np.abs(x2 * x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break;
    if f1(x2) * f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2
        x2prev = x2
print("Bisección - la raiz es: ", x2)
print("Bisección - Numero de iteraciones: ", iter)

print("Con 10^-10")
x0 = 1.0
x1 = 2.0
Tolx = 10 ** -10
Tolf = Tolx
x2prev = x1
iter = 0
while 1:
    iter += 1
    x2 = (x0 + x1) / 2.0
    if np.abs(x2 * x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break;
    if f1(x2) * f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2
        x2prev = x2
print("Bisección - la raiz es: ", x2)
print("Bisección - Numero de iteraciones: ", iter)

##
import numpy as np
import matplotlib.pyplot as plt


def f2(x):
    return -(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5

print("Con 10^-5")

x0 = 1.0
x1 = 2.0
Tolx = 10 ** -5
Tolf = Tolx
x2prev = x1
iter = 0
while 1:
    iter += 1
    x2 = (x0 + x1) / 2.0
    if np.abs(x2 * x2prev) <= Tolx:
        break
    if np.abs(f2(x2)) <= Tolf:
        break;
    if f2(x2) * f2(x0) < 0:
        x1 = x2
    else:
        x0 = x2
        x2prev = x2
print("Bisección - la raiz es: ", x2)
print("Bisección - Numero de iteraciones: ", iter)

print("Con 10^-10")

x0 = 1.0
x1 = 2.0
Tolx = 10 ** -10
Tolf = Tolx
x2prev = x1
iter = 0
while 1:
    iter += 1
    x2 = (x0 + x1) / 2.0
    if np.abs(x2 * x2prev) <= Tolx:
        break
    if np.abs(f2(x2)) <= Tolf:
        break;
    if f2(x2) * f2(x0) < 0:
        x1 = x2
    else:
        x0 = x2
        x2prev = x2
print("Bisección - la raiz es: ", x2)
print("Bisección - Numero de iteraciones: ", iter)