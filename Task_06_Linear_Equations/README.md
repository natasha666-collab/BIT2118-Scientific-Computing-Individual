# Task 6: Solution of Systems of Linear Equations

## 1. Introduction

This task explores how systems of linear equations can be solved computationally using Python and NumPy.

A system of linear equations consists of two or more equations containing unknown variables. Numerical methods can be used to determine values that satisfy all the equations simultaneously.

The task uses NumPy's `np.linalg.solve()` function to solve linear systems and verifies the results using residual calculations.

## 2. Mathematical Concepts

### Systems of Linear Equations

A system of linear equations contains multiple equations involving unknown variables.

For example:

\[
2x+3y=8
\]

\[
4x+y=6
\]

The objective is to find values of x and y that satisfy both equations.

### Matrix Representation

A system of linear equations can be represented in matrix form as:

\[
Ax=b
\]

Where:

- A is the coefficient matrix.
- x is the vector of unknown variables.
- b is the vector of known results.

### NumPy Linear Solver

The function `np.linalg.solve(A, b)` calculates the solution of a square system of linear equations when the coefficient matrix is nonsingular.

### Residual

A residual measures the difference between the known results and the values calculated using the solution.

\[
r=b-Ax
\]

A residual close to zero indicates that the calculated solution satisfies the original equations.

### Residual Norm

The residual norm measures the overall magnitude of the residual vector.

\[
\|r\|=\sqrt{r_1^2+r_2^2+\cdots+r_n^2}
\]

A value close to zero indicates a small numerical difference.

## 3. Original Problem

The original problem involves determining the number of active servers of two types based on their CPU and memory consumption.

The server specifications are:

| Server type | CPU usage | Memory usage |
|---|---:|---:|
| Type A | 4 CPU units | 8 GB |
| Type B | 2 CPU units | 12 GB |

The total observed resource usage is 20 CPU units and 72 GB of memory.

Let:

- x = number of Type A servers.
- y = number of Type B servers.

The resulting equations are:

\[
4x+2y=20
\]

\[
8x+12y=72
\]

The equations are represented using NumPy arrays and solved using `np.linalg.solve()`.

## 4. Original Program

**File:** `Task_06_linear_equations.py`

The program:

1. Defines the coefficient matrix A.
2. Defines the resource vector b.
3. Uses `np.linalg.solve()` to calculate the unknown server quantities.
4. Calculates the residual to verify the solution.
5. Calculates the residual norm to measure the overall numerical difference.

## 5. Original Program Results and Interpretation

**Output:**

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

**Interpretation:**

The program determines that there are 3 Type A servers and 4 Type B servers.

The solution can be verified mathematically:

CPU usage:

\[
4(3)+2(4)=20
\]

Memory usage:

\[
8(3)+12(4)=72
\]

The verification output `[20. 72.]` confirms that the calculated solution reproduces the original resource totals.

The residual is `[0. 0.]`, and the residual norm is 0.0. This confirms that the solution satisfies both equations at the displayed numerical precision.

## 6. Parameter Modification and Results

The original resource vector was:

```python
b = np.array([20.0, 72.0])
```

The CPU usage was increased from 20 to 24 units while memory usage remained unchanged.

The modified parameter was:

```python
b = np.array([24.0, 72.0])
```

The modified system becomes:

\[
4x+2y=24
\]

\[
8x+12y=72
\]

**Modified output:**

```text
Type A servers: 4
Type B servers: 3
Verification A @ solution: [24. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

**Interpretation:**

The modified solution is 4 Type A servers and 3 Type B servers.

Increasing the total CPU usage while maintaining the same memory usage changed the number of servers of each type.

The verification output confirms that the calculated resource usage is 24 CPU units and 72 GB of memory.

The residual and residual norm remain zero, demonstrating that the modified solution also satisfies both equations.

This experiment shows how changes in input parameters affect the solution of a system of linear equations.

## 7. Real-World Application: Campus Computer Laboratory Resource Allocation

### Problem

A campus computer laboratory has two workstation configurations with different power and memory requirements.

The laboratory wants to determine how many computers of each configuration can be accommodated using its available resources.

### Workstation Specifications

| Configuration | Power consumption | RAM |
|---|---:|---:|
| Workstation A | 200 watts | 8 GB |
| Workstation B | 300 watts | 16 GB |

### Assumptions

- The laboratory has a total power allocation of 1,200 watts.
- The laboratory has 64 GB of RAM available.
- Every workstation uses its specified power and memory capacity.
- The resources are fully allocated.
- The number of workstations must be non-negative whole numbers.

### Mathematical Model

Let:

- x = number of Workstation A computers.
- y = number of Workstation B computers.

The equations are:

\[
200x+300y=1200
\]

\[
8x+16y=64
\]

### Program

**File:** `Task_06_real_world.py`

The program uses NumPy to solve the system, determine the workstation quantities and verify the resource allocation.

### Output

```text
CAMPUS COMPUTER LAB RESOURCE ALLOCATION
---------------------------------------
Workstation A: 0
Workstation B: 4
Total resources used: [1200.   64.]
Residual: [0. 0.]
Residual norm: 0.0
```

### Interpretation

The solution indicates that the laboratory can accommodate four Workstation B computers and zero Workstation A computers under the stated assumptions.

The four Workstation B computers consume:

Power:

\[
4(300)=1200\text{ watts}
\]

Memory:

\[
4(16)=64\text{ GB}
\]

Both available resource totals are fully utilized.

The residual is zero, confirming that the calculated allocation satisfies both equations.

This application demonstrates how systems of linear equations can support resource allocation and planning in computer laboratories.

## 8. Conclusion

This task demonstrated how Python and NumPy can be used to solve systems of linear equations through matrix operations.

The original server allocation problem showed how unknown quantities can be determined from known resource requirements. The parameter modification demonstrated how changing an input affects the resulting solution.

The campus computer laboratory application further demonstrated how the same mathematical technique can be applied to practical resource allocation problems.

Overall, the task highlights the importance of linear algebra in scientific computing, engineering, computer systems and resource management.
