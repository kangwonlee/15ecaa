from math import cos, atan, sqrt, exp


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
    # How can you know if this makes the program run faster?

    # init x buffer
    list_x = [tuple(x0)]

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
# end function bwd_euler()


def mod_euler(f, x0, ti, te, deltaT):
    """

    Modified Euler Method for Ordinary Differential Equations

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
    # How can you know if this makes the program run faster?

    # init x buffer
    list_x = [tuple(x0)]

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

        # go one step forward
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
# end function bwd_euler()


# it is more than a good idea to indicate the unit of a variable
tau_sec = 0.5
m_kg = 10.0
c_N_p_mps = 100.0
k_Npm = 1000.0


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
    u_N = 1

    y1 = xk[0]
    y2 = xk[1]

    y1dot = y2
    y2dot = (u_N - (k_Npm*y1 + c_N_p_mps*y2))/m_kg

    return y1dot, y2dot
# end function func()


def exact(t):
    """
    Exact solution of a 1-DOF mechanical vibration
    Ref: Rao, Mechanical Vibration, 2nd ed,
        ISBN 0-201-55693-6, Example 4.3
    """
    # step input
    u_N = 1
    # natural frequency (rad/sec)
    wn_rad_per_sec = (k_Npm / m_kg)**0.5
    # damping ratio
    zeta = c_N_p_mps / (2.0 * m_kg * wn_rad_per_sec)

    s = sqrt(1.0 - zeta * zeta)
    s1 = 1.0 / s

    # damped frequency (rad/sec)
    wd_rad_per_sec = wn_rad_per_sec * s
    # phase (rad)
    phi_rad = atan(zeta * s)

    y1 = (u_N / k_Npm) * (1.0 - s1 * exp(-zeta * wn_rad_per_sec * t) * cos(wd_rad_per_sec * t - phi_rad))

    return y1
# end function exact()


if "__main__" == __name__:
    help(fwd_euler)
    ti_sec = 0.0
    te_sec = 2.0
    delta_t_sec = 0.01
    x0 = (0.0, 0.0)
    time_list_0_01_sec, x_list_fwd_euler_0_01 = fwd_euler(func, x0, ti_sec, te_sec, delta_t_sec)
    delta_t_sec = 0.001
    time_list_0_001_sec, x_list_fwd_euler_0_001 = fwd_euler(func, x0, ti_sec, te_sec, delta_t_sec)

    # exact solution
    list_x_exact_0_01 = tuple([exact(tk) for tk in time_list_0_01_sec])

    import pylab
    pylab.plot(time_list_0_01_sec, x_list_fwd_euler_0_01, label='fwd Euler (0.01)')
    pylab.plot(time_list_0_001_sec, x_list_fwd_euler_0_001, label='fwd Euler (0.001)')
    pylab.plot(time_list_0_01_sec, list_x_exact_0_01, 'k', label='exact')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('x')
    pylab.xlabel('t')
    pylab.show()

    vP, vV = zip(*x_list_fwd_euler_0_01)
    vP01, vV01 = zip(*x_list_fwd_euler_0_001)

    pylab.plot(vP, vV, label='fwd Euler (0.01)')
    pylab.plot(vP01, vV01, label='fwd Euler (0.001)')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('xdot')
    pylab.xlabel('x')
    pylab.show()
