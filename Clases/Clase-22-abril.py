import numpy as np
Xi = np.array([13, 16, 17, 23, 28, 33])
Yi = np.array([30, 92, 21, 159, 94, 236])
Xk = np.array([15, 19, 21, 25, 27, 32])

def lagrangeValues(Xi, Yi, Xk):
    Yk = np.zeros(np.size(Xk))
    for k in range(np.size(Xk)):
        for i in range(np.size(Yi)):
            multaux = 1
            for j in range(np.size(Yi)):
                if i == j:
                    continue
                multaux *= ((Xk[k]-Xi[j])/(Xi[i]-Xi[j]))
            Yk[k] += Yi[i]*multaux
    return Yk

Yk = lagrangeValues(Xi, Yi, Xk)
CiPoly = np.polyfit(Xi, Yi, np.size(Xi)-1)
YkPoly = np.polyval(CiPoly, Xk)

print("Xk \t{:^35s}\t{:^20s}\t".format("Yk", "YkPolyval"))
for i in range(np.size(Xk)):
    print("C_{:d}\t{:25.10f}\t{:25.10f}".format(Xk[i], Yk[i], YkPoly[i]))


##
import numpy as np
Xi = np.array([13, 16, 17, 23, 28, 33])
Yi = np.array([30, 92, 21, 159, 94, 236])
Xk = np.array([14, 18, 20, 22, 24, 26, 30, 31])

def lagrangeValues(Xi, Yi, Xk):
    Yk = np.zeros(np.size(Xk))
    for k in range(np.size(Xk)):
        for i in range(np.size(Yi)):
            multaux = 1
            for j in range(np.size(Yi)):
                if i == j:
                    continue
                multaux *= ((Xk[k]-Xi[j])/(Xi[i]-Xi[j]))
            Yk[k] += Yi[i]*multaux
    return Yk

Yk = lagrangeValues(Xi, Yi, Xk)
CiPoly = np.polyfit(Xi, Yi, np.size(Xi)-1)
YkPoly = np.polyval(CiPoly, Xk)

print("Xk \t{:^35s}\t{:^20s}\t".format("Yk", "YkPolyval"))
for i in range(np.size(Xk)):
    print("C_{:d}\t{:25.10f}\t{:25.10f}".format(Xk[i], Yk[i], YkPoly[i]))

##

