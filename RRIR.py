import math
import numpy as np
import scipy.integrate as si

N = 10
uR = 5
Omega = [0, 1]
beta = 2
gamma = 3

def a(x):
    return x ** 2


def b(x):
    return math.sin(x)


def c(x):
    return math.cos(x)

def f(x):
    return x


def solveLinArr(A, B):
    return(np.linalg.solve(A,B))


def integrate(f):
    return si.quad(f,0,1)


def takeX(n):
    return n/N


def eFun(i):
    return lambda x: e(x, i)

def e(x, n):
    assert n >= 0, 'n jest mniejsze od 0'
    assert N+1 >= n, 'n jest wieksze od ilosci elementow'
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
            return N*(takeX(n+1)-x)

def diffE(x, n):
    assert n >= 0, 'n jest mniejsze od 0'
    assert N+1 >= n, 'n jest wieksze od ilosci elementow'
    if n > 0:
        if x < takeX(n-1) or x > takeX(n+1):
            return 0
        elif x<takeX(n):
            return N
        else:
            return -N
    else:
        if (x<takeX(1)):
            return -N
        else:
            return 0


def l(n):
    if n==N:
        return uR
    en = eFun(n)
    return integrate(lambda x: f(x)*en(x))[0]-gamma*en(0)


def B(e1,e2):
    first = -beta*e1(0)*e2(0)
    return first #TODO

def BToMatrix(i, j):
    if i==N:
        if j==N:
            return 1
        return 0
    e1 = eFun(i)
    e2 = eFun(j)
    return B(e1, e2)


def makeABMatrix():
    np_arr = np.zeros((N+1,N+1))
    for i in range(N+1):
        for j in range(N+1):
            np_arr[i][j] = BToMatrix(i, j)
    return np_arr

def makeALMatrix():
    np_arr = np.zeros((N+1))
    for i in range(N+1):
        np_arr[i] = l(i)
    return np_arr

def arrayOfU():
    return solveLinArr(makeABMatrix(), makeALMatrix())

print(arrayOfU())