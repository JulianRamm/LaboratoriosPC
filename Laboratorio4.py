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
        return ((x ** i) / f) + exponencial(x, n, i + 1, f)


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
import math as m


def fact(n):
    if n == 0 or n == 1:  # por defincición factorial(0 V 1) =1
        return 1
    else:
        return n * fact(n - 1)


# def exponencial(x, inicio, fin, f, arr):
#     if inicio != 0:
#         f *= inicio
#         a = (inicio + 9) - fin
#         if a < 10:
#             arr[a] = f
#     if inicio == fin:
#         return (x ** fin) / f
#     else:
#         return ((x ** inicio) / f) + exponencial(x, inicio + 1, fin, f, arr)


def exponencial(x, n, i=0, f=1):
    if i != 0:
        f *= i
    if i == n:
        return (x ** n) / f
    else:
        return ((x ** i) / f) + exponencial(x, n, i + 1, f)


# def graficarEX():
#     x = int(input("Ingrese el x a aplicar a la función exponencial"))
#     exponentes = np.array([], dtype=float)
#     valores = np.arange(10, 1001, 10)
#     arr = [0]*10
#     exponentes = np.append(exponentes, exponencial(x, 10, 20, fact(10), arr))
#     for i in range(1, len(valores)):
#         print(arr[0])
#         print(exponentes[i-2] + exponencial(x, valores[i]+1, valores[i]+10, arr[9], arr))
#         exponentes = np.append(exponentes, exponentes[i-2] + exponencial(x, valores[i]+1, valores[i]+10, fact(valores), arr))
#     plt.plot(valores, exponentes)
#     plt.title("Valor de e^{} con n de diferentes valores".format(x))
#     plt.xlabel("N")
#     plt.ylabel("e^{} con N".format(x))
#     plt.show()

