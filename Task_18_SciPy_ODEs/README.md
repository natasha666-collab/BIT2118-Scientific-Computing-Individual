# Task 18: Numerical Solution of ODEs Using SciPy

## 1. Introduction

Ordinary Differential Equations (ODEs) describe how quantities change with respect to variables such as time.

In Task 17, Euler's method was used to approximate solutions by manually calculating successive values.

This task introduces `scipy.integrate.solve_ivp()`, an advanced SciPy function for numerically solving initial-value ordinary differential equations.

The solver uses numerical integration methods and can automatically adjust its internal step sizes to achieve the specified accuracy.

## 2. Mathematical Concepts

### 2.1 Ordinary Differential Equations

The general form of an ordinary differential equation is:

\[
\frac{dy}{dt}=f(t,y)
\]

Where:

- \(y\) represents the dependent variable.
- \(t\) represents the independent variable.
- \(f(t,y)\) describes the rate of change.

### 2.2 SciPy solve_ivp()

The `solve_ivp()` function solves an initial-value ODE over a specified time interval.

Its main inputs include:

- The differential equation function.
- The time interval.
- The initial condition.
- Optional evaluation points.
- Numerical error tolerances.

The function returns a solution containing the calculated values at the requested evaluation points.

### 2.3 Error Tolerances

The solver supports two important tolerance parameters:

- `rtol`: Relative tolerance.
- `atol`: Absolute tolerance.

These control the accuracy requirements of the numerical solver.

### 2.4 Applications

Numerical ODE solvers are used in:

- Electrical circuits.
- Control systems.
- Robotics.
- Chemical reactions.
- Mechanical systems.
- Population and epidemiological models.

## 3. Original Problem: RC Circuit Charging

### 3.1 Problem Description

An RC circuit consists of a resistor and a capacitor connected to a voltage supply.

When connected to the supply, the capacitor gradually charges.

The objective is to model the capacitor voltage over five seconds using SciPy's `solve_ivp()` and compare the numerical solution with the exact mathematical solution.

### 3.2 Mathematical Model

The charging differential equation is:

\[
\frac{dV}{dt}=\frac{V_s-V}{RC}
\]

The exact solution is:

\[
V(t)=V_s\left(1-e^{-t/(RC)}\right)
\]

### 3.3 Input Parameters

| Parameter | Value |
|---|---:|
| Supply voltage | 5 V |
| Resistance | 1000 Ω |
| Capacitance | 0.001 F |
| Initial voltage | 0 V |
| Time interval | 0–5 seconds |
| Evaluation points | 200 |

### 3.4 Implementation

The program uses:

- NumPy to generate evaluation time points.
- `solve_ivp()` to solve the differential equation.
- A Python function to define the charging rate.
- The exact mathematical solution for comparison.
- `np.max()` to calculate the maximum numerical error.
- Matplotlib to plot the numerical and exact solutions.

### 3.5 Original Output

```text id="u5n6os"
RC Circuit Charging - SciPy ODE Solver
Solver success: True
Capacitor voltage at 5 s: 4.9663 V
Maximum error against exact solution: 9.282e-10 V
```

### 3.6 Interpretation

The solver successfully calculated the capacitor voltage over the five-second interval.

The capacitor voltage reached 4.9663 V, approaching the 5 V supply voltage.

The maximum numerical error was approximately \(9.282 \times 10^{-10}\) V, indicating that the numerical solution was extremely close to the exact solution.

The graph showed the capacitor voltage increasing towards the supply voltage.

## 4. Parameter Modification and Experiment

### 4.1 Modification

The original supply voltage was:

`Vs = 5.0`

It was changed to:

`Vs = 6.0`

All other parameters remained unchanged.

### 4.2 Modified Output

```text id="s6j0jk"
RC Circuit Charging - SciPy ODE Solver
Solver success: True
Capacitor voltage at 5 s: 5.9596 V
Maximum error against exact solution: 1.124e-09 V
```

### 4.3 Interpretation

Increasing the supply voltage from 5 V to 6 V increased the capacitor voltage after five seconds.

The final voltage increased from 4.9663 V to 5.9596 V.

The solver remained successful, and the numerical error remained extremely small.

This demonstrates how the supply voltage affects the charging behaviour of an RC circuit.

## 5. Real-World Application: Campus Emergency Indicator Capacitor Discharge

### 5.1 Problem Description

A campus emergency indicator may use a capacitor as part of its electrical circuit.

When the external power supply is interrupted, a charged capacitor can discharge through a resistor.

This application models the decrease in capacitor voltage over time using SciPy's numerical ODE solver.

### 5.2 Assumptions

- The initial capacitor voltage is 5 V.
- The resistance is 2000 Ω.
- The capacitance is 0.001 F.
- The capacitor discharges through a resistor.
- The resistance and capacitance remain constant.
- The simulation covers five seconds.

### 5.3 Mathematical Model

The capacitor discharge equation is:

\[
\frac{dV}{dt}=-\frac{V}{RC}
\]

The exact solution is:

\[
V(t)=V_0e^{-t/(RC)}
\]

### 5.4 Implementation

The program uses:

- NumPy to generate evaluation time points.
- `solve_ivp()` to solve the discharge differential equation.
- The exact exponential decay solution for comparison.
- `np.max()` to calculate the maximum numerical error.
- Matplotlib to plot the capacitor voltage over time.

### 5.5 Output

```text id="f3z8b5"
Campus Emergency Indicator - Capacitor Discharge
Solver success: True
Initial capacitor voltage: 5.00 V
Capacitor voltage after 5 s: 0.4104 V
Maximum error against exact solution: 1.140e-09 V
```

### 5.6 Interpretation

The capacitor initially had a voltage of 5 V.

After five seconds of discharging, the voltage decreased to 0.4104 V.

The maximum numerical error was approximately \(1.140 \times 10^{-9}\) V.

The graph demonstrated the exponential decrease in capacitor voltage over time.

This application shows how numerical ODE solvers can model electrical discharge behaviour.

## 6. Comparison of the Experiments

| Experiment | Initial/Final Voltage | Voltage after 5 seconds | Maximum Error |
|---|---|---:|---:|
| Original charging model | 5 V supply | 4.9663 V | 9.282e-10 V |
| Modified charging model | 6 V supply | 5.9596 V | 1.124e-09 V |
| Discharge application | 5 V initial | 0.4104 V | 1.140e-09 V |

The charging experiments showed how increasing the supply voltage changes the final capacitor voltage.

The discharge application demonstrated how capacitor voltage decreases when the stored charge is released through a resistor.

## 7. Conclusion

This task demonstrated how SciPy's `solve_ivp()` function can numerically solve ordinary differential equations.

The original RC circuit problem modelled capacitor charging and compared the numerical solution with the exact solution.

The parameter experiment demonstrated how changing the supply voltage affects capacitor charging.

The real-world application modelled capacitor discharge in a simplified campus emergency indicator circuit.

The very small numerical errors demonstrated the accuracy of the solver under the selected tolerances.
