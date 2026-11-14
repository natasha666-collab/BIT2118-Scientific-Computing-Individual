import numpy as np

# Computer laboratory floor-plan coordinates
points = np.array([
    [0.0, 0.0],
    [4.0, 0.0],
    [4.0, 3.0],
    [0.0, 3.0]
])

# Rotation angle
angle = np.deg2rad(30)

# Rotation matrix
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Scaling matrix
scale = np.array([
    [1.5, 0.0],
    [0.0, 2.0]
])

# Combine scaling and rotation
transformation = rotation @ scale

# Calculate transformed coordinates
transformed_points = points @ transformation.T

print("CAMPUS COMPUTER LAB FLOOR-PLAN")
print("--------------------------------")
print("Original coordinates:\n", points)
print("Transformed coordinates:\n", transformed_points)
print("Transformation matrix:\n", transformation)
print("Determinant:", np.linalg.det(transformation))