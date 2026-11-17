import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Hourly computer laboratory temperature readings
hours = np.array(
    [8, 9, 10, 11, 12, 13, 14],
    dtype=float
)

temperature = np.array(
    [19.0, 20.5, 22.0, 23.5, 25.0, 26.0, 25.5]
)

# Create interpolation functions
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Generate estimates every 15 minutes
quarter_hour_times = np.arange(8, 14 + 0.25, 0.25)

linear_estimates = linear(quarter_hour_times)
cubic_estimates = cubic(quarter_hour_times)

# Display selected estimates
print("Campus Computer Laboratory Temperature Monitoring")
print()

for t in [8.25, 9.5, 10.75, 12.5, 13.75]:
    print(
        f"Time: {t:.2f} hours | "
        f"Linear: {float(linear(t)):.2f} C | "
        f"Cubic: {float(cubic(t)):.2f} C"
    )

# Plot the recorded readings and estimated temperatures
plt.scatter(
    hours,
    temperature,
    label="Recorded temperatures"
)

plt.plot(
    quarter_hour_times,
    linear_estimates,
    label="Linear interpolation"
)

plt.plot(
    quarter_hour_times,
    cubic_estimates,
    label="Cubic spline interpolation"
)

plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Campus Computer Laboratory Temperature Monitoring")
plt.legend()
plt.grid(True)
plt.show()
