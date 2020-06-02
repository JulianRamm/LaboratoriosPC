from math import pi
import datetime
## Punto 1
from math import pi
radio = float(input("Ingrese el radio"))
print("EL area de la esfera es: " + str(4 * pi * radio ** 2)) #El área de una esfera es igual a 4*pi*r^2 eso es lo que calcula esta línea con el radio ingresado por parámetro
## Punto 2
nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
print("Su apellido y nombre son: {} {}".format(apellido, nombre)) #Se retorna un mensaje con las posiciones nombre y apellido, invertidas
## Punto 3
n = int(input("Ingrese el número n"))
print("El valor de (n+n*n+n*n*n) es: " + str(n + n * n + n * n * n))#
## Punto 4
import datetime

date1 = input("Ingrese la primera fecha en formato AAAA MM DD").split();
date2 = input("Ingrese la segunda fecha en formato AAAA MM DD").split();
x = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
y = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))
print("La diferencia entre las fechas es: " + str(abs(x - y))) #La clase datetime se encarga de realizar la diferencia entre las fechas y valor absoluto sirve para que la diferencia no sea negativa
## Punto 5
from math import pi

radio = float(input("Ingrese el radio"))
print("EL volumen de la esfera es: " + str((4 / 3) * pi * radio ** 2)) #El volumen de una esfera es igual a (4/3)*pi*r^3
## Punto 6
n = int(input("Ingrese el número n"))
if (n - 12) > 0:
    print("La diferencia es mayor a 12, el valor de |n|^2 es :" + str(abs((n - 12) ** 2))) #Si la diferencia es mayor a 12, se devuelve el valor absoluto de la diferencia al cuadrado
else:
    print("La diferencia es menor a 12")
## Punto 7
n = int(input("Ingrese el número n"))
if n < 100:
    print("El número es menor a 100")
elif 100 < n < 1000:
    print("El número es mayor a 100 y menor a 1000")
elif 1000 < n < 2000:
    print("El número es mayor a 1000 y menor a 2000")
elif n > 2000:
    print("El número es mayor a 2000")# Se crea una estructura condicional para verificar el rango al que pertenece el número n
## Punto 8
n = int(input("Ingrese el número n"))
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
## Punto 9
n = int(input("Ingrese el número n"))
nums = input("Ingrese los numeros separados por espacio")
cont = 0
lista = list(map(int, nums.split()))
for i in lista:
    if (i == n): #Se recorre la lista nums y cada vez que un número de la lista sea igual a n, se suma una variable qu guarda la cuenta con 1
        cont = cont + 1
print("El número de veces que se repite {} en el arreglo es: {}".format(n, cont))
## Punto 10
n = int(input("Ingrese el número n"))
cad = input("ingrese la cadena")
print("Los últimos {} caracteres de la cadena son: {}".format(n, cad[-n:])) #cad[-n:] significa que se toma la cadena desde la posición -n hasta len(cadena)-1
## Punto 11
num = list(map(int, input("Ingrese los números separados por espacio").split()))
if num[0] == num[1] == num[2]: #Se verifica si todos los números son iguales para enviar una respuesta de 0
    print("Todos los números son iguales, la respuesta es 0")
else:
    print("La suma de los números es: " + str(num[0] + num[1] + num[2]))
## Punto 12
nums = input("Ingrese los numeros separados por espacio").split()
sum = int(nums[0]) + int(nums[1])
if 15 < sum < 20: #Se mira si la suma de ambos números está entre 15 y 20 para enviar una respuesta de 20
    print("La suma está entre 15 y 20, la respuesta es 20")
else:
    print("La suma de los numeros es: " + str(sum))
## Punto 13
x = int(input("ingrese x"))
y = int(input("ingrese y"))
print("El valor de ({} + {})^2 es: ".format(str(x), str(y)) + str((x + y) ** 2))
## Punto 14
from math import sqrt

prims = list(map(float, input("Ingrese x1 y y1").split()))
secs = list(map(float, input("Ingrese x2 y y2").split()))
print("La distancia euclideana entre los 2 puntos es: " + str(
    sqrt(((secs[0] - prims[0]) ** 2) + ((secs[1] - prims[1]) ** 2)))) #La distancia euclideana entre 2 puntos se calcula como: raiz((x2-x1)^2 +(y2-y1)^2)
