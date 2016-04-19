__author__ = 'KangWon LEE'
import random
random.seed()


def normal_samples(n, mu = 0.0, sigma = 0.1):
    """
    normal distribution random numbers
    :param n: number of samples
    :param mu: average
    :param sigma: standard deviation
    :return: list of n samples of random numbers following normal distribution
    """
    return list([random.normalvariate(mu, sigma) for k in range(n)])


if __name__ == '__main__':
    help(random)
    print(normal_samples(10))
