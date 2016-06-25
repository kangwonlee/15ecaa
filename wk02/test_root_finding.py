import unittest

import root_finding as rf


def f(x):
    x = float(x)
    return (x - 1.0) * (x * x + x + 1.0)


def df_dx(x):
    """derivative"""
    x = float(x)
    return (x * x + x + 1.0) + (2 * x + 1.0)


class TestRootFinding(unittest.TestCase):
    def test_sequential(self):
        result = rf.sequential(f, 0.1)
        expected = 1.0
        self.assertAlmostEqual(result, expected, delta=0.001)

    def test_bisection(self):
        result = rf.bisection(f, 0.0, 1.1)
        expected = 1.0
        self.assertAlmostEqual(result, expected, delta=0.001)

    def test_newton_raphson(self):
        result = rf.newton(f, df_dx, 0.0)
        expected = 1.0
        self.assertAlmostEqual(result, expected, delta=0.001)


if __name__ == '__main__':
    unittest.main()
