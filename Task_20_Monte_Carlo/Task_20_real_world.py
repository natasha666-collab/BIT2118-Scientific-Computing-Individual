import numpy as np
import matplotlib.pyplot as plt

# Reproducible random number generator
rng = np.random.default_rng(42)

# Campus network parameters
available_bandwidth = 500.0
mean_demand = 400.0
std_demand = 65.0
N = 100_000

# Generate random campus network demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

# Identify scenarios where demand exceeds bandwidth
overloaded = demand > available_bandwidth

# Estimate probability of network overload
overload_probability = overloaded.mean()

print("Campus Network Service Reliability Estimation")
print(f"Available bandwidth: {available_bandwidth:.2f} Mbps")
print(f"Average network demand: {mean_demand:.2f} Mbps")
print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Calculate running probability
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

# Select simulation points for the graph
indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

# Plot convergence
plt.semilogx(
    indices + 1,
    running_probability[indices]
)

plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo Estimate of Campus Network Overload")
plt.grid(True)
plt.show()
