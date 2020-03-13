## Punto 1
import numpy as np


def punto1():
    n = int(input("Ingrese el tamaño n de columnas de las matrices"))
    mat = [[0] * n] * n
    mat = np.array(mat)
    # mat = np.array([[1, 2, 3],
    #                 [4, 5, 6],
    #                 [7, 8, 100]])
    x = [0] * n
    aumentada = [[0] * (n + 1)] * (n) #La matriz aumentada tiene un tamaño de NX(N+1)
    aumentada = np.array(aumentada)
    for i in range(n):
        row = list(map(float, input(
            "Ingrese {} números separados por , para cada fila de la matriz A, de NXN".format(n)).split(' ')))
        mat[i] = row
    b = list(map(float, input("Ingrese {} números separados por espacio, para la matriz 1XN, b".format(n)).split(' ')))
    b = np.array(b)
    for i in range(n):
        aumentada[i] = np.append(mat[i], b[i])
    print("Matriz aumentada: ")
    print(aumentada)
    for i in range(n):
        for j in range(n):
            if i > j: # Solo queremos modificar la parte inferior de la matriz, por eso j debe ser menor a i
                constante = aumentada[i][j] / aumentada[j][j] # Esta constante se repite en todos los calculos de las celdas
                for k in range(j, n + 1):
                    aumentada[i][k] = aumentada[i][k] - aumentada[j][k] * constante #Finalmente, a cada celda se le realiza la operación descrita, para cancelar la primera posición y que
                                                                                    #las posiciones siguientes de la fila sean modificadas también, ya que se trata de una ecuación
    for i in range(n - 1, -1, -1):
        x[i] = (aumentada[i][n] - np.dot(aumentada[i][0:-1], x)) / aumentada[i][i]   # Esta operación se realiza para encontrar las soluciones al sistema. Se repite en todos los calculos, es igual
                                                                                    # a la posición i de la matriz b y el producto punto de x con la aumentada de i a n sobre la posición de la diagonal en i
    print("x: ", x)
    return x


punto1()

## Punto 2
import numpy as np


def punto2():
    # n = int(input("Ingrese el tamaño n de columnas de las matrices"))
    # mat = [[0] * n] * n
    # mat = np.array(mat)
    # x = [0] * n
    # aumentada = [[0] * (n + 1)] * (n)
    # aumentada = np.array(aumentada)
    # for i in range(n):
    #     row = list(map(float, input(
    #         "Ingrese {} números separados por , para cada fila de la matriz A, de NXN".format(n)).split(' ')))
    #     mat[i] = row
    # b = list(map(float, input("Ingrese {} números separados por espacio, para la matriz 1XN, b".format(n)).split(' ')))
    # b = np.array(b)
    # for i in range(n):
    #     aumentada[i] = np.append(mat[i], b[i])
    print("Matriz aumentada: ")
    n = 3
    aumentada = np.array([[1, 2, 3, 3],
                          [4, 5, 6, 4],
                          [7, 8, 100, 600]])
    print(aumentada)
    for i in range(n):
        for j in range(n):
            if i > j:
                constante = aumentada[i][j] / aumentada[j][j]
                for k in range(j, n + 1):
                    aumentada[i][k] = aumentada[i][k] - aumentada[j][k] * constante
    print(aumentada)
    for i in range(n, -1, -1):
        for j in range(n - 1, -1, -1):
            if i < j:
                constante = aumentada[i][j] / aumentada[j][j]
                for k in range(n - 1, j - 1, -1):
                    aumentada[i][k] = aumentada[i][k] - aumentada[j][k] * constante
    print("segunda: ")
    print(aumentada)
    for i in range(n):
        aumentada[i][n] = float(aumentada[i][n] / aumentada[i][i])
        aumentada[i][i] = 1
    print(aumentada)
    x = [aumentada[i][n] for i in range(n)]
    print("x: ", x)


punto2()

