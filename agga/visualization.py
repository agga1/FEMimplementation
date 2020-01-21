from agga.params import solveDifferentialEquation
import matplotlib.pyplot as plt
import numpy as np

res = solveDifferentialEquation()
for x in np.arange(0, 1.1, 0.1):
    print("x: ", round(x,2), "\t u(x) = ", round(res(x), 4))


t1 = np.arange(0.0, 1.0, 0.1)
t2 = [round(res(x), 3) for x in t1]

plt.plot(t1, t2)

plt.show()