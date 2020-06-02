import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpol

Xi = np.array([13,16,17,23])
Yi = np.array([30,92,21,159])

f1Nat = interpol.CubicSpline(Xi, Yi, bc_type='natural')
f1NaK = interpol.CubicSpline(Xi, Yi, bc_type='not-a-knot')
f1Clam = interpol.CubicSpline(Xi, Yi, bc_type='clamped')

Xp = np.arange(Xi[0], Xi[-1], 0.001)

plt.figure()
plt.plot(Xi, Yi, 'sr')
plt.plot(Xp, f1Nat(Xp), '--b')
plt.plot(Xp, f1NaK(Xp), '--m')
plt.plot(Xp, f1Clam(Xp), '--g')
plt.xlim([10.0, 25.0])
plt.ylim([-200.0, 180.0])
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Puntos conocidos", "Natural", "Not-a-Knot", "Clamped"])
plt.grid(1)
##
Xk = np.array([15,19,21])
YkNat


##
import matplotlib.pyplot as plt
# Importamos la librería de scipy para interpolación
import scipy.interpolate as interpol
# Definimos los puntos (x,y) conocidos
Xi = np.array([1,4,7,10,12,16,21,24,26,30,33,37])
Yi = np.array([1,7,12,26,52,92,96,96,139,274,236,126])

# Definimos los valores de Xk para los
# cuales queremos encontrar el valor de yk
Xk = np.array([2,3,5,6,8,9,11,13,14,15,17,18,19,20,22,
               23,25,27,28,29,31,32,34,35,36])
YkOrg = np.array([2,6,18,11,8,37,30,25,71,72,21,48,69,
               94,108,159,106,79,94,201,169,250,67,76,127])

# Interpolación Polinomial
Ci1 = CoefValues(Xi, Yi)
YkPol = YkValues(Ci1, Xk)

# Interpolación Polinomial - Lagrange
YkLag = LagrangeValues(Xi, Yi, Xk)

# En este caso 'natural'
f1Nat = interpol.CubicSpline(Xi, Yi, bc_type='natural')
# En este caso 'not-a-knot'
f1NaK = interpol.CubicSpline(Xi, Yi, bc_type='not-a-knot')
# En este caso 'clamped' con valor K=0
f1Clam = interpol.CubicSpline(Xi, Yi, bc_type='clamped')
# Hallamos los correspondientes valores
# estimados de Yk para cada tipo de splines
# Natural
YkNat =  f1Nat(Xk)
# Not-a-Knot
YkNaK = f1NaK(Xk)
# Clamped
YkClam = f1Clam(Xk)

# Imprimimos los valores de Yk obtenidos con
# cada tipo de método de interpolación
print("Xk\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}".
      format("YkOrg", "YkPol", "YkLag", "YkNat", "YkNaK", "YkClam"))
for i in range(np.size(Xk)):
    print("{:d}\t{: 5d}\t{: 5d}\t{: 5d}\t{: 5d}\t{: 5d}\t{: 5d}".
          format(Xk[i], YkOrg[i], np.int(YkPol[i]),
                 np.int(YkLag[i]), np.int(YkNat[i]),
                 np.int(YkNaK[i]), np.int(YkClam[i])))

# Imprimimos la suma de residuos al cuadrado
print("{:^10}\t{:^10s}\t{:^10s}\t{:^10s}\t{:^10s}\t".
      format("YkPol", "YkLag", "YkNat", "YkNaK", "YkClam"))
print("{: 5.02f}\t{: 5.02f}\t{: 5.02f}\t{: 5.02f}\t{: 5.02f}".
      format(np.sum((YkPol-YkOrg)**2), np.sum((YkLag-YkOrg)**2),
             np.sum((YkNat-YkOrg)**2), np.sum((YkNaK-YkOrg)**2),
             np.sum((YkClam-YkOrg)**2)))

# Graficamos los polinomios resultantes
# con cada método de interpolación
plt.figure()
plt.plot(Xi, Yi, 'sr')
plt.plot(Xk, YkOrg, '--sk')
plt.plot(Xk, YkPol, '--sc')
plt.plot(Xk, YkLag, '--sm')
plt.plot(Xk, YkNat, '--sb')
plt.plot(Xk, YkNaK, '--sy')
plt.plot(Xk, YkClam, '--sg')
plt.xlim([0.0, 38.0])
plt.ylim([-70.0, 300.0])
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Puntos conocidos", "Verdaderos", "Polinomial",
            "Lagrange", "Natural","Not-a-Knot","Clamped"])
plt.grid(1)
