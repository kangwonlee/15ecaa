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


def main():
    a_vector = [1.0, 0.0]
    b_vector = [3.0, 4.0]
    a_dot_b = dot(a_vector, b_vector)

    print "a =", a_vector
    print "b =", b_vector
    print "a dot b =", a_dot_b


if "__main__" == __name__:
    main()