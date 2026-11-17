# Task 13: Interpolation

## 1. Introduction

Interpolation is a numerical method used to estimate unknown values between known data points.

It is useful when measurements are available at specific intervals but estimates are required at intermediate points.

This task explores two interpolation methods:

- Linear interpolation
- Cubic spline interpolation

Python libraries such as NumPy, SciPy and Matplotlib are used to perform calculations and visualize the results.

## 2. Objectives

- Understand the mathematical concept of interpolation.
- Apply linear interpolation to estimate intermediate values.
- Apply cubic spline interpolation to produce smooth estimates.
- Compare the results obtained from both methods.
- Investigate how changing recorded data affects interpolation.
- Apply interpolation to a campus laboratory temperature monitoring problem.

## 3. Tools and Libraries

- Python
- NumPy
- SciPy (`scipy.interpolate`)
- Matplotlib

## 4. Original Problem

The original assignment involves estimating temperatures between hourly sensor measurements.

The recorded data is:

| Hour | Temperature |
|---|---:|
| 8:00 | 18.0°C |
| 9:00 | 20.0°C |
| 10:00 | 22.5°C |
| 11:00 | 24.0°C |
| 12:00 | 25.0°C |
| 13:00 | 25.5°C |
| 14:00 | 25.0°C |

The program uses linear interpolation and cubic spline interpolation to estimate temperatures every 10 minutes.

The target time selected for comparison is 10:30 AM.

### Original Program Output

```text
Linear estimate at 10:30: 23.25 C
Cubic estimate at 10:30: 23.36 C
```

### Interpretation

Linear interpolation estimated the temperature at 10:30 AM as 23.25°C.

Cubic spline interpolation estimated it as 23.36°C.

The difference between the estimates is 0.11°C.

The two methods produce slightly different results because they use different mathematical approaches.

Linear interpolation assumes a straight line between neighbouring measurements, while cubic spline interpolation uses smooth cubic curves.

The graph displayed the original hourly measurements alongside both interpolation curves.

## 5. Parameter Change Experiment

The original temperature measurement at 10:00 AM was changed from 22.5°C to 24.0°C.

The modified temperature array was:

```python
temperature = np.array(
    [18.0, 20.0, 24.0, 24.0, 25.0, 25.5, 25.0]
)
```

### Modified Program Output

```text
Linear estimate at 10:30: 24.00 C
Cubic estimate at 10:30: 24.23 C
```

### Comparison

| Method | Original estimate | Modified estimate | Difference |
|---|---:|---:|---:|
| Linear | 23.25°C | 24.00°C | +0.75°C |
| Cubic spline | 23.36°C | 24.23°C | +0.87°C |

### Interpretation

Changing the 10:00 AM measurement affected both interpolation methods.

The linear estimate increased by 0.75°C, while the cubic spline estimate increased by 0.87°C.

The graph also changed because the interpolation curves were recalculated using the modified temperature data.

This demonstrates that interpolation results depend on the original recorded measurements.

## 6. Real-World Application: Campus Computer Laboratory Temperature Monitoring

### Problem Description

A university computer laboratory uses a temperature sensor to record hourly temperature measurements.

However, a monitoring application requires temperature estimates every 15 minutes.

Interpolation can estimate the missing intermediate values using the available hourly measurements.

### Recorded Data

| Hour | Temperature |
|---|---:|
| 8:00 | 19.0°C |
| 9:00 | 20.5°C |
| 10:00 | 22.0°C |
| 11:00 | 23.5°C |
| 12:00 | 25.0°C |
| 13:00 | 26.0°C |
| 14:00 | 25.5°C |

### Method

The application uses:

- `interp1d()` for linear interpolation.
- `CubicSpline()` for cubic spline interpolation.
- NumPy to generate 15-minute intervals.
- Matplotlib to visualize the recorded and estimated temperatures.

Five selected intermediate times are evaluated.

### Program Output

```text
Campus Computer Laboratory Temperature Monitoring

Time: 8.25 hours | Linear: 19.38 C | Cubic: 19.37 C
Time: 9.50 hours | Linear: 21.25 C | Cubic: 21.25 C
Time: 10.75 hours | Linear: 23.12 C | Cubic: 23.12 C
Time: 12.50 hours | Linear: 25.50 C | Cubic: 25.62 C
Time: 13.75 hours | Linear: 25.62 C | Cubic: 25.83 C
```

### Interpretation

The application successfully estimated laboratory temperatures at five intermediate times.

At 8:15 AM, the two methods produced nearly identical estimates.

At 9:30 AM and 10:45 AM, both methods produced the same estimates to two decimal places.

At 12:30 PM, cubic spline interpolation estimated 25.62°C compared with 25.50°C from linear interpolation.

At 1:45 PM, the cubic spline estimate was 25.83°C compared with 25.62°C from linear interpolation.

The results demonstrate how different interpolation methods can produce slightly different estimates from the same measurements.

The graph displayed the hourly readings and both interpolation curves.

These readings are illustrative and do not represent actual measurements from a university laboratory.

## 7. Conclusion

This task demonstrated how interpolation estimates unknown values between recorded data points.

Linear interpolation and cubic spline interpolation were implemented using SciPy.

The original experiment estimated the temperature at 10:30 AM using both methods.

The parameter change experiment showed that modifying one recorded measurement affects the estimated values and the resulting graph.

The real-world application demonstrated how interpolation can support more frequent temperature monitoring when sensors only record measurements hourly.

The task highlighted the importance of interpolation in sensor monitoring, data estimation and scientific computing.