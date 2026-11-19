import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
rng = np.random.default_rng(42)

# Server parameters
capacity = 1000.0
mean_demand = 900.0
std_demand = 120.0
N = 100_000

# Generate random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

# Identify overloaded scenarios
overloaded = demand > capacity

# Estimate overload probability
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Calculate running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

# Select points for the convergence graph
indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

# Plot estimated probability
plt.semilogx(
    indices + 1,
    running_probability[indices]
)

plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.grid(True)
plt.show()
