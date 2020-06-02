import numpy as np
import matplotlib.pyplot as plt


# Algoritmo de euler hacia adelante

def F1(t, y):
    return (0.49 - ((0.00245 * np.exp(0.49 * t)) / (0.49 + 0.005 * np.exp(0.49 * t) - 1))) * y


def F1EulerBack(t, y, h):
    return y / (1 - h * (0.49 - ((0.00245 * np.exp(0.49 * t)) / (0.49 + 0.005 * (np.exp(0.49 * t) - 1)))))


def F1EulerMod(t, h):
    return 1 - (h / 2.0) * (0.49 - ((0.00245 * np.exp(0.49 * t)) / (0.49 + 0.005 * (np.exp(0.49 * t) - 1))))


h = 0.01
y0 = 0.01
t0 = 0.0
tf = 30.0
t = np.arange(t0, tf + h, h)

analitica = np.zeros(len(t))
YEulerFor = np.zeros(len(t))
YEulerBack = np.zeros(len(t))
YEulerMod = np.zeros(len(t))
y = np.random.rand(0, 30, len(t))
YEulerFor[0] = y0
YEulerBack[0] = y0
YEulerMod[0] = y0
print(len(t))
for iter in range(1, len(t)):
    analitica[iter] = F1(t[iter], y[iter])
    YEulerFor[iter] = YEulerFor[iter - 1] + (h * F1(t[iter - 1], YEulerFor[iter - 1]))
    YEulerBack[iter] = F1EulerBack(t[iter - 1], YEulerBack[iter - 1], h)
    YEulerMod[iter] = (YEulerMod[iter - 1] + (h / 2.0) * F1(t[iter - 1], YEulerMod[iter - 1])) / F1EulerMod(t[iter], h)

print(YEulerFor)
plt.figure()
plt.plot(t, analitica, "b")
plt.plot(t, YEulerFor, "r")
plt.plot(t, YEulerFor, "g")
plt.plot(t, YEulerMod, "m")
plt.xlabel("t", fontsize=15)
plt.ylabel("y(t)", fontsize=15)
plt.legend(["Analítica", "EulerFor", "EulerBack", "EulerMod"], fontsize=12)
plt.grid(1)

##
