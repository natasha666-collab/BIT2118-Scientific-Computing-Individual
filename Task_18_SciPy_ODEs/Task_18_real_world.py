import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Campus emergency indicator capacitor discharge

V0 = 5.0
R = 2000.0
C = 0.001

# Capacitor discharge differential equation
def capacitor_discharge(t, V):
    return [-V[0] / (R * C)]

# Time values
t_eval = np.linspace(0, 5, 200)

# Solve using SciPy
solution = solve_ivp(
    capacitor_discharge,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact solution for comparison
exact = V0 * np.exp(-solution.t / (R * C))

# Calculate maximum error
error = np.max(np.abs(solution.y[0] - exact))

print("Campus Emergency Indicator - Capacitor Discharge")
print("Solver success:", solution.success)
print(f"Initial capacitor voltage: {V0:.2f} V")
print(f"Capacitor voltage after 5 s: {solution.y[0, -1]:.4f} V")
print(f"Maximum error against exact solution: {error:.3e} V")

# Plot results
plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, "--", label="Exact solution")
plt.xlabel("Time (seconds)")
plt.ylabel("Capacitor voltage (V)")
plt.title("Emergency Indicator Capacitor Discharge")
plt.legend()
plt.grid(True)
plt.show()
