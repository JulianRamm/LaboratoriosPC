## Punto 1
import numpy as np

A = np.array([[1, 1, 1], [3, 2, 1], [4, 3, 1]], dtype=float)
b = np.array([[60], [95], [125]])
Au = np.concatenate((A, b), 1)


def gaussJordan(A, b):
    Au = np.concatenate((A, b), 1) #Primero creamos la matriz aumentada
    for i in range(np.size(Au, 0)):
        maxi = np.argmax(np.abs(Au[i:, i])) #Luego, encontramos el índice de la fila que tiene el mayor elemento en la columna i
        if maxi != 0:
            Au[[i, maxi]] = Au[[maxi, i]]  #Si hay un número estrictamente mayor a la fila actual, se hace un swap de filas y se sigue normalemente
        Au[i, :] = (1.0 / Au[i, i]) * Au[i, :]  #Primero convertimos cada fila de la diagonal superior en 1
        for j in range(0, np.size(Au, 0)):
            if i == j: #     Esto se hace para dejar libres los elementos de la diagonal
                continue
            filaux = (-1.0 * Au[j, i]) * Au[i, :]
            Au[j, :] = Au[j, :] + filaux #Luego, cada fila de la diagonal inferior y superior se vuelve 0
    x2 = Au[:, np.size(Au, 1) - 1]
    print(Au)

    print("Solución por Gauss-Jordan: \n", x2)
    return [x2]


gaussJordan(A, b)
print("Solución de Numpy: ", np.linalg.solve(A, b)) #Comparamos el resultado con las librerías de numpy
## Punto 3
import numpy as np
import matplotlib.pyplot as plt
import struct as st


def punto3(x, y):
    A = [[1, (1 / len(x)) * np.sum(x)], [np.average(x), np.average(np.multiply(x, x))]]
    b = [[np.average(y)], [np.average(np.multiply(x, y))]]   #Como está descrito en el docuemnto de word adjunto, esta es la matriz a la que llegamos

    coefs = gaussJordan(A, b) #Solucionamos la matriz con el método de gauss-jprdan previamente creado para obtener los coeficientes
    a_0 = coefs[0][0]
    a_1 = coefs[0][1] #Obtenemos los coeficientes del resultado
    print(a_0, a_1)

    y_ = np.multiply(x, a_1) + a_0 #Creamos una recta de la forma y = a_1x + a_0, la cual es la que mejor se ajusta a los datos ingresados de x y y
    print("Coeficientes obtenidos con polyfit: ", np.polyfit(x, y, 1))

    plt.plot(x, y, "r", x, y_, "b")
    plt.title("Grafica de los puntos (x,y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.text(6.5, 35, "Gráfica de la recta obtenida:\n y = {}x +{}".format(a_1, a_0),
             rotation=32,
             multialignment="center", color="b"
             )
    plt.show() #Graficamos la curva y la recta obtenida con la regresión


filex = open("./archivos/Lab-Reg-X.bin", "rb")  #leemos los datos ubicados en los archivos dados para x y y
filey = open("./archivos/Lab-Reg-Y.bin", "rb")

varx = filex.read() #leemos los datos de los archivos
vary = filey.read()

x = st.unpack("d" * int(len(varx) / 8), varx) #Por último, desempaquetamos los datos con una "d" ya que son de tipo double y se divide a su vez en 8 para obtener su longitud real
y = st.unpack("d" * int(len(vary) / 8), vary)

punto3(x, y)


## Punto 4
import matplotlib.patches as mpatches
def acomodar(x, y):
    A = [[1, (1 / len(x)) * np.sum(x)], [np.average(x), np.average(np.multiply(x, x))]]
    b = [[np.average(y)], [np.average(np.multiply(x, y))]]

    coefs = gaussJordan(A, b)
    print("Coeficientes obtenidos con polyfit: ", np.polyfit(x, y, 1))
    return coefs


def punto4():
    años = [1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004]
    hombres = [10.80, 10.30, 10.30, 10.30, 10.40, 10.50, 10.20, 10.00, 9.95, 10.14, 10.06, 10.25, 9.99, 9.92, 9.96,
               9.84, 9.87, 9.85] #Simplemente pasé los datos que estaba en el archivo de word a mano, ya que eran poquitos
    mujeres = [12.20, 11.90, 11.50, 11.90, 11.50, 11.50, 11.00, 11.40, 11.08, 11.07, 11.08, 11.06, 10.97, 10.54, 10.82,
               10.94, 10.75, 10.93]

    reg_h = acomodar(años, hombres) #Obtenemos los coeficientes de las rectas que mejor se acomodan a las curvas con el método creado anteriormente, para hombres y mujeres
    reg_m = acomodar(años, mujeres)

    años_l = range(1928, 2201, 4) #Aumentamos el rango de los años hasta 2200, para poder realizar una extrapolación de los datos y encontrar el punto de intersección de las rectas

    y_h = reg_h[0][1] * años_l + reg_h[0][0] #Calculamos los datos de las rectas de hombres y mujeres con los coeficientes encontrados anteriormente
    y_m = reg_m[0][1] * años_l + reg_m[0][0]

    plt.plot(años_l, y_h, "b")
    plt.plot(años_l, y_m, "r")

    plt.title("Grafica de los puntos (x,y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(('Hombres', 'Mujeres'), #Ubicamos el punto en el que se intersectan con una ayuda gráfica, que en este caso está alrededor de 2113
               loc='upper right')
    plt.annotate('Punto de intersección en el año: 2113', xy=(2113, 8.8), xytext=(1960, 8),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()



punto4()

##
