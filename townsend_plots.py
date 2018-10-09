"""Bart van Baal, UvA, 10615989
Very basic script to reproduce Figure 1. from Townsend 2003,
"Asymptotic expressions for the angular dependence of low-frequency pulsation
modes in rotating stars"
Copied the functions from F. Chambers' gnuplot code (which I cannot run since
my shitty ass version of ubuntu no longer has the capability to install gnuplot)
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import numpy as np
import pandas as pd
import copy
import random
import os


l_eq_38 = lambda m, s, q : (q**2) * ((2.*s + 1.)**2)
l_eq_39 = lambda m, s, q : ( (m*q - m**2) / (q * 2.*s + 1.) )**2

l_eq_40_41 = lambda m, q : (q - m)**2

l_eq_55 = lambda m, q : (m**2) * 2.*m*q / (2*m*q + 1.)


## q > condition statement (eg q>1 for g_mode)
g_mode_cond = np.abs(1)
r_mode_cond = lambda m, s : ((2.*s + 1.)**2 + m**2) / np.abs(m)  # paper error in 2s+1 term
k_mode_cond = lambda m : np.abs(3. / m)
#y_mode_cond = lambda m, q : (m*q < m**2 and m*q > 0) ? r_mode_cond(m, 0) : g_mode_cond

#l_l = lambda lam, lim, q : q < -lim ? lam : 1/0
#l_r = lambda lam, lim, q : q > lim ? lam : 1/0


m = -2
x = np.linspace(-10, 10, 10000)
left = np.linspace(-10, -1, 10000)
right = np.linspace(1, 10, 10000)

test_38_s1_l = l_eq_38(m, 1, left)
test_38_s1_r = l_eq_38(m, 1, right)
test_40_s0_l = l_eq_40_41(m, left[left < -2.5])
test_40_s0_r = l_eq_40_41(m, right)

test_55_s1_r = l_eq_55(m, right)
test_38_s3_l = l_eq_38(m, 3, left)
test_38_s2_l = l_eq_38(m, 2, left)
test_39_s1_l = l_eq_39(m, 1, left[left < -6.])


plt.plot(left, test_38_s1_l, color="blue", label="38, s=1")
plt.plot(right, test_38_s1_r, color="purple", label="38, s=1")
plt.plot(left[left < -2.5], test_40_s0_l, color="red", label="40")
plt.plot(right, test_40_s0_r, color="green", label= "40")
plt.plot(right, test_55_s1_r, color="cyan", label="55")
plt.plot(left, test_38_s3_l, color="orange", label="38, s=3")
plt.plot(left, test_38_s2_l, color="yellow", label="38, s=2")
plt.plot(left[left < -6.], test_39_s1_l, color="black", label="39, s=1")
plt.yscale('log')
plt.legend(fontsize=16, frameon=True, fancybox=True, edgecolor="#000066")
plt.xlim([-10, 10])
plt.show()
