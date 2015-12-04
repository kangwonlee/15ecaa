import unittest

import eigenanalysis as ea
import linear_algebra as la


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

        lamda1, x1 = ea.jacobi_method(A)
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
                self.assertAlmostEqual(Ax1[i_row][k_pivot], lambda_i * x1[i_row][k_pivot])

        # check VT A V = Lambda
        x1TAx1 = la.multiply_matrix_matrix(zip(*x1), Ax1)

        for i_row in xrange(0, len(A) - 1):
            # check diagonal
            self.assertAlmostEqual(x1TAx1[i_row][i_row], lamda1[i_row][i_row])
            # check off-diagonal
            for j_column in xrange(i_row + 1, len(A)):
                self.assertAlmostEqual(x1TAx1[i_row][j_column], 0.0)

    def test_cholesky_decomposition_00(self):
        A = [[16.0, 12.0,  4.0,],
             [12.0, 34.0, 13.0,],
             [ 4.0, 13.0, 41.0,]]

        L_expected = ((4, 0, 0),
                      (3, 5, 0),
                      (1, 2, 6),)

        L = ea.cholesky_decomposition(A)

        A_expected = la.multiply_matrix_matrix(L, zip(*L))

        # check size
        self.assertEqual(len(A), len(L))

        # check row
        for i_row in xrange(0, len(A)):
            self.assertEqual(len(A), len(L[i_row]))
            for j_column in xrange(0, len(A)):
                self.assertAlmostEqual(A[i_row][j_column], A_expected[i_row][j_column])
                self.assertAlmostEqual(L_expected[i_row][j_column], L[i_row][j_column])

    def test_cholesky_decomposition_01(self):
        L_expected = [[10.0, 0.0, 0.0, 0.0],
                      [4.0, 9.0, 0.0, 0.0],
                      [3.0, 5.0, 8.0, 0.0],
                      [1.0, 2.0, 6.0, 7.0]]

        A = la.multiply_matrix_matrix(L_expected, zip(*L_expected))

        L = ea.cholesky_decomposition(A)

        A_expected = la.multiply_matrix_matrix(L, zip(*L))

        # check size
        self.assertEqual(len(A), len(L))

        # check row
        for i_row in xrange(0, len(A)):
            self.assertEqual(len(A), len(L[i_row]))
            for j_column in xrange(0, len(A)):
                self.assertAlmostEqual(A[i_row][j_column], A_expected[i_row][j_column])
                self.assertAlmostEqual(L_expected[i_row][j_column], L[i_row][j_column])

    def test_general_eigenproblem_symmetric_00(self):
        """
        Az = labmda Bz
        """
        A = [[7100, -1100, -1000],
             [-1100, 1100, 0],
             [-1000, 0, 1000]]
        B = [[10000., 0., 0.],
             [0., 200., 0.],
             [0., 0., 210.]]

        w, Z = ea.general_eigenproblem_symmetric(A, B)

        ZT = zip(*Z)

        for wi, zi in zip(w, ZT):

            left = la.multiply_matrix_vector(A, zi)
            Bz = la.multiply_matrix_vector(B, zi)

            self.assertEqual(len(left), len(Bz))

            for li, ri in zip(left, Bz):
                self.assertAlmostEqual(li, wi * ri)


if "__main__" == __name__:
    unittest.main()
