## Punto 1
def multpl(arr):
    multp = 1;
    for i in range(len(arr)):
        multp *= arr[i] #Esta función multiplica todos los elementos de un arreglo
    return multpl


def punto1():
    arr = list(map(int, input("Ingrese los números separados por espacio").split(" ")))
    print(multpl(arr))


## Punto 2
def fact(n):
    if n == 0 or n == 1: #por defincición factorial(0 V 1) =1
        return 1
    else:
        return n * fact(n - 1) #Factorial de n está definido por la multiplicación de todos los números anteriores y n


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
        cad = cad.replace(a, b).replace(a.upper(), b.upper())  #Si se encuentra una letra con tilde o un espacio, se reemplaza por su equivalente sin tilde o sin espacio
    cad = cad.upper() #se convierte la cadena a mayúsculas para normalizar
    return cad == cad[::-1] #Si la cadena original es igual a su reverso, es un palíndrome


def punto4():
    cad = int(input("Ingrese la cadena de caracteres"))
    print(esPalindrome(cad))


## Punto 5
import math as m


def pertFib(n):
    pro1 = 5 * n * n + 4
    par1 = int(m.sqrt(pro1)) #Si un número n cumple que (5*n^2 + 4) o (5*n^2 - 4) es un cuadrado perfecto, se sabe que el número pertenece a la secuancia de fibonacci
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
    for i in range(n): #Esta función calcula la media de un arreglo, sumando todos sus elementos y dividiendolos entre n = longitud del arreglo
        suma += arr[i]
    return suma / n


def punto_6(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]]*n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row #Obtenemos n filas con n elementos que vienen como entrada del usuario
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in range(n)] #Si se quiere calcular la media de cada columna, se calcula la traspuesta de la matriz
    for i in range(n):
        resp[i] = calcMedia(aux[i]) #En cada posisicón de la respuesta, se guarda la media de la fila o columna i
    return resp

## Punto 7
def maxArr(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


def punto_7(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]] * n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row  # Obtenemos n filas con n elementos que vienen como entrada del usuario
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in
               range(n)]  # Si se quiere calcular la media de cada columna, se calcula la traspuesta de la matriz
    for i in range(n):
        resp[i] = maxArr(aux[i])  # En cada posisicón de la respuesta, se guarda la media de la fila o columna i
    return resp

## Punto 8
import math as m


def minArr(arr):
    min = m.inf
    for i in arr:
        if i < min:
            min = i
    return min


def punto_8(filas):
    n = int(input("Ingrese el número n (Tamaño de filas y columnas de la matriz)"))
    mat = [[None] * n] * n  # Creamos una matriz NxN
    resp = [[None]] * n
    aux = mat
    for i in range(n):
        row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
        mat[i] = row  # Obtenemos n filas con n elementos que vienen como entrada del usuario
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in
               range(n)]  # Si se quiere calcular la media de cada columna, se calcula la traspuesta de la matriz
    for i in range(n):
        resp[i] =minArr(aux[i])  # En cada posisicón de la respuesta, se guarda la media de la fila o columna i
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
sumaMatrices()
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
            mult[i][j] = mat1[i][j] * mat2[i][j]  # Se sabe que multiplicar 2 matrices elemento por elemento es igual a multiplicar cada entrada en una posición con la entrada de la otra matriz en la misma posición
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
        mat[i] = row  # Obtenemos n filas con n elementos que vienen como entrada del usuario
    if not filas:
        aux = [[mat[j][i] for j in range(n)] for i in
               range(n)]  # Si se quiere calcular la media de cada columna, se calcula la traspuesta de la matriz
    for i in range(n):
        resp[i] = calcMedia(aux[i])  #La función mean() de numpy calcula la media de un arreglo que entra por parámetro
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
        return np.amax(mat, 1) #La función amax() recibe los arreglos a los cuales se les va a calcular los máximos , si el segundo parámetro es 1 se calcula los máximos de las filas
                            #Si es 0, se calculan los máximos de las columnas
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
        return np.amin(mat, 1) #La función amin() recibe los arreglos a los cuales se les va a calcular los minimos , si el segundo parámetro es 1 se calcula los minimos de las filas
                            #Si es 0, se calculan los minimos de las columnas
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
    return np.add(mat1, mat2) #La función add() de numpy, calcula la suma de 2 o más matrices y más tipos de datos

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
    print(np.multiply(mat1, mat2)) #La función multiply() de numpy, calcula la multiplicación elemento a elemento de 2 o más matrices y más tipos de datos
    return np.multiply(mat1, mat2)
## Punto 12
import numpy as np
import matplotlib.pyplot as plt

def punto_12():
    x = np.arange(0, 10, 0.005)
    frecuencias = np.arange(0 ,10, 1) # Primero obtenemos las frecuencias de 1 a 10
    for i in range(len(frecuencias)):
        y = np.sin(2*np.pi*x*(i+1)) # Seno se puede definir con una frecuencia y un tiempo * 2 * pi
        plt.subplot(10, 1, i+1) #Creamos 10 subplots para ver las gráficas
        plt.plot(x, y)
        plt.title("Seno con {} frecuencia".format(i+1))
        plt.xlabel("Tiempo")
        plt.ylabel("Seno(t)")
    plt.show()
## Punto 13
import numpy as np
import matplotlib.pyplot as plt
def punto_13():
    v = np.random.uniform(0, 5, 10000)  #Creamos 10000 números con una distribución uniforme de 0 a 5
    for i in range(10, 51, 10):
        if i == 40:
            continue
        plt.subplot(5, 2, i // 10)
        plt.hist(v, bins=i, density=1) # Creamos 4 histogramas
        plt.title("Histograma con {} particiones".format(i))
    plt.show()
punto_13()
## Punto_14
def punto_14():
    v = np.random.normal(0, 1, 10000) #Se crea una distribución normal estándar con 10000 valores
    for i in range(10, 51, 10):
        if i == 40:
            continue
        plt.subplot(5, 2, i // 10)
        plt.hist(v, bins=i, density=1) # Creamos 4 histogramas
        plt.title("Histograma con {} particiones".format(i))
    plt.show()




