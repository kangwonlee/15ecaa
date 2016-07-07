# -*- coding: cp949 -*-
"""
1���� �������� ��
� (����) �Լ� f(x) ���� 0 �� �ǵ��� ����� x �� ã��
"""

# ��ǻ���� �޸𸮿��� ������ ���ѵ� �ڸ����� 2������ ������ �� ����
# �Ǽ��� �����Ϸ��� ������ �߻��ϰ� ��
# epsilon �� ��� �Ǵ� ���� ������ �ǹ���
# |x| < epsilon == (x = 0)
# |x - y| < epsilon == (x == y)
epsilon = 1e-4


def sequential(f, x0, delta_x=1e-6, epsilon=epsilon):
    """
    sequential method
    x0 �� ���� �����ؼ�  delta_x ��ŭ�� ������Ű�鼭 |f(x)| ���� epsilon �� ���� �۾������� ������
    :param f: f(x) = 0 �� x�� ã���� �ϴ� �Լ�
    :param x0: x�� �ʱⰪ
    :param delta_x: x�� �ѹ��� delta_x ��ŭ�� ������Ŵ
    :param epsilon: ���� ��� ����

    :return: |f(x)| < epsilon �� x
    """
    # � ������ �Է°��� ������ �� �� ������
    # xi �� �ʱⰪ�� (�ε��Ҽ���) �Ǽ��� �Ǿ�� �ϹǷ�
    # float() �� �̿�
    xi = float(x0)
    # delta_x �� �ǹ̴�
    # "���� ���� ã�� ������ �� xi�� �󸶸�ŭ ������ų ���ΰ�"

    # counter �� �Ʒ� ���� �ݺ����� ������ Ƚ��
    counter = 0

    # ���� �ݺ���
    while True:
        # f(x)
        fi = f(xi)
        # |f(x)| < epsilon �̸�
        if abs(fi) < epsilon:
            # ���� �ݺ����� �ߴ�
            break
        # �׷��� ������
        # x �� delta_x ��ŭ ������Ŵ
        xi += delta_x
        # �ݺ����� �ѹ� ���� �Ǿ����Ƿ� counter �� 1 ���� ��Ŵ
        counter += 1

    # �ݺ����� ����� Ƚ���� ǥ��
    print "seq_counter =", counter

    # �ݺ������� ã�� ����� ��ȯ
    return xi
# end of sequential()


def bisection(f, xl, xh, epsilon=epsilon, b_verbose=False):
    """
    bisection method
    f(xl) �� f(xh)�� ��ȣ�� �ݴ��� xl, xh ���� ����
    xl ~ xh ������ ������ ���� ������ xn�� ã��
    f(xl) �� f(xn) �� ��ȣ�� �ݴ��̸� xh�� xn ���� �ű�
        �̷��� �ϸ� ��� f(xl) �� f(xh)�� ��ȣ�� �ݴ���
    �׷��� ������ xl�� xn���� �ű�
        f(xn) �� f(xh)�� ��ȣ�� �ݴ��� ����

    xl ~ xh ������ ������ ���̰� epsilon ���� �۾����� �ߴ�

    :param f: f(x) = 0 �� x�� ã���� �ϴ� �Լ�
    :param xl: x�� �ʱⰪ xl < xh && f(xl) f(xh) < 0
    :param xh: x�� �ʱⰪ xl < xh && f(xl) f(xh) < 0
    :param epsilon: ���� ��� ����
    :param b_verbose: �߰� ���� ǥ��. ���� ���� ������ False
    :return: f(x) == 0 �� x �� ����� ��
    """

    # � ������ �Է°��� ������ �� �� ������
    # xi �� �ʱⰪ�� (�ε��Ҽ���) �Ǽ��� �Ǿ�� �ϹǷ�
    # float() �� �̿�
    xl = float(xl)
    xh = float(xh)

    # xn �� �ʱ�ȭ �Ѵ�
    xn = xl

    # counter �� �Ʒ� ���� �ݺ����� ������ Ƚ��
    counter = 0

    # ���� �ݺ���
    while True:
        # xl ~ xh ������ ��� ������ xn ���� ��´�
        xn = 0.5 * (xl + xh)

        # f(xn) �� f(xh)�� ��ȣ�� ��
        if f(xn) * f(xh) < 0:
            # �ٸ��� : ���� xn ~ xh ���̿� ����. xl �� xn �� ����
            xl = xn
        else:
            # ������ : ���� xl ~ xn ���̿� ����. xh �� xn �� ����
            xh = xn

        # �ݺ����� �ѹ� ���� �Ǿ����Ƿ� counter �� 1 ���� ��Ŵ
        counter += 1

        if b_verbose:
            # �߰� ������ ǥ��
            print ("xl = %8f f(xl) = %+8f xn = %+8f f(xn) = %+8f xh = %+8f f(xh) = %8f |xh-xl| = %-8f" % (
                xl, f(xl), xn, f(xn), xh, f(xh), abs(xh - xl)))

        # xl ~ xh ������ ���̰� epsilon ���� ª���� ���� �ݺ����� �ߴ�
        if abs(xh - xl) < epsilon:
            break

    if b_verbose:
        # counter �� ǥ��
        print "bis_counter =", counter

    # xn �� ��ȯ
    return xn
