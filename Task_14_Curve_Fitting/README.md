# Task 14: Curve Fitting and Approximation

## 1. Introduction

Curve fitting is a numerical method used to find a mathematical function that best represents a set of observed data points.

It is useful when measurements follow a pattern and we want to describe the relationship between variables or estimate values that have not been measured.

This task demonstrates quadratic curve fitting using Python, NumPy, SciPy and Matplotlib.

## 2. Mathematical Concept

The least-squares method determines model parameters by minimizing the sum of squared differences between actual observations and predicted values.

For this task, a quadratic model is used:

\[
y=ax^2+bx+c
\]

Where:
- \(x\) is the independent variable.
- \(y\) is the dependent variable.
- \(a\), \(b\), and \(c\) are fitted coefficients.

The Root Mean Square Error (RMSE) measures the difference between actual and predicted values:

\[
RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2}
\]

A smaller RMSE generally indicates a closer fit to the observed data.

## 3. Tools and Libraries

- Python
- NumPy – numerical arrays and calculations.
- SciPy – curve fitting using `scipy.optimize.curve_fit`.
- Matplotlib – plotting observations and fitted curves.

## 4. Original Problem: Server Response-Time Modelling

### Objective

Fit a quadratic model to measurements of server response time at different numbers of concurrent users.

The model is then used to estimate response time at 400 concurrent users.

### Input Data

| Concurrent users | Response time (ms) |
|---:|---:|
| 50 | 82 |
| 100 | 95 |
| 150 | 115 |
| 200 | 145 |
| 250 | 185 |
| 300 | 238 |
| 350 | 305 |

### Original Output

```text
Fitted model: y = 0.002167x^2 + -0.1345x + 85.00
RMSE: 1.55 ms
Predicted response at 400 users: 377.86 ms
```

### Interpretation

The fitted quadratic model describes the relationship between concurrent users and server response time.

The positive quadratic coefficient indicates that response time increases at an accelerating rate as the number of users increases.

The RMSE of 1.55 ms indicates that the fitted model follows the measured observations closely.

The predicted response time at 400 concurrent users is 377.86 ms. This is an extrapolated estimate because the original measurements only extend to 350 users.

A graph was generated showing the measured data points and fitted quadratic curve.

## 5. Parameter-Change Experiment

### Objective

Investigate how changing one measurement affects the fitted model.

The response time at 250 concurrent users was increased from 185 ms to 200 ms.

### Modified Input Data

```python
response_ms = np.array([82, 95, 115, 145, 200, 238, 305], dtype=float)
```

### Modified Output

```text
Fitted model: y = 0.001952x^2 + -0.0381x + 78.57
RMSE: 4.21 ms
Predicted response at 400 users: 375.71 ms
```

### Comparison

| Measurement | Original | Modified |
|---|---:|---:|
| Response at 250 users | 185 ms | 200 ms |
| Quadratic coefficient | 0.002167 | 0.001952 |
| Linear coefficient | -0.1345 | -0.0381 |
| Constant | 85.00 | 78.57 |
| RMSE | 1.55 ms | 4.21 ms |
| Prediction at 400 users | 377.86 ms | 375.71 ms |

### Interpretation

Changing the response-time measurement at 250 users affected all three fitted coefficients.

The RMSE increased from 1.55 ms to 4.21 ms, indicating that the modified quadratic model fits the complete dataset less closely.

The predicted response time at 400 users decreased slightly from 377.86 ms to 375.71 ms.

This demonstrates that curve fitting considers all observations when determining the best-fitting model. Changing one measurement can therefore affect the entire fitted curve.

## 6. Real-World Application: Campus Wi-Fi Bandwidth Demand Estimation

### Problem Description

A campus IT department needs to estimate network bandwidth requirements as more devices connect to the campus Wi-Fi network.

Curve fitting can help model the relationship between the number of connected devices and bandwidth consumption.

The application uses illustrative measurements and a quadratic model to estimate bandwidth demand for 80 connected devices.

### Input Data

| Connected devices | Bandwidth consumption (Mbps) |
|---:|---:|
| 10 | 8 |
| 20 | 18 |
| 30 | 32 |
| 40 | 51 |
| 50 | 75 |
| 60 | 105 |
| 70 | 140 |

### Output

```text
Campus Wi-Fi Bandwidth Demand Estimation
Fitted model: y = 0.025595x^2 + 0.1417x + 4.43
RMSE: 0.34 Mbps
Predicted bandwidth for 80 devices: 179.57 Mbps
```

### Interpretation

The fitted quadratic model describes the relationship between connected devices and network bandwidth consumption.

The RMSE of 0.34 Mbps indicates that the model closely follows the illustrative measurements.

The estimated bandwidth requirement for 80 connected devices is 179.57 Mbps.

This application demonstrates how numerical curve fitting can support campus network capacity planning and help IT departments estimate future bandwidth requirements.

The prediction is an estimate rather than a guarantee of actual network usage, since real demand also depends on the activities performed by connected users.

A graph was generated showing the measured bandwidth values and the fitted quadratic curve.

## 7. Conclusion

This task demonstrated curve fitting and approximation using Python.

The original experiment modelled server response time against concurrent users. The parameter-change experiment showed how modifying one observation affects fitted coefficients, RMSE and predictions.

The real-world application demonstrated how curve fitting can estimate campus Wi-Fi bandwidth demand.

Overall, curve fitting is useful for understanding relationships between measured variables, identifying trends and making predictions from observed data.
