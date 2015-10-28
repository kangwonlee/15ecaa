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
    print "seq_counter =", counter
    return xi
# end of sequential()


def bisection(f, xl, xh, epsilon=1e-6):
    xl = float(xl)
    xh = float(xh)
    
    counter = 0

    fxl = f(xl)
    fxh = f(xh)

    if 0 < fxl * fxh :
        # 프로그램에서 오류가 발생했음을 알림
        print "Incorrect initial condition"
        # raise Exception
        return None

    while True:
        xn = 0.5 * (xl + xh)
        fxn = f(xn)

        print "xl = %8f f(xl) = %+8f xn = %+8f f(xn) = %+8f xh = %+8f f(xh) = %8f |xh-xl| = %-8f" % (xl, fxl, xn, fxn, xh, fxh, abs(xh-xl))

        if fxn * fxh < 0:
            # xn 에서의 함수값과 xh 에서의 함수값의 부호가 반대
            # f(x) = 0 을 만족시키는 근이 xn 과 xh 사이에 있음
            # xl ~ xn 사이의 구간을 버림
            # xl 을 xn 으로 덮어 씀
            xl = xn
            fxl = fxn
        elif fxn * fxl < 0:
            # xn 에서의 함수값과 xl 에서의 함수값의 부호가 반대
            # f(x) = 0 을 만족시키는 근이 xl 과 xn 사이에 있음
            # xn ~ xh 사이의 구간을 버림
            # xh 를 xn 으로 덮어 씀
            xh = xn
            fxh = fxn
        else:
            # 프로그램에서 오류가 발생했음을 알림
            print "Incorrect initial condition"
            # raise Exception
            return None

        counter += 1

        if abs(xh - xl) < epsilon:
            break

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
            xi += (-fi/df(xi))
            
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


# |x| < epsilon == (x = 0)
epsilon = 1e-4

if "__main__" == __name__:
    # initial value
    x0 = "0.01"

    # call sequential method
    x_seq = sequential(func, x0)
    print "x_seq =", x_seq
    print "f(x_seq) =", func(x_seq)

    x_bis = bisection (func, 0.01, 2.0)
    print "x_bis =", x_bis
    print "f(x_bis) =", func(x_bis)

    x_nr = newton (func, dfunc, 2.0)
    print "x_nr =", x_nr
    print "f(x_nr) =", func(x_nr)

    print "error   seq         bis        nr"
    print "        %7g %7g %7g" % ( abs(2.0**0.5 - x_seq), abs(2.0**0.5 - x_bis), abs(2.0**0.5 - x_nr))
