import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(y, t):
    k = 0.3  # example parameter
    dydt = -k * y  # example differential equation
    return dydt

y0 = 5.0


t = np.linspace(0, 20, 100)  # from 0 to 20, with 100 points

# Solve
y = odeint(model, y0, t)

# Plot results 2D
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of the Differential Equation')
plt.grid(True)
plt.show()
