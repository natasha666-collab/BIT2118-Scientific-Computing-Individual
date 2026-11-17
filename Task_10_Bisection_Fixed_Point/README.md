# Task 10: Root Finding – Bisection and Fixed-Point Methods

## 1. Introduction

This task demonstrates two numerical methods used to find roots of nonlinear equations: the Bisection Method and the Fixed-Point Iteration Method.

A root is a value of \(x\) that satisfies:

\[
f(x)=0
\]

The task uses a heat-balance model to calculate an equilibrium temperature. A separate application demonstrates how the methods can estimate equilibrium workload in a campus server model.

## 2. Mathematical Concepts

### Bisection Method

The Bisection Method starts with an interval \([a,b]\) where the function has opposite signs at the endpoints.

It repeatedly divides the interval into two halves and selects the half containing the root.

The midpoint is calculated using:

\[
c=\frac{a+b}{2}
\]

The process continues until the required accuracy is achieved.

### Fixed-Point Iteration

Fixed-point iteration rearranges an equation into:

\[
x=g(x)
\]

It then repeatedly calculates:

\[
x_{n+1}=g(x_n)
\]

The method stops when consecutive estimates differ by less than a specified tolerance.

## 3. Original Problem: Equilibrium Temperature

The original program uses the heat-balance equation:

\[
f(T)=T-25-10e^{-T/20}
\]

The equilibrium temperature is obtained when:

\[
f(T)=0
\]

The program applies:
- Bisection with the interval [20, 40].
- Fixed-point iteration using \(g(T)=25+10e^{-T/20}\).
- An initial fixed-point estimate of 30°C.
- A tolerance of \(10^{-10}\).

### Original Program Output

```text
Bisection equilibrium temperature: 27.525211 C
Fixed-point equilibrium temperature: 27.525211 C
Fixed-point iterations: 13
```

### Interpretation

Both methods calculated an equilibrium temperature of approximately 27.525211°C.

The agreement between the two results indicates that both methods successfully located the root of the heat-balance equation.

The graph displays the heat-balance function, its zero line and the estimated equilibrium temperature.

## 4. Parameter-Change Experiment

The initial fixed-point estimate was changed from:

```python
T = 30.0
```

to:

```python
T = 35.0
```

All other parameters remained unchanged.

### Modified Program Output

```text
Bisection equilibrium temperature: 27.525211 C
Fixed-point equilibrium temperature: 27.525211 C
Fixed-point iterations: 14
```

### Comparison

| Measurement | Original | Modified |
|---|---:|---:|
| Initial estimate | 30°C | 35°C |
| Bisection result | 27.525211°C | 27.525211°C |
| Fixed-point result | 27.525211°C | 27.525211°C |
| Fixed-point iterations | 13 | 14 |

### Interpretation

Changing the initial estimate did not change the final equilibrium temperature. However, the fixed-point method required one additional iteration.

This demonstrates that the initial estimate can affect the convergence process and the number of iterations required.

## 5. Real-World Application: Campus Server Workload Equilibrium

### Problem Description

An illustrative campus server workload model is represented by:

\[
L=40+12e^{-L/30}
\]

Where:
- \(L\) represents the equilibrium workload in normalized units.
- 40 represents the baseline workload.
- The exponential term represents an additional workload component that decreases as the modeled load increases.

The objective is to find the workload value at which both sides of the equation balance.

### Methods Used

The program applies:
- Bisection using the interval [40, 60].
- Fixed-point iteration using \(g(L)=40+12e^{-L/30}\).
- An initial fixed-point estimate of 50 units.
- A tolerance of \(10^{-10}\).

### Actual Program Output

```text
Bisection equilibrium workload: 42.874180 units
Fixed-point equilibrium workload: 42.874180 units
Fixed-point iterations: 12
```

### Interpretation

Both numerical methods estimated the equilibrium server workload as approximately 42.874180 units.

The fixed-point method reached this result after 12 iterations.

The graph plots the workload-balance function, the zero line and the estimated equilibrium point.

This application demonstrates how numerical root-finding methods can help solve nonlinear workload models.

*Note: This is an illustrative mathematical model, not a measurement of an actual campus server.*

## 6. Conclusion

This task demonstrated how the Bisection and Fixed-Point Iteration methods can solve nonlinear equations.

The original heat-balance problem produced the same equilibrium temperature using both methods. Changing the initial estimate affected the number of fixed-point iterations but not the final result.

The campus server application further demonstrated how the same numerical techniques can be applied to a separate workload model.

The task improved understanding of root-finding, convergence, numerical accuracy and the practical application of numerical methods.

## 7. Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib

## 8. Files in This Folder

- `Task_10_bisection_fixed_point.py` – Original heat-balance problem.
- `Task_10_real_world.py` – Campus server workload application.
- `README.md` – Documentation, results and interpretation.
