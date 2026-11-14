# Task 5: Matrix Algebra and Matrix Operations

## 1. Introduction

This task explores matrix algebra and matrix operations using Python and NumPy.

A matrix is a rectangular arrangement of values organized into rows and columns. Matrices are useful in scientific computing because they allow multiple mathematical operations to be performed efficiently.

The task demonstrates matrix representation, matrix multiplication, scaling, rotation and determinants through a computer graphics application.

## 2. Mathematical Concepts

### Matrix Representation

A matrix organizes numerical values into rows and columns.

For example:

\[
A=\begin{bmatrix}1&2\\3&4\end{bmatrix}
\]

### Matrix Addition

Matrix addition combines corresponding elements of two matrices of compatible dimensions.

### Matrix Multiplication

Matrix multiplication combines rows of the first matrix with columns of the second matrix.

\[
c_{ij}=\sum_k a_{ik}b_{kj}
\]

### Determinant

The determinant is a numerical value calculated from a square matrix. A nonzero determinant indicates that the matrix is invertible.

### Matrix Inverse

The inverse of a matrix \(A\), written as \(A^{-1}\), satisfies:

\[
AA^{-1}=I
\]

where \(I\) is the identity matrix.

### Matrix Transformations

In computer graphics, matrices can represent transformations such as rotation and scaling. Multiple transformations can be combined using matrix multiplication.

## 3. Original Problem

A graphics program needs to rotate and scale a set of two-dimensional coordinates representing points on an object.

The solution represents the object's four corners as coordinate vectors, creates rotation and scaling matrices, combines the matrices and uses matrix multiplication to calculate the transformed coordinates.

## 4. Original Program

**File:** `Task_05_matrix_algebra.py`

The program uses NumPy to:

- Represent the four corners of a square as a matrix of coordinates.
- Create a rotation matrix for a 45-degree rotation.
- Create a scaling matrix with horizontal scaling of 2.0 and vertical scaling of 1.5.
- Combine the rotation and scaling matrices.
- Calculate the transformed coordinates.
- Calculate the determinant of the transformation matrix.

The combined transformation is:

\[
T=RS
\]

where \(R\) is the rotation matrix and \(S\) is the scaling matrix.

The program stores points as row vectors, so it multiplies the points by the transpose of the combined transformation matrix.

## 5. Original Program Results and Interpretation

**Output:**

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]

Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]

Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]

Determinant: 3.000000000000001
```

**Interpretation:**

The original square has four corners represented by the coordinates (0,0), (1,0), (1,1) and (0,1).

After applying the scaling and 45-degree rotation, the coordinates change to represent the transformed square.

Some coordinates become negative because the object is rotated around the origin.

The determinant is approximately 3. Since it is nonzero, the transformation matrix is invertible. This means the original coordinates can theoretically be recovered using the inverse transformation.

## 6. Parameter Modification and Results

The original program used a rotation angle of 45 degrees:

```python
angle = np.deg2rad(45)
```

The angle was modified to 90 degrees:

```python
angle = np.deg2rad(90)
```

**Modified output:**

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]

Transformation matrix:
 [[ 1.22464680e-16 -1.50000000e+00]
 [ 2.00000000e+00  9.18485099e-17]]

Transformed points:
 [[ 0.00000000e+00  0.00000000e+00]
 [ 1.22464680e-16  2.00000000e+00]
 [-1.50000000e+00  2.00000000e+00]
 [-1.50000000e+00  9.18485099e-17]]

Determinant: 2.9999999999999996
```

**Interpretation:**

Changing the rotation angle from 45 to 90 degrees changes the orientation and transformed coordinates of the square.

The very small values close to zero are caused by floating-point precision when calculating trigonometric functions.

The determinant remains approximately 3 because the scaling factors remain unchanged. Rotation preserves area, while the scaling factors multiply to give an area scaling factor of:

\[
2.0\times1.5=3
\]

Therefore, changing the rotation angle does not change the determinant.

## 7. Real-World Application: Campus Computer Laboratory Floor-Plan Transformation

### Problem

A campus facilities team has a rectangular computer laboratory represented by two-dimensional coordinates on a digital floor plan.

The layout needs to be enlarged horizontally and vertically and rotated by 30 degrees for display.

Matrix transformations can be used to calculate the new coordinates of the laboratory's four corners.

### Assumptions

- The original laboratory is represented by a rectangle measuring 4 coordinate units by 3 coordinate units.
- Horizontal scaling factor: 1.5.
- Vertical scaling factor: 2.0.
- Rotation angle: 30 degrees.
- The transformation takes place around the origin (0,0).
- Coordinate units are arbitrary floor-plan units and do not represent actual metres.

### Input Data

Original coordinates:

\[
P=\begin{bmatrix}
0&0\\
4&0\\
4&3\\
0&3
\end{bmatrix}
\]

Horizontal scaling factor: 1.5

Vertical scaling factor: 2.0

Rotation angle: 30 degrees.

### Program

**File:** `Task_05_real_world.py`

The program creates the original laboratory coordinates, constructs rotation and scaling matrices, combines the transformations and calculates the new coordinates using NumPy matrix multiplication.

### Output

```text
CAMPUS COMPUTER LAB FLOOR-PLAN
--------------------------------
Original coordinates:
 [[0. 0.]
 [4. 0.]
 [4. 3.]
 [0. 3.]]

Transformed coordinates:
 [[ 0.          0.        ]
 [ 5.19615242  3.        ]
 [ 2.19615242  8.19615242]
 [-3.          5.19615242]]

Transformation matrix:
 [[ 1.29903811 -1.        ]
 [ 0.75        1.73205081]]

Determinant: 2.9999999999999996
```

### Interpretation

The original rectangular laboratory coordinates are scaled horizontally and vertically and then rotated by 30 degrees.

The transformed coordinates represent the new positions of the four corners on the digital floor plan.

The determinant is approximately 3, indicating that the transformation scales the area by a factor of 3.

Since the determinant is nonzero, the transformation is invertible.

This application demonstrates how matrix operations can be used in computer graphics and digital floor-plan systems to manipulate and transform coordinates.

## 8. Conclusion

This task demonstrated how matrices can represent and transform two-dimensional coordinates using Python and NumPy.

It explored matrix multiplication, scaling, rotation, determinants and matrix invertibility through a computer graphics example.

The parameter modification showed that changing the rotation angle changes the transformed coordinates without changing the determinant when the scaling factors remain constant.

The campus computer laboratory floor-plan application demonstrated how similar mathematical operations can be used in a practical coordinate transformation scenario.

Overall, matrix algebra provides an efficient way of performing multiple mathematical operations and is an important concept in computer graphics, scientific computing, robotics and engineering.
