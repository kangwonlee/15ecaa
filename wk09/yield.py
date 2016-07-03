import math

# set path to root_finding.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.pardir, 'wk02')))
import root_finding


class Experiment(object):
    def __init__(self):
        self.force_N = 100.0
        self.safety_factor = 2.0
        self.stress_max_Pa = 207e6

    def problem_to_solve(self, radius_m):
        return circular_section_stress(radius_m, self.force_N) \
               - self.stress_max_Pa / self.safety_factor


def main():
    experiment = Experiment()

    experiment.force_N = float(raw_input("Enter force (N):"))

    x_l_init = root_finding.epsilon * 2
    x_h_init = 1.0
    result = root_finding.bisection(experiment.problem_to_solve, x_l_init, x_h_init, 1e-9)
    print "result =", result


def circular_section_stress(r_m, force_N):
    area_m2 = r_m * r_m * math.pi
    stress_Pa = force_N / area_m2
    return stress_Pa


if "__main__" == __name__:
    main()
