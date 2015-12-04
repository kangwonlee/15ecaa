# -*- coding: cp949 -*-
from sympy import *

print '''2.10.1.1'''
a = Rational(1, 2)
print "a =", a

print "pi**2 =", pi ** 2

print "pi.evalf() =", pi.evalf()

print "pi + exp(1) =", pi + exp(1)

print "(pi + exp(1)).evalf() =", (pi + exp(1)).evalf()

print "oo =", oo

print "oo > 99999 =", oo > 99999

print '''2.10.1.2'''
print "sqrt(2) =", sqrt(2).evalf(100)

print "1/2 + 1/3 =", Rational(1, 2) + Rational(1, 3)

F, r, sigma_max, sf = symbols('F r sigma_max safety_factor')

area = pi * r * r
sigma = F / area
solution = solve([sigma - sigma_max / sf], r)
print "solution =", simplify(solution)

print '''2.10.1.3'''

x = Symbol('x')
y = Symbol('y')

print "x+y+x-y =", x + y + x - y

print "(x+y)**2 =", (x + y) ** 2

print '''2.10.2.1'''

print "expand((x+y)**3) =", expand((x + y) ** 3)

print "expand(x+y, complex=True) =", expand(x + y, complex=True)

print "expand(cos(x+y), trig=True) =", expand(cos(x + y), trig=True)

print '''2.10.2.2'''

print "simplify((x+x*y)/x) =", simplify((x + x * y) / x)

print '''2.10.3.1'''
print "limit(sin(x)/x,x,0) =", limit(sin(x) / x, x, 0)

print "limit(x,x,oo) =", limit(x, x, oo)

print "limit(1/x,x,oo) =", limit(1 / x, x, oo)

print "limit(x**x,x,0) =", limit(x ** x, x, 0)

print '''2.10.3.2'''

print "diff(sin(x), x) =", diff(sin(x), x)

print "diff(sin(2*x), x) =", diff(sin(2 * x), x)

print "diff(tan(x), x) =", diff(tan(x), x)

print "limit((tan(x+y)-tan(x))/y,y,0) =", limit((tan(x + y) - tan(x)) / y, y, 0)

print "diff(sin(2*x), x, 1) =", diff(sin(2 * x), x, 1)

print "diff(sin(2*x), x, 2) =", diff(sin(2 * x), x, 2)

print "diff(sin(2*x), x, 3) =", diff(sin(2 * x), x, 3)

print '''2.10.3.3'''

print "series(cos(x), x) =", series(cos(x), x)

print "series(1/cos(x), x) =", series(1 / cos(x), x)

# Series 설명을 위하여 그래프를 그림
import pylab

x_deg = pylab.arange(-90, 90 + 1)
x_rad = pylab.deg2rad(x_deg)
y_cos = pylab.cos(x_rad)
y_series_1 = 1 * pylab.ones_like(x_rad)
y_series_2 = 1 - x_rad ** 2 / 2
y_series_3 = 1 - x_rad ** 2 / 2 + x_rad ** 4 / 24

pylab.plot(x_deg, y_cos, label='cos')
pylab.plot(x_deg, y_series_1, label='series 1')
pylab.plot(x_deg, y_series_2, label='series 2')
pylab.plot(x_deg, y_series_3, label='series 3')
pylab.grid()
pylab.legend(loc=0)
# pylab.show()

print '''2.10.3.5'''
print "integrate(6*x**5, x) =", integrate(6 * x ** 5, x)

print "integrate(sin(x), x) =", integrate(sin(x), x)

print "integrate(log(x), x) =", integrate(log(x), x)

print "integrate(2*x + sinh(x), x) =", integrate(2 * x + sinh(x), x)

print "integrate(exp(-x**2)*erf(x), x) =", integrate(exp(-x ** 2) * erf(x), x)

print "integrate(x**3, (x, -1, 1)) =", integrate(x ** 3, (x, -1, 1))

print "integrate(sin(x), (x, 0, pi/2)) =", integrate(sin(x), (x, 0, pi / 2))

print "integrate(cos(x), (x, -pi/2, pi/2)) =", integrate(cos(x), (x, -pi / 2, pi / 2))

print "integrate(exp(-x), (x, 0, oo)) =", integrate(exp(-x), (x, 0, oo))

print "integrate(exp(-x**2), (x, -oo, oo)) =", integrate(exp(-x ** 2), (x, -oo, oo))

print '''2.10.4'''
print "solve(x**4 - 1, x) =", solve(x ** 4 - 1, x)

print "solve([x + 5*y - 2, -3*x + 6*y - 15], [x,y]) =", solve([x + 5 * y - 2, -3 * x + 6 * y - 15], [x, y])

print "solve(exp(x) + 1, x) =", solve(exp(x) + 1, x)

f = x ** 4 - 3 * x ** 2 + 1
print "factor(f) =", factor(f)

print "factor(f, modulus=5) =", factor(f, modulus=5)

print "satisfiable(x&y) =", satisfiable(x & y)
print "satisfiable(x^y) =", satisfiable(x ^ y)

print '''2.10.5.1'''
print "Matrix([[1,0], [0,1]]) =", Matrix([[1, 0], [0, 1]])
A = Matrix([[1, x], [y, 1]])
print "A =", A
print "A**2 =", A ** 2

print '''2.10.5.2'''
f = Function('f')
print "f(x).diff(x, x) + f(x) =", f(x).diff(x, x) + f(x)
print "dsolve(f(x).diff(x, x) + f(x)) =", dsolve(f(x).diff(x, x) + f(x))

m, c, k, t = symbols('m c k t')
x = Function('x')
vib_eq = m * x(t).diff(t, t) + c * x(t).diff(t) + k * x(t)
result = dsolve(vib_eq)
print "dsolve() result"
print result

forced_vib_eq = m * x(t).diff(t, t) + c * x(t).diff(t) + k * x(t) - sin(t)
result = dsolve(forced_vib_eq)
print "forced vibration result:"
print result