## Punto 3
# Tiene una sola solución si todas las ecuaciones son independientes entre sí. Es decir, si al hacer la eliminación de gauss-jordan, el resultado es de la forma:
# [  1  0   0   x_1]
# [  0  1   0   x_2]
# [  0  0   1   x_3]
# Tiene infinitas soluciones si 2 o más de las ecuaciones son dependientes entre sí, por lo tanto, son la misma ecuación Es decir, si al hacer la eliminación de gauss-jordan, el resultado es de la forma:
# [  1  0   0   x_1]
# [  0  1   0   x_1]
# [  0  0   1   x_1]
# Tiene infinitas soluciones si 2 o más de las ecuaciones son dependientes entre sí, por lo tanto, son la misma ecuación Es decir, si al hacer la eliminación de gauss-jordan, el resultado es de la forma:
# [  1  0   0   x_1]
# [  0  0   0   x_2]
# [  0  0   1   x_3]
# Con x_3 != 0

## Punto 4
import numpy as np
import matplotlib.pyplot as plt


# Tenemos el siguiente sistema de ecuaciones:
# { -2a + c = -4, -7a +b + c= -50, 5a -b +c = -26
# El cual se soluciona con la función realizada en el punto 1, utilizando la matriz aumentada:
# [[-2, 0, 1 -4]
# [-7, 1, 1 -50]
# [5, -1, 1 -26]]
def punto1():
    n = 3
    x = [0] * n
    aumentada = [[-2, 0, 1, -4], [-7, 1, 1, -50], [5, -1, 1, -26]]
    print(aumentada)
    for i in range(n):
        for j in range(n):
            if i > j:
                constante = aumentada[i][j] / aumentada[j][j]
                for k in range(j, n + 1):
                    aumentada[i][k] = aumentada[i][k] - aumentada[j][k] * constante
    for i in range(n - 1, -1, -1):
        x[i] = (aumentada[i][n] - np.dot(aumentada[i][0:-1], x)) / aumentada[i][i]
    return x


def punto4():
    x = punto1()
    print(x)
    # Con lo cual nos dará una ecuación de la forma x^2 + y^2 +ax +by +c =0
    # completando cuadrados se convierte en: (x + a/2)^2 + (y + b/2)^2 = -c + (a/2)^2 + (b/2)^2
    # reemplazadno obtenemos: (x - 17)^2 + (y - 108)^2 = 72 + (-34/2)^2 +(-216/2)^2
    # Por lo tanto el centro es igual a (17, 108) y el radio = raiz(12025) = 109.65856
    teta = np.linspace(0, 2 * np.pi, 50)
    r = 12025 ** (1 / 2)
    x = 17 + r * np.cos(teta) # Se suma 17 y 108 ya que el centro del círculo no está en el origen
    y = 108 + r * np.sin(teta)
    plt.plot(x, y)
    plt.show()


punto4()


## Punto 5
import numpy as np
import matplotlib.pyplot as plt


def punto1(arr):
    n = 5
    x = [0] * n
    aumentada = arr
    for i in range(n):
        for j in range(n):
            if i > j:
                constante = aumentada[i][j] / aumentada[j][j]
                for k in range(j, n + 1):
                    aumentada[i][k] = aumentada[i][k] - aumentada[j][k] * constante
    for i in range(n - 1, -1, -1):
        x[i] = (aumentada[i][n] - np.dot(aumentada[i][0:-1], x)) / aumentada[i][i]
    return x
def punto5():
    # Obtenemos la matriz de la forma
    mat = [[(-2.68) ** 4, (-2.68) ** 3, (-2.68) ** 2, (-2.68), 1, 0],
           [(-3.25) ** 4, (-3.25) ** 3, (-3.25) ** 2, (-3.25), 1, 1.15],
           [(-4.45) ** 4, (-4.45) ** 3, (-4.45) ** 2, (-4.45), 1, -1.56],
           [(-6.25) ** 4, (-6.25) ** 3, (-6.25) ** 2, (-6.25), 1, -2.84],
           [(-8.15) ** 4, (-8.15) ** 3, (-8.15) ** 2, (-8.15), 1, 0.23]]
    vals = punto1(mat)
    print(vals)
    x = np.arange(-8.15, -2.68, 0.1)
    f_x = vals[0]*(x**4) + vals[1]*(x**3) +vals[2]*(x**2) +vals[3]*x +vals[4] # Aplicamos la definición del polinomio de grado 4
    plt.plot(x, f_x)
    plt.show()
punto5()
##

