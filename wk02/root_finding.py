# -*- coding: cp949 -*-


# |x| < epsilon == (x = 0)
epsilon = 1e-4


def sequential(f, x0):
    # � ������ �Է°��� ������ �� �� ������
    # xi �� �ʱⰪ�� (�ε��Ҽ���) �Ǽ��� �Ǿ�� �ϹǷ�
    # float() �� �̿��Ѵ�
    xi = float(x0)
    # delta_x �� �ǹ̴�
    # "���� ���� ã�� ������ �� xi�� �󸶸�ŭ ������ų ���ΰ�"
    # �̴�
    delta_x = 1e-6
    counter = 0
    while True:
        fi = f(xi)
        if abs(fi) < epsilon:
            break
        xi += delta_x
        counter += 1
    print "seq_counter =", counter
    return xi


# end of sequential()


def bisection(f, xl, xh, epsilon=epsilon, b_verbose=False):
    xl = float(xl)
    xh = float(xh)
    xn = xl

    counter = 0
    while True:
        xn = 0.5 * (xl + xh)

        if f(xn) * f(xh) < 0:
            xl = xn
        else:
            xh = xn

        counter += 1

        if b_verbose:
            print ("xl = %8f f(xl) = %+8f xn = %+8f f(xn) = %+8f xh = %+8f f(xh) = %8f |xh-xl| = %-8f" % (
                xl, f(xl), xn, f(xn), xh, f(xh), abs(xh - xl)))

        if abs(xh - xl) < epsilon:
            break

    if b_verbose:
        print "bis_counter =", counter

    return xn


# end of bisection()


def newton(f, df, x0):
    counter = 0
    xi = float(x0)
    while True:
        fi = f(xi)
        counter += 1
        if abs(fi) < epsilon:
            break
        else:
            xi += (-fi / df(xi))

    print "nr_counter =", counter
    return xi


# end of newton


def func(x):
    return 1.0 * x * x - 2.0


# end of func()
# inspired by Scratch example


def dfunc(x):
    return 2.0 * x


# end of dfunc()
# for later use

if "__main__" == __name__:
    # initial value
    x0 = "0.01"

    # call sequential method
    x_seq = sequential(func, x0)
    print "x_seq =", x_seq
    print "f(x_seq) =", func(x_seq)

    x_bis = bisection(func, 0.01, 2.0, b_verbose=True)
    print "x_bis =", x_bis
    print "f(x_bis) =", func(x_bis)

    x_nr = newton(func, dfunc, 2.0)
    print "x_nr =", x_nr
    print "f(x_nr) =", func(x_nr)

    print "error   seq         bis        nr"
    print "        %7g %7g %7g" % (abs(2.0 ** 0.5 - x_seq), abs(2.0 ** 0.5 - x_bis), abs(2.0 ** 0.5 - x_nr))
