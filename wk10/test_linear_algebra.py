import unittest

import linear_algebra as lin_alg
import gauss_jordan as gj
import random

random.seed()


class TestVectorMatrix(unittest.TestCase):
    def assertSequenceAlmostEqual(self, seq_a, seq_b, msg=None):
        """
        :param seq_a: a list or a tuple
        :param seq_b: a list or a tuple
        :param msg: default None
        :return:
        """

        self.assertEqual(len(seq_a), len(seq_b))
        for aij, bij in zip(seq_a, seq_b):
            self.assertAlmostEqual(aij, bij, msg=msg)

    def test_assertSequenceAlmostEqual(self):
        x = [random.random(), random.random()]
        self.assertSequenceAlmostEqual(x, x)

    def assertMatrixAlmostEqual(self, mat_a, mat_b, msg=None):
        """
        :param mat_a: list of list
        :param mat_b: list of list
        :return:
        """

        self.assertEqual(len(mat_a), len(mat_b))
        for a_row, b_row in zip(mat_a, mat_b):
            self.assertEqual(len(a_row), len(b_row))
            for aij, bij in zip(a_row, b_row):
                self.assertAlmostEqual(aij, bij, msg=msg)

    def test_assertMatrixAlmostEqual(self):
        n = 3
        i_3_3 = identity_matrix(n)
        self.assertAlmostEqual(i_3_3, i_3_3)


class TestLinearAlgebra(TestVectorMatrix):
    def test_dot(self):
        x = [1.0, 2.0]
        y = [2.0, -1.0]
        result = lin_alg.dot(x, y)
        expected = 0.0
        self.assertAlmostEqual(result, expected)

    def test_multiply_matrix_vector(self):
        x = [[1.0, 0.0],
             [0.0, 1.0]]
        y = [2.0, -1.0]
        result = lin_alg.multiply_matrix_vector(x, y)
        expected = [2.0, -1.0]
        self.assertAlmostEqual(result, expected)


def random_matrix(n):
    result = []

    for row in range(n):
        new_row = []
        result.append(new_row)
        for column in range(n):
            new_row.append(random.random())

    return result


def identity_matrix(n):
    result = []

    for row in range(n):
        new_row = []
        result.append(new_row)
        for column in range(n):
            new_row.append(0.0)
        new_row[row] = 1.0

    return result


class TestGaussJordan(TestVectorMatrix):
    def test_gauss_jordan(self):
        n = 3
        m_3_3 = random_matrix(n)
        m_inv = gj.gauss_jordan(m_3_3)
        i_3_3 = identity_matrix(n)

        m_m_inv = lin_alg.multiply_matrix_matrix(m_3_3, m_inv)

        self.assertMatrixAlmostEqual(m_m_inv, i_3_3)


if __name__ == '__main__':
    unittest.main()