def punto6():
    x = int(input("Ingrese el x a aplicar a la función exponencial"))
    exponentes = np.array([], dtype=float)
    valores = np.arange(10, 1001, 10)
    for i in valores:
        exponentes = np.append(exponentes, exponencial(x, i))
    plt.subplot(3, 1, 1)
    plt.plot(valores, exponentes)
    plt.title("Valor de e^{} con n de diferentes valores".format(x))
    plt.xlabel("N")
    plt.ylabel("e^{} con N".format(x))
    plt.show()

    absolutos = []
    relativos = []
    e_x = m.exp(x)
    for i in range(len(valores)):
        absolutos = np.append(absolutos, abs(exponentes[i] - e_x))
        relativos = np.append(relativos, abs(exponentes[i] - e_x) // exponentes[i])
    plt.subplot(3, 1, 2)
    plt.plot(valores, absolutos)
    plt.title("Error absoluto".format(x))
    plt.xlabel("N")
    plt.ylabel("Error absoluto con N".format(x))
    plt.show()

    plt.subplot(3, 1, 3)
    plt.plot(valores, relativos)
    plt.title("Error relativo".format(x))
    plt.xlabel("N")
    plt.ylabel("Error relativo con N".format(x))
    plt.show()


punto6()
## Punto 7
import numpy as np
import matplotlib.pyplot as plt
import math as m


def sen(x, n, f=1, i=1):
    if x == 0:
        return 0
    if i != 0:
        f *=
    if i == n:
        return (((-1) ** n) * (x ** (2 * n + 1))) / f
    else:
        return ((((-1) ** i) * (x ** (2 * i + 1))) / f) + sen(x, n, f, i + 1)


print(sen(1, 4))


def sen(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return x
    else:
        return (((-1) ** n) * (x ** (2 * n + 1)) / fact(2 * n + 1)) + sen(x, n - 1)


def punto7():
    x = int(input("Ingrese el x a aplicar a la función seno"))
    senos = np.array([], dtype=float)
    valores = np.arange(10, 1001, 10)
    for i in valores:
        senos = np.append(senos, sen(x, i))
    plt.subplot(3, 1, 1)
    plt.plot(valores, senos)
    plt.title("Valor de sen({}) con n de diferentes valores".format(x))
    plt.xlabel("N")
    plt.ylabel("sen({}) con N".format(x))
    plt.show()

    absolutos = []
    relativos = []
    sen_x = m.sin(x)
    for i in range(len(valores)):
        absolutos = np.append(absolutos, abs(senos[i] - sen_x))
        relativos = np.append(relativos, abs(senos[i] - sen_x) // senos[i])
    plt.subplot(3, 1, 2)
    plt.plot(valores, absolutos)
    plt.title("Error absoluto".format(x))
    plt.xlabel("N")
    plt.ylabel("Error absoluto con N".format(x))
    plt.show()

    plt.subplot(3, 1, 3)
    plt.plot(valores, relativos)
    plt.title("Error relativo".format(x))
    plt.xlabel("N")
    plt.ylabel("Error relativo con N".format(x))
    plt.show()


## Punto 8
import numpy as np
import matplotlib.pyplot as plt
import math as m


def cos(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (((-1) ** n) * (x ** (2 * n)) / fact(2 * n)) + cos(x, n - 1)


def punto8():
    x = int(input("Ingrese el x a aplicar a la función coseno"))
    coss = np.array([], dtype=float)
    valores = np.arange(10, 1001, 10)
    for i in valores:
        coss = np.append(coss, sen(x, i))
    plt.subplot(3, 1, 1)
    plt.plot(valores, coss)
    plt.title("Valor de cos({}) con n de diferentes valores".format(x))
    plt.xlabel("N")
    plt.ylabel("cos({}) con N".format(x))
    plt.show()

    absolutos = []
    relativos = []
    cos_x = m.cos(x)
    for i in range(len(valores)):
        absolutos = np.append(absolutos, abs(coss[i] - cos_x))
        relativos = np.append(relativos, abs(coss[i] - cos_x) // coss[i])
    plt.subplot(3, 1, 2)
    plt.plot(valores, absolutos)
    plt.title("Error absoluto".format(x))
    plt.xlabel("N")
    plt.ylabel("Error absoluto con N".format(x))
    plt.show()

    plt.subplot(3, 1, 3)
    plt.plot(valores, relativos)
    plt.title("Error relativo".format(x))
    plt.xlabel("N")
    plt.ylabel("Error relativo con N".format(x))
    plt.show()


punto8()
## Punto 9
import numpy as np
import struct as st


def punto9():
    var1 = np.random.randint(-10, 10, 1000)
    file = open("FileBinInt16.bin", "wb")
    var2 = st.pack("h" * int(len(var1)), *var1)
    file.write(var2)
    file.close()


punto9()
## Punto 10
import struct as st


def punto10():
    file = open("FileBinInt16.bin", "rb")
    var2 = file.read()
    var3 = st.unpack("h" * int(len(var2) / 2), var2)
    plt.hist(var3, bins=30, density=1)
    plt.show()
    file.close()


punto10()
## Punto 11
import numpy as np
import struct as st


def punto11():
    var1 = np.random.randint(-1, 1, 1000)
    file = open("FileBinDouble.bin", "wb")
    var2 = st.pack("d" * int(len(var1)), *var1)
    file.write(var2)


punto11()

#### Punto 12
import struct as st


def punto12():
    file = open("FileBinDouble.bin", "rb")
    var2 = file.read()
    var3 = st.unpack("d" * int(len(var2) / 8), var2)
    plt.hist(var3, bins=30, density=1)
    plt.show()
    file.close()


punto12()

## Punto 13
import struct as st
import numpy as np


def punto13():
    file = open("File-214.bin", "rb")
    var2 = file.read()
    var3 = st.unpack("I" * int(len(var2) / 4), var2)
    return np.mean(var3)
    file.close()


punto13()

## Punto 14
import struct as st
import numpy as np


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


def punto14():
    file = open("File-214.bin", "rb")
    var2 = file.read()
    var3 = st.unpack("I" * int(len(var2) / 4), var2)
    cont = 0
    for i in var3:
        if pertFib(i):
            cont += 1
    return cont


punto14()

## Punto 15
import struct as st
import numpy as np


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


def punto15():
    file = open("File-214.bin", "rb")
    var2 = file.read()
    var3 = st.unpack("I" * int(len(var2) / 4), var2)
    cont = 0
    for i in var3:
        if pertSerieC(i):
            cont += 1
    return cont


punto15()

##

