import unittest

import eigenanalysis as ea
import linear_algebra as la

from pprint import pprint

class TestEigenAnalysis(unittest.TestCase):
    def test_power_method(self):
        A = [[-2.0, -1.0],
             [-1.0, -3.0]]

        lamda1, x1 = ea.power_method(A)
        Ax1 = la.multiply_matrix_vector(A, x1)

        self.assertEqual(len(Ax1), len(A))

        for x1i, Ax1i in zip(x1, Ax1):
            self.assertAlmostEqual(Ax1i, lamda1 * x1i)

    def test_jacobi_method(self):
        A = [[-1.0, -0.5, -0.2],
             [-0.5, -2.0, -1.0],
             [-0.2, -1.0, -3.0]]

        lamda1, x1 = ea.jacobi_method (A)
        self.assertEqual(len(A), len(lamda1))
        self.assertEqual(len(A[0]), len(lamda1[0]))
        self.assertEqual(len(A), len(x1))
        self.assertEqual(len(A[0]), len(x1[0]))

        Ax1 = la.multiply_matrix_matrix(A, x1)
        # check A V = Lambda V
        for k_pivot in xrange(len(A)):
            # diagonal term
            lambda_i = lamda1[k_pivot][k_pivot]

            # off diagonal
            for i_row in xrange(len(A)):
                self.assertAlmostEqual(Ax1[i_row][k_pivot],lambda_i * x1[i_row][k_pivot])

        # check VT A V = Lambda
        x1TAx1 = la.multiply_matrix_matrix(zip(*x1), Ax1)

        for i_row in xrange(0, len(A) - 1):
            # check diagonal
            self.assertAlmostEqual(x1TAx1[i_row][i_row], lamda1[i_row][i_row])
            # check off-diagonal
            for j_column in xrange(i_row + 1, len(A)):
                self.assertAlmostEqual(x1TAx1[i_row][j_column], 0.0)

    def test_cholesky_decomposition_00(self):
        A = [[4.0, 0.5, 0.2],
             [0.5, 2.0, 1.0],
             [0.2, 1.0, 3.0]]

        L_expected = [[2.0, 0.0, 0.0],
                      [0.25, 1.3919410907075056, 0.0],
                      [0.1, 0.700460677904422, 1.580934799006486]]

        L = ea.cholesky_decomposition(A)
        print("Cholesky Decomposition:")
        pprint(L)

        A_expected = la.multiply_matrix_matrix(L, zip(*L))
        print("L LT:")
        pprint(A_expected)

        # check size
        self.assertEqual(len(A), len(L))

        for i_row in xrange(0, len(A)):
            self.assertEqual(len(A), len(L[i_row]))
            for j_column in xrange(0, len(A)):
                self.assertAlmostEqual(A[i_row][j_column], A_expected[i_row][j_column])

    def test_cholesky_decomposition_01(self):
        A = [[64.0,  32.0,   2.0,   1.0],
             [32.0, 128.0,  16.0,   4.0],
             [ 2.0,  16.0, 256.0,   8.0],
             [ 1.0,   4.0,   8.0, 512.0]]

        L_expected = [[8.0, 0.0, 0.0, 0.0],
                      [4.0, 10.583005244258363, 0.0, 0.0],
                      [0.25, 1.417366773784602, 15.935136379352748, 0.0],
                      [0.125, 0.3307189138830738, 0.47065803652096727, 22.619758641786127]]

        L = ea.cholesky_decomposition(A)
        print("Cholesky Decomposition:")
        pprint(L)

        A_expected = la.multiply_matrix_matrix(L, zip(*L))
        print("L LT:")
        pprint(A_expected)

        # check size
        self.assertEqual(len(A), len(L))

        for i_row in xrange(0, len(A)):
            self.assertEqual(len(A), len(L[i_row]))
            for j_column in xrange(0, len(A)):
                self.assertAlmostEqual(A[i_row][j_column], A_expected[i_row][j_column])

if "__main__" == __name__:
    unittest.main()
