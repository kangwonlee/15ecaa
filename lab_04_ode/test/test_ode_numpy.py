import os
import sys
import unittest

import numpy

sys.path.append(os.pardir)
import ode_numpy
import ode


class TestOdeNumpy(unittest.TestCase):
    def test_forward_euler(self):
        function_under_test = ode_numpy.fwd_euler
        function_reference = ode.fwd_euler

        self.ode_test(function_reference, function_under_test)

    def test_modified_euler(self):
        function_under_test = ode_numpy.mod_euler
        function_reference = ode.mod_euler

        self.ode_test(function_reference, function_under_test)

    def test_runge_kutta_4(self):
        function_under_test = ode_numpy.runge
        function_reference = ode.runge_while

        self.ode_test(function_reference, function_under_test)

    def test_modified_euler_step(self):
        def f_mod_euler_step_test(x, tk):
            return x

        xk_list = [0.5]
        tk = 1.0
        delta_t = 1.0
        result_x, result_s = ode_numpy.mod_euler_step(f_mod_euler_step_test, xk_list, tk, delta_t)

        expected_slope_k0 = f_mod_euler_step_test(xk_list, tk)
        expected_xk1_list = [xk_list[0] + expected_slope_k0[0] * delta_t]
        expected_slope_k1 = f_mod_euler_step_test(expected_xk1_list, tk + delta_t)
        averaged_slope = [(expected_slope_k0[0] + expected_slope_k1[0]) * 0.5]

        expected_xk1_final_list = [xk_list[0] + averaged_slope[0] * delta_t]

        self.assertAlmostEqual(result_s[0], averaged_slope[0])
        self.assertAlmostEqual(result_x[0], expected_xk1_final_list[0])

    def ode_test(self, function_reference, function_under_test):
        ti = 0.0
        te = 2.0
        delta_t = 0.01
        x0 = (1.0, -1.0)
        result_array_t, result_array_x = function_under_test(ode.func, x0, ti, te, delta_t)
        expected_list_t, expected_list_x = function_reference(ode.func, x0, ti, te, delta_t)
        expected_array_t = numpy.array(expected_list_t)
        expected_array_x = numpy.array(expected_list_x)
        # check number of time steps
        delta_t_rms = expected_array_t - result_array_t
        self.assertEqual(len(expected_array_t), result_array_t.shape[0])
        self.assertEqual(len(result_array_x), result_array_x.shape[0])
        self.assertEqual(result_array_t.shape[0], result_array_x.shape[0])
        # check number of states
        self.assertEqual(len(x0), result_array_x.shape[1])
        self.assertEqual(len(result_array_x[0]), result_array_x.shape[1])
        # check each time step
        self.assertAlmostEqual(0.0, rms_numpy_array_1d(result_array_t, expected_array_t))
        # check state at each time step
        self.assertAlmostEqual(0.0, rms_numpy_array_2d(result_array_x, expected_array_x))


def rms_numpy_array_1d(x, y):
    """
    calculate root mean square error using numpy
    :param x: array-like
    :param y: array-like
    :return:
    """
    return numpy.sqrt(numpy.average((numpy.array(x) - numpy.array(y)) ** 2))


def rms_numpy_array_2d(x, y):
    """
    calculate root mean square error using numpy
    :param x: array-like
    :param y: array-like
    :return:
    """

    delta_array = numpy.array(x) - numpy.array(y)
    square_array = delta_array ** 2
    average_0_array = numpy.average(square_array, axis=0)
    average_1_array = numpy.average(average_0_array)
    result = numpy.sqrt(average_1_array)

    return result


if __name__ == '__main__':
    unittest.main()
