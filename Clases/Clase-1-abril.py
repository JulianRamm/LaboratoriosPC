import numpy as np


def f1(x):
    return (-1.440 * (1 / x ** 2.0)) + (0.710 * (1 / x ** 1.0)) + 0.688 + (0.0636 * x) - 0.6


def g1(x):
    return 1.440 * x ** -2 - 0.710 * x ** -1 - 0.0636 * x - 0.088 + x


def g2(x):  ##Segunda opción para g(x) = x
    return (((np.abs(np.sqrt(3.0 * x)) ** 2 / 5) - 4.0 * x ** 2.0) / np.cos(2 * x)) ** 1 / 3


def g3(x):  ##Tercera opción para g(x) = x
    return x * ((np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2.0)) / 7.0


x1 = 2.0
Tolx = 10 ** -5
Tolf = Tolx
x2prev = x1
iter = 0

print("Con g1(x)")
while 1:
    iter += 1
    x2 = g1(x1)
    print(x2)
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break
    if iter >= 100:
        print("La función no converge")
        break
    x1 = x2
    x2prev = x2

# print("Punto fijo - la raiz es: ", x2)
# print("Punto fijo - Numero de iteraciones: ", iter)
#
# print("Con g2(x)")
# x1 = 2.0
# Tolx = 10 ** -5
# Tolf = Tolx
# x2prev = x1
# iter = 0
#
# while 1:
#     iter += 1
#     x2 = g2(x1)
#     if np.abs(x2 - x2prev) <= Tolx:
#         break
#     if np.abs(f1(x2)) <= Tolf:
#         break
#     if iter >= 100:
#         print("La función no converge")
#         break
#     x1 = x2
#     x2prev = x2
#
# print("Punto fijo - la raiz es: ", x2)
# print("Punto fijo - Numero de iteraciones: ", iter)
#
# print("Con g3(x)")
# x1 = 2.0
# Tolx = 10 ** -5
# Tolf = Tolx
# x2prev = x1
# iter = 0
#
# while 1:
#     iter += 1
#     x2 = g3(x1)
#     if np.abs(x2 - x2prev) <= Tolx:
#         break
#     if np.abs(f1(x2)) <= Tolf:
#         break
#     if iter >= 100:
#         print("La función no converge")
#         break
#     x1 = x2
#     x2prev = x2
#
# print("Punto fijo - la raiz es: ", x2)
# print("Punto fijo - Numero de iteraciones: ", iter)


##
import numpy as np
def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2.0) - 7


def df1(x):
    return -((3.0 ** (1.0 / 5.0)) / 5.0) * (x ** (-4.0 / 5.0)) - 3.0 * (x ** 3.0) * np.sin(
        3.0 * x) + 3 * x ** 2 * np.cos(3.0 * x) + 8 * x


x1 = 2.0
Tolx = 10 ** -15
Tolf = Tolx
x2prev = x1
iter = 0

while 1:
    iter += 1
    x2 = x1 - (f1(x1) / df1(x1))
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break
    x1 = x2
    x2prev = x2

print("Newton - la raiz es: ", x2)
print("Newton - Numero de iteraciones: ", iter)


##

def f2(x):
    return -(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5


def g1(x):  ##Primera opción para g(x) = x
    return -(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5 + x


def g2(x):  ##Segunda opción para g(x) = x
    return -(-(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5)/2


x1 = 2.0
Tolx = 10 ** -5
Tolf = Tolx
x2prev = x1
iter = 0

print("Con g1(x)")
while 1:
    iter += 1
    x2 = g1(x1)
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break
    if iter >= 100:
        print("La función no converge")
        break
    x1 = x2
    x2prev = x2

print("Punto fijo - la raiz es: ", x2)
print("Punto fijo - Numero de iteraciones: ", iter)

print("Con g2(x)")
x1 = 2.0
Tolx = 10 ** -5
Tolf = Tolx
x2prev = x1
iter = 0

while 1:
    iter += 1
    x2 = g2(x1)
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f1(x2)) <= Tolf:
        break
    if iter >= 100:
        print("La función no converge")
        break
    x1 = x2
    x2prev = x2

print("Punto fijo - la raiz es: ", x2)
print("Punto fijo - Numero de iteraciones: ", iter)

##
import numpy as np

def f2(x):
    return -(x ** 0.25) + np.sin(3.5 * x) + 4 * (x ** 0.5) + 2 * x - 5


def df2(x):
    return -0.25*x**(-0.75) + 2.0*x**(-0.5) + 3.5*np.cos(3.5*x) + 2


print("Con 10^-5")
x1 = 2.0
Tolx = 10 ** -5
Tolf = Tolx
x2prev = x1
iter = 0

while 1:
    iter += 1
    x2 = x1 - (f2(x1) / df2(x1))
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f2(x2)) <= Tolf:
        break
    x1 = x2
    x2prev = x2

print("Newton - la raiz es: ", x2)
print("Newton - Numero de iteraciones: ", iter)

print("Con 10^-15")
x1 = 2.0
Tolx = 10 ** -15
Tolf = Tolx
x2prev = x1
iter = 0

while 1:
    iter += 1
    x2 = x1 - (f2(x1) / df2(x1))
    if np.abs(x2 - x2prev) <= Tolx:
        break
    if np.abs(f2(x2)) <= Tolf:
        break
    x1 = x2
    x2prev = x2

print("Newton - la raiz es: ", x2)
print("Newton - Numero de iteraciones: ", iter)
##

