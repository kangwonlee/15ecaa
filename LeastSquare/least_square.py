__author__ = 'KangWon LEE'
import random
random.seed()

import pylab


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

    generate_plot(x_list, y_contaminated, y_list)


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
