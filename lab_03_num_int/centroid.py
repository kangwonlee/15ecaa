# -*- coding: utf8 -*-
import math
# 그래프 그리기 관련 기능 등을 담고 있는 pylab 모듈을 불러 들임
import pylab

# set path to root_finding.py

import num_int


def main():
    y_min = 0.0
    y_max = 0.12
    area = num_int.trapezoid1(f, y_min, y_max, 120)
    moment_first = num_int.trapezoid1(g, y_min, y_max, 120)

    centroid = moment_first / area

    print "area =", area
    print "moment =", moment_first
    print("centroid = %g" % centroid)

    y_list = pylab.arange(y_min, y_max, 1e-6)
    w_list = [f(y) for y in y_list]

    pylab.fill_between(y_list, w_list)
    pylab.axvline(x=centroid, c='r')

    pylab.axis('equal')
    pylab.grid()
    pylab.show()


def f(y):
    if 0.0 <= y < 0.02:
        r = 0.01
        result = 0.04 + math.sqrt(r * r - (y - r) ** 2)
        # result = 0.06
    elif 0.02 <= y < 0.10:
        result = 0.02
    elif 0.10 <= y <= 0.12:
        result = 0.06
    else:
        result = 0.0

    return result


def g(y):
    result = y * f(y)
    return result


if "__main__" == __name__:
    main()
