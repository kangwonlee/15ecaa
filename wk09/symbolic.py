# -*- coding: cp949 -*-
from sympy import *
a = Rational(1, 2)
print "a =", a

print "pi**2 =", pi**2

print "pi.evalf() =", pi.evalf()

print "pi + exp(1) =", pi + exp(1)

print "(pi + exp(1)).evalf() =", (pi + exp(1)).evalf()

print "oo =", oo

print "oo > 99999 =", oo > 99999

print "sqrt(2) =", sqrt(2).evalf(100)

print "1/2 + 1/3 =", Rational(1, 2) + Rational(1, 3)

F, r, sigma_max, sf = symbols('F r sigma_max safety_factor')

area = pi * r * r
sigma = F / area
solution = solve([sigma - sigma_max/sf], r)
print "solution =", simplify(solution)

