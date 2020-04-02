import numpy as np
def bono():

    # [[10, 12, 15, 960]
    # [6, 8, 12,  660]
    # [12, 12, 18, 1080]
    n = 3
    x = [0] * n
    aumentada = np.array([[10, 12, 15,16*60],[6, 8, 12, 11*60 ],[12, 12, 18, 18*60]])
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

print(bono())
##

