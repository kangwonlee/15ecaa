import numpy as np
import pylab


def ode_slope_1state_interval(func, delta_t, delta_x, te, ti, x_max, x_min):
    time_list = np.arange(ti, te, delta_t)
    x_list = np.arange(x_min, x_max + 0.5 * delta_x, delta_x)
    ode_slope_1state(func, x_list, time_list)
    return time_list


def ode_slope_1state(func, x_list, time_list):
    """
    Plot field of arrows indicating derivatives of the state
    :param func:
    :param x_list:
    :param time_list:
    :return:
    """
    time_mesh, x_mesh = np.meshgrid(time_list, x_list)
    u_mesh = np.ones_like(x_mesh)
    v_mesh = func(x_mesh, time_mesh)
    # magnitude as color
    color_mesh = np.sqrt(u_mesh * u_mesh + v_mesh * v_mesh)
    # 1
    pylab.figure()
    pylab.quiver(time_mesh, x_mesh, u_mesh, v_mesh, color_mesh, angles='xy')
    pylab.xlabel('t')
    pylab.ylabel('x')
    pylab.xlim((time_list[0] - (time_list[1] - time_list[0]) * 0.125, time_list[-1]))
    pylab.ylim((min(x_list) - (x_list[1] - x_list[0]) * 0.125,
                max(x_list) + (x_list[-1] - x_list[-2]) * 0.125))
    pylab.grid(True)


def ode_slopes_2states(func, radii_list, theta_deg_list, time_list):
    """
    Plot field of arrows indicating derivatives of the state
    :param func:
    :param radii_list:
    :param theta_deg_list:
    :param time_list:
    :return:
    """
    # to convert angle unit from degree to radian
    deg2rad = np.pi / 180
    # list of angles in radian
    theta_rad_list = tuple([(theta_deg * deg2rad) for theta_deg in theta_deg_list])
    # radii x angles mesh grid
    radii_mesh, theta_rad_mesh = np.meshgrid(radii_list, theta_rad_list)
    # polar coordinate to cartesian coordinate
    y = radii_mesh * np.cos(theta_rad_mesh), radii_mesh * np.sin(theta_rad_mesh)
    # derivatives of state at each point
    y_dot = func(y, time_list)
    # color
    color_mesh = np.sqrt(y_dot[0] * y_dot[0] + y_dot[1] * y_dot[1])
    # 1
    pylab.figure()
    pylab.quiver(y[0], y[1], y_dot[0], y_dot[1], color_mesh, angles='xy')
    l, r, b, t = pylab.axis()
    x_span, y2_mesh = r - l, t - b
    pylab.axis([l - 0.05 * x_span, r + 0.05 * x_span, b - 0.05 * y2_mesh, t + 0.05 * y2_mesh])
    pylab.axis('equal')
    pylab.grid()


if "__main__" == __name__:
    save_fig = True


    def main_1state(save_fig):
        # time constant
        tau = 1.0

        # intervals in time and space
        delta_t = 0.2
        delta_x = 0.5

        ti = 0.0
        te = 5.0

        x_min = -6.0
        x_max = 6.0

        # initial value of x(t) at t = 0
        x0 = 4.0
        # for exact solution
        tau_inverse = -1.0 / tau

        t_list = ode_slope_1state_interval(f_1state, delta_t, delta_x, te, ti, x_max, x_min)

        # exact solution
        x_exact_list = x0 * np.exp(tau_inverse * t_list)

        pylab.plot(t_list, x_exact_list, 'k')

        pylab.title(r'tau x_dot + x = 0')

        if save_fig:
            pylab.savefig("quiver_x_dot_x_0.png", dpi=300)
        else:
            pylab.show()


    def f_1state(x, t, tau=1.0, u=0.0):
        """
        Differential equation
        tau x_dot + x = u
        :param x: scalar float. value of x(t) at (t)
        :param t: scalar float
        :param tau: default argument. time constant. 1.0 by default
        :param u: input. 0.0 by default
        :return: x_dot scalar
        """
        return (-x + u) / tau


    main_1state(save_fig)

    #################################################################

    # m x_ddot + c x_dot + k x = 0
    # X = x
    # Y = x_dot

    # dX = x_dot = Y
    # dY = x_ddot = (c Y + k X) / (-m)


    # parameters for the differential equation
    m = 10.0
    c = 5.0
    k = 10.0


    def main_2states(save_fig):

        time_list = np.arange(0, 20, .01)
        y_exact_list = [exact_2states(t) for t in time_list]
        y_exact_list, y_dot_exact_list = list(zip(*y_exact_list))

        y_limit = 5

        # number of radii
        n_radii = 50

        # number of angles
        delta_angle_deg = 5

        # list of radii
        radii_list = np.arange(1.0 * y_limit / n_radii, y_limit, 1.0 * y_limit / n_radii)
        # list of angles in degree
        theta_deg_list = tuple(range(0, 360, delta_angle_deg))
        ode_slopes_2states(f_2states, radii_list, theta_deg_list, time_list)

        pylab.plot(y_exact_list, y_dot_exact_list, 'k')

        pylab.title(r'10 x_ddot + 5 x_dot + 10 x = 0')
        pylab.xlabel('x')
        pylab.ylabel('x_dot')
        if save_fig:
            pylab.savefig('quiver_2states.png', dpi=300)
        else:
            pylab.show()


    def f_2states(y, t):
        """
        Differential equation
        y_dot = f(y, t)

        need global variables m, c, k

        :param y: y0, y1
        :param t: time
        :return: y_dot
        """
        global m, c, k

        y1_dot = y[1]
        y2_dot = (c * y[1] + k * y[0]) / (-m)
        y_dot = (y1_dot, y2_dot)
        return y_dot


    def exact_2states(t):
        """
        The exact solution of a 2nd order differential equation
        :param t: time in sec
        :return: (y1, y2)
        """
        # 10 x_ddot + 5 x_dot + 10 x = 0, x(0) = 5, x_dot(0) = 0
        sqrt_15 = 15 ** 0.5
        wdt = sqrt_15 * t * 0.25
        y1 = ((sqrt_15 / 3.0) * np.sin(wdt)
              + 5.0 * np.cos(wdt)) * np.exp(-0.25 * t)
        y2 = -(1.0 + 1.0 / 3.0) * sqrt_15 * np.exp(-0.25 * t) * np.sin(wdt)
        return y1, y2


    main_2states(save_fig)
