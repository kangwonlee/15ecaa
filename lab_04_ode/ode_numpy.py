# -*- coding: utf8 -*-
# 수학 관련 기능을 담은 모듈을 불러 들임
import numpy


def fwd_euler(f, x_init, t_start, t_end, delta_t):
    """
    상미분 방정식의 초기값 문제를 위한 전진 오일러법

    t[k] 와 t[k+1] 사이에는 dx/dt 가 상수일 것으로 가정함

    dx/dt 로 t[k] 에서의 값을 사용

    delta_t_sec 가 작은 값이 되지 않으면 오차가 커지는 경향이 있음

    :param f: dx/dt = f(x,t)
    :param x_init: x 의 초기값
    :param t_start: 초기 시간
    :param t_end: 끝 시간
    :param delta_t: 시간 간격
    :return: 시간, x 의 list
    """
    # time step tk 를 순서대로 나열
    array_t = numpy.arange(t_start, t_end, delta_t)

    # t_start ~ t_end 사이를 delta_t 간격으로 나눈 갯수. 소숫점 아래는 버림? 반올림?
    m_time_step = array_t.shape[0]

    # 상태의 갯수 == 초기 상태 벡터의 길이
    n_states = len(x_init)

    # time step 인덱스 k를 순서 대로 나열
    #   0, 1, ...., m_time_step-1
    array_k = numpy.arange(m_time_step)

    # 예를 들어 t_start, t_end, delta_t 이 0.0, 1.0, 0.1 로 주어졌다면
    #   m_time_step 은 10
    #       array_t 에는 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 가 저장될 것이며
    #       len(array_t) == 10

    # 각 time step 에서의 상태 변수 값을 저장할 list 를 미리 할당(allocate) 시작
    # array_x 를 초기화 함
    # array_x[0] == k = 0 일때의 x 값 == 초기값 x_init
    array_x = numpy.zeros((m_time_step, n_states))
    array_x[0] = x_init

    # 이렇게 하면 m_time_step x n_states 의 크기를 갖는 2차원 배열 공간이 준비됨

    # python 의 경우, 위와 같이 미리 할당하지 않고 각 time step 마다 state x 를 append 할 수도 있음
    # 다른 프로그래밍 언어의 경우 자료를 저장하기 전에 저장할 장소를 할당할 필요가 있을 경우가 많음

    # 상태 변수 저장할 공간 할당 끝

    # time step 반복문 시작
    for k in array_k[:-1]:
        # 이번 time step 에서의 기울기 dx/dt = f(x) 를 계산하여 sk 라는 변수에 저장
        sk = numpy.array(f(array_x[k], array_t[k]))

        # 전진 오일러법을 적용
        array_x[k + 1] = array_x[k] + sk * delta_t

    # time step 반복문 끝

    # 각 time step 별 시간, 상태 값을 반환
    return array_t, array_x

# fwd_euler() 함수 끝