## Punto 15
n = int(input("Ingrese el número de segundos"))
days = n // (24 * 3600)
n = n % (24 * 3600)
hours = n // 3600
n = n % 3600
minutes = n // 60
n = n % 60
seconds = n
print("El valor de n en dias, horas, minutos y segundos es: " + str(days), "dias", str(hours), "horas", str(minutes),
      "minutos", str(seconds), "segundos")
## Punto 16
from math import sqrt

num = list(map(int, input("Ingrese los números separados por espacio").split()))
cont = 0
for i in num:
    raiz = sqrt(i)
    j = 2;
    while j < raiz: #Para verificar que un número sea primo basta conv erificar que no hayan factores hasta la raíz del número que se quiere probar
        if i % j == 0: #En esta línea se calcula el residuo de la división de i con j. Donde i es el i-esimo número de la lista y j es un número menor a la raíz de i
            cont = cont + 1;
        j = j + 1;

print("El numero de primos es : " + str(len(num) - cont))

## Punto 17
n = int(input("Ingrese el número n"))
print("La suma de 1 a " + str(n) + " es: " + str((n * (n + 1)) / 2)) #Se utiliza la fórmula cerrada de la suma de 1 a n que usó euler. La cual se define como suma(1...n) = n(n+1)/2
## Punto 18
num = list(map(int, input("Ingrese los números separados por espacio").split()))
max = 0
for i in num:
    if i > max: #Cada vez que se encuentre un número mayor a max, se actualiza la variable max con el valor de ese número
        max = i
print("El maximo del arreglo es: " + str(max))
## Punto 19
num = list(map(int, input("Ingrese los números separados por espacio").split()))
min = float("inf") #Para encontrar el mínimo se utiliza el concepto de infinito
for i in num:
    if i < min: #Cada vez que se encuentre un número menor a min , se actualiza la variable max con el valor de ese número
        min = i
print("El mínimo del arreglo es: " + str(min))
## Punto 20
num = list(map(int, input("Ingrese los números separados por espacio").split()))
sum = 0
for i in num:
    sum = sum + i; #Primero se encuentra la suma de todos los elementos del arreglo
print("El promedio de arreglo es: " + str(sum / len(num))) #Luego, se calcula el promedio como sum(num[0],num[1], ...,num[n-1])/n
## Punto 21
from math import sqrt

num = list(map(int, input("Ingrese los números separados por espacio").split()))
sum = 0
for i in num:
    sum = sum + i #Primero se calcula la suma de todos los elementos del arreglo para obtener la media
n = int(len(num))
prom = sum / n #Se calcula la media como: sum(num[0],num[1], ...,num[n-1])/#num
distancia = 0
for i in num:
    distancia = distancia + (i - prom) ** 2 #Realizamos la suma de las distancias al cuadrado de todos los números con la media
print("La desviación estándar muestral del arreglo de números es: " + str(sqrt(distancia / n-1))) #Calculamos la desviación estándar con la fórmula:
                                                                                         #raíz(sum((num[0] - media)^2,(num[1] - media)^2, ...,(num[n-1] - media)^2)/n-1) se divide sobre n-1
                                                                                         #ya que estamos hablando de una muestra y no la población
## Punto 22
num = list(map(int, input("Ingrese los números separados por espacio").split()))
med = 0
n = len(num)
for i in range(len(num)): #Se utiliza un algortimo de ordenamiento llamado: selection sort para ordenar los números del arreglo. Ya que la mediana requiere que los elementos estén ordenados
    max = i
    for j in range(i + 1, len(num)): #Se compara el i-esimo elemento del arreglo con todos los restantes hasta encontrar uno mayor a él
        if num[max] > num[j]: #Si el número j-esimo es mayor, al i-esimo, se hace un swap de elementos
            max = j
    num[i], num[max] = num[max], num[i]
