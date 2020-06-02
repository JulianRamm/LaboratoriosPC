import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#Definimos las funciones F1 y F1 a estudiar
def F1(x1, x2):
    return x1 ** 2.0 + x2 - 3.0


def F2(x1, x2):
    return ((x1 - 2.0) ** 2.0) + ((x2 + 3.0) ** 2.0) - 4.0


delta = 0.1 #Definimos el valor de delta para avanzar en los valores
x1 = np.arange(-10.0, 10.0, delta)
x2 = np.arange(-10.0, 10.0, delta)
x1, x2 = np.meshgrid(x1, x2)
plt.figure()
c1 = plt.contour(x1, x2, F1(x1, x2),[0.0],  colors='b') #Graficamos las lineas de contorno de las funciones para ver el punto
plt.clabel(c1, fontsize=10)                             #en donde ambas gráficas tienen un valor de 0. Una azul y la otra roja
c2 = plt.contour(x1, x2, F2(x1, x2), colors='r')
plt.clabel(c2, fontsize=10)
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(1)

def Jaco(x1, x2):  #Definimos el jacobiano de las funciones. El cual es igual a la matriz de derivadas con respecto a x1 y x2
    A = np.zeros([2, 2])     #para ambas funciones
    x, y = sp.symbols("x y")  #Creamos los simbolos x y y con la libreria de sympy
    F1 = x ** 2.0 + y - 3.0
    F2 = ((x - 2.0) ** 2.0) + ((y + 3.0) ** 2.0) - 4.0  #Creamos ambas funciones con los simbolos de sympy
    A[0, 0] = sp.lambdify([x, y], sp.diff(F1, x))(x1, x2)  #Utilizamos sp.diff para derivar y sp.lamdify para evaluar la funcion en un punto
    A[0, 1] = sp.lambdify([x, y], sp.diff(F1, y))(x1, x2)
    A[1, 0] = sp.lambdify([x, y], sp.diff(F2, x))(x1, x2)
    A[1, 1] = sp.lambdify([x, y], sp.diff(F2, y))(x1, x2)
    return A

print("-------------------------------------------------------------------------------------------------------------")
print("Con 10^-5:")
x1i0 = 1.5
x2i0 = 0

Tolx = 10 ** -5
Toly = 10 ** -5
iter = 0

while 1:
    iter += 1
    A = Jaco(x1i0, x2i0)
    b = np.zeros([2, 1])
    b[0] = -F1(x1i0, x2i0)
    b[1] = -F2(x1i0, x2i0)
    delta_x = np.linalg.solve(A, b)  #Solucionamos el sistema Ax = b para el jacobiano y b siendo -F1 y - F2
    x1 = np.float(x1i0 + delta_x[0]) #Hallamos las raíces candidatas realizando la operación: x^i = x^i-1 + Deltax
    x2 = np.float(x2i0 + delta_x[1])
    if np.abs(x1 - x1i0) <= Tolx and np.abs(x2 - x2i0) <= Tolx: #Evaluamos el criterio de parada en x
        break
    if np.abs(F1(x1, x2)) <= Toly and np.abs(F2(x1, x2)) <= Toly: #Evaluamos el criterio de parada en y
        break
    x1i0 = x1  #Actualizamos los valores de x1i0 y x2i0 para según los valores de x1 y x2
    x2i0 = x2

print("Multivariables - Raiz x1: ", x1)
print("Multivariables - Raiz x2: ", x2)
print("Multivariables - numero de iteraciones: ", iter)

print("-------------------------------------------------------------------------------------------------------------")
print("Con 10^-10:")
x1i0 = 1.5
x2i0 = 0

Tolx = 10 ** -10
Toly = 10 ** -10
iter = 0

while 1:
    iter += 1
    A = Jaco(x1i0, x2i0)
    b = np.zeros([2, 1])
    b[0] = -F1(x1i0, x2i0)
    b[1] = -F2(x1i0, x2i0)
    delta_x = np.linalg.solve(A, b)
    x1 = np.float(x1i0 + delta_x[0])
    x2 = np.float(x2i0 + delta_x[1])
    if np.abs(x1 - x1i0) <= Tolx and np.abs(x2 - x2i0) <= Tolx:
        break
    if np.abs(F1(x1, x2)) <= Toly and np.abs(F2(x1, x2)) <= Toly:
        break
    x1i0 = x1
    x2i0 = x2

