import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return a * x ** 2 + b * x + c * x

x = np.array([1.45631068, 1.496010638, 1.537410318, 1.612036539, 1.624548736])
y = np.array([0.539, 0.588, 0.637, 0.686, 0.735])

popt_cons, _ = curve_fit(func, x, y, bounds=([-np.inf, 0, 0], [np.inf, 0.000000000000001, 0.000000000000001]))
print(popt_cons)

residuals = y - func(x, popt_cons[0], popt_cons[1], popt_cons[2])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res/ss_tot)
print(r_squared)

xnew = np.linspace(0,10)

plt.plot(x, y, 'bo')
plt.plot(xnew, func(xnew, *popt_cons), 'r-')
plt.axis([0, 2, 0, 2])
plt.show()
