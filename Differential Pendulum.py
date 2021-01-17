'''
From 3Blue1Brown:

https://www.youtube.com/watch?v=p_di4Zn4wz4&t=1472s&ab_channel=3Blue1Brown

Solving for the swing of a pendulum
'''

import numpy as np

# Physical constants:
g = 9.8 # gravity
L = 2 # Length of the pendulum
mu = 0.1 # friction coeficient

THETA_0 = np.pi / 3 # 60 degrees
THETA_DOT_0 = 0 # Initial angular velocity
delta_t = 0.01 # Some time step

# Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)

# Solution to the differential equation:
def theta(t):
    theta = THETA_0
    theta_dot = THETA_DOT_0
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
    return print(f'Theta is {theta}')

theta(5)