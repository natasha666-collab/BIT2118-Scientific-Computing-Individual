import numpy as np
import matplotlib.pyplot as plt

# Simplified traffic-load model for five interconnected campus routers.
# The matrix is diagonally dominant to support convergence.

A = np.array([
    [ 4., -1.,  0.,  0.,  0.],
    [-1.,  4., -1.,  0.,  0.],
    [ 0., -1.,  4., -1.,  0.],
    [ 0.,  0., -1.,  4., -1.],
    [ 0.,  0.,  0., -1.,  4.]
])

# Traffic measurements in simplified load units.
b = np.array([100., 80., 60., 40., 20.])


def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x_new, errors

        x = x_new

    return x, errors


def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        old = x.copy()

        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]

        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x, errors

    return x, errors


# Calculate router loads using both iterative methods.
x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)

# Calculate a direct solution for comparison.
x_exact = np.linalg.solve(A, b)

print("Jacobi estimated router loads:", x_j)
print("Gauss-Seidel estimated router loads:", x_gs)
print("Direct solution:", x_exact)

print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))

# Plot convergence.
plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of campus network traffic estimation")
plt.legend()
plt.grid(True)
plt.show()