print(num)
if n % 2 == 0: #Ya que la mediana puede tener 2 casos: si n es par o impar cambia el valor de la mediana
    med = (num[(n // 2) - 1] + num[(n // 2)]) / 2 #Si es par, la mediana es igual al promedio de los elementos en la mitad
else:
    med = num[n // 2] #Si es impar, la mediana es el elemento en el centro
print("La mediana es: " + str(med))
## Punto 23
num = list(map(int, input("Ingrese los números separados por espacio").split()))
k = len(num)
max = 0
moda = 0
for i in range(k):
    num[num[i] % k] += k #Cada vez que se encuentra el mismo número en el arreglo, suma el número k a la posición num[i] % k que es el modulo
                         #De esta forma, habrá una posición con el número mayor en el arreglo. Por que solo faltaría encontrar el mayor
for i in range(k):
    if num[i] > max:
        max = num[i] #Encontramos el número mayor y si este es el mayor, significa que la posición i es la moda ya que fue la que mayor tuvo el número k sumado a él
        moda = i
print("La moda es: " + str(moda))
## Punto 24
num = list(map(int, input("Ingrese los números separados por espacio").split()))
for i in range(len(num)): #Se utiliza un algortimo de ordenamiento llamado: selection sort para ordenar los números del arreglo.
    max = i
    for j in range(i + 1, len(num)):
        if num[max] < num[j]: #Se compara el i-esimo elemento del arreglo con todos los restantes hasta encontrar uno mayor a él
            max = j    #Si el número j-esimo es mayor, al i-esimo, se hace un swap de elementos
    num[i], num[max] = num[max], num[i]
print("El arreglo ordenado es: ")
print(num)

## Punto 25
num = list(map(int, input("Ingrese los números separados por espacio").split()))
cont = 0
for i in num:
    if (i % 7 == 0): #Cada vez que se cumple que num[i] % 7 = 0, sabemos que num[i] es un múltiplo de 7
        cont += 1
print("la cantidad de números múltiplos de 7 son: " + str(cont))
## Punto 26
N = int(input("ingrese N"))
M = int(input("ingrese M"))
n = int(input("ingrese n"))
matrix = [[None for y in range(M)] for x in range(N)] #Creamos una matriz de tamaño NxM
for i in range(N):
    for j in range(M):
        matrix[i][j] = n #A cada posición de la matriz asignamos el número n
print("La matriz resultante es: ")
print(matrix)
## Punto 27
n = int(input("Ingrese el tamaño n de filas de la matriz"))
mat = [[None] * n] * n #Creamos una matriz NxN
suma = 0
for i in range(n):
    row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
    mat[i] = row
for i in range(n):
    for j in range(n):
        if i == j:  #Sabemos que la diagonal de una matriz es igual a todos los puntos para los cuales los índices son iguales
            suma = suma + mat[i][j]  #Se suman todos los puntos que cumplen la condición anterior
print("La suma de la diagonal es: " + str(suma))
## Punto 28
n = int(input("Ingrese el tamaño n de filas de la matriz"))
j = n - 1
mat = [[None] * n] * n #Creamos una matriz NxN
suma = 0
for i in range(n):
    row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
    mat[i] = row
for i in range(n):
            suma = suma + mat[i][j] #Se suman todos los puntos en los cuales i es cualquier indice de 1...n y j comienza en n y se reduce en 1 cada vez que se aumente i
            j = j - 1
print("La suma de la diagonal es: " + str(suma))
## Punto 29
n = int(input("Ingrese el tamaño n de columnas de las matrices"))
m = int(input("Ingrese el tamaño m de filas de las matrices"))
mat1 = [[0] * n] * m
mat2 = [[0] * n] * m
suma = [[0] * n] * m
print("Primera matriz: ")
for i in range(m):
    row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
    mat1[i] = row
print("Segunda matriz: ")
for i in range(m):
    row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
    mat2[i] = row
for i in range(m):
    for j in range(n):
        suma[i][j] = mat1[i][j] + mat2[i][j] #Se sabe que sumar 2 matrices es igual a sumar cada entrada en una posición con la entrada de la otra matriz en la misma posición
print("La suma de la matriz {} con {}".format(mat1, mat2) + " es: ")
for r in suma:
    print(r)
## Punto 30
n = int(input("Ingrese el tamaño n de columnas de las matrices"))
m = int(input("Ingrese el tamaño m de filas de las matrices"))
mat = [[None] * n] * m
for i in range(m):
    row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
    mat[i] = row
transpose = [[mat[j][i] for j in range(m)] for i in range(n)] #Recorremos la matriz en el sentido contrario para encontrar la transpuesta de la matriz
print("La matriz transpuesta es: ")
print(transpose)
##

