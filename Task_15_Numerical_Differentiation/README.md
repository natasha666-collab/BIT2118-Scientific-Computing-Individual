# Task 15: Numerical Differentiation

## 1. Introduction

Numerical differentiation is a numerical method used to approximate the derivative of a function using nearby data points.

A derivative measures the rate of change of a quantity. For example, the derivative of position with respect to time represents velocity.

This task demonstrates numerical differentiation using GPS position measurements to estimate vehicle speed.

The implementation uses NumPy for numerical calculations and Matplotlib for visualization.

## 2. Mathematical Concepts

### Forward Difference

Forward difference estimates the derivative using the current point and the next point.

\[
f'(x)\approx\frac{f(x+h)-f(x)}{h}
\]

### Backward Difference

Backward difference uses the current point and the previous point.

\[
f'(x)\approx\frac{f(x)-f(x-h)}{h}
\]

### Central Difference

Central difference uses points on both sides of the current point.

\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]

Central difference is often more accurate than forward and backward differences for the same step size when the function is sufficiently smooth.

## 3. Tools and Libraries

- Python
- NumPy – storing measurements and performing numerical calculations.
- Matplotlib – plotting estimated speed against time.

## 4. Original Problem: Estimating Vehicle Speed from GPS Data

### Objective

A GPS device records a vehicle's position at different times. Numerical differentiation is used to estimate its speed at each recorded time.

The implementation uses:
- Forward difference for the first measurement.
- Central difference for interior measurements.
- Backward difference for the final measurement.

### Input Data

| Time (seconds) | Position (metres) |
|---:|---:|
| 0 | 0.0 |
| 1 | 4.8 |
| 2 | 10.2 |
| 3 | 16.1 |
| 4 | 22.7 |
| 5 | 30.0 |
| 6 | 38.0 |

### Original Output

```text
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=5.65m/s
t=3s, position=16.1m, estimated speed=6.25m/s
t=4s, position=22.7m, estimated speed=6.95m/s
t=5s, position=30.0m, estimated speed=7.65m/s
t=6s, position=38.0m, estimated speed=8.00m/s
```

### Interpretation

The estimated speed increases from 4.80 m/s at the beginning to 8.00 m/s at the final measurement.

This indicates that the vehicle is accelerating during the recorded period.

The graph visualizes the increase in estimated speed over time.

## 5. Parameter-Change Experiment

### Objective

Investigate how changing one GPS position measurement affects the estimated speeds.

The position at 3 seconds was changed from 16.1 metres to 17.1 metres.

### Modified Input

```python
position = np.array([0.0, 4.8, 10.2, 17.1, 22.7, 30.0, 38.0])
```

### Modified Output

```text
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=6.15m/s
t=3s, position=17.1m, estimated speed=6.25m/s
t=4s, position=22.7m, estimated speed=6.45m/s
t=5s, position=30.0m, estimated speed=7.65m/s
t=6s, position=38.0m, estimated speed=8.00m/s
```

### Comparison

| Time (s) | Original speed (m/s) | Modified speed (m/s) |
|---:|---:|---:|
| 0 | 4.80 | 4.80 |
| 1 | 5.10 | 5.10 |
| 2 | 5.65 | 6.15 |
| 3 | 6.25 | 6.25 |
| 4 | 6.95 | 6.45 |
| 5 | 7.65 | 7.65 |
| 6 | 8.00 | 8.00 |

### Interpretation

Changing the position measurement at 3 seconds affected the estimated speeds at 2 and 4 seconds.

This occurs because central difference uses measurements on both sides of the point being evaluated.

The speed at 2 seconds increased from 5.65 m/s to 6.15 m/s, while the speed at 4 seconds decreased from 6.95 m/s to 6.45 m/s.

The experiment demonstrates that numerical differentiation is sensitive to changes in measured data.

The modified graph also showed changes in the estimated speed curve.

## 6. Real-World Application: Campus Shuttle Speed Monitoring

### Problem Description

A university transport department wants to estimate the speed of a campus shuttle using GPS position measurements collected at regular intervals.

Numerical differentiation can estimate the shuttle's speed from its recorded positions.

The application uses illustrative GPS measurements collected every five seconds.

### Input Data

| Time (seconds) | Position (metres) |
|---:|---:|
| 0 | 0 |
| 5 | 18 |
| 10 | 42 |
| 15 | 72 |
| 20 | 108 |
| 25 | 150 |
| 30 | 198 |

### Output

```text
Campus Shuttle Speed Monitoring
Time: 0s | Position: 0.0m | Estimated speed: 3.60m/s
Time: 5s | Position: 18.0m | Estimated speed: 4.20m/s
Time: 10s | Position: 42.0m | Estimated speed: 5.40m/s
Time: 15s | Position: 72.0m | Estimated speed: 6.60m/s
Time: 20s | Position: 108.0m | Estimated speed: 7.80m/s
Time: 25s | Position: 150.0m | Estimated speed: 9.00m/s
Time: 30s | Position: 198.0m | Estimated speed: 9.60m/s
```

### Interpretation

The estimated shuttle speed increases from 3.60 m/s to 9.60 m/s.

The final estimated speed is equivalent to:

\[
9.60\times3.6=34.56\text{ km/h}
\]

This demonstrates how numerical differentiation can estimate vehicle speed using GPS position measurements.

A transport department could use similar calculations to analyse vehicle movement and monitor changes in speed.

The graph displays the estimated shuttle speed at each recorded time.

The measurements in this application are illustrative and do not represent actual campus shuttle records.

## 7. Conclusion

This task demonstrated numerical differentiation using forward, central and backward difference methods.

The original experiment estimated vehicle speed from GPS measurements. The parameter-change experiment demonstrated how modifying one position measurement can affect multiple derivative estimates.

The real-world application demonstrated how a campus transport department could estimate shuttle speed using GPS data.

Overall, numerical differentiation is useful for estimating rates of change when only discrete measurements are available.