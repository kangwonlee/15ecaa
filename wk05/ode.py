from math import sin, cos, atan, pi, sqrt, exp


def fwd_euler(f, x0, ti, te, deltaT):
    """
    Forward Euler Method for Ordinary Differential Equations

    Assume slope is constant between t[k] and t[k+1]

    Parameters
    ----------
    f: dx/dt = f(x, t)
    x0: initial state
    ti: initial time
    te: final time
    deltaT: time step

    Returns
    -------
    listT: 1-dimensional list of time at each time step
    listX: 2-dimensional list of state x at each time step
    """
    # number of time steps
    mTimeStep = int((te-ti) * 1.0 / deltaT)

    # number of states == length of initial state vector
    nStates = len(x0)

    # tuple of time step index
    #   0, 1, ...., mTimeStep-1
    listK = tuple(range(mTimeStep))
    # tuple of time step
    #   because time step will be constant,
    #   define as a tuple instead of a list
    listT = tuple(([ti + deltaT*i for i in listK]))
    # if ti, te, deltaT are given as 0.0, 1.0, 0.1
    #   then mTimeStep wil be 10
    #   and listT will be [0:0.1:0.9];
    #       len(listT) == 10

    # pre-allocate memory space
    #   to store state vector of each time step
    listX = [tuple(x0)]     # init x buffer

    # allocation loop
    #   at k = 0, x is x0
    #   at k = [1, 2, ..., n-1] x is not known
    #       so use [0.0] * nStates
    for k in listT[1:]:
        listX.append([0.0] * nStates)
    # end allocation loop
    # now 2d array of mTimeStep x nStates prepared

    xk = x0

    # time step loop
    for k in listK[:-1]:
        # derivatives are currently time step
        sk = f(xk, listT[k])

        # next step x
        xk1 = listX[k+1]

        # state loop
        for i in xrange(nStates):
            # apply forward Euler method
            xk1[i] = xk[i] + sk[i]*deltaT
        # end state loop at time step k

        # update xk to next step
        xk = xk1
    # end time step loop

    return listT, listX
# end function fwd_euler()


def mod_euler(f, x_init, t_start, t_end, delta_t):
    """
    Modified Euler Method Solver
    Usage: listT, listX = mod_euler(f, x_init, t_start, t_end, delta_t)

    Assume slope changes linearly between t[k] and t[k+1]

    Parameters
    ----------
    f : callable(x, t)
        Computes the derivatives of x at (x, t)
        dx/dt = f(x, t)
        Returns a list of [x0, x1, ... ]
    x_init : list or tuple
         initial state of x
    t_start : float
        Initial time
    t_end : float
        Ending time
    deltaT : float
        Sampling time
    delta_t: time step
    Returns
    -------
    t_list : list, shape(int(te-ti)/deltaT + 1,1)
    x_list : list, shape(int(te-ti)/deltaT + 1,len(x_init))

    Examples
    --------
    >>> lT, lX = mod_euler(lambda x, t:[(math.sin(math.pi*t) - x[0])*0.5],[0],0.0, 0.5, 0.1)
    >>> print lT
    [0.0, 0.10000000000000001, 0.20000000000000001, 0.30000000000000004, 0.40000000000000002, 0.5]
    >>> print lX
    [[0], [0.0077254248593736849], [0.029382595321196046], [0.062135518400607666], [0.10209697840236187], [0.14470734296725662]]
    """
    x_list = [tuple(x_init)]    # init x buffer
    t_list = [t_start]

    tk = t_start
    tk1 = tk + delta_t

    # to make t_end the last element of t_list
    t_end += ((-0.5) * delta_t)

    # time step loop
    while tk < t_end:
        xk = x_list[-1]

        # step 1 : same as forward Euler
        sk = f(xk, tk)
        xk1_p = [(x + sk[i]*delta_t) for i, x in enumerate(xk)]

        # step 2 : calculate slope at (xk + f(xk, tk) * delta_t, tk + delta_t)
        sk1_p = f(xk1_p, tk1)

        # step 3 : average of f(xk, tk) and f(xk + f(xk, tk) * delta_t, tk + delta_t)
        sk_c = [(0.5*(s+sk1_p[i])) for (i, s) in enumerate(sk)]

        # step 4 : go forward using averaged slope
        xk1_c = [(x + sk_c[i] * delta_t) for i, x in enumerate(xk)]

        x_list.append(xk1_c)

        # time advance
        tk += delta_t
        tk1 += delta_t

        # append time
        t_list.append(tk)

    return t_list, x_list


