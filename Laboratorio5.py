## Punto 1
import numpy as np


def punto1():
     # n = int(input("Ingrese el tamaño n de columnas de las matrices"))
    n = 3
    # mat1 = [[0] * n] * n
    mat1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print(mat1)
    # print(np.array(mat1))
    # b = [0] * n
    b = np.array([3,4,5])
    print("Primera matriz: ")
    # for i in range(n):
    #     row = list(map(int, input("Ingrese {} números separados por espacio".format(n)).split(' ')))
    #     mat1[i] = row
    for i in range(1, n, 1):
        for j in range(n):
            mat1[j][j] = mat1[i][j] - mat1[i][j] * (mat1[i][j] / mat1[i - 1][j])
            b[i] = b[i-1] - b[i]
    print(mat1)

punto1()
##

##
