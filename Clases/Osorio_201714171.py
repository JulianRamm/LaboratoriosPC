import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2.0) - 7


x0 = 2.0
x1 = 1.9
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
    x0 = x1
    x1 = x2
    x2prev = x2

print("Secante - la raiz es: ", x2)
print("Secante - Numero de iteraciones: ", iter)

print("Con 10^-15")

x0 = 2.0
x1 = 1.9
Tolx = 10 ** -15
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
    x0 = x1
    x1 = x2
    x2prev = x2

print("Secante - la raiz es: ", x2)
print("Secante - Numero de iteraciones: ", iter)

##
import numpy as np


def f2(x):
    return -(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5


print("Con 10^-5")
x0 = 2.0
x1 = 1.9
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
    x0 = x1
    x1 = x2
    x2prev = x2

print("Secante - la raiz es: ", x2)
print("Secante - Numero de iteraciones: ", iter)

print("Con 10^-15")

x0 = 2.0
x1 = 1.9
Tolx = 10 ** -15
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
    x0 = x1
    x1 = x2
    x2prev = x2

print("Secante - la raiz es: ", x2)
print("Secante - Numero de iteraciones: ", iter)

##
import scipy.optimize as opt
import matplotlib.pyplot as plt

def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2.0) - 7


x0 = 2.0
x1 = 1.9
Tolx = 10 ** -5
Tolf = Tolx
x2prev = x1
iter = 0
xr_iter = np.array([])

while 1:
    iter += 1
    x2 = x1 - (f1(x1) * (x1 - x0) / (f1(x1) - f1(x0)))
    xr_iter = np.append(xr_iter, x2)
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break
    x0 = x1
    x1 = x2
    x2prev = x2

print("Secante - la raiz es: ", x2)
print("Secante - Numero de iteraciones: ", iter)

xroot_true = opt.fsolve(f1, x1)
eps_array = np.abs(xr_iter - xroot_true)
r_array = (np.log10(eps_array[1:np.size(eps_array) - 1] / eps_array[2:np.size(eps_array)]) /
           np.log10(eps_array[0:np.size(eps_array) - 2] / eps_array[1:np.size(eps_array) - 1]))

iter_array = np.arange(1.0, np.size(r_array)+1)
plt.figure()
plt.plot(iter_array, r_array)
plt.plot(iter_array, r_array, "or")
plt.xlabel("Iteración")
plt.ylabel("Tasa de convergencia est.")
plt.title("Método de la secante")
plt.grid(1)


