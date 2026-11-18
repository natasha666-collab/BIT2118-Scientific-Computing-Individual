# Task 16: Numerical Integration

## 1. Introduction

Numerical integration is a numerical method used to estimate the area under a curve or calculate the accumulated value of a quantity over an interval.

It is useful when an exact mathematical integral is difficult to calculate or when data is available as discrete measurements.

This task demonstrates two numerical integration methods:

- Trapezoidal Rule
- Simpson's Rule

The implementation uses NumPy and SciPy.

## 2. Mathematical Concepts

### 2.1 Trapezoidal Rule

The trapezoidal rule estimates the area under a curve by dividing it into trapezoids.

For equally or unequally spaced data, the method approximates the total area by adding the areas of individual trapezoids.

### 2.2 Simpson's Rule

Simpson's rule approximates the curve using parabolic segments.

It generally provides more accurate estimates than the trapezoidal rule for sufficiently smooth functions when its assumptions are satisfied.

### 2.3 Applications

Numerical integration is used in:

- Electrical energy consumption estimation.
- Water-flow and fluid-volume calculations.
- Distance estimation from velocity measurements.
- Signal processing.
- Probability calculations.

## 3. Original Problem: Smart Meter Energy Estimation

### 3.1 Problem Description

A smart electricity meter records power consumption every two hours.

The objective is to estimate the total electrical energy consumed over the 12-hour monitoring period using the trapezoidal rule and Simpson's rule.

### 3.2 Input Data

Time readings in hours:

`[0, 2, 4, 6, 8, 10, 12]`

Power readings in kilowatts:

`[0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9]`

### 3.3 Implementation

The program uses:

- `numpy.array()` to store time and power readings.
- `np.trapezoid()` to estimate energy using the trapezoidal rule.
- `scipy.integrate.simpson()` to estimate energy using Simpson's rule.
- `abs()` to calculate the difference between the estimates.

### 3.4 Original Output

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

### 3.5 Interpretation

The trapezoidal rule estimated energy consumption at 15.700 kWh, while Simpson's rule estimated 15.800 kWh.

The difference between the two estimates was 0.100 kWh.

Both methods provide approximations of the accumulated electrical energy over the monitoring period.

## 4. Parameter Modification and Experiment

### 4.1 Modification

The power reading at 6 hours was increased from 1.8 kW to 2.2 kW.

Original power readings:

`[0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9]`

Modified power readings:

`[0.8, 1.0, 1.4, 2.2, 1.6, 1.2, 0.9]`

All other readings remained unchanged.

### 4.2 Modified Output

```text
Energy using trapezoidal rule: 16.500 kWh
Energy using Simpson's rule: 16.867 kWh
Difference between estimates: 0.367 kWh
```

### 4.3 Interpretation

Increasing the power reading at 6 hours increased the estimated total energy consumption.

The trapezoidal estimate increased from 15.700 kWh to 16.500 kWh.

The Simpson's estimate increased from 15.800 kWh to 16.867 kWh.

The difference between the estimates also increased from 0.100 kWh to 0.367 kWh.

This demonstrates how changes in measured values affect numerical integration results.

## 5. Real-World Application: Campus Water Tank Flow Monitoring

### 5.1 Problem Description

A campus water tank monitoring system records water flow rates every 10 minutes.

The objective is to estimate the total volume of water that flows into the tank during a one-hour period.

The trapezoidal rule and Simpson's rule are used to estimate the accumulated water volume.

### 5.2 Assumptions

- Water flow measurements are collected at regular 10-minute intervals.
- The flow rate changes smoothly between recorded measurements.
- The readings represent litres per minute.
- The seven measurements cover a one-hour monitoring period.

### 5.3 Input Data

Time in minutes:

`[0, 10, 20, 30, 40, 50, 60]`

Water flow rate in litres per minute:

`[12, 15, 18, 20, 17, 14, 10]`

### 5.4 Implementation

The program uses:

- NumPy arrays to store time and flow-rate measurements.
- `np.trapezoid()` to estimate the total water volume using trapezoids.
- `simpson()` to estimate the total water volume using parabolic approximations.
- `abs()` to calculate the difference between the estimates.

### 5.5 Output

```text
Campus Water Tank Flow Monitoring
Water volume using trapezoidal rule: 950.00 litres
Water volume using Simpson's rule: 960.00 litres
Difference between estimates: 10.00 litres
```

### 5.6 Interpretation

The trapezoidal rule estimated that 950 litres of water flowed into the tank during the one-hour period.

Simpson's rule estimated 960 litres.

The difference between the two estimates was 10 litres.

This demonstrates how numerical integration can be applied in water management systems to estimate total water flow from periodic flow-rate measurements.

## 6. Comparison of the Two Methods

| Feature | Trapezoidal Rule | Simpson's Rule |
|---|---|---|
| Approximation | Trapezoids | Parabolic segments |
| Basic approach | Straight-line approximation between points | Curved approximation between points |
| Application | Area and accumulated quantities | Area and accumulated quantities |
| Result | Approximate integral | Approximate integral |

The two methods may produce different results because they use different approximations of the area under a curve.

## 7. Conclusion

This task demonstrated how numerical integration can estimate accumulated quantities from discrete measurements.

The original smart-meter problem showed how numerical integration estimates electrical energy consumption.

The parameter experiment demonstrated how changing one power measurement affects the final estimate.

The real-world application demonstrated how numerical integration can estimate the total volume of water flowing into a campus water tank.

Both the trapezoidal rule and Simpson's rule are useful numerical methods for solving practical accumulation problems.