print("Multivariables - Raiz x1: ", x1)
print("Multivariables - Raiz x2: ", x2)
print("Multivariables - numero de iteraciones: ", iter)
print("-------------------------------------------------------------------------------------------------------------")

##
#"Además del código,  deberán contestar  las siguientes preguntas:
#¿Cuántas raíces tiene el sistema de ecuaciones, y porqué?
#  R:/Como podemos ver, la función 1 es la gráfica de una parábola y la otra función corresponde a un círculo.
#  Esto, viendo solamente las líneas de contorno. Por lo tanto, podemos concluir que la parábola interseca al circulo en 2 lugares
#  ya que no es tangente al círculo, es decir, no es igual a la recta con pendiente igual a la derivada en un punto de la grafica del circulo.
#  Por lo tanto, podemos afirmar que hay 2 raíces en el sistema de ecuaciones. Lo anterior también se puede ver en la gráfica de las líneas de contorno
#¿Qué implicación tiene escoger los puntos iniciales:  x1= 40, x2 = -80?, ¿Converge más o menos rápido, y porqué?

print("-------------------------------------------------------------------------------------------------------------")
print("Con 10^-10:")
x1i0 = 40
x2i0 = -80

Tolx = 10 ** -10
Toly = 10 ** -10
iter = 0

while 1:
    iter += 1
    A = Jaco(x1i0, x2i0)
    b = np.zeros([2, 1])
    b[0] = -F1(x1i0, x2i0)
    b[1] = -F2(x1i0, x2i0)
    delta_x = np.linalg.solve(A, b)
    x1 = np.float(x1i0 + delta_x[0])
    x2 = np.float(x2i0 + delta_x[1])
    if np.abs(x1 - x1i0) <= Tolx and np.abs(x2 - x2i0) <= Tolx:
        break
    if np.abs(F1(x1, x2)) <= Toly and np.abs(F2(x1, x2)) <= Toly:
        break
    x1i0 = x1
    x2i0 = x2

print("Multivariables - Raiz x1: ", x1)
print("Multivariables - Raiz x2: ", x2)
print("Multivariables - numero de iteraciones: ", iter)
print("-------------------------------------------------------------------------------------------------------------")

#  Como podemos ver, el número de iteraciones para converger a un valor fue mayor con estos puntos iniciales.
#  Principalmente, la razón para esto es debido a que estos punto están muy alejados a una raíz en la que ambas funciones son 0
#  Están muy alejados, ya que el comportamiento de las funciones no crece de manera tan rápida.
#¿Qué efecto tiene aumentar el valor de tolerancia?, ¿La solución converge mas rápido?
#  Ejecutando el código de la anterior celda, podemos observar los siguientes resultados:
#-------------------------------------------------------------------------------------------------------------
# Con 10^-5:
# # Multivariables - Raiz x1:  1.9999999999602593
# # Multivariables - Raiz x2:  -0.9999999998141519
# # Multivariables - numero de iteraciones:  4
# # -------------------------------------------------------------------------------------------------------------
# # Con 10^-10:
# # Multivariables - Raiz x1:  2.0
# # Multivariables - Raiz x2:  -1.0
# # Multivariables - numero de iteraciones:  5
# # -------------------------------------------------------------------------------------------------------------
#  Por lo tanto, podemos asumir que se espera un mayor número de iteraciones cuado se aumenta el valor de las tolerancias.
#  Ya que el criterio de parada que se debe cumplir es más estricto. Es decir, un valor más pequeño, lo que significa que
#  en algunos casos se deba realizar 1 o más operaciones para cumplir con el criterio de parada del algoritmo

#¿Pueden identificar algún conjunto de valores iniciales x1 y x2, en donde la solución diverja?
#  Sí, el conjunto de valores iniciales donde la solución no diverge es el siguiente:
#  {(x1,x2): x1<0}. Lo que hice para descubrirlo, fue correr el algoritmo con un valor de x1 negativo y lo que vi fue que
#  Se quedaba infinitamente corriendo soluciones. Por ejemplo, con x1 = -1 y x2 = 1.0 o -1.0 la solución no converge

##

