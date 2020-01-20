from agga.params import solveDifferentialEquation
import matplotlib.pyplot as plt
import numpy as np

res = solveDifferentialEquation()
for x in np.arange(0, 1.1, 0.1):
    print("x: ", round(x,2), "\t u(x) = ", round(res(x), 4))

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 1.0, 0.05)
t2 = [res(x) for x in t1]

plt.figure()
plt.subplot(211)
plt.plot(t1, t2, 'k')

plt.show()