import numpy as np
import matplotlib.pyplot as plt

# Newton's law of cooling:
# dT/dt = -k(T - T_ambient)

T_ambient = 25.0
T_initial = 90.0
k = 0.12
h = 0.5  # minutes
end_time = 30.0


def cooling_rate(T):
    return -k * (T - T_ambient)


time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

# Apply Euler's method
for i in range(len(time) - 1):
    temperature[i + 1] = (
        temperature[i] + h * cooling_rate(temperature[i])
    )

# Exact solution for comparison
exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

# Calculate final error
error = abs(temperature[-1] - exact[-1])

print("Newton's Law of Cooling - Euler Method")
print(f"Step size: {h} minutes")
print(f"Euler temperature after {end_time:.0f} minutes: {temperature[-1]:.4f} °C")
print(f"Exact temperature after {end_time:.0f} minutes: {exact[-1]:.4f} °C")
print(f"Absolute error: {error:.4f} °C")

# Plot results
plt.plot(time, temperature, "o-", label="Euler Method")
plt.plot(time, exact, "-", label="Exact Solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Newton's Law of Cooling")
plt.legend()
plt.grid(True)
plt.show()
