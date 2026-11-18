import numpy as np
from scipy.integrate import simpson

# Water flow readings collected every 10 minutes
time_minutes = np.array([0, 10, 20, 30, 40, 50, 60], dtype=float)

# Water flow rate in litres per minute
flow_lpm = np.array([12, 15, 18, 20, 17, 14, 10], dtype=float)

# Estimate total water volume
volume_trapezoid = np.trapezoid(flow_lpm, time_minutes)
volume_simpson = simpson(flow_lpm, x=time_minutes)

print("Campus Water Tank Flow Monitoring")
print(f"Water volume using trapezoidal rule: {volume_trapezoid:.2f} litres")
print(f"Water volume using Simpson's rule: {volume_simpson:.2f} litres")
print(
    f"Difference between estimates: "
    f"{abs(volume_simpson - volume_trapezoid):.2f} litres"
)
