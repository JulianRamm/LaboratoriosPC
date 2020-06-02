import numpy as np
import matplotlib.pyplot as plt


# Punto 1
def biseccion(f_x, x0, x1, Tolx, Toly):
    print("Bisección - Intervalo [{},{}]".format(x0, x1))
    x2prev = x1
    iter = 0
    xr_iter = np.array([])
    while 1:
        iter += 1
        x2 = (x0 + x1) / 2.0
        xr_iter = np.append(xr_iter, x2)
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2)) <= Toly:
            break
        if f_x(x2) * f_x(x0) < 0:
            x1 = x2
        else:
            x0 = x2
        x2prev = x2
    print("Bisección - la raiz es: ", x2)
    print("Bisección - Numero de iteraciones: ", iter)
    print("Bisección - El valor de la función en la raíz es: ", f_x(x2))
    print("-------------------------------------------------------------------------------------------------------")
    return xr_iter


# Punto 2
def falsaPosicion(f_x, x0, x1, Tolx, Toly):
    print("Falsa posición - Intervalo [{},{}]".format(x0, x1))
    iter = 0
    x2prev = x1
    xr_iter = np.array([])
    while 1:
        iter += 1
        x2 = x1 - (f_x(x1) * (x1 - x0) / (f_x(x1) - f_x(x0)))
        xr_iter = np.append(xr_iter, x2)
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2)) <= Toly:
            break
        if f_x(x2) * f_x(x0) < 0:
            x1 = x2
        else:
            x0 = x2
        x2prev = x2
    print("Falsa posición - la raiz es: ", x2)
    print("Falsa posición - Numero de iteraciones: ", iter)
    print("Falsa posición - El valor de la función en la raíz es: ", f_x(x2))
    print("-------------------------------------------------------------------------------------------------------")
    return xr_iter


# Punto 3
def puntoFijo(f_x, g_x, x1, Tolx, Toly):
    iter = 0
    x2prev = x1
    xr_iter = np.array([])
    while 1:
        iter += 1
        x2 = g_x(x1)
        xr_iter = np.append(xr_iter, x2)
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2)) <= Toly:
            break
        if iter >= 100:
            print("La función no converge")
            break
        x1 = x2
        x2prev = x2
    print("Punto fijo - la raiz es: ", x2)
    print("Punto fijo - Numero de iteraciones: ", iter)
    print("Punto fijo - El valor de la función en la raíz es: ", f_x(x2))
    print("-------------------------------------------------------------------------------------------------------")
    return xr_iter


# Punto 4
import sympy as sp


def newton(f_x, x1, Tolx, Toly):
    print("Newton - punto: ", x1)
    iter = 0
    x2prev = x1
    xr_iter = np.array([])
    x = sp.Symbol("x")
    d_f = sp.diff(f_x, x)
    f_x = sp.lambdify(x, f_x)
    d_f = sp.lambdify(x, d_f)
    while 1:
        iter += 1
        x2 = x1 - (f_x(x1) / d_f(x1))
        xr_iter = np.append(xr_iter, x2)
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2)) <= Toly:
            break
        x1 = x2
        x2prev = x2
    print("Newton - la raiz es: ", x2)
    print("Newton - Numero de iteraciones: ", iter)
    print("Newton - El valor de la función en la raíz es: ", f_x(x2))
    print("-------------------------------------------------------------------------------------------------------")
    return xr_iter


# Punto 5
def secante(f_x, x0, x1, Tolx, Toly):
    print("Secante - los puntos son {},{}: ".format(x0, x1))
    x2prev = x1
    iter = 0
    xr_iter = np.array([])
    while 1:
        iter += 1
        x2 = x1 - (f_x(x1) * (x1 - x0) / (f_x(x1) - f_x(x0)))
        xr_iter = np.append(xr_iter, x2)
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2)) <= Toly:
            break
        x0 = x1
        x1 = x2
        x2prev = x2
    print("Secante - la raiz es: ", x2)
    print("Secante - Numero de iteraciones: ", iter)
    print("Secante - El valor de la función en la raíz es: ", f_x(x2))
    print("-------------------------------------------------------------------------------------------------------")
    return xr_iter


# Punto 6
import scipy.optimize as opt


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2.0) - 7


def calcularConvergencia(xr_iter):
    xroot_true = opt.fsolve(f1, 1.503062455936674)
    eps_array = np.abs(xr_iter - xroot_true)
    r_array = (np.log10(eps_array[1:np.size(eps_array) - 1] / eps_array[2:np.size(eps_array)]) /
               np.log10(eps_array[0:np.size(eps_array) - 2] / eps_array[1:np.size(eps_array) - 1]))
    return r_array


# Punto 7
def f_1(x):
    return (np.e ** (-5.0 * (x ** 2.0))) - x ** 0.75 + np.sin(4.0 * x) - 1


def f_2(x):
    return np.sin(4.0 * x) * x + x ** 5.0 + 6.0 * x - 4.0


def f_3(x):
    return -3.65 * np.log(x / 5.33) + np.sqrt(2) * (np.e ** (-((np.pi / 2) ** 2)) - 4.25) + 10.54 * np.cos(
        x - 2.2) - 6.67 * (np.pi / 2)


Tolx = 10 ** -5

print("Para f_1(x): ")
biseccion(f_1, 0.2, 0.6, Tolx, Tolx)
falsaPosicion(f_1, 0.2, 0.6, Tolx, Tolx)
x = sp.Symbol("x")
f_x = (sp.exp(1) ** (-5.0 * (x ** 2.0))) - x ** 0.75 + sp.sin(4.0 * x) - 1
newton(f_x, 0.6, Tolx, Tolx)
secante(f_1, 0.55, 0.6, Tolx, Tolx)

