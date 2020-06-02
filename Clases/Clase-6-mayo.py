import numpy as np
import matplotlib.pyplot as plt


# Algoritmo de euler hacia adelante

def F1(t, y):
    return (0.49 - ((0.00245 * np.exp(0.49 * t)) / (0.49 + 0.005 * np.exp(0.49 * t)-1))) * y


h = 0.01
y0 = 0.01
t0 = 0.0
tf = 30.0
t = np.arange(t0, tf + h, h)

YEulerFor = np.zeros(len(t))
YEulerFor[0] = y0

for iter in range(1, len(t)):
    YEulerFor[iter] = YEulerFor[iter - 1] + h * F1(t[iter - 1], YEulerFor[iter - 1])

plt.figure()
plt.plot(t, YEulerFor, "r")
plt.xlabel("t", fontsize=15)
plt.ylabel("y(t)", fontsize=15)
plt.grid(1)


## Solución analítica

def yAnalitic(t):
    a = 0.5
    b = 0.01
    So = 0.99
    Io = 1 - So
    N = So + Io
    return ((a * N - b) * Io * np.exp((a * N - b) * t)) / ((a * N - b) + a * Io * (np.exp((a * N - b) * t) - 1))


plt.figure()
plt.plot(t, yAnalitic(t), "b")
plt.plot(t, YEulerFor, "r")
plt.xlabel("t", fontsize=15)
plt.ylabel("y(t)", fontsize=15)
plt.legend(["Analitica", "EulerFor"], fontsize = 12)
plt.grid(1)
##

