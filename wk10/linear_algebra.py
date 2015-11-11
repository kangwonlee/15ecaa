# -*- coding: cp949 -*-
def dot(a, b):
    """
    크기가 같은 두 벡터 a, b의 내적 dot product
    """
    # 벡터 a 의 크기.
    # 벡터 b 의 크기는 같을 것이라고 가정한다
    #   (어떤 경우 오류가 발생할 수 있는가?)
    n = len(a)
    result = 0.0
    for i in xrange(n):
        result += a[i] * b[i]
    return result


def multiply_matrix_vector(A, x):
    n_row = len(A)
    n_column = len(A[0])

    result = [0.0] * n_row
    for i in xrange(n_row):
        result[i] = dot(A[i], x)

    return result


def multiply_matrix_matrix(A, B):
    n_row = len(A)
    n_column = len(B[0])
    n_dummy = len(A[0])
    n_dummy2 = len(B)

    # 행렬 크기 확인
    if n_dummy != n_dummy2:
        print "Incorrect Matrix Size"
        return None

    # 행렬을 저장할 공간을 지정
    result = []
    for i_row in xrange(n_row):
        # 각 행을 저장할 공간을 지정
        result.append([0.0] * n_column)

    # 행 반복문
    for i in xrange(n_row):
        # 열 반복문
        for j in xrange(n_column):
            result[i][j] = 0.0
            # dummy index
            for k in xrange(n_dummy):
                result[i][j] += A[i][k] * B[k][j]

    return result


def main():
    a_vector = [1.0, 0.0]
    b_vector = [3.0, 4.0]
    a_dot_b = dot(a_vector, b_vector)

    print "a =", a_vector
    print "b =", b_vector
    print "a dot b =", a_dot_b

    A_matrix = [[0.0, 1.0],
                [1.0, 0.0]]
    x_vector = [3.0, 4.0]
    A_x = multiply_matrix_vector(A_matrix, x_vector)

    print "A =", A_matrix
    print "x =", x_vector
    print "A*x =", A_x

    B_matrix = [[100, 101],
                [110, 111]]

    print "A =", A_matrix
    print "B =", B_matrix
    print "A*B =", multiply_matrix_matrix(A_matrix, B_matrix)


if "__main__" == __name__:
    main()
