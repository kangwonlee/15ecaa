import root_finding as rf


def g(x):
    return (x-1.0) * (x-2.0) + 10.0


def dgdx(x):
    return 2.0*x - 3.0


if "__main__" == __name__:
    x_nr = rf.newton(g, dgdx, 2.5)



