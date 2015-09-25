# from math module, import exp() function
from math import exp


def rect0(f, x0, x1, n=100):
    """
    Numerical integration

    Assume f(x) is a constant between x[k] and x[k+1]

    Parameters
    ----------
    f:function to be integrated
    x0:lower bound of integration
    x1:upper bound of integration
    n:number of intervals

    Return:
    ------
    Numerical integration of function f(x) in interval [x0, x1]
    """
    # calculate x interval
    delta_x = (float(x1) - float(x0)) / n

    # generate list x
    # k = 0, 1, 2, ..., (n-1)
    # list of mid point of each rectangle
    x = [x0 + delta_x * (0.5 + k ) for k in xrange(n)]

    # integration result
    result = 0.0

    # k loop
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # k-th x
        xk = x[k]
        # k-th area
        F_k = f(xk) * delta_x
        # accumulate to integration result
        result += F_k
    # end k loop

    # return integration result
    return result
# end of function rect0()


def trapezoid1(f, x0, x1, n=100):
    """
    Numerical integration

    Assume f(x) is a straight line between x[k] and x[k+1]

    Parameters
    ----------
    f:function to be integrated
    x0:lower bound of integration
    x1:upper bound of integration
    n:number of intervals

    Return:
    ------
    Numerical integration of function f(x) in interval [x0, x1]
    """
    # initialization
    # calculate x interval
    delta_x = (float(x1) - float(x0)) / n

    xk = x0
    fxk = f(xk)

    # integration result
    result = 0.0

    # for each interval
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # k+1-th x
        xk1 = xk + delta_x
        # k+1-th f(x)
        fxk1 = f(xk1)
        # k-th area
        F_k = (fxk + fxk1) * delta_x * 0.5
        # accumulate to integration result
        result += F_k
        xk = xk1
        fxk = fxk1
    # end k loop

    # return integration result
    return result
# end of function trapezoid1()


def func(x):
    return exp(x)
# end of function func()


def Func(x):
    return exp(x)
# end of function Func()


if "__main__" == __name__:
    help(rect0)
    # initial value
    x_begin = 0.0
    # final value
    x_end = 1.0
    # number of intervals
    n_interval = 2

    # theoretical exact solution
    exact = (Func(x_end) - Func(x_begin))
    print "exact solution =", exact

    # call rect0 function
    F_0 = rect0(func, x_begin, x_end, n_interval)
    print "F_0 =", F_0, "err =", F_0 - exact

    # call trapezoid1 function
    F_1 = trapezoid1(func, x_begin, x_end, n_interval)
    print "F_1 =", F_1, "err =", F_1 - exact

    from pylab import fill, bar, show, xlim, ylim, grid
    # exact
    n_plot = 100
    deltaX_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k*deltaX_plot for k in xrange(n_plot)]
    y = [func(x[k]) for k in xrange(n_plot)]
    x += [x_end, x_end, x_begin]
    y += [func(x_end), 0.0, 0.0]

    fill (x, y)

    # rect0()
    n_plot = n_interval
    deltaX_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k*deltaX_plot for k in xrange(n_plot)]
    y = [func(xk + 0.5*deltaX_plot) for xk in x]
    x += [x_end]
    y += [0]

    bar(x, y, width=deltaX_plot, color='g', alpha=0.3)

    # trapezoid1()
    n_plot = n_interval
    deltaX_plot = (float(x_end) - float(x_begin)) / n_plot
    x = [x_begin + k*deltaX_plot for k in xrange(n_plot)]
    y = [func(xk) for xk in x]
    x += [x_end, x_end, x_begin]
    y += [func(x_end), 0.0, 0.0]

    fill(x, y, color='r', alpha=0.2)

    xlim((x_begin, x_end))
    ylim((0.0, ylim()[1]))

    grid()
    show()
