import math
import numpy as np
import scipy.integrate as si

N = 100
uR = 5


def a(x):
    return x ** 2


def b(x):
    return math.sin(x)


def c(x):
    return math.cos(x)


def solveLinArr(A, B):
    return(np.linalg.solve(A,B))


def integrate(f):
    return si.quad(f,0,np.pi)

