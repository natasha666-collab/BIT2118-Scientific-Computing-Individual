import numpy as np

# Adjacency matrix representing connections between campus facilities.
# Node order: Library, Computer Labs, Lecture Halls,
# Administration, Student Centre.

A = np.array([
    [0., 1., 1., 0., 0.],
    [1., 0., 1., 1., 0.],
    [1., 1., 0., 1., 1.],
    [0., 1., 1., 0., 1.],
    [0., 0., 1., 1., 0.]
])

facilities = [
    "Library",
    "Computer Labs",
    "Lecture Halls",
    "Administration",
    "Student Centre"
]

# Calculate eigenvalues and eigenvectors.
eigenvalues, eigenvectors = np.linalg.eig(A)

# Identify the dominant eigenvalue.
index = np.argmax(np.real(eigenvalues))

dominant_value = np.real(eigenvalues[index])

# Obtain and normalize the dominant eigenvector.
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

importance = dominant_vector / dominant_vector.sum()

print("Dominant eigenvalue:", dominant_value)
print("Campus facility importance:")

for facility, score in zip(facilities, importance):
    print(f"{facility}: {score:.4f}")

# Verify the eigenvalue equation.
v = np.real(eigenvectors[:, index])

print(
    "Verification error:",
    np.linalg.norm(A @ v - dominant_value * v)
)
