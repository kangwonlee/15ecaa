# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이 사용되었다는 점을 표시하는 것임

# 수학 관련 기능을 담고 있는 math 모듈에서 exp 함수를 불러들임
from math import exp


def rect0(f, xi, xe, n=100):
    """
    0차 수치 적분
    xi ~ xe 사이를 n 개의 구간으로 나눔
    한 구간 안에서는 f(x) 가 상수일 것이라고 가정함

    :param f: 적분될 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝 지점
    :param n: 구간을 나누는 갯수
    :return: f(x) 를 xi ~ xe 구간에서 정적분한 근사값
    """
    # 초기화 시작
    # n개로 나눈 각 구간의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 각 구간 시작 지점 x 값의 list 를 만듦
    # k = 0, 1, 2, ..., (n-1)
    # list of mid point of each rectangle
    x = [xi + delta_x * (0.5 + k) for k in xrange(n)]

    # 적분 결과를 저장할 변수를 초기화
    result = 0.0

    # 초기화 끝

    # 주 반복문 main loop
    # 각 구간별로 연산을 반복 실시
    # k = 0, 1, 2, ..., (n-1)ㅁ
    for k in xrange(n):
        # k 번째 x 값을 위에서 만든 list 에서 찾음
        xk = x[k]
        # k 번쨰 구간의 넓이를 직사각형의 면적으로 구함
        area_k = f(xk) * delta_x
        # 적분 결과에 누적시킴
        result += area_k
    # 주 반복문 끝

    # 적분 결과를 반환함
    return result


def trapezoid1(f, xi, xe, n=100):
    """
    1차 수치 적분
    xi ~ xe 사이를 n 개의 구간으로 나눔
    한 구간 안에서는 f(x) 가 1차 직선일 것이라고 가정함

    :param f: 적분될 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝 지점
    :param n: 구간을 나누는 갯수
    :return: f(x) 를 xi ~ xe 구간에서 정적분한 근사값
    """
    # 초기화 시작
    # n개로 나눈 각 구간의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 적분 구간 시작 지점 k번째 x 초기화
    xk = xi
    # 적분 구간 시작 지점 함수값 k번째 f(x) 초기화
    fxk = f(xk)

    # 적분 결과를 저장할 변수를 초기화
    result = 0.0

    # 초기화 끝

    # 주 반복문 main loop
    # 각 구간별로 연산을 반복 실시
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # 적분 구간 끝 지점 k+1 번째 x 계산
        xk1 = xk + delta_x
        # 적분 구간 끝 지점 k+1 번째 f(x) 계산
        fxk1 = f(xk1)
        # k 번째 구간의 면적을 사다리꼴 공식으로 계산
        area_k = (fxk + fxk1) * delta_x * 0.5
        # 적분 결과에 누적시킴
        result += area_k

        # 현재 구간의 끝점이 다음 구간의 시작점이 됨
        # k+1 번째 x 값을 다음 구간 시작점의 x 값으로 지정
        xk = xk1
        # k+1 번째 f(x) 값을 다음 구간 시작점의 f(x) 값으로 지정
        fxk = fxk1
    # 주 반복문 끝

    # 적분 결과를 반환함
    return result


def simpson2(f, x0, x1, n=100):
    """
    Numerical integration

    Assume f(x) is a 2nd order polynomial between x[k] and x[k+2]

    Parameters
    ----------
    f:function to be integrated
    x0:lower bound of integration
    x1:upper bound of integration
    n:number of intervals

    Return:
    ------
    Numerical integration of function f(x) in interval [x0, x1]
    """
    # initialization
    # calculate x interval

    print "n =", n
    print "n%2 =", n % 2

    # if n is an odd number make it an even number
    if (n % 2): n += 1
    delta_x = (float(x1) - float(x0)) / n

    xk = x0
    fxk = f(xk)

    # integration result
    result = 0.0

    # for each two-interval
    # k = 0, 2, 4, ..., (n-1)
    for k in xrange(0, n, 2):
        # k+1-th x
        xk1 = xk + delta_x
        # k+1-th f(x)
        fxk1 = f(xk1)

        # k+2-th x
        xk2 = xk1 + delta_x
        # k+2-th f(x)
        fxk2 = f(xk2)

        # k-th area
        F_k = (fxk + 4 * fxk1 + fxk2) * (delta_x / 3.0)

        # accumulate to integration result
        result += F_k
        xk = xk2
        fxk = fxk2
    # end k loop

    # return integration result
    return result


# end of function simpson2()


def func(x):
    return exp(x)


# end of function func()


def Func(x):
    return exp(x)


# end of function Func()


if "__main__" == __name__:
    def main():
        help(rect0)
        # initial value
        x_begin = 0.0
        # final value
        x_end = 1.0
        # number of intervals
        n_interval = 8

        # theoretical exact solution
        exact = (Func(x_end) - Func(x_begin))
        print "exact solution =", exact

        # call rect0 function
        F_0 = rect0(func, x_begin, x_end, n_interval)
        print "F_0 =", F_0, "err =", F_0 - exact

        # call trapezoid1 function
        F_1 = trapezoid1(func, x_begin, x_end, n_interval)
        print "F_1 =", F_1, "err =", F_1 - exact

        # call simpson2 function
        F_2 = simpson2(func, x_begin, x_end, n_interval)
        print "F_2 =", F_2, "err =", F_2 - exact

        from pylab import fill, bar, show, xlim, ylim, grid
        # exact
        n_plot = 100
        deltaX_plot = (float(x_end) - x_begin) / n_plot
        x = [x_begin + k * deltaX_plot for k in xrange(n_plot)]
        y = [func(x[k]) for k in xrange(n_plot)]
        x += [x_end, x_end, x_begin]
        y += [func(x_end), 0.0, 0.0]

        fill(x, y)

        # rect0()
        n_plot = n_interval
        deltaX_plot = (float(x_end) - x_begin) / n_plot
        x = [x_begin + k * deltaX_plot for k in xrange(n_plot)]
        y = [func(xk + 0.5 * deltaX_plot) for xk in x]
        x += [x_end]
        y += [0]

        bar(x, y, width=deltaX_plot, color='g', alpha=0.3)

        # trapezoid1()
        n_plot = n_interval
        deltaX_plot = (float(x_end) - float(x_begin)) / n_plot
        x = [x_begin + k * deltaX_plot for k in xrange(n_plot)]
        y = [func(xk) for xk in x]
        x += [x_end, x_end, x_begin]
        y += [func(x_end), 0.0, 0.0]

        fill(x, y, color='r', alpha=0.2)

        xlim((x_begin, x_end))
        ylim((0.0, ylim()[1]))

        grid()
        show()


    main()
