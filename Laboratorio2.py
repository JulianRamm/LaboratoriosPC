## Punto 1
n = float(input("ingrese el número  a convertir"))
res = ""
if n > n // 1 or n < 0: ##si n es mayor a su parte entera o negativo se retorna un mensaje de error
    print("Error garrafal: el número es racional o menor a 0")
else:
    n = int(n)
    aux = n
    while aux >= 1:
        res = str(aux % 2) + res ##El mensaje que contiene el número en binario se concatena al revés
        aux = aux // 2 ##Se disminuye el valor del número entero a su mitad entera
    print("El valor de {} en binario es: {}".format(n, res))
## Punto 2
N = float(input("ingrese el número  a convertir"))
n = int(input("Ingrese el número de bits a utilizar"))
res = ""
if n > n // 1 or not(-2**(n-1) <= N <= (2**(n-1))-1):  ##si n es mayor a su parte entera no está dentro del rango [-2^(n-1), 2^(n-1) -1] que es el rango de valores
                                                       # que se pueden representar en complemento a 2, se retorna un mensaje de error
    print("Error garrafal: el número es racional o el número de bits no es suficiente")
else:
    N = int(N)
    compl = N
    if N < 0:
        compl = 2 ** n + N ##Utilizamos la fórmula para convertir un número a su complemento a 2: 2^n - N
    print(compl)
    while compl >= 1:      ##Luego convertimos el número a su representación binaria
        res = str(compl % 2) + res
        compl = compl // 2
    res = "0"*(n-len(res)) + res
    print("El valor de {} en complemento a 2 es: {}".format(N, res))
## Punto 3
N = float(input("ingrese el número  a convertir"))
n = int(input("Ingrese el número de bits a utilizar"))
res = ""
if n / 1 > n // 1 or not(-2**(n-1) <= N <= (2**(n-1))-1):##si n es mayor a su parte entera no está dentro del rango [-2^(n-1), 2^(n-1) -1] que es el rango de valores
                                                         # que se pueden representar en offset binario, se retorna un mensaje de error
    print("Error garrafal: el número es racional o el número de bits no es suficiente")
else:
    acal = int(N) + 2**(n-1)   ##Convertimos el número a su valor en offset binario, lo cual corresponde a sumar 2^(n-1). n-1 ya que el primer bit se utiliza para el signo
    while acal >= 1:           ##Luego convertimos el número a su representación binaria
        res = str(acal % 2) + res
        acal = acal // 2
    res = "0"*(n-len(res)) + res
    print("El valor de {} en complemento a 2 es: {}".format(int(N), res))
## Punto 4
N = float(input("ingrese el número  a convertir"))
res = ""
ent = int(N)
rac = N - int(N)  ##Obtenemos  la parte racional del número para su conversión a binario
entm = ""
potencia = ""
mantissa = ""
if N > 0:
    res += "0"
else:             ##Si el número es positivo, se pone un 0 al principio de la cadena, 1 de lo contrario
    res += "1"
while ent >= 1:
    entm = str(ent % 2) + entm  ##Convertimos la parte entera a su representación binaria
    ent = ent // 2
for i in range(24 - len(entm)):  ##Para la mantissa, necesitamos agregar la parte entera que queda después de la coma + la parte decimal, por lo tanto necesitamos 23 - longitud de parte entera +1
    rac = rac*2                  ##Para convertir la parte decimal a su equivalente binario, multiplicamos la parte decimal por 2 y tomamos el número antes de la coma (1 o 0)
    mantissa = mantissa + str(int(rac//1))  ##Obtenemos el número antes de la coma, calculando la división entera del número. Lo cual, al usar la función floor, siempre va a dar 1 o 0
    if rac > 1:
        rac = rac - 1           ##Si el número es mayor a 1, le restamos 1 para obtener sólo la parte decimal
potencian = len(entm) + 126     ##La potencia se calcula como el número de veces que se corrió la coma más 127. Como la coma se lleva hasta el 2do número de la cadena, se suma len(entm) -1 + 127
                                #Que es equivalente a len(entm) + 126
while potencian >= 1:           #Por último, transformamos la potencia a su representación binaria
    potencia = str(potencian % 2) + potencia
    potencian = potencian // 2
print("El número {} en formato IEE 754 es: {}".format(N, res + potencia + entm[1:] + mantissa))
## Punto 5
N = float(input("ingrese el número  a convertir"))
res = ""
ent = int(N)
rac = N - int(N) ##Obtenemos  la parte racional del número para su conversión a binario
entm = ""
potencia = ""
mantissa = ""
if N > 0:
    res += "0"
else:            ##Si el número es positivo, se pone un 0 al principio de la cadena, 1 de lo contrario
    res += "1"
while ent >= 1:
    entm = str(ent % 2) + entm     ##Convertimos la parte entera a su representación binaria
    ent = ent // 2
for i in range(53 - len(entm)):     ##Para la mantissa, necesitamos agregar la parte entera que queda después de la coma + la parte decimal, por lo tanto necesitamos 22 - longitud de parte entera +1
    rac = rac*2                     ##Para convertir la parte decimal a su equivalente binario, multiplicamos la parte decimal por 2 y tomamos el número antes de la coma (1 o 0)
    mantissa = mantissa + str(int((rac//1) % 2))     ##Obtenemos el número antes de la coma, calculando la división entera del número. Lo cual, al usar la función floor, siempre va a dar 1 o 0
    if rac > 1:
        rac = rac - 1                ##Si el número es mayor a 1, le restamos 1 para obtener sólo la parte decimal
potencian = len(entm) + 1022         ##La potencia se calcula como el número de veces que se corrió la coma más 1023. Como la coma se lleva hasta el 2do número de la cadena, se suma len(entm) -1 + 1023
while potencian >= 1:                #Que es equivalente a len(entm) + 1022
    potencia = str(potencian % 2) + potencia     #Por último, transformamos la potencia a su representación binaria
    potencian = potencian // 2
print("El número {} en formato IEE 754 es: {}".format(N, res + potencia + entm[1:] + mantissa))
##

