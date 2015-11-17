# -*- coding: cp949 -*-
import linear_algebra as la


def power_method(A, epsilon=1e-9):
    n = len(A)

    lambda_k = 0.0
    x0 = [1.0] * n

    counter = 0
    while True:
        y1 = la.multiply_matrix_vector(A, x0)

        lambda_k1 = abs(y1[0])
        for y1i in y1[1:]:
            if abs(y1i) > lambda_k1:
                lambda_k1 = abs(y1i)

        for k in xrange(n):
            x0[k] = y1[k] / lambda_k1

        if abs(lambda_k1 - lambda_k) < epsilon:
            break
        lambda_k = lambda_k1

        del y1
        counter += 1

    print("power method counter = %d" % counter)

    return lambda_k1, x0


if "__main__" == __name__:
    A = [[2.0, 1.0],
         [1.0, 3.0]]

    lamda1, x1 = power_method(A)
    print "lambda =", lamda1
    print "x =", x1
