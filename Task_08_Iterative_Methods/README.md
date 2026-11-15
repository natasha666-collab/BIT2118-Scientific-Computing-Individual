# Task 8: Iterative Methods for Linear Systems

## 1. Introduction

This task explores two iterative methods used to solve systems of linear equations:

1. Jacobi method.
2. Gauss-Seidel method.

Unlike direct methods, iterative methods begin with an initial guess and repeatedly improve the estimated values until the difference between successive estimates becomes smaller than a specified tolerance.

The Jacobi method calculates all new estimates using values from the previous iteration.

The Gauss-Seidel method immediately uses newly calculated values within the same iteration.

These methods are useful in scientific computing, particularly when working with large systems of equations.

## 2. Original Problem

The original program models the steady-state temperature distribution across five interior grid points.

The left boundary temperature is 100°C, while the right boundary temperature is 20°C.

The system is represented by:

\[
A=
\begin{bmatrix}
2&-1&0&0&0\\
-1&2&-1&0&0\\
0&-1&2&-1&0\\
0&0&-1&2&-1\\
0&0&0&-1&2
\end{bmatrix}
\]

The boundary influence vector is:

\[
b=
\begin{bmatrix}
100\\0\\0\\0\\20
\end{bmatrix}
\]

### 2.1 Input and Mathematical Operations

**Input:**
- A coefficient matrix representing the relationships between the five temperature points.
- A vector representing the influence of the boundary temperatures.
- A tolerance of \(10^{-8}\).
- A maximum of 500 iterations.

**Mathematical operations:**
1. Extracting the diagonal elements of the coefficient matrix.
2. Applying the Jacobi iterative formula.
3. Applying the Gauss-Seidel iterative formula.
4. Calculating the maximum change between successive estimates.
5. Comparing the iterative results with a direct solution using `np.linalg.solve()`.
6. Plotting the convergence of both methods using Matplotlib.

### 2.2 Original Program

File: `Task_08_iterative_linear.py`

The program implements both iterative methods and plots their convergence.

### 2.3 Original Output

```text
Jacobi temperatures: [86.66666665 73.33333331 59.99999997 46.66666664 33.33333332]
Gauss-Seidel temperatures: [86.66666665 73.3333333  59.99999997 46.66666665 33.33333332]
Direct solution: [86.66666667 73.33333333 60.         46.66666667 33.33333333]
```

### 2.4 Interpretation of Original Output

- The Jacobi method estimates the five temperatures as approximately 86.67°C, 73.33°C, 60°C, 46.67°C and 33.33°C.
- The Gauss-Seidel method produces almost identical estimates.
- The direct solution also produces the same temperature distribution to the displayed precision.
- The small differences between the iterative and direct solutions result from the stopping tolerance.

### 2.5 Interpretation of Original Convergence Graph

The graph titled *Convergence of iterative temperature solution* compares the maximum change between successive estimates for the two methods.

- The blue line represents Jacobi.
- The orange line represents Gauss-Seidel.
- The horizontal axis represents the iteration number.
- The vertical axis represents the maximum change on a logarithmic scale.

The Jacobi method takes approximately 150 iterations to reach the \(10^{-8}\) tolerance, while Gauss-Seidel takes approximately 74 iterations.

The graph demonstrates that Gauss-Seidel converges faster than Jacobi for this particular system.

## 3. Parameter Modification

The stopping tolerance was changed to investigate its effect on convergence.

**Original tolerance:**

\[
10^{-8}
\]

**Modified tolerance:**

\[
10^{-4}
\]

The two method calls were changed to:

```python
x_j, err_j = jacobi(A, b, tol=1e-4)
x_gs, err_gs = gauss_seidel(A, b, tol=1e-4)
```

Two additional print statements were included to display the number of iterations used by each method.

### 3.1 Modified Output

```text
Jacobi iterations: 86
Gauss-Seidel iterations: 43
Direct solution: [86.66666667 73.33333333 60.         46.66666667 33.33333333]
```

### 3.2 Comparison of Results

| Method | Original tolerance | Modified tolerance |
|---|---:|---:|
| Jacobi iterations | Approximately 150 | 86 |
| Gauss-Seidel iterations | Approximately 74 | 43 |

