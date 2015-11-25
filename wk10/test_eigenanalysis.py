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
        A = [[-2.0, -1.0],
             [-1.0, -3.0]]

        lamda1, x1 = ea.jacobi_method (A)
        self.assertEqual(len(A), len(x1))
        self.assertEqual(len(A[0]), len(x1[0]))


        from pprint import pprint

        pprint(lamda1)

        pprint(x1)

        Ax1 = la.multiply_matrix_matrix(A, x1)

        # check A V = Lambda V
        for k_pivot in xrange(len(A)):
            lambda_i = lamda1[k_pivot][k_pivot]

            for i_row in xrange(len(A)):
                self.assertAlmostEqual(Ax1[i_row][k_pivot],lambda_i * x1[i_row][k_pivot])

        # check VT A V = Lambda
        x1TAx1 = la.multiply_matrix_matrix(zip(*x1), Ax1)

        for i_row in xrange(0, len(A) - 1):
            # check diagonal
            self.assertAlmostEqual(x1TAx1[i_row][i_row], lamda1[i_row][i_row])
            # check off-diagonal
            for j_column in xrange(1, len(A)):
                self.assertAlmostEqual(x1TAx1[i_row][j_column], 0.0)


        pprint(x1TAx1)




if "__main__" == __name__:
    unittest.main()
