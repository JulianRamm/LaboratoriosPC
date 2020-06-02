import numpy as np
import matplotlib.pyplot as plt


def f(y, z):
    return y ** 2.0 * np.log(y ** 2.0) + 371.0930 * y ** 2.0 + 12800.0 * ((y ** 2) - 1.0) * z - 2874.3785


z = np.arange(0.001, 0.111, 0.01)
y = np.arange(0.5, 12.0, 0.001)
plt.figure()
for i in z:
    plt.plot(y, f(y, i))
    plt.grid(1)
    plt.title("Graficas de f(y) con diferentes valores de z")
    plt.xlabel("y")
    plt.ylabel("f(y)")
    plt.show()

##
import sympy as sp


def biseccion(z, f_x=f, x0=1.0, x1=12.0, Tolx=10 ** -5, Toly=10 ** -5, ):
    x2prev = x1
    iter = 0
    while 1:
        iter += 1
        x2 = (x0 + x1) / 2.0
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2, z)) <= Toly:
            break
        if f_x(x2, z) * f_x(x0, z) < 0:
            x1 = x2
        else:
            x0 = x2
        x2prev = x2
    print("Bisección - Numero de iteraciones: ", iter)
    print("Bisección - la raiz es: ", x2)
    print("Bisección - El valor rcrit es: ", 0.00055 * x2)
    print("-------------------------------------------------------------------------------------------------------")
    return x2


def newton(z, f_x, x1=12.0, Tolx=10 ** -5, Toly=10 ** -5):
    iter = 0
    x2prev = x1
    x = sp.Symbol("y")
    d_f = sp.diff(f_x, x)
    f_x = sp.lambdify(x, f_x)
    d_f = sp.lambdify(x, d_f)
    while 1:
        iter += 1
        x2 = x1 - (f_x(x1) / d_f(x1))
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2)) <= Toly:
            break
        x1 = x2
        x2prev = x2
    print("Newton - Numero de iteraciones: ", iter)
    print("Newton - la raiz es: ", x2)
    print("Newton - El valor rcrit es: ", 0.00055 * x2)
    print("-------------------------------------------------------------------------------------------------------")
    return x2


def falsaPosicion(z, f_x=f, x0=1.0, x1=3.0, Tolx=10 ** -5, Toly=10 ** -5):
    iter = 0
    x2prev = x1
    while 1:
        iter += 1
        x2 = x1 - (f_x(x1, z) * (x1 - x0) / (f_x(x1, z) - f_x(x0, z)))
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f_x(x2, z)) <= Toly:
            break
        if f_x(x2, z) * f_x(x0, z) < 0:
            x1 = x2
        else:
            x0 = x2
        x2prev = x2
    print("Falsa pos - Numero de iteraciones: ", iter)
    print("Falsa pos - la raiz es: ", x2)
    print("Falsa pos - El valor rcrit es: ", 0.00055 * x2)
    print("-------------------------------------------------------------------------------------------------------")
    return x2


y = sp.Symbol("y")
bi = np.array([])
ne = np.array([])
fa = bi = np.array([])
for i in z:
    f_y = y ** 2.0 * sp.log(y ** 2.0) + 371.0930 * y ** 2.0 + 12800.0 * ((y ** 2) - 1.0) * i - 2874.3785
    print("con z = ", i)
    bi = np.append(bi, biseccion(i))
    ne = np.append(ne, newton(i, f_y))
    fa = np.append(fa,falsaPosicion(i))

##
plt.figure()
plt.plot(z, bi)
plt.grid(1)
plt.title("biseccion")
plt.xlabel("z")
plt.ylabel("y")
plt.show()

plt.figure()
plt.plot(z, 0.00055*bi)
plt.grid(1)
plt.title("biseccion")
plt.xlabel("z")
plt.ylabel("rcrit")
plt.show()

plt.figure()
plt.plot(z, ne)
plt.grid(1)
plt.title("newton")
plt.xlabel("z")
plt.ylabel("y")
plt.show()

plt.figure()
plt.plot(z, 0.00055*ne)
plt.grid(1)
plt.title("newton")
plt.xlabel("z")
plt.ylabel("rcrit")
plt.show()

plt.figure()
plt.plot(z, fa)
plt.grid(1)
plt.title("falsa pos")
plt.xlabel("z")
plt.ylabel("y")
plt.show()

plt.figure()
plt.plot(z, 0.00055*fa)
plt.grid(1)
plt.title("falsa pos")
plt.xlabel("z")
plt.ylabel("rcrit")
plt.show()

##
import struct as st
filex = open("./archivos/Parcial-03-P02-X.bin", "rb")
filey = open("./archivos/Parcial-03-P02-Y.bin", "rb")

varx = filex.read()
vary = filey.read()

x = st.unpack("d" * int(len(varx) / 8), varx)
y = st.unpack("d" * int(len(vary) / 8), vary)
A = [[1, (1 / len(x)) * np.sum(x)], [np.average(x), np.average(np.multiply(x, x))]]
b = [[np.average(y)], [np.average(np.multiply(x, y))]]
print((1 / len(x)) * np.sum(x))
print(np.average(np.multiply(x, x)))
print(np.average(y))
print(np.average(np.multiply(x, y)))
coefs = np.linalg.solve(A, b)
a_0 = coefs[0]
a_1 = coefs[1]
print(a_0, a_1)

##