def runge_while (f, x_init, t_init, t_end, delta_t):
    """
    Runge Method Solver
    Usage: listT, listX = runge_while(f, x_init, t_init, t_end, delta_t)

    Calculate four slopes and take weighted average

    Parameters
    ----------
    f : callable(x, t)
        Computes the derivatives of x at 0.
        Returns a list of [x_init, x1, ... ]
    x_init : list or tuple
        Initial state of x
    t_init : float
        Initial time
    t_end : float
        Ending time
    delta_t : float
        Sampling time

    Returns
    -------
    t_list : list, shape(int(te-ti)/deltaT + 1,1)
    x_list : list, shape(int(te-ti)/deltaT + 1,len(x_init))


    Examples
    --------
    >>> lT, lX = runge_while(lambda x, t:[(math.sin(math.pi*t) - x[0])*0.5],[0],0.0, 0.5, 0.1)
    >>> print lT
    [0.0, 0.10000000000000001, 0.20000000000000001, 0.30000000000000004, 0.40000000000000002, 0.5]
    >>> print lX
    [[0], [0.0076608912592762328], [0.029394418941171337], [0.062350250267466614], [0.10261479161461737], [0.14559255884915154]]
    """

    listX = [x_init]    # init x buffer
    listT = [t_init]

    deltaThalf = 0.5 * delta_t
    deltaTsixth = delta_t/6.0

    tk = t_init
    tk_half = tk + 0.5 * delta_t
    tk1 = tk + delta_t

    # to make t_end the last element of t_list
    t_end += (deltaThalf)

    # time step loop
    while tk < t_end:
        xk = listX[-1]

        # step 1
        k1 = f(xk, tk)

        # step 2
        xk1_p = [(xk[i] + k*deltaThalf) for (i, k) in enumerate(k1)]
        k2 = f(xk1_p, tk_half)

        # step 3
        xk2_p = [(xk[i] + k*deltaThalf) for (i, k) in enumerate(k2)]
        k3 = f(xk2_p, tk_half)

        # step 4
        xk3_p = [(xk[i] + k * delta_t) for (i, k) in enumerate(k3)]
        k4 = f(xk3_p, tk1)

        # step 5
        xk1_c = [x + deltaTsixth*(k1[i] + 2*(k2[i] + k3[i]) + k4[i]) for (i, x) in enumerate(xk)]

        listX.append(xk1_c)
        tk += delta_t
        tk_half += delta_t
        tk1 += delta_t
        listT.append(tk)

    return listT, listX


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
    xk: state vector at time step k
        xk[0] = x
        xk[1] = xdot

    Returns
    -------
    ydot : list of derivatives
    """
    # step input
    u = 1

    y1, y2 = xk[0], xk[1]

    y1dot = y2
    y2dot = (u - (k*y1 + c*y2))/m

    return (y1dot, y2dot)
# end of function func()


def exact(t):
    """
    Exact solution of a  1-DOF mechanical vibration
    Ref : Rao, Mechanical Vibration, 2nd ed,
        ISBN 0-201-55693-6, Example 4.3
    """
    # step input
    u = 1
    # natural frequency (rad/sec)
    wn = sqrt(k/m)
    # damping ratio
    zeta = c/(2.0 * m * wn)

    s = sqrt(1.0 - zeta * zeta)
    s1 = 1.0 / s

    # damped frequency (rad/sec)
    wd = wn * s
    # phase (rad)
    phi = atan(zeta * s)

    y1 = (u/k) * (1.0 - s1 * exp(-zeta * wn * t) * cos(wd*t-phi))

    return (y1)
# end of function exact()


if "__main__" == __name__:
    help(fwd_euler)

    ti = 0.0
    te = 2.0
    delta_T = 0.01
    x0 = (0.0, 0.0)
    vT, vX = fwd_euler(func, x0, ti, te, delta_T)
    t_list_mod_euler, x_list_mod_euler = mod_euler(func, x0, ti, te, delta_T)
    t_list_runge, x_list_runge = runge_while(func, x0, ti, te, delta_T)

    delta_T = 0.001
    vT01, vX01 = fwd_euler(func, x0, ti, te, delta_T)

    # exact solution
    vXexact = tuple([exact(tk) for tk in vT])

    import pylab
    pylab.plot(vT, vX, 'b', label='fwd Euler(0.01)')
    pylab.plot(vT01, vX01, 'g', label='fwd Euler(0.001)')
    pylab.plot(t_list_mod_euler, x_list_mod_euler, '*',label='Modified Euler(0.01)')
    pylab.plot(t_list_runge, x_list_runge, 'x-', label='Runge(0.01)')
    pylab.plot(vT, vXexact, 'ko-', label='exact')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('x')
    pylab.xlabel('t')
    pylab.show()

    vP, vV = zip(*vX)
    vP01, vV01 = zip(*vX)
    p_list_mod_euler, v_list_mod_euler = zip(*x_list_mod_euler)
    p_list_runge, v_list_runge = zip(*x_list_runge)

    pylab.plot(vP,vV, label='fwd Euler (0.01)')
    pylab.plot(vP01, vV01, label='fwd Euler(0.001)')
    pylab.plot(p_list_mod_euler, v_list_mod_euler, label='Modified Euler(0.01)')
    pylab.plot(p_list_runge, v_list_runge, label='Runge(0.01)')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('xdot')
    pylab.xlabel('x')
    pylab.show()
