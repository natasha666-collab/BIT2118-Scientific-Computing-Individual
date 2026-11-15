
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Model of three interconnected campus network nodes.
# The matrix represents the relationships between the nodes.
A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

# Traffic measurements from three monitoring periods.
# Values are simplified traffic-load units.
traffic_measurements = [
    np.array([12.0, 9.0, 6.0]),
    np.array([14.0, 8.0, 7.0]),
    np.array([10.0, 11.0, 8.0])
]

# Factorise the matrix once.
lu, piv = lu_factor(A)

# Reuse the LU factors for each monitoring period.
for period, b in enumerate(traffic_measurements, start=1):
    estimated_load = lu_solve((lu, piv), b)

    residual = b - A @ estimated_load

    print(f"Monitoring period {period}")
    print("Estimated node loads:", estimated_load)
    print("Residual norm:", np.linalg.norm(residual))
    print()
