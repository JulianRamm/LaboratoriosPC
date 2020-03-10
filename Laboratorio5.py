## Punto 1
def punto1():
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


