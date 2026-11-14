import numpy as np

# x = number of Workstation A computers
# y = number of Workstation B computers

# Workstation A: 200 watts and 8 GB RAM
# Workstation B: 300 watts and 16 GB RAM

# Available resources:
# 1200 watts and 64 GB RAM

A = np.array([
    [200.0, 300.0],
    [8.0, 16.0]
])

b = np.array([1200.0, 64.0])

# Solve the system
solution = np.linalg.solve(A, b)

# Verify the solution
verification = A @ solution
residual = b - verification

print("CAMPUS COMPUTER LAB RESOURCE ALLOCATION")
print("---------------------------------------")
print(f"Workstation A: {solution[0]:.0f}")
print(f"Workstation B: {solution[1]:.0f}")

print("Total resources used:", verification)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))