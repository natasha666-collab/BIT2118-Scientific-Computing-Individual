# Task 7: Gaussian Elimination and LU Decomposition

## 1. Introduction

This task explores two numerical methods used to solve systems of linear equations: Gaussian elimination and LU decomposition.

Gaussian elimination transforms a system of linear equations into an upper triangular form through row operations. The unknown variables are then calculated using back substitution.

LU decomposition expresses a square matrix as the product of two triangular matrices:

\[
A=LU
\]

Where:
- **L** is a lower triangular matrix.
- **U** is an upper triangular matrix.

LU decomposition is particularly useful when the same coefficient matrix is used with multiple right-hand-side vectors. Instead of repeatedly solving the entire system from the beginning, the matrix can be factorised once and the factors reused.

## 2. Original Problem

The original program solves three systems of linear equations using the same coefficient matrix but different measurement vectors.

The coefficient matrix is:

\[
A=
\begin{bmatrix}
4&-1&0\\
-1&4&-1\\
0&-1&3
\end{bmatrix}
\]

The three measurement vectors are:

\[
b_1=
\begin{bmatrix}
15\\10\\10
\end{bmatrix},
\quad
b_2=
\begin{bmatrix}
16\\11\\9
\end{bmatrix},
\quad
b_3=
\begin{bmatrix}
14\\12\\11
\end{bmatrix}
\]

The program uses SciPy's `lu_factor()` to factorise the matrix and `lu_solve()` to calculate the solutions.

### 2.1 Input and Mathematical Operations

**Input:**
- A coefficient matrix containing the relationships between three unknown variables.
- Three measurement vectors representing different sets of measurements.

**Mathematical operations:**
1. LU factorisation of the coefficient matrix.
2. Forward and backward substitution through the LU solver.
3. Matrix multiplication to calculate residuals.
4. Calculation of the residual norm to measure solution accuracy.
5. Direct solution using NumPy's `np.linalg.solve()` for comparison.

### 2.2 Original Program

File: `Task_07_gaussian_lu.py`

The program follows the original implementation provided in the assignment.

### 2.3 Original Output

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

### 2.4 Interpretation of Original Output

- The first measurement set produces a solution of `[5, 5, 5]`.
- The second and third measurement sets produce different solutions because their measurement vectors contain different values.
- The residual norms are zero or extremely close to zero, indicating that the calculated solutions satisfy the original equations to numerical precision.
- The direct solution from `np.linalg.solve()` matches the LU decomposition result for the first measurement set.

The experiment demonstrates that LU decomposition can efficiently solve multiple systems when the coefficient matrix remains unchanged.

## 3. Parameter Modification

To investigate how changing the input affects the solution, the first measurement vector was modified.

**Original parameter:**

```python
np.array([15.0, 10.0, 10.0])
```

**Modified parameter:**

```python
np.array([18.0, 10.0, 10.0])
```

The other two measurement vectors and the coefficient matrix remained unchanged.

### 3.1 Modified Output

```text
Measurement set 1
Solution: [5.80487805 5.2195122  5.07317073]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5.80487805 5.2195122  5.07317073]
```

### 3.2 Interpretation of Modified Output

- The first solution changed from `[5, 5, 5]` to approximately `[5.8049, 5.2195, 5.0732]`.
- The second and third solutions remained unchanged because their measurement vectors were not modified.
- The residual norms remained zero or extremely close to zero.
- The direct solution still matched the LU decomposition result.

**Conclusion:** Changing the right-hand-side measurement vector changes the solution, even when the coefficient matrix remains constant. The experiment also demonstrates why LU decomposition is useful when solving repeated systems with the same coefficient matrix.

## 4. Real-World Application: Campus Network Traffic Estimation

### 4.1 Problem Description

A campus network consists of three interconnected network nodes. Network administrators want to estimate the traffic load handled by each node during different monitoring periods.

A simplified mathematical model represents the relationships between the three nodes. The model's coefficient matrix remains constant, but traffic measurements change over time.

LU decomposition is suitable for this scenario because the same coefficient matrix can be factorised once and reused for multiple sets of traffic measurements.

### 4.2 Assumptions

1. The network is represented by three interconnected nodes.
2. The relationships between the nodes remain constant during the monitoring periods.
3. Traffic measurements change between monitoring periods.
4. The numerical values are simplified traffic-load units for demonstration purposes.
5. The model is assumed to be linear.

### 4.3 Input

The coefficient matrix is:

\[
A=
\begin{bmatrix}
4&-1&0\\
-1&4&-1\\
0&-1&3
\end{bmatrix}
\]

The traffic measurement vectors are:

- Period 1: `[12, 9, 6]`
- Period 2: `[14, 8, 7]`
- Period 3: `[10, 11, 8]`

### 4.4 Program

File: `Task_07_real_world.py`

The program:
1. Defines the network model matrix.
2. Stores three sets of traffic measurements.
3. Factorises the matrix once using `lu_factor()`.
4. Reuses the LU factors to solve each measurement set using `lu_solve()`.
5. Calculates the residual norm for each solution.

### 4.5 Actual Output

```text
Monitoring period 1
Estimated node loads: [4.02439024 4.09756098 3.36585366]
Residual norm: 1.7763568394002505e-15

Monitoring period 2
Estimated node loads: [4.51219512 4.04878049 3.68292683]
Residual norm: 1.9860273225978185e-15

Monitoring period 3
Estimated node loads: [3.68292683 4.73170732 4.24390244]
Residual norm: 1.7763568394002505e-15
```

### 4.6 Interpretation of Results

- During monitoring period 1, the estimated loads for the three nodes are approximately 4.0244, 4.0976 and 3.3659.
- During period 2, the estimated loads change to approximately 4.5122, 4.0488 and 3.6829.
- During period 3, the estimated loads are approximately 3.6829, 4.7317 and 4.2439.
- The residual norms are extremely small, approximately \(10^{-15}\), meaning the calculated solutions satisfy the model to numerical precision.

The results demonstrate how LU decomposition can be reused to solve repeated network-model calculations without factorising the same matrix again.

This is an educational model rather than a calibrated representation of a real campus network.

## 5. Conclusion

This task demonstrated how Gaussian elimination and LU decomposition are used to solve systems of linear equations.

The original experiment showed that LU decomposition can efficiently solve multiple systems sharing the same coefficient matrix. The parameter modification demonstrated that changing the measurement vector changes the calculated solution while leaving the other solutions unaffected.

The campus network traffic application further illustrated how LU decomposition can be applied to repeated calculations involving interconnected systems. The very small residual norms confirmed the numerical accuracy of the calculated solutions.

Overall, LU decomposition is useful when solving several linear systems with the same coefficient matrix because the factorisation can be performed once and reused.

## 6. Files in This Folder

```text
Task_07_Gaussian_LU/
│
├── Task_07_gaussian_lu.py
├── Task_07_real_world.py
└── README.md
```

## 7. Libraries Used

- **NumPy:** Used for matrices, arrays, matrix multiplication, residual calculations and direct solutions.
- **SciPy:** Used for LU factorisation and solving systems through `scipy.linalg`.

