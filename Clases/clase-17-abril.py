import numpy as np
import matplotlib.pyplot as plt

Xi = np.array([13, 16, 17, 23, 28, 33])
Yi = np.array([30, 92, 21, 159, 94, 236])


def coefValues(Xi, Yi):
    N = np.size(Xi)
    A = np.zeros([N, N])
    b = np.zeros([N, 1])
    for i in range(N):
        for j in range(N):
            A[i, j] = Xi[i] ** (N - j - 1)
        b[i] = Yi[i]
    Ci = np.linalg.solve(A, b)
    return Ci


Ci = coefValues(Xi, Yi)
CiPoly = np.polyfit(Xi, Yi, np.size(Xi) - 1)
print("Coef. \t{:^35s}\t{:^20s}\t".format("Ci", "CiPolyfit"))
for i in range(np.size(Ci) - 1, -1, -1):
    print("C_{:d}\t{:25.10f}\t{:25.10f}".format(i, Ci[i][0], CiPoly[i]))

##
Xk = np.array([15, 19, 21, 25, 27, 32])


def YkValues(Cin, Xin):
    N = np.size(Cin)
    Yout = np.zeros(np.size(Xin))
    for i in range(np.size(Xin)):
        for j in range(N):
            Yout[i] += (Cin[j] * (Xin[i] ** (N - j - 1)))
    return Yout


Yk = YkValues(Ci, Xk)
YkPoly = np.polyval(CiPoly, Xk)

print("Coef. \t{:^35s}\t{:^20s}\t".format("Yk", "YkPolyval"))
for i in range(np.size(Ci)):
    print("C_{:d}\t{:25.10f}\t{:25.10f}".format(Xk[i], Yk[i], YkPoly[i]))

##
Xp = np.arange(Xi[0], Xi[-1], 0.01)
Yp = YkValues(Ci, Xp)
plt.figure()
plt.plot(Xp, Yp, 'b')
plt.plot(Xi, Yi, 'sr')
plt.plot(Xi, Yi, '--', color = '0.5')
plt.plot(Xk, Yk, 'sg')
plt.xlim([0.0, 37.0])
dis = (np.max(Yp)- np.min(Yp))*0.1
plt.ylim([np.min(Yp)- dis, np.max(Yp) + dis])
plt.xlabel("x")
plt.ylabel("y")
plt.grid(1)

