import unittest

import linear_algebra as lin_alg


class TestLinearAlgebra(unittest.TestCase):
    def test_dot(self):
        x = [1.0, 2.0]
        y = [2.0, -1.0]
        result = lin_alg.dot(x, y)
        expected = 0.0
        self.assertAlmostEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
