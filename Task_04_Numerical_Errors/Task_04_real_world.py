import numpy as np

# Reference temperature and sensor measurement
reference_temperature = 25.0
measured_temperature = 25.2

# Calculate numerical errors
absolute_error = abs(
    reference_temperature - measured_temperature
)

relative_error = (
    absolute_error / abs(reference_temperature)
)

# Check whether the measurement is within tolerance
acceptable = np.isclose(
    measured_temperature,
    reference_temperature,
    atol=0.5
)

print("TEMPERATURE SENSOR ERROR ANALYSIS")
print("---------------------------------")
print(f"Reference temperature: {reference_temperature} °C")
print(f"Measured temperature: {measured_temperature} °C")
print(f"Absolute error: {absolute_error:.4f} °C")
print(f"Relative error: {relative_error:.2%}")
print(f"Within acceptable tolerance: {acceptable}")