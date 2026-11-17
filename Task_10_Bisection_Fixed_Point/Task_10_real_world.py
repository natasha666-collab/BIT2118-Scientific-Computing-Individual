import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Illustrative campus server workload model.
# Equilibrium occurs when f(L) = 0.

def workload_balance(L):
    return L - 40 - 12 * np.exp(-L / 30)

# Bisection method
bisection = root_scalar(
    workload_balance,
    bracket=[40, 60],
    method="bisect",
    xtol=1e-10
)

# Fixed-point iteration
def g(L):
    return 40 + 12 * np.exp(-L / 30)

L = 50.0
history = [L]

for _ in range(100):
    L_new = g(L)
    history.append(L_new)

    if abs(L_new - L) < 1e-10:
        break

    L = L_new

print(
    f"Bisection equilibrium workload: "
    f"{bisection.root:.6f} units"
)

print(
    f"Fixed-point equilibrium workload: "
    f"{history[-1]:.6f} units"
)

print("Fixed-point iterations:", len(history) - 1)

# Plot the workload balance function
loads = np.linspace(40, 60, 300)

plt.plot(loads, workload_balance(loads))
plt.axhline(0, linewidth=0.8)
plt.axvline(bisection.root, linestyle="--")

plt.xlabel("Server workload (units)")
plt.ylabel("Workload balance function")
plt.title("Campus Server Workload Equilibrium")
plt.grid(True)
plt.show()
