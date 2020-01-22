import math
import numpy as np
import scipy.integrate as si
from typing import Callable

""" ----------------------- unused! ---------------------------------"""
class DiffEquationSolver:
    def __init__(self, a: Callable[[float], float], b: Callable[[float], float], c: Callable[[float], float],
                 f: Callable[[float], float], uR: float, beta: float, gamma: float, N: int):
        self.a = a
        self.b = b
        self.c = c
        self.f = f
        self.N = N

    def integrate(self, f):
        return si.quad(f, 0, 1)

    def eFun(self, n: int):
        return lambda x: self.e(x, n)

    def eDiffFun(self, n: int):
        return lambda x: self.eDiff(x, n)

    def nthX(self, n: int) -> float:
        """
        :param n: ordinal nr of x to be calculated (from 0 to N)
        :return: n-th x coordinates
        """
        return n / self.N

    def e(self, x: float, n: int) -> float:
        assert n >= 0, 'n cannot be less than 0'
        assert N >= n, 'n cannot exceed N'

        if n > 0:
            if x < nthX(n - 1) or x > nthX(n + 1):
                return 0
            if x < nthX(n):
                return N * (x - nthX(n - 1))
            else:
                return N * (nthX(n + 1) - x)
        elif n == 0:
            if x > nthX(n + 1):
                return 0
            else:
                return N * (nthX(n + 1) - x)

    def eDiff(self, x: float, n: int) -> float:
        assert n >= 0, 'n cannot be less than 0'
        assert N >= n, 'n cannot exceed N'

        if n > 0:
            if x < nthX(n - 1) or x > nthX(n + 1):
                return 0
            if x < nthX(n):
                return N
            else:
                return -N
        elif n == 0:
            if x > nthX(n + 1):
                return 0
            else:
                return -N

    def B(self, eNrA: int, eNrB: int) -> float:
        """
        :param eNrA, eNrB: ordinal numbers of base functions ( B(1,2) <=> B(e1, e2) )
        :return: B(u, v) (where u, v - specified base functions)
        """
        e1 = eFun(eNrA)
        e2 = eFun(eNrB)
        e1Diff = eDiffFun(eNrA)
        e2Diff = eDiffFun(eNrB)

        firstComp = -beta * e1(0) * e2(0)
        secondComp = -1 * integrate(lambda x: a(x) * e1Diff(x) * e2Diff(x))[0]
        thirdComp = integrate(lambda x: b(x) * e1Diff(x) * e2(x))[0]
        fourthComp = integrate(lambda x: c(x) * e1(x) * e2(x))[0]

        return firstComp + secondComp + thirdComp + fourthComp

    def l(nr):
        """
        :param nr: ordinal number of base function ( l(1) <=> l(e1) )
        :return: l(v)
        """
        e1 = eFun(nr)
        firstComp = integrate(lambda x: f(x) * e1(x))[0]
        secondComp = -gamma * e1(0)

        return firstComp + secondComp

    def leftMatrixEl(i, j):
        if i == N:
            if j == N:
                return 1
            return 0
        return B(i, j)

    def rightMatrixEl(i):
        if i == N:
            return uR
        return l(i)

    def solveLinArr(A, B):
        return (np.linalg.solve(A, B))

    def getLeftMatrix():
        A = np.zeros((N + 1, N + 1))
        for i in range(0, N + 1):
            for j in range(0, N + 1):
                A[i][j] = leftMatrixEl(i, j)
        print(A)
        return A

    def getRightMatrix():
        A = np.array([rightMatrixEl(i) for i in range(0, N + 1)])
        print(A)
        return A

    def solveDifferentialEquation():
        Am = getLeftMatrix()
        Bm = getRightMatrix()
        uFactors = solveLinArr(Am, Bm)
        u = lambda x: sum([uFactors[i] * e(x, i) for i in range(0, N + 1)])
        return u
