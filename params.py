import math
import numpy as np
import scipy.integrate as si

N = 10
uR = 5
Omega = [0, 1]


def a(x):
    return x ** 2


def b(x):
    return math.sin(x)


def c(x):
    return math.cos(x)


def eFun(n):
    return lambda x: e(x, n)


def xFunc(n):
    return n/N


def e(x, n):
    assert n >= 0, 'n cannot be less than 0'
    assert N >= n, 'n cannot exceed N'

    if n > 0:
        if x < xFunc(n-1) or x > xFunc(n+1):
            return 0
        if x < xFunc(n):
            return N*(x-xFunc(n-1))
        else:
            return N*(xFunc(n+1)-x)
    elif n == 0:
        if x > xFunc(n + 1):
            return 0
        else:
            return N*(xFunc(n+1)-x)

print( e(0.05, 0))

print(xFunc(1))

def solveLinArr(A, B):
    return(np.linalg.solve(A,B))


def integrate(f):
    return si.quad(f,0,np.pi)

