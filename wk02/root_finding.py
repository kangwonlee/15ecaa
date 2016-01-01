# -*- coding: cp949 -*-
def sequential(f, x0):
    # 어떤 형태의 입력값이 들어올지 알 수 없으나
    # xi 의 초기값은 (부동소숫점) 실수가 되어야 하므로
    # float() 를 이용한다
    xi = float(x0)
    # delta_x 의 의미는
    # "아직 답을 찾지 못했을 때 xi를 얼마만큼 증가시킬 것인가"
    # 이다
    delta_x = 1e-6
    counter = 0
    while True:
        fi = f(xi)
        if abs(fi) < epsilon:
            break
        xi += delta_x
        counter += 1
    print("seq_counter =", counter)
    return xi


# end of sequential()


def bisection(f, xl, xh):
    xl = float(xl)
    xh = float(xh)

    counter = 0
    while True:
        xn = 0.5 * (xl + xh)

        if f(xn) * f(xh) < 0:
            xl = xn
        else:
            xh = xn

        counter += 1

        print("xl = %8f f(xl) = %+8f xn = %+8f f(xn) = %+8f xh = %+8f f(xh) = %8f |xh-xl| = %-8f" % (
        xl, f(xl), xn, f(xn), xh, f(xh), abs(xh - xl)))

        if abs(xh - xl) < epsilon:
            break

    print("bis_counter =", counter)
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

    print("nr_counter =", counter)
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


# |x| < epsilon == (x = 0)
epsilon = 1e-4

if "__main__" == __name__:
    # initial value
    x0 = "0.01"

    # call sequential method
    x_seq = sequential(func, x0)
    print("x_seq =", x_seq)
    print("f(x_seq) =", func(x_seq))

    x_bis = bisection(func, 0.01, 2.0)
    print("x_bis =", x_bis)
    print("f(x_bis) =", func(x_bis))

    x_nr = newton(func, dfunc, 2.0)
    print("x_nr =", x_nr)
    print("f(x_nr) =", func(x_nr))

    print("error   seq         bis        nr")
    print("        %7g %7g %7g" % (abs(2.0 ** 0.5 - x_seq), abs(2.0 ** 0.5 - x_bis), abs(2.0 ** 0.5 - x_nr)))
