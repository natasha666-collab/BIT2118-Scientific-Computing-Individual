# Task 11: Root Finding – Newton-Raphson and Secant Methods

## 1. Introduction

This task demonstrates two numerical methods used to find roots of nonlinear equations: Newton-Raphson and the Secant Method.

A root is a value of \(x\) that satisfies:

\[
f(x)=0
\]

Both methods estimate roots iteratively. Newton-Raphson uses the derivative of the function, while the Secant Method estimates the derivative using two previous points.

The original assignment calculates the Internal Rate of Return (IRR) of an investment. A separate application uses the same methods to analyse hypothetical campus ICT equipment replacement cash flows.

## 2. Mathematical Concepts

### Newton-Raphson Method

Newton-Raphson improves an initial estimate using:

\[
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
\]

It uses the function and its derivative to move closer to the root.

### Secant Method

The Secant Method approximates the derivative using two previous estimates:

\[
x_{n+1}=x_n-
f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}
\]

It does not require an explicitly calculated derivative.

Both methods can converge quickly when suitable starting estimates are selected.

## 3. Original Problem: Calculating Internal Rate of Return

### Problem Description

The original program calculates the interest rate at which the Net Present Value (NPV) of a set of cash flows equals zero.

The cash flows are:

| Year | Cash flow |
|---|---:|
| 0 | -10,000 |
| 1 | 3,000 |
| 2 | 3,500 |
| 3 | 4,000 |
| 4 | 2,500 |

The NPV function is:

\[
NPV(r)=\sum_{t=0}^{n}\frac{CF_t}{(1+r)^t}
\]

The program uses:
- Newton-Raphson with an initial estimate of 10%.
- Secant with initial estimates of 5% and 20%.
- A tolerance of \(10^{-12}\).

### Original Program Output

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
NPV at Secant solution: 0.000000
```

### Interpretation

Both methods calculated an IRR of approximately 11.542461%.

The NPV at both solutions was zero to the displayed precision. This indicates that both methods successfully located the root of the NPV function.

## 4. Parameter-Change Experiment

The initial estimate for Newton-Raphson was changed from 10% to 15%.

Original parameter:

```python
x0=0.10
```

Modified parameter:

```python
x0=0.15
```

The Secant initial estimates remained unchanged.

### Modified Program Output

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: -0.000000
NPV at Secant solution: 0.000000
```

### Comparison

| Measurement | Original | Modified |
|---|---:|---:|
| Newton initial estimate | 10% | 15% |
| Newton-Raphson IRR | 11.542461% | 11.542461% |
| Secant IRR | 11.542461% | 11.542461% |
| NPV at Newton solution | 0.000000 | -0.000000 |
| NPV at Secant solution | 0.000000 | 0.000000 |

### Interpretation

Changing the Newton-Raphson initial estimate did not change the final calculated IRR.

Both methods still converged to approximately 11.542461%.

The negative zero in the modified output is a floating-point rounding effect. It represents a value extremely close to zero.

This experiment demonstrates that a change in the initial estimate does not necessarily change the final root when the method converges successfully.

## 5. Real-World Application: Campus ICT Equipment Replacement Analysis

### Problem Description

An illustrative campus ICT department is evaluating a hypothetical equipment replacement.

The objective is to calculate the discount rate at which the Net Present Value of the replacement cash flows equals zero.

The example uses these cash flows:

| Year | Cash flow |
|---|---:|
| 0 | -20,000 |
| 1 | 6,000 |
| 2 | 7,000 |
| 3 | 8,000 |
| 4 | 9,000 |

### Methods Used

The program applies:
- Newton-Raphson with an initial estimate of 15%.
- Secant with initial estimates of 10% and 25%.
- A tolerance of \(10^{-12}\).

Both methods calculate the root of the same NPV function.

### Actual Program Output

```text
Equipment replacement IRR using Newton-Raphson: 17.093686%
Equipment replacement IRR using Secant: 17.093686%
NPV at Newton solution: 0.000000
NPV at Secant solution: -0.000000
```

### Interpretation

Both methods estimated the equipment replacement model's IRR as approximately 17.093686%.

The NPV values were extremely close to zero, confirming that the calculated rates satisfy the equation.

This application demonstrates how numerical root-finding methods can be used to solve cash-flow equations with different sets of values.

*Note: The cash flows are illustrative and do not represent an actual campus equipment investment or financial recommendation.*

## 6. Conclusion

This task demonstrated the use of Newton-Raphson and Secant methods for solving nonlinear equations.

In the original problem, both methods calculated an IRR of approximately 11.542461%. Changing the Newton-Raphson initial estimate from 10% to 15% did not affect the final result.

The separate campus ICT equipment replacement application produced an estimated IRR of approximately 17.093686% using both methods.

The task improved understanding of numerical root-finding, derivatives, iterative estimation, convergence and the practical application of numerical methods.

## 7. Technologies Used

- Python
- SciPy

## 8. Files in This Folder

- `Task_11_newton_secant.py` – Original IRR calculation.
- `Task_11_real_world.py` – Campus ICT equipment replacement application.
- `README.md` – Documentation, results and interpretation.
