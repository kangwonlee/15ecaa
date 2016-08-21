# -*- coding: utf8 -*-
"""
1변수 방정식의 근을 찾는 방법 중 sequential method 를 사용하여
어떤 함수 g(x)의 근을 찾고자 함
"""

# 1변수 방정식의 근을 찾는 함수를 모아둔 root_finding 모듈을 불러들임
import root_finding as rf


def g(x):
    # 근을 구하고자 하는 함수
    return (x - 1.0) * (x - 2.0) + 10.0


def dgdx(x):
    # g(x) 의 x 에 대한 미분
    return 2.0 * x - 3.0


if "__main__" == __name__:
    x_nr = rf.newton(g, dgdx, 2.5)
