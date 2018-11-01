import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import optimize

# Changing plotting parameters to bigger values for readable large plots
import matplotlib as mpl
mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['axes.titlesize'] = 22
mpl.rcParams['axes.labelsize'] = 18
mpl.rcParams['axes.formatter.limits'] = -5, 5
mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.major.width'] = 1.4
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.major.width'] = 1.4
mpl.rcParams['ytick.labelsize'] = 16


class Solver(object):
    """
    Class to solve the equations using scipy's odeint function
    """
    def __init__(self, qlist, m, x):
        """
        Initialize with the input paramters to set the polytropic index and the
        values in xilist
        """
        self.m = m
        self.x = x
        self.qlist = qlist

        self.msq = m*m
        self.xsq = x*x

    def derivs(self, param, q):
        """
        Figures out the derivatives of theta and phi for the current values of
        theta, phi and xi. Theta and phi come in as a list under the name param
        """
        mqx = self.m * self.x * q
        lam, P, Q = param  # lam is the first parameter, P second, Q third
        Pprime = ( (q**2*self.msq - 1)*Q + (mqx)*P ) / (1-self.xsq)
        Qprime = (lam - self.msq/(1-self.xsq))*P - (mqx/(1-self.xsq))*Q
        lamprime = 0
        return [lamprime, Pprime, Qprime]

#    def analytical_solver(self):
#        """
#        Calculates the analytical solution. Works if n=0 or n=1
#        """
#        if self.index==0:
#            thetalist = np.copy(self.qlist)  # To get the theta/xi lists to align perfectly
#            for i in range(len(thetalist)):
#                thetalist[i] = (1-(thetalist[i]**2)/6.)
#            return thetalist
#        elif self.index==1:
#            thetalist = np.copy(self.qlist)
#            for i in range(len(thetalist)):
#                thetalist[i] = np.sin(thetalist[i])/thetalist[i]
#            return thetalist
#        else:
#            return "No analytical solution given"

    def numerical_solver(self, param):
        """
        Runs the odeint function for the given input parameters
        param are the initial conditions
        """
        # theta is the first parameter, phi the second
        return odeint(self.derivs, param, self.qlist)


def density_compare(qlist, inid_cond):
    poly_index = [0., 1., 1.5, 2., 3., 4.]  # Values for the polytropic index
    for index in poly_index:
        func = Solver(qlist, index)  # Create Solver class
        solved = func.numerical_solver(init_cond)
        theta_list = solved[:,0]
        plt.plot(qlist, theta_list**index, label=index, lw=3)

    plt.ylim(0, 1.25)
    plt.xlim(0, max(qlist))
    plt.legend(fontsize=14, frameon=True, fancybox=True, edgecolor="#005500")
    plt.title("Densities for different polytropic indices")
    plt.xlabel(u"Values of x")
    plt.ylabel(u"Densities ($\u03B8^{n}$)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Initial values/boundary conditions
    start = -10.
    end = 10.
    steps = 1e5
    init_cond = [10, 1, 0]  # lam=0, P=1, Q=0 initial conditions
    qlist = np.linspace(start, end, steps)  # Values of q - from -10 to 10

    lam = 0 # Wouldnt I want to rootfind on lam at the same time as solving the ODE?
    func = Solver(qlist, -2, 0)  # Create Solver class (qlist, m, x, lam)

    # Unsure what to do in this setup; do a rootfinder for lambda for **every**
    # value in qlist? and then plot those against each other?
    # And then do that for all different kinds of x (=mu)??
    # So rootfind to lambda for an entire matrix of q&x?

    solved = func.numerical_solver(init_cond)
    print solved[:,0]
#    P_list = solved[:,0]
#    plt.plot(qlist, P_list, lw=3)

##    plt.ylim(0, 1.25)
#    plt.xlim(0, max(qlist))
#    plt.legend(fontsize=14, frameon=True, fancybox=True, edgecolor="#005500")
#    plt.title("Densities for different polytropic indices")
#    plt.xlabel(u"Values of x")
#    plt.ylabel(u"Densities ($\u03B8^{n}$)")
#    plt.grid(True)
#    plt.show()


#    density_compare(qlist, init_cond)
