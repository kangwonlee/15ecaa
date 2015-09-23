# from math module, import exp() function
from math import exp

def rect0(f, x0, x1, n = 100):
    """
    Numerical integration

    Assume f(x) is constant between x[k] and x[k+1]

    Parameters
    ----------
    f: function to be integrated
    x0: lower bound of integration
    x1: upper bound of integration
    n: number of intervals

    Return
    ______
    Numerical integration of function f(x) in interval [x0, x1]
    """
    # calculate x interval
    deltaX = (float(x1) - float(x0)) / n

    # generate list x
    # k = 0, 1, 2, ..., (n-1)
    # list of mid point of each rectangle
    x = [x0 + deltaX * (0.5+k) for k in xrange(n)]

    # integration result
    result = 0.0

    # k loop
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # k-th x
        xk = x[k]
        # k-th area
        F_k = f(xk) * deltaX
        # accumulate to integration result
        result += F_k
    # end k loop

    # return integration result
    return result
# end of function rect0()

def func(x):
    return exp(x)
# end of function func()

def Func(x):
    return exp(x)
# end of function Func()

if "__main__" == __name__:
    help(rect0)
    # initial value
    x0 = 0.0
    # final value
    x1 = 1.0
    # number of intervals
    n = 10

    # theoretical exact solution
    print "exact solution =", (Func(x1) - Func(x0))

    # call rect0 function
    F_0 = rect0(func, x0, x1, n)
    print "F_0 =", F_0

    from pylab import plot, show, ylim, grid
    n_plot = 100
    deltaX_plot = (float(x1) - x0) / n_plot
    x = [x0 + k*deltaX_plot for k in xrange(n_plot)]
    x.append(x1)
    y = [func(x[k]) for k in xrange(n_plot)]
    y.append(func(x1))

    plot(x, y)
    ylim((0.0, ylim()[1]))
    grid()
    show()