### 3.3 Interpretation of Modified Output and Graph

- Increasing the tolerance from \(10^{-8}\) to \(10^{-4}\) allowed both methods to stop earlier.
- Jacobi required 86 iterations instead of approximately 150.
- Gauss-Seidel required 43 iterations instead of approximately 74.
- Both methods still produced estimates close to the direct solution.
- The modified graph shows both methods reaching the \(10^{-4}\) threshold earlier.

A larger tolerance allows a less strict approximation, reducing the number of iterations but potentially reducing accuracy.

Gauss-Seidel remained faster than Jacobi in this experiment.

## 4. Real-World Application: Campus Network Traffic Distribution

### 4.1 Problem Description

A campus network consists of five interconnected routers. A network administrator wants to estimate the traffic load handled by each router using measurements collected across the network.

A simplified mathematical model represents the relationships between neighbouring routers.

The Jacobi and Gauss-Seidel methods are used to estimate the traffic load at each router. A direct solution is also calculated for comparison.

### 4.2 Assumptions

1. The campus network is represented by five interconnected routers.
2. The relationships between neighbouring routers are represented by a fixed coefficient matrix.
3. The network model is linear.
4. The traffic measurements are represented using simplified load units.
5. The coefficient matrix is diagonally dominant to support convergence.
6. The model is an educational example rather than a calibrated representation of an actual campus network.

### 4.3 Input

The coefficient matrix is:

\[
A=
\begin{bmatrix}
4&-1&0&0&0\\
-1&4&-1&0&0\\
0&-1&4&-1&0\\
0&0&-1&4&-1\\
0&0&0&-1&4
\end{bmatrix}
\]

The traffic measurement vector is:

\[
b=
\begin{bmatrix}
100\\80\\60\\40\\20
\end{bmatrix}
\]

### 4.4 Program

File: `Task_08_real_world.py`

The program:
1. Defines the network coefficient matrix and traffic measurement vector.
2. Implements the Jacobi method.
3. Implements the Gauss-Seidel method.
4. Calculates estimated traffic loads for all five routers.
5. Calculates a direct solution using NumPy for comparison.
6. Displays the number of iterations required by each method.
7. Plots the convergence of both methods.

### 4.5 Actual Output

```text
Jacobi estimated router loads: [33.92307692 35.69230769 28.84615384 19.69230769  9.92307692]
Gauss-Seidel estimated router loads: [33.92307692 35.69230769 28.84615385 19.69230769  9.92307692]
Direct solution: [33.92307692 35.69230769 28.84615385 19.69230769  9.92307692]
Jacobi iterations: 27
Gauss-Seidel iterations: 15
```

### 4.6 Interpretation of Results

The estimated traffic loads for the five routers are approximately:

- Router 1: 33.9231 units.
- Router 2: 35.6923 units.
- Router 3: 28.8462 units.
- Router 4: 19.6923 units.
- Router 5: 9.9231 units.

The Jacobi method converged in 27 iterations, while the Gauss-Seidel method converged in 15 iterations.

Both methods produced results that closely match the direct solution.

The results demonstrate that iterative methods can estimate unknown values in interconnected systems. Gauss-Seidel required fewer iterations than Jacobi for this particular example.

## 5. Conclusion

This task demonstrated how the Jacobi and Gauss-Seidel methods can solve systems of linear equations through repeated approximations.

The original temperature distribution problem showed that both methods can produce accurate results when the coefficient matrix supports convergence.

The parameter modification demonstrated that increasing the tolerance reduces the number of iterations required, although it allows a less precise approximation.

The campus network application demonstrated how iterative methods can estimate traffic loads in a simplified interconnected system.

Overall, iterative methods are useful in scientific computing, especially when solving large systems of equations. Gauss-Seidel converged faster than Jacobi in both experiments conducted in this task.

## 6. Files in This Folder

```text
Task_08_Iterative_Methods/
│
├── Task_08_iterative_linear.py
├── Task_08_real_world.py
└── README.md
```

## 7. Libraries Used

- **NumPy:** Used for matrix operations, array calculations, iterative solutions and direct solutions.
- **Matplotlib:** Used to plot and compare the convergence of the iterative methods.