print("\nPara f_2(x): ")
biseccion(f_2, 0.0, 1.0, Tolx, Tolx)
falsaPosicion(f_2, 0.0, 1.0, Tolx, Tolx)
x = sp.Symbol("x")
f_x = sp.sin(4.0 * x) * x + x ** 5.0 + 6.0 * x - 4.0
newton(f_x, 1.0, Tolx, Tolx)
secante(f_2, 0.95, 1.0, Tolx, Tolx)

print("\nPara f_3(x): ")
biseccion(f_3, 0.01, 0.1, Tolx, Tolx)
falsaPosicion(f_3, 0.01, 0.1, Tolx, Tolx)
x = sp.Symbol("x")
f_x = -3.65 * sp.log(x / 5.33) + sp.sqrt(2) * (sp.exp(1) ** (-((sp.pi / 2) ** 2)) - 4.25) + 10.54 * sp.cos(
    x - 2.2) - 6.67 * (sp.pi / 2)
newton(f_x, 0.01, Tolx, Tolx)
secante(f_3, 0.01, 0.015, Tolx, Tolx)

##Punto 8
import numpy as np
import matplotlib.pyplot as plt


def puntoFijo(f_x, g_x, x1, Tolx, Toly):
    iter = 0
    x2prev = x1
    xr_iter = np.array([])
    while 1:
        iter += 1
        x2 = g_x(x1)
        xr_iter = np.append(xr_iter, x2)
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2)) <= Toly:
            break
        if iter >= 100:
            print("La función no converge")
            break


        x1 = x2
        x2prev = x2
    print("Punto fijo - la raiz es: ", x2)
    print("Punto fijo - Numero de iteraciones: ", iter)
    print("Punto fijo - El valor de la función en la raíz es: ", f_x(x2))
    print("-------------------------------------------------------------------------------------------------------")
    return xr_iter


def imprimirResultados(g_x, xr_iter, modo):
    if modo == 1:
        print("nr_0: ", xr_iter[0], "g(nr_0): ", g_x(xr_iter[0]), "|nr_0 - nr_1|: ", np.abs(xr_iter[0]))
        print("nr_1: ", xr_iter[1], "g(nr_1): ", g_x(xr_iter[1]), "|nr_1 - nr_0|: ", np.abs(xr_iter[1] - xr_iter[0]))
        print("nr_5: ", xr_iter[5], "g(nr_5): ", g_x(xr_iter[5]), "|nr_5 - nr_4|: ", np.abs(xr_iter[5] - xr_iter[4]))
        print("nr_10: ", xr_iter[10], "g(nr_10): ", g_x(xr_iter[10]),
              "|nr_10 - nr_9|: ", np.abs(xr_iter[10] - xr_iter[9]))
        print("nr_13: ", xr_iter[13], "g(nr_13): ", g_x(xr_iter[13]),
              "|nr_13 - nr_12|: ", np.abs(xr_iter[13] - xr_iter[12]))
    else:
        print("nr_0: ", xr_iter[0], "g(nr_0): ", g_x(xr_iter[0]), "|nr_1 - nr_0|: ", np.abs(xr_iter[0]))
        print("nr_1: ", xr_iter[1], "g(nr_1): ", g_x(xr_iter[1]), "|nr_2 - nr_1|: ", np.abs(xr_iter[1] - xr_iter[0]))
        print("nr_5: ", xr_iter[5], "g(nr_5): ", g_x(xr_iter[5]), "|nr_6 - nr_5|: ", np.abs(xr_iter[5] - xr_iter[4]))
        print("nr_10: ", xr_iter[10], "g(nr_10): ", g_x(xr_iter[10]),
              "|nr_11 - nr_10|: ", np.abs(xr_iter[10] - xr_iter[9]))
        print("nr_13: ", xr_iter[13], "g(nr_13): ", g_x(xr_iter[13]),
              "|nr_14 - nr_13|: ", np.abs(xr_iter[13] - xr_iter[12]))
    print("-------------------------------------------------------------------------------------------------------")


def reflectancia(nr):
    return (-1.440 * (1 / nr ** 2.0)) + (0.710 * (1 / nr ** 1.0)) + 0.688 + (0.0636 * nr) - 0.6


def g1(nr):
    return ((1 / 1.440) * (0.710 * nr ** -1 + 0.0636 * nr + 0.088)) ** (-1 / 2)


def g2(nr):
    return (1 / 0.0636) * (1.440 * nr ** -2 - 0.710 * nr ** -1 - 0.088)


def g3(nr):
    return 1.440 * nr ** -2 - 0.710 * nr ** -1 - 0.0636 * nr - 0.088 + nr


nr = np.arange(0, 30, 0.2)
plt.figure()
plt.plot(nr, reflectancia(nr))
plt.grid(1)
plt.xlabel("n_r")
plt.ylabel("reflectancia(n_r)")
plt.show()

print("respuesta: bb. [1, 1.5]")

xr_iter1 = puntoFijo(reflectancia, g1, 2, 10 ^ -5, 10 ^ -5)
xr_iter2 = puntoFijo(reflectancia, g2, 2, 10 ^ -5, 10 ^ -5)
xr_iter3 = puntoFijo(reflectancia, g3, 2, 10 ^ -5, 10 ^ -5)

imprimirResultados(g1, xr_iter1, 1)
imprimirResultados(g2, xr_iter2, 1)
imprimirResultados(g3, xr_iter3, 0)

##
