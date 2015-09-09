# -*- coding: cp949 -*-
import sequential

print dir(sequential)

def func(x):
    return 1.0 * x * x - 3.0
# end of func()
# inspired by Scratch example


print sequential.sequential(func, 0.01)

