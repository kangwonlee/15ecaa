import unittest

import num_int as ni


def f(x):
    x = float(x)
    return x * (x - 5.0) * (x - 10.0)


class TestNumericalIntegration(unittest.TestCase):
    def test_rect0(self):
        result = ni.rect0(f, 0.0, 10.0, n=15)
        expected = 0.0
        self.assertAlmostEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
