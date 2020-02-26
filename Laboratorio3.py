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
    print(suma/n)
    return suma / n


def mediasFilas(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]*n]
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in range(n)]
    print(mat, resp)
    print(aux[0])
    for i in range(n-1):
        resp[i] = calcMedia(aux[i])
    return resp


mediasFilas(True)
## Punto 7
def maxArr(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


def maxsFilas(arr):
    resp = []
    for i in range(len(arr)):
        resp[i] = maxArr(arr[i])
    return resp


## Punto 8
import math as m


def minArr(arr):
    min = m.inf
    for i in arr:
        if i < min:
            min = i
    return min


def minsFilas(arr):
    resp = []
    for i in range(len(arr)):
        resp[i] = minArr(arr[i])
    return resp


## Punto 9
def sumaMatrices(mat1, mat2):
    resp = [[]]
    for i in len(mat1):
        for j in len(mat1[0]):
            resp[i][j] = mat1[i][j] + mat2[i][j]
    return resp;
## Punto 10
