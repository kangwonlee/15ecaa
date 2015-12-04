# -*- coding: cp949 -*-
import root_finding

print dir(root_finding)


def func(x):
    return 1.0 * x * x - 3.0


# end of func()
# inspired by Scratch example


print root_finding.sequential(func, 0.01)
