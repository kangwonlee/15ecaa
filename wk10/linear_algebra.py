# -*- coding: cp949 -*-
def dot(a, b):
    """
    ũ�Ⱑ ���� �� ���� a, b�� ���� dot product
    """
    # ���� a �� ũ��.
    # ���� b �� ũ��� ���� ���̶�� �����Ѵ�
    #   (� ��� ������ �߻��� �� �ִ°�?)
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