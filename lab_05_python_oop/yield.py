# -*- coding: utf8 -*-
"""
일정 하중 아래 허용응력과 안전률을 고려한 봉의 최소 직경
"""
# 수학 관련 기능을 담은 모듈을 읽어들임
import math

# 1변수 방정식의 해법을 담은 root_finding.py 의 위치를 import 경로에 추가
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.pardir, 'lab_02_root_finding')))
# 1변수 방정식의 해법을 담은 root_finding.py 의 위치를 import 경로에 추가 끝
import root_finding


# class 정의 시작
# 객체의 모양틀이 되어 줌
# 객체를 사용하면, 문제에 관련된 다른 변수들을 지정, 변경하는 것이 쉬워짐
class Experiment(object):
    def __init__(self):
        # 안전률
        self.safety_factor = 2.0
        # 최대 허용 응력
        self.stress_max_Pa = 207e6

        # 힘
        self.force_N = None

    def problem_to_solve(self, radius_m):
        """
        안전률을 고려한 허용 응력
        :param radius_m:
        :return:
        """
        if self.force_N is None:
            print ".force_None 값이 지정되지 않았음"
            result = None
        else:
            result = circular_section_stress(radius_m, self.force_N) \
                     - self.stress_max_Pa / self.safety_factor

        return result


def circular_section_stress(r_m, force_N):
    """
    원형 단면의 응력을 계산
    :param r_m:
    :param force_N:
    :return:
    """
    area_m2 = r_m * r_m * math.pi
    stress_Pa = force_N / area_m2
    return stress_Pa


def main():
    # 객체를 만듦
    experiment = Experiment()

    # 객체의 변수 force_N 을 지정하기 위해 사용자 입력을 받아 들임
    # force_N 에는 문자열? 실수 중 어떤 것이 저장될 것인가?
    experiment.force_N = float(raw_input("Enter force (N):"))
    # 예를 들어 허용 최대 응력이나 안전률을 변경하는 것도 객체를 수정 하는 대신 main() 함수 값을 바꾸면 됨

    # 2분법을 이용하여 허용 응력과 안전률을 고려한 최소 직경을 구함
    # 더 적은 초기값
    x_l_init = root_finding.epsilon_global * 2
    # 더 큰 초기값
    x_h_init = 1.0
    # 2분법 호출
    result = root_finding.bisection(experiment.problem_to_solve, x_l_init, x_h_init, 1e-9)
    # 결과 표시
    print "result =", result


if "__main__" == __name__:
    main()
