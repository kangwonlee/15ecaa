__author__ = 'KangWon LEE'
import random
random.seed()

import pylab
import os
import sys

sys.path.append(os.path.join('..', 'wk10'))

import linear_algebra as la
import gauss_jordan as gj


def normal_samples(n, mu = 0.0, sigma = 0.1):
    """
    normal distribution random numbers
    :param n: number of samples
    :param mu: average
    :param sigma: standard deviation
    :return: list of n samples of random numbers following normal distribution
    """
    return list([random.normalvariate(mu, sigma) for k in range(n)])


def main():
    x_list, y_contaminated, y_list = generate_data()

    a = pseudo_inverse(x_list, y_contaminated)

    print('a =', a)

    generate_plot(x_list, y_contaminated, y_list)


def pseudo_inverse(x_list, y_contaminated):
    """
    # y = x a
    # xT y =  xT x a
    # inv(xT x )xT y =  inv(xT x ) xT x a
    :param x_list:
    :param y_contaminated:
    :return:
    """
    x_matrix_transpose = [x_list,
                          [1.0] * len(x_list)]
    x_matrix = list(zip(*x_matrix_transpose))
    xtx = la.multiply_matrix_matrix(x_matrix_transpose, x_matrix)
    xtx_inv = gj.gauss_jordan(xtx)
    xtx_inv_xt = la.multiply_matrix_matrix(xtx_inv, x_matrix_transpose)
    y_matrix = list(zip(*[y_contaminated]))
    a = la.multiply_matrix_matrix(xtx_inv_xt, y_matrix)
    return a


def generate_plot(x_list, y_contaminated, y_list):
    pylab.plot(x_list, y_list, '.', label='true')
    pylab.plot(x_list, y_contaminated, '.', label='contaminated')
    pylab.grid()
    pylab.xlabel('x')
    pylab.xlabel('y')
    pylab.axis('equal')
    pylab.legend(loc=0)
    pylab.show()


def generate_data():
    a = 0.5
    b = 1.0
    x_list = [x * 1.0 for x in range(10)]
    y_list = [a * x + b for x in x_list]
    noise = normal_samples(len(x_list), sigma=1)
    y_contaminated = [y + w for y, w in zip(y_list, noise)]
    return x_list, y_contaminated, y_list


if __name__ == '__main__':
    main()
