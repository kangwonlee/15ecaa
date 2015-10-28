import math
import num_int


def main():
    y_min = 0.0
    y_max = 0.12
    area = num_int.trapezoid1(f, y_min, y_max, 120)
    moment_first = num_int.trapezoid1(g, y_min, y_max, 120)

    center = moment_first / area

    print "area =", area
    print "moment =", moment_first
    print("center =", center)


def f(y):
    if 0.0 <= y < 0.02:
        r = 0.01
        result = 0.04 + math.sqrt( r*r - (y-r)**2 )
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
