# -*- coding: cp949 -*-
"""
1변수 방정식의 해
어떤 (비선형) 함수 f(x) 값이 0 이 되도록 만드는 x 를 찾음
"""

# 컴퓨터의 메모리에는 원래는 제한된 자릿수의 2진수만 저장할 수 있음
# 실수를 저장하려면 오차가 발생하게 됨
# epsilon 은 허용 되는 오차 범위를 의미함
# |x| < epsilon == (x = 0)
# |x - y| < epsilon == (x == y)
epsilon = 1e-4


def sequential(f, x0, delta_x=1e-6, epsilon=epsilon):
    """
    sequential method
    x0 로 부터 시작해서  delta_x 만큼씩 증가시키면서 |f(x)| 값이 epsilon 값 보다 작아지는지 관찰함
    :param f: f(x) = 0 인 x를 찾고자 하는 함수
    :param x0: x의 초기값
    :param delta_x: x를 한번에 delta_x 만큼씩 증가시킴
    :param epsilon: 오차 허용 범위

    :return: |f(x)| < epsilon 인 x
    """
    # 어떤 형태의 입력값이 들어올지 알 수 없으나
    # xi 의 초기값은 (부동소숫점) 실수가 되어야 하므로
    # float() 를 이용
    xi = float(x0)
    # delta_x 의 의미는
    # "아직 답을 찾지 못했을 때 xi를 얼마만큼 증가시킬 것인가"

    # counter 는 아래 무한 반복문을 실행한 횟수
    counter = 0

    # 무한 반복문
    while True:
        # f(x)
        fi = f(xi)
        # |f(x)| < epsilon 이면
        if abs(fi) < epsilon:
            # 무한 반복문을 중단
            break
        # 그렇지 않으면
        # x 를 delta_x 만큼 증가시킨다
        xi += delta_x
        # 반복문이 한번 실행 되었으므로 counter 를 1 증가 시킨다
        counter += 1

    # 반복문이 실행된 횟수를 표시
    print "seq_counter =", counter

    # 반복문에서 찾은 결과를 반환
    return xi
# end of sequential()


def bisection(f, xl, xh, epsilon=epsilon, b_verbose=False):
    """
    bisection method
    f(xl) 과 f(xh)의 부호가 반대인 xl, xh 에서 시작
    xl ~ xh 사이의 구간을 절반 지점인 xn를 찾음
    f(xl) 과 f(xn) 의 부호가 반대이면 xh를 xn 으로 옮김
        이렇게 하면 계속 f(xl) 과 f(xh)의 부호가 반대임
    그렇지 않으면 xl을 xn으로 옮김
        f(xn) 과 f(xh)의 부호가 반대일 것임

    xl ~ xh 사이의 구간의 길이가 epsilon 보다 작아지면 중단


    :param f: f(x) = 0 인 x를 찾고자 하는 함수
    :param xl: x의 초기값 xl < xh && f(xl) f(xh) < 0
    :param xh: x의 초기값 xl < xh && f(xl) f(xh) < 0
    :param epsilon: 오차 허용 범위
    :param b_verbose: 중간 과정 표시. 정해 주지 않으면 False
    :return: f(x) == 0 인 x 와 가까운 값
    """

    # 어떤 형태의 입력값이 들어올지 알 수 없으나
    # xi 의 초기값은 (부동소숫점) 실수가 되어야 하므로
    # float() 를 이용
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
