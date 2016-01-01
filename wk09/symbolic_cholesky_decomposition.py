from pprint import pprint

import sympy as sp
from functools import reduce


def main():
    # Brendan Wood, MRocklin, Amelio Vazquez-Reina, Automatically populating matrix elements in SymPy,
    # http://stackoverflow.com/questions/6877061/automatically-populating-matrix-elements-in-sympy, 2011 Aug 02,
    # (accessed 2015 Dec 01)
    L = sp.Matrix(3, 3, lambda i, j: sp.var('L_%d%d' % (i, j)))

    # symmetric matrix
    A = sp.Matrix(3, 3, lambda i, j: sp.var('A_%d%d' % tuple(sorted((i, j)))))

    make_lower_triangle(L)

    LLT = L * L.transpose()

    print(L)
    print(LLT)
    print(A)

    eq = sp.Equality(LLT, A)

    print(eq)

    solution = sp.solve(eq, reduce(lambda x, y: x + y, [[L[i, j] for j in range(3)] for i in range(3)]))
    simplified_solution = sp.simplify(solution)

    print("solution")
    pprint(solution)
    print("simplified solution")
    pprint(simplified_solution, width=60)


def make_lower_triangle(M):
    for i in range(2):
        for j in range(i + 1, 3):
            M[i, j] = 0


if "__main__" == __name__:
    main()
