import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Number of connected campus Wi-Fi devices
devices = np.array([10, 20, 30, 40, 50, 60, 70], dtype=float)

# Illustrative bandwidth consumption in Mbps
bandwidth = np.array([8, 18, 32, 51, 75, 105, 140], dtype=float)

# Quadratic model
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the model
parameters, covariance = curve_fit(model, devices, bandwidth)

a, b, c = parameters

# Calculate fitted values and RMSE
predicted = model(devices, a, b, c)
rmse = np.sqrt(np.mean((bandwidth - predicted)**2))

# Predict bandwidth for 80 devices
future_devices = 80
future_bandwidth = model(future_devices, a, b, c)

print("Campus Wi-Fi Bandwidth Demand Estimation")
print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} Mbps")
print(f"Predicted bandwidth for {future_devices} devices: {future_bandwidth:.2f} Mbps")

# Plot measurements and fitted curve
x_plot = np.linspace(devices.min(), 80, 300)

plt.scatter(devices, bandwidth, label="Measured bandwidth")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")

plt.xlabel("Number of connected devices")
plt.ylabel("Bandwidth consumption (Mbps)")
plt.title("Campus Wi-Fi Bandwidth Demand")
plt.legend()
plt.grid(True)
plt.show()
