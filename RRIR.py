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


def solveLinArr(A, B):
    return(np.linalg.solve(A,B))


def integrate(f):
    return si.quad(f,0,1)


def B(u,v):
    return 0

def takeX(n):
    return n/N

def e(x, n):
    assert n >= 0, 'n jest mniejsze od 0'
    assert N >= n, 'n jest wieksze od ilosci elementow'
    if n > 0:
        if x < takeX(n-1) or x > takeX(n+1):
            return 0
        elif x < takeX(n):
            return N*(x-takeX(n-1))
        else:
            return N*(takeX(n+1)-x)
    elif n == 0:
        if x > takeX(n+1):
            return 0
        else:
            return N*(x-takeX(n-1))

print (e(0,0))


def makeOneRow(row):
    if row!=0:
        length = 1/N
        np_arr = np.arange(N)
        for i in range(N):
            if (i==row-1) or (i==row) or i==row+1:
                np_arr[i] = 2
            else:
                np_arr[i] = 0
        return np_arr


