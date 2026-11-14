# Task 4: Floating-Point Arithmetic and Numerical Errors

## 1. Introduction

This task explores floating-point arithmetic and numerical errors in computer calculations using Python and NumPy.

Computers store most real numbers using a finite number of binary digits. Consequently, some decimal numbers cannot be represented exactly, resulting in small numerical inaccuracies.

The task demonstrates floating-point comparisons, absolute error, relative error, round-off error and numerical stability.

## 2. Mathematical Concepts

### Floating-Point Arithmetic

Floating-point arithmetic is the computer representation of real numbers using finite precision. Some decimal values, such as 0.1 and 0.2, cannot be represented exactly in binary.

### Absolute Error

Absolute error measures the difference between the true value and the approximate value.

\[
E_a=|x_{\text{true}}-x_{\text{approx}}|
\]

### Relative Error

Relative error measures the absolute error in relation to the magnitude of the true value.

\[
E_r=\frac{E_a}{|x_{\text{true}}|}
\]

### Round-off Error

Round-off error occurs when a computer approximates a number because it cannot store an unlimited number of digits.

### Truncation Error

Truncation error occurs when an exact mathematical process is replaced by an approximation.

### Numerical Stability

A numerically stable formula maintains accuracy during computation and avoids unnecessary loss of precision.

## 3. Original Problem

The original problem demonstrates why directly comparing floating-point numbers can produce unexpected results.

For example, adding 0.1 and 0.2 may produce 0.30000000000000004 instead of exactly 0.3.

The program also calculates absolute and relative errors when approximating the square root of 2. Finally, it compares a numerically unstable formula with a more stable equivalent formulation.

## 4. Original Program

**File:** `Task_04_numerical_errors.py`

The program uses NumPy to perform floating-point comparisons and calculate numerical errors.

It also compares the following two mathematically equivalent expressions:

Direct formula:

\[
\frac{\sqrt{1+x}-1}{x}
\]

Stable formula:

\[
\frac{1}{\sqrt{1+x}+1}
\]

The second expression avoids subtracting two nearly equal numbers.

## 5. Original Program Results and Interpretation

The program produced the following output:

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

**Interpretation:**

- The addition of 0.1 and 0.2 produces a slightly different value from 0.3 because of floating-point representation.
- The exact comparison returns False, while `np.isclose()` returns True because the values are sufficiently close within its default tolerance.
- The absolute error when approximating the square root of 2 is approximately 0.00021356.
- The relative error is approximately 0.01510114%.
- The direct formula becomes less accurate as x becomes smaller, while the stable formula maintains a result closer to 0.5.

## 6. Parameter Modification and Results

The original program used the following input values:

```python
for x in [1e-4, 1e-8, 1e-12]:
```

The parameter was modified to include a smaller value:

```python
for x in [1e-4, 1e-8, 1e-12, 1e-14]:
```

**Modified output:**

```text
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
x=1e-14: direct=0.488498130835, stable=0.500000000000
```

**Interpretation:**

As x becomes smaller, the direct formula becomes increasingly inaccurate.

At x = 1e-14, the direct formula produces approximately 0.48849813, whereas the stable formula produces 0.5 to the displayed precision.

This demonstrates subtractive cancellation, which occurs when subtracting two nearly equal numbers and losing significant numerical precision.

The experiment shows why choosing a numerically stable mathematical expression is important.

## 7. Real-World Application: Temperature Sensor Error Analysis

### Problem

A scientific temperature sensor measures a temperature that is compared with a reference value. Numerical error analysis is used to determine how accurate the sensor reading is.

### Assumptions

- The reference temperature is 25.0°C.
- The measured temperature is 25.2°C.
- An absolute tolerance of 0.5°C is considered acceptable.
- The reference temperature is assumed to be accurate for this demonstration.

### Input Data

- Reference temperature: 25.0°C
- Measured temperature: 25.2°C
- Acceptable tolerance: 0.5°C

### Program

**File:** `Task_04_real_world.py`

The program calculates absolute and relative errors and uses NumPy's `isclose()` function to determine whether the measurement is within the specified tolerance.

### Output

```text
TEMPERATURE SENSOR ERROR ANALYSIS
---------------------------------
Reference temperature: 25.0 °C
Measured temperature: 25.2 °C
Absolute error: 0.2000 °C
Relative error: 0.80%
Within acceptable tolerance: True
```

### Interpretation

The sensor reading differs from the reference temperature by 0.2°C, representing a relative error of 0.80%.

Since the difference is below the specified tolerance of 0.5°C, the measurement is considered acceptable in this example.

This application demonstrates how numerical error calculations and tolerance-based comparisons can be used to assess the accuracy of scientific measurements.

## 8. Conclusion

This task demonstrated how floating-point representation can introduce small inaccuracies into computer calculations.

It explored absolute error, relative error, round-off error, truncation error and numerical stability. The parameter modification demonstrated how subtractive cancellation can reduce the accuracy of a direct mathematical formula.

The temperature sensor application further demonstrated how error calculations and tolerance-based comparisons can be used in a practical scientific measurement scenario.

Overall, the task highlights the importance of understanding numerical precision and selecting appropriate computational methods when solving scientific and engineering problems.