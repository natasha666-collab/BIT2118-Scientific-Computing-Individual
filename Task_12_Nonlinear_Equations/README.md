# Task 12: Polynomial and Nonlinear Equation Solving

## 1. Introduction

This task explores polynomial equations and systems of nonlinear equations using Python and the SciPy library.

A polynomial equation contains terms with different powers of a variable. A nonlinear system consists of two or more equations that are not all linear.

Numerical methods are used to find approximate solutions when equations are difficult to solve analytically.

## 2. Objectives

- Understand polynomial and nonlinear equations.
- Use SciPy's `root()` function to solve systems of nonlinear equations.
- Investigate how initial guesses influence numerical solutions.
- Verify solutions using residuals.
- Apply nonlinear equation solving to an illustrative server workload problem.

## 3. Tools and Libraries

- Python
- NumPy
- SciPy (`scipy.optimize.root`)

## 4. Original Problem

The original problem involves finding the intersection points between a circle and a parabola.

The equations are:

Circle:

\[
x^2+y^2=4
\]

Parabola:

\[
y=x^2-1
\]

The equations are rearranged into residual functions:

\[
f_1(x,y)=x^2+y^2-4
\]

\[
f_2(x,y)=y-(x^2-1)
\]

The `root()` function attempts to find values of \(x\) and \(y\) that make both residuals equal to zero.

### Original Program

The program uses two initial guesses:

- [1.0, 1.0]
- [-1.0, 1.0]

### Original Output

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

### Interpretation

The solver found two intersection points:

- (1.51748991, 1.30277564)
- (-1.51748991, 1.30277564)

Both solutions converged successfully.

The residuals are extremely close to zero, confirming that the calculated points satisfy both equations to a high degree of numerical accuracy.

The different initial guesses allowed the solver to find the two different intersection points.

## 5. Parameter Change Experiment

The initial guesses were changed from:

```python
[1.0, 1.0]
[-1.0, 1.0]
```

To:

```python
[2.0, 1.5]
[-2.0, 1.5]
```

### Modified Output

```text
Initial guess: [2.0, 1.5]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.615685446016869e-13), np.float64(-7.105427357601002e-14)]
Converged: True

Initial guess: [-2.0, 1.5]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.615685446016869e-13), np.float64(-7.105427357601002e-14)]
Converged: True
```

### Comparison and Interpretation

Changing the initial guesses did not change the final intersection points.

Both solutions still converged successfully, and the residuals remained extremely close to zero.

This demonstrates that the solver can find the same solutions from different starting points for this particular problem.

However, initial guesses are important in nonlinear equation solving because they can influence which solution the numerical method finds.

## 6. Real-World Application: Campus Server Workload Modelling

### Problem Description

Consider an illustrative campus ICT environment with two interconnected servers.

The workloads of the two servers are represented by two nonlinear equations:

\[
x^2+y=10
\]

\[
x+y^2=10
\]

Where:

- \(x\) represents Server A's normalized workload.
- \(y\) represents Server B's normalized workload.

The equations represent an illustrative nonlinear relationship between the two server workloads.

The objective is to estimate workload values that satisfy both equations simultaneously.

### Method

The `scipy.optimize.root()` function is used to solve the system.

Two initial guesses are tested:

- [2.0, 3.0]
- [3.0, 2.0]

Residuals are calculated to verify the accuracy of the solutions.

### Program Output

```text
Initial guess: [2.0, 3.0]
Server A workload: 2.701562 units
Server B workload: 2.701562 units
Residuals: [np.float64(-2.965805379062658e-11), np.float64(2.5778490453376435e-11)]
Converged: True

Initial guess: [3.0, 2.0]
Server A workload: 2.701562 units
Server B workload: 2.701562 units
Residuals: [np.float64(2.5778490453376435e-11), np.float64(-2.965805379062658e-11)]
Converged: True
```

### Interpretation

The solver estimated the workloads of both servers as approximately 2.701562 units.

Both initial guesses produced the same solution, demonstrating the symmetry of the equations.

The residuals are very close to zero, and both computations converged successfully.

This illustrates how nonlinear equation solving can be applied to mathematical models involving interconnected system variables.

The model is illustrative rather than a measured representation of an actual campus server system.

## 7. Conclusion

This task demonstrated how Python and SciPy can solve polynomial and nonlinear equation problems.

The original problem successfully identified two intersection points between a circle and a parabola.

Changing the initial guesses did not affect the final solutions in this experiment.

The real-world application demonstrated how nonlinear equation solving can estimate interconnected server workload variables.

The experiments showed the importance of initial guesses, convergence checks, and residual verification when using numerical solvers.