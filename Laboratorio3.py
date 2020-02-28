## Punto 1
def multpl(arr):
    multp = 1;
    for i in range(len(arr)):
        multp *= arr[i]
    return multpl


def punto1():
    arr = list(map(int, input("Ingrese los números separados por espacio").split(" ")))
    print(multpl(arr))


## Punto 2
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def punto2():
    n = int(input("Ingrese el número n"))
    print(fact(n))


## Punto 3
import math as m;


def esPrimo(n):
    raiz = m.sqrt(n)
    j = 2;
    while j < raiz:  # Para verificar que un número sea primo basta conv erificar que no hayan factores hasta la raíz del número que se quiere probar
        if n % j == 0:  # En esta línea se calcula el residuo de la división de i con j. Donde i es el i-esimo número de la lista y j es un número menor a la raíz de i
            return False
    return True


def punto3():
    n = int(input("Ingrese el número n"))
    print(esPrimo(n))


## Punto 4
def esPalindrome(cad):
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        (" ", ""),
    )
    for a, b in reemplazos:
        cad = cad.replace(a, b).replace(a.upper(), b.upper())
    cad = cad.upper()
    return cad == cad[::-1]


def punto4():
    cad = int(input("Ingrese la cadena de caracteres"))
    print(esPalindrome(cad))


## Punto 5
import math as m


def pertFib(n):
    pro1 = 5 * n * n + 4
    par1 = int(m.sqrt(pro1))
    pro2 = 5 * n * n - 4
    par2 = int(m.sqrt(pro2))
    return par1 * par1 == pro1 or par2 * par2 == pro2


def punto5():
    n = int(input("Ingrese el número n"))
    print(pertFib(n))


## Punto 6
def calcMedia(arr):
    suma = 0
    n = len(arr)
    for i in range(n):
        suma += arr[i]
    return suma / n


def mediasFilas(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]]*n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        resp[i] = calcMedia(aux[i])
    return resp

mediasFilas(False)
## Punto 7
def maxArr(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


def maxsFilas(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]] * n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        resp[i] = maxArr(aux[i])
    return resp

## Punto 8
import math as m


def minArr(arr):
    min = m.inf
    for i in arr:
        if i < min:
            min = i
    return min


def minsFilas(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]] * n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        resp[i] = minArr(aux[i])
    return resp


## Punto 9
def sumaMatrices():
    n = int(input("Ingrese el tamaño n de columnas de las matrices"))
    mat1 = [[0] * n] * n
    mat2 = [[0] * n] * n
    suma = [[0] * n] * n
    print("Primera matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat1[i] = row
    print("Segunda matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat2[i] = row
    for i in range(n):
        for j in range(n):
            suma[i][j] = mat1[i][j] + mat2[i][j]  # Se sabe que sumar 2 matrices es igual a sumar cada entrada en una posición con la entrada de la otra matriz en la misma posición
    return suma
## Punto 10
def multpElemMatrices():
    n = int(input("Ingrese el tamaño n de columnas de las matrices"))
    mat1 = [[0] * n] * n
    mat2 = [[0] * n] * n
    mult = [[0] * n] * n
    print("Primera matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat1[i] = row
    print("Segunda matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat2[i] = row
    for i in range(n):
        for j in range(n):
            mult[i][j] = mat1[i][j] * mat2[i][j]  # Se sabe que sumar 2 matrices es igual a sumar cada entrada en una posición con la entrada de la otra matriz en la misma posición
    return mult
print(multpElemMatrices())
## Punto 11
import numpy as np
def punto11_6(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]] * n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        resp[i] = np.mean(aux[i])
    return resp

def punto11_7(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]] * n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row
    if filas:
        print(np.amax(mat, 1))
        return np.amax(mat, 1)
    print(np.amax(mat, 0))
    return np.amax(mat, 0)

def punto11_8(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]] * n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row
    if filas:
        print(np.amin(mat, 1))
        return np.amin(mat, 1)
    print(np.amin(mat, 0))
    return np.amin(mat, 0)

def punto11_9():
    n = int(input("Ingrese el tamaño n de columnas de las matrices"))
    mat1 = [[0] * n] * n
    mat2 = [[0] * n] * n
    mult = [[0] * n] * n
    print("Primera matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat1[i] = row
    print("Segunda matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat2[i] = row
    print(np.add(mat1, mat2))
    return np.add(mat1, mat2)

def punto11_10():
    n = int(input("Ingrese el tamaño n de columnas de las matrices"))
    mat1 = [[0] * n] * n
    mat2 = [[0] * n] * n
    mult = [[0] * n] * n
    print("Primera matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat1[i] = row
    print("Segunda matriz: ")
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat2[i] = row
    print(np.multiply(mat1, mat2))
    return np.multiply(mat1, mat2)
## Punto 12
import numpy as np
import matplotlib.pyplot as plt

def punto_12():
    t = np.arange(0, 10, 0.1)
    frecuencias = np.arange(0 ,10, 1)

    for i in range(len(frecuencias)):
        y = np.sin(2*np.pi*t)
        plt.subplot(10, 1, i+1)




