import numpy as np


def thomasAlg(a, b, c, d) -> np.array:
    """
    :param a, b, c: one of 3 "stripes" from diagonal matrix
    :param d: resulting 1-dim vector (1-dim array)
    :return: x - vector solving the equation (1-dim array)
    """
    nf = len(d)  # number of equations
    aCp, bCp, cCp, dCp = map(np.array, (a, b, c, d))  # copy arrays

    for it in range(1, nf):
        mc = aCp[it - 1] / bCp[it - 1]
        bCp[it] = bCp[it] - mc * cCp[it - 1]
        dCp[it] = dCp[it] - mc * dCp[it - 1]

    x = bCp
    x[-1] = dCp[-1] / bCp[-1]

    for il in range(nf - 2, -1, -1):
        x[il] = (dCp[il] - cCp[il] * x[il + 1]) / bCp[il]

    return x