# end of bisection()


def newton(f, df, x0, epsilon=epsilon, b_verbose=False):
    """
    Newton Raphson method
    ���� �Լ��� f(x) �� xi ���������� ������ �������� ���� ����

    xi ���������� f(x)�� ���Ⱑ di, �Լ����� fi �̸�
    ������ ������ di (x - xi) + fi �� x = xi - fi/di �̸� 0�� ��
    ��, ������ �������� ���� xi - fi/di �̰� ���� xi �κ��� (- fi/di) ��ġ�� ����
    �̸� �̿��Ͽ� i + 1  ��° x �� xi - fi/di�� ����

    f(x) �� xi ������ ���� di �� ���밪�� 0�� ����� ��� xi �� ���� �ſ� �� ��ġ�� xi�� �ڸ��ϰ� ��
    ���ο� ��ġ���� |f(x)| ���� epsilon �� ���� �۾����� �ߴ�
    �׷��� ������ ������ �������� ���� �ٽ� ����

    :param f: f(x) = 0 �� �����ϴ� x �� ã���� �ϴ� �Լ�
    :param df: f(x) �� �̺�
    :param x0: x�� �ʱⰪ
    :param epsilon: ���� ��� �ѵ�
    :param b_verbose: �߰� ���� ǥ��. ���� ���� ������ False
    :return: |f(x)| < epsilon �� x
    """
    # xi �� (�ε��Ҽ���) �Ǽ��� �ʱ�ȭ
    xi = float(x0)

    # counter �� �Ʒ� ���� �ݺ����� ������ Ƚ��
    counter = 0

    # ���� �ݺ���
    while True:
        # xi ������ �Լ���
        fi = f(xi)

        # �ݺ����� �ѹ� ���� �Ǿ����Ƿ� counter �� 1 ���� ��Ŵ
        counter += 1

        # |f(x)| < epsilon �̸�
        if abs(fi) < epsilon:
            # ���� �ݺ����� �ߴ�
            break
        # �׷��� ������
        else:
            # xi �� (-fi / df(xi) �� ����
            xi += (-fi / df(xi))

    if b_verbose:
        # counter �� ǥ��
        print("nr_counter = %d" % counter)

    # xi �� ��ȯ
    return xi


# end of newton


def func(x):
    return 1.0 * x * x - 2.0


# end of func()
# inspired by Scratch example


def dfunc(x):
    return 2.0 * x


# end of dfunc()
# for later use

if "__main__" == __name__:
    # initial value
    x0 = "0.01"

    x_seq = sequential(func, x0)
    print "x_seq =", x_seq
    print "f(x_seq) =", func(x_seq)

    x_bis = bisection(func, 0.01, 2.0, b_verbose=True)
    print "x_bis =", x_bis
    print "f(x_bis) =", func(x_bis)

    x_nr = newton(func, dfunc, 2.0)
    print "x_nr =", x_nr
    print "f(x_nr) =", func(x_nr)

    print "error   seq         bis        nr"
    print "        %7g %7g %7g" % (abs(2.0 ** 0.5 - x_seq), abs(2.0 ** 0.5 - x_bis), abs(2.0 ** 0.5 - x_nr))
