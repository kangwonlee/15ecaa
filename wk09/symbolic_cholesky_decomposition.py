import sympy as sp

# Brendan Wood, MRocklin, Amelio Vazquez-Reina, Automatically populating matrix elements in SymPy, http://stackoverflow.com/questions/6877061/automatically-populating-matrix-elements-in-sympy, 2011 Aug 02, (accessed 2015 Dec 01)

M = sp.Matrix(3, 3, lambda i, j: sp.var('M_%d%d' % (i+1,j+1)))


for i in xrange(2):
    for j in xrange(i+1, 3):
        M[i, j] = 0

print(M)
