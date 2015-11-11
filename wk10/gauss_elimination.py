# -*- coding: cp949 -*-
import linear_algebra as la
from pprint import pprint


def gauss_elimination(A, b):
    """
    1차 다원 연립 방정식 Ax = b 에서 x 를 구함
    A: 계수 행렬
    b: 상수 벡터
    """

    n_row = len(A)
    n_column = len(A[0])

    # Augmented Matrix 를 만듦

    Ab = []
    for i_row in xrange(n_row):
        Ab_row = [0.0] * (n_column + 1)
        for j_column in xrange(n_column):
            Ab_row[j_column] = A[i_row][j_column]
        Ab_row[n_column] = b[i_row]
        Ab.append(Ab_row)

    # pivot 반복문
    for i_pivot in xrange(n_row):
        # pivot 아래 행 반복문
        for j_row in xrange(i_pivot + 1, n_row):
            ratio = -Ab[j_row][i_pivot] / float(Ab[i_pivot][i_pivot])
            # 열 반복문
            for k_column in xrange(n_column + 1):
                Ab[j_row][k_column] += ratio * Ab[i_pivot][k_column]
    # 이 반복문이 끝나고 나면 주 대각선 아래 요소는 모두 0

    pprint(Ab)

    # 결과 저장 공간 지정
    x = [0.0] * n_row

    # 후진대입법

    for i_row in xrange(n_row - 1, -1, -1):
        s = Ab[i_row][-1]

        for k_column in xrange(i_row + 1, n_row):
            s -= Ab[i_row][k_column] * x[k_column]

        x[i_row] = s / Ab[i_row][i_row]

    print x

    return x


def main():
    A = [[3, 2, 1],
         [2, 3, 2],
         [1, 2, 3]]
    b = [1,
         2,
         3]

    x = gauss_elimination(A, b)

    Ax = la.multiply_matrix_vector(A, x)
    print Ax, '==', b


if "__main__" == __name__:
    main()
