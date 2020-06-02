import numpy as np


def F1(y2):
    return y2


def F2(t, y1, y2):
    return 2.0 * y2 - 4.0 * y1 + 8.0 * t - 12.0 * np.sin(2.0 * t)


def F2EulerBack(t, y1, y2, h):
    return (y2 + h * (-4.0 * y1 + 8.0 * t - 12.0 * np.sin(2.0 * t))) / (1 - 2 * h + 4 * (h ** 2))


def F2EulerMod(t1, t2, y1, y2, h):
    return (y2 + (h/2.0)*(F2(t1, y1, y2)-4.0*(y1+(h/2.0)*y2)+8.0*t2-12.0*np.sin(2.0*t2)))/(1-h+(h**2))

h = 0.01
Y10 = -2
Y20 = 8
To = 0.0
Tf = 10.0
T = np.arange(To, Tf+h, h)
Y1EulerFor = np.zeros(len(T))
Y1EulerBack = np.zeros(len(T))
Y1EulerMod = np.zeros(len(T))
Y1RK2 = np.zeros(len(T))
Y1RK4 = np.zeros(len(T))

Y2EulerFor = np.zeros(len(T))
Y2EulerBack = np.zeros(len(T))
Y2EulerMod = np.zeros(len(T))
Y2RK2 = np.zeros(len(T))
Y2RK4 = np.zeros(len(T))

Y1EulerFor[0] = Y10
Y1EulerBack[0] = Y10
Y1EulerMod[0] = Y10
Y1RK2[0] = Y10
Y1RK4[0] = Y10

Y2EulerFor[0] = Y20
Y2EulerBack[0] = Y20
Y2EulerMod[0] = Y20
Y2RK2[0] = Y20
Y2RK4[0] = Y20

for iter in range(1, len(T)):
    Y1EulerFor[iter] = Y1EulerFor[iter - 1] + (h * F1(Y1EulerFor[iter - 1]))
    Y1EulerBack[iter] = F1EulerBack(t[iter - 1], Y1EulerBack[iter - 1], h)
    Y1EulerMod[iter] = (Y1EulerMod[iter - 1] + (h / 2.0) * F1(T[iter - 1], Y1EulerMod[iter - 1])) / Y1EulerMod(T[iter], h)

    Y2EulerFor[iter] = Y2EulerFor[iter - 1] + (h * F1(T[iter - 1], Y1EulerFor[iter - 1]))
    Y2EulerBack[iter] = F2EulerBack(t[iter - 1], Y1EulerBack[iter - 1], h)
    Y2EulerMod[iter] = (Y1EulerMod[iter - 1] + (h / 2.0) * F1(T[iter - 1], Y1EulerMod[iter - 1])) / Y1EulerMod(t[iter],
                                                                                                               h)

