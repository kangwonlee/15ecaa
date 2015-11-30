import sympy as sp


def main():
    # Brendan Wood, MRocklin, Amelio Vazquez-Reina, Automatically populating matrix elements in SymPy,
    # http://stackoverflow.com/questions/6877061/automatically-populating-matrix-elements-in-sympy, 2011 Aug 02,
    # (accessed 2015 Dec 01)
    L = sp.Matrix(3, 3, lambda i, j: sp.var('L_%d%d' % (i+1, j+1)))

    make_lower_triangle(L)

    LLT = L * L.transpose()

    print(L)
    print(LLT)


def make_lower_triangle(M):
    for i in xrange(2):
        for j in xrange(i + 1, 3):
            M[i, j] = 0


if "__main__" == __name__:
    main()
