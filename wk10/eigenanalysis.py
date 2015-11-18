# -*- coding: cp949 -*-
import math
from pprint import pprint

import linear_algebra as la


def power_method(A, epsilon=1e-9):
    # 행렬의 크기
    n = len(A)

    # 가장 큰 고유치를 담게 될 변수
    lambda_k = 0.0
    # 위 고유치의 고유 벡터를 저장할 장소
    zk = [1.0] * n

    counter = 0
    # k : 반복횟수
    # i : i 번째 고유치, 고유 벡터
    while True:
        # 행렬 곱셈
        # k 가 큰 값이라면 z_k 는 첫번째 고유벡터와 거의 같은 방향이므로
        # y_k+1 = A z_k = lambda_1 z_k
        # z_k 의 가장 큰 요소는 1 이었으므로
        # y_k+1 의 가장 큰 요소가 lambda_1 인 것이라고 볼 수 있다.
        yk1 = la.multiply_matrix_vector(A, zk)

        # yk1 벡터에서 절대값이 가장 큰 요소를 찾음
        lambda_k1 = abs(yk1[0])
        for yk1_i in yk1[1:]:
            if abs(yk1_i) > abs(lambda_k1):
                lambda_k1 = yk1_i

        # 위에서 찾은 값으로 yk1 모든 요소를 나누어서 zk 벡터에 저장
        # "위에서 찾은 값으로 yk1 을 normalize 한다"
        # zk 의 가장 큰 요소는 1이 됨
        for i in xrange(n):
            zk[i] = yk1[i] / lambda_k1

        # 이전 단계의 가장 큰 요소와 비교
        if abs(lambda_k1 - lambda_k) < epsilon:
            break
        lambda_k = lambda_k1

        # 사용이 왼료된 y1 벡터의 메모리 공간을 반환
        del yk1
        counter += 1

    print("power method counter = %d" % counter)

    return lambda_k1, zk


def alloc_vec(n):
    return [0.0] * n


def alloc_mat(m, n):
    result = alloc_vec(m)
    for k in xrange(m):
        result[k] = alloc_vec(n)
    return result


def identity(n_row):
    identity_matrix = alloc_mat(n_row, n_row)
    for iPivot in xrange(n_row):
        identity_matrix[iPivot][iPivot] = 1.0
    return identity_matrix


def find_r_s(A0, n):
    r = 0
    s = 1
    ars = A0[r][s]
    abs_ars = abs(ars)

    for i in xrange(n - 1):
        for j in xrange(i + 1, n):
            aij = abs(A0[i][j])
            if aij > abs_ars:
                r = i
                s = j
                abs_ars = aij
                ars = A0[i][j]

    return abs_ars, ars, r, s


def calc_theta(ars, arr, ass):
    theta_rad = 0.5 * math.atan2((2.0 * ars), (arr - ass))
    return theta_rad


def jacobi_method(A, epsilon = 1e-9, bVerbose=False):
    n = len(A)

    A0 = alloc_mat(n, n)
    for i in xrange(n):
        for j in xrange(n):
            A0[i][j] = A[i][j]

    X = identity(n)

    #########################
    counter = 0
    while True:
        abs_ars, ars, r, s = find_r_s(A0, n)

        if abs_ars < epsilon:
            break
        if bVerbose:
            print "ars =", ars
            print "r, s =", r, s

        arr = A0[r][r]
        ass = A0[s][s]

        theta_rad = calc_theta(ars, arr, ass)
        if bVerbose:
            print "theta =", theta_rad * 180 / math.pi, "(deg)"
        cos = math.cos(theta_rad)
        sin = math.sin(theta_rad)

        for k in xrange(n):
            if k == r:
                pass
            elif k == s:
                pass
            else:
                akr = A0[k][r]
                aks = A0[k][s]
                A0[r][k] = akr * cos + aks * sin
                A0[s][k] = aks * cos - akr * sin

                A0[k][r] = A0[r][k]
                A0[k][s] = A0[s][k]

            xkr = X[k][r]
            xks = X[k][s]
            X[k][r] = xkr * cos + xks *sin
            X[k][s] = xks * cos - xkr *sin

        A0[r][r] = arr * cos*cos + 2.0 * ars * sin * cos + ass * sin*sin
        A0[s][s] = arr * sin*sin - 2.0 * ars * sin * cos + ass * cos*cos
        A0[r][s] = A0[s][r] = 0.0
        if bVerbose:
            print "A0"
            pprint(A0)
            print "X"
            pprint(X)
        counter += 1

    print("Jacobi method counter = %d" % counter)

    return A0, X


if "__main__" == __name__:
    A = [[2.0, 1.0],
         [1.0, 3.0]]

    lamda1, x1 = power_method(A)
    print "lambda =", lamda1
    print "x =", x1

    lamda, x = jacobi_method(A)
    print "lambda =", lamda
    print "x ="
    pprint(x)
