# -*- coding: utf8 -*-

"""
1변수 방정식의 해법이 맞게 작동하는지 검사해 주는 프로그램
python 기본 모듈 중 unittest 를 불러들여 사용함
unittest 는 python 프로그램이 의도 대로 작성되었는지 검사하기 위한 기능을 담고 있음
"""

# 소프트웨어 테스트를 위해 unittest 를 불러들임
import unittest

# 1변수 방정식의 해법을 담고 있는 root_finding 를 불러들임
import root_finding as rf


def f(x):
    """
    이 함수 f(x) 를 0 으로 만드는 x 를 찾고자 함
    :param x:
    :return:
    """
    x = float(x)
    return (x - 1.0) * (x * x + x + 1.0)


def df_dx(x):
    """
    f(x) 의 x 에 대한 미분
    Newton-Raphson Method를 위해 사용함
    :param x:
    :return:
    """
    x = float(x)
    return (x * x + x + 1.0) + (2 * x + 1.0)


class TestRootFinding(unittest.TestCase):
    def test_sequential(self):
        # sequential method 로 f(x) 를 0 으로 만드는 x를 찾기 위한 시도
        result = rf.sequential(f, 0.1)
        # 예상되는 결과
        # x == 1.0 이라면 f(x) == 0 일 것임
        expected = 1.0
        # bisection method 의 결과와 예상값을 비교하여 검사
        # abs(expected - result) < delta 이면 통과 그렇지 않으면 예외 Exception 발생
        # 실수 계산은 어느 정도 이하의 오차는 무시함
        self.assertAlmostEqual(expected, result, delta=0.001)

    def test_bisection(self):
        # bisection method 로 f(x) 의 해를 찾기 위해 시도 함
        result = rf.bisection(f, 0.0, 1.1)
        # 예상되는 결과
        expected = 1.0
        # 결과와 예상값을 비교하여 검사
        self.assertAlmostEqual(expected, result, delta=0.001)

    def test_newton_raphson(self):
        # Newton-Raphson method 로 f(x) 의 해를 찾기 위해 시도 함
        result = rf.newton(f, df_dx, 0.0)
        # 예상되는 결과
        expected = 1.0
        # 결과와 예상값을 비교하여 검사
        self.assertAlmostEqual(expected, result, delta=0.001)


# 이 python script 파일이 import 될 때는 실행되지 않음
if __name__ == '__main__':
    # unittest 기능을 이용하는 시험을 시작
    unittest.main()
