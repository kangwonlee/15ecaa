from math import sin, cos, atan, pi, sqrt, exp


def fwd_euler(f, x0, ti, te, deltaT):
    """

    Forward Euler Method for Ordinary Differential Equations

    Assume slope is constant between t[k] and t[k+1]

    Parameters
    ----------
    f : dx/dt = f(x, t)
    x0 : initial state
    ti : initial time
    te : final time
    deltaT : time step

    Returns
    -------
    listT: 1-dimensional list of time at each time step
    listX: 2-dimensional list of state x at each time step
    """
    # number of time steps
    n_time_steps = int((te - ti) * 1.0 / deltaT)

    # number of states == length of initial state vector
    n_states = len(x0)

    # tuple of time step index
    #   0, 1, ..., mTimeStep - 1
    list_k = tuple(range(n_time_steps))
    # tuple of time step
    #   because time step will be constant,
    #   define as a tuple instead of a list
    list_t = tuple([ti + deltaT*i for i in list_k])
    # if ti, te, deltaT are given as 0.0, 1.0, 0.1
    #   then mTimeStep will be 10
    #   and listT will be [0:0.1:0.9];
    #       len (listT) == 10

    # pre-allocate memory space
    #   to store state vector of each time step
    list_x = [tuple(x0)]    # init x buffer

    # allocation loop
    #   at k = 0, x is x0
    #   at k = [1, 2, ..., n-1], x is not know
    #       so use [0.0] * nStates
    for k in list_t[1:]:
        list_x.append([0.0] * n_states)
    # end allocation loop
    # now 2d array of mTimeStep x nStates prepared

    xk = x0

    # time step loop
    for k in list_k[:-1]:
        # derivatives at current time step
        sk = f(xk, list_t[k])

        # next step x
        xk1 = list_x[k+1]

        # state loop
        for i in xrange(n_states):
            # apply forward Euler method
            xk1[i] = xk[i] + sk[i] * deltaT
        # end state loop at time step k

        # update xk to next step
        xk = xk1
    # end time step loop

    return list_t, list_x
# end function fwd_euler()


tau = 0.5
m = 10.0
c = 100.0
k = 1000.0


def func(xk, tk):
    """
    Differential equation

    m x2dot(t) + c xdot(t) + k x(t) = u(t)
    u(t) = 1

    Use m, c, k defined outside of this function

    Parameters
    ----------
    xk : state vector at time step k
         xk[0] = x
         xk[1] = xdot
    tk : time at time step k

    Returns
    -------
    xdot : list of derivatives
    """
    # step input
    u = 1

    y1 = xk[0]
    y2 = xk[1]

    y1dot = y2
    y2dot = (u - (k*y1 + c*y2))/m

    return y1dot, y2dot
# end function func()


def exact(t):
    """
    Exact solution of a 1-DOF mechanical vibration
    Ref: Rao, Mechanical Vibration, 2nd ed,
        ISBN 0-201-55693-6, Example 4.3
    """
    # step input
    u = 1
    # natural frequency (rad/sec)
    wn = sqrt(k / m)
    # damping ratio
    zeta = c / (2.0 * m * wn)

    s = sqrt(1.0 - zeta * zeta)
    s1 = 1.0 / s

    # damped frequency (rad/sec)
    wd = wn * s
    # phase (rad)
    phi = atan(zeta * s )

    y1 = (u / k) * (1.0 - s1 * exp(-zeta * wn * t) * cos(wd * t - phi))

    return y1
# end function exact()


if "__main__" == __name__:
    help(fwd_euler)
    ti = 0.0
    te = 2.0
    delta_T = 0.01
    x0 = (0.0, 0.0)
    vT, vX = fwd_euler(func, x0, ti, te, delta_T)
    delta_T = 0.001
    vT01, vX01 = fwd_euler(func, x0, ti, te, delta_T)

    # exact solution
    list_x_exact = tuple([exact(tk) for tk in vT])

    import pylab
    pylab.plot(vT, vX, label='fwd Euler (0.01)')
    pylab.plot(vT01, vX01, label='fwd Euler (0.001)')
    pylab.plot(vT, list_x_exact, 'k', label='exact')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('x')
    pylab.xlabel('t')
    pylab.show()

    vP, vV = zip(*vX)
    vP01, vV01 = zip(*vX01)

    pylab.plot(vP, vV, label='fwd Euler (0.01)')
    pylab.plot(vP01, vV01, label='fwd Euler (0.001)')
    pylab.legend(loc = 0)
    pylab.grid(True)
    pylab.ylabel('xdot')
    pylab.xlabel('x')
    pylab.show()
