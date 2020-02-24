## Punto 1
def multpl():
    arr = list(map(int, input("Ingrese los números separados por espacio").split()))
    multp = 1;
    for i in range(len(arr)):
        multp *= arr[i]
    return multpl
## Punto 2
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
## Punto 3
import math as m;
def esPrimo(n):
    raiz = m.sqrt(n)
    j = 2;
    while j < raiz:  # Para verificar que un número sea primo basta conv erificar que no hayan factores hasta la raíz del número que se quiere probar
        if n % j == 0:  # En esta línea se calcula el residuo de la división de i con j. Donde i es el i-esimo número de la lista y j es un número menor a la raíz de i
            return False
    return True
##
def esPalindrome(cad):
        reemplazos = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in reemplazos:
            cad = cad.replace(a, b).replace(a.upper(), b.upper())
        return cad.upper() ==
print(esPalindrome("Halí"))
##

