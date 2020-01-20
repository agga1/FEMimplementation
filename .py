def aproximateSolutionFunction(x, us):
    result = 0
    for n in range(0, N):
        result = result+us[n]*e(x, n)
    return result

def visualize():
    x = np.linespace(0, 1)
    y = aproximateSolutionFunction(x)
    pylab.plot(x,y)
    pylab.show()