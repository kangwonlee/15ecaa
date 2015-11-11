# -*- coding: cp949 -*-
import linear_algebra as la
from pprint import pprint


def gauss_jordan(A):
    # 행렬의 크기
    n_row = len(A)
    n_column = len(A[0])

    # 단위 행렬과의 Augmented Matrix 를 만듦
    AI = []
    for i_row in xrange(n_row):
        AI_row = [0.0] * (n_column * 2)
        for j_column in xrange(n_column):
            AI_row[j_column] = A[i_row][j_column]
        for j_column in xrange(n_column, n_column*2):
            AI_row[j_column] = 0.0
        AI_row[n_column + i_row] = 1.0
        AI.append(AI_row)

    print "Augmented matrix"
    pprint(AI, width=40)

    # pivot 반복문
    for i_pivot in xrange(n_row):
        # pivot 행을 pivot 요소로 나눔.
        # pivot 요소는 1이 됨
        ratio = 1.0 / float(AI[i_pivot][i_pivot])
        for k_column in xrange(n_column * 2):
            AI[i_pivot][k_column] *= ratio

        # 행 반복문
        for j_row in xrange(0, n_row):
            if j_row != i_pivot:
                ratio = -AI[j_row][i_pivot]
                # 열 반복문
                for k_column in xrange(n_column * 2):
                    AI[j_row][k_column] += ratio * AI[i_pivot][k_column]
    # 이 반복문이 끝나고 나면 주 대각선 이외의 요소는 모두 0

    print "After Gauss Jordan"
    pprint (AI)

    # 오른쪽의 행렬을 떼어냄
    result = []
    for i_row in xrange(n_row):
        result.append(AI[i_row][n_column:])

    return result


if "__main__" == __name__:
    A = [[3, 2, 1],
         [2, 3, 2],
         [1, 2, 3]]

    A_inverse = gauss_jordan(A)
    print "A inverse"
    pprint(A_inverse)

    I_expected = la.multiply_matrix_matrix(A, A_inverse)
    print "I expected"
    pprint(I_expected)
