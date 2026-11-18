# Task 17: Ordinary Differential Equations – Euler Method

## 1. Introduction

An ordinary differential equation (ODE) describes how a quantity changes with respect to another variable, commonly time.

Euler's method is a numerical technique used to approximate solutions to ordinary differential equations when an exact solution is difficult to obtain.

The general form of an ODE is:

\[
\frac{dy}{dt}=f(t,y)
\]

Euler's method uses the following formula:

\[
y_{n+1}=y_n+h f(t_n,y_n)
\]

Where:

- \(y_n\) is the current value.
- \(y_{n+1}\) is the next estimated value.
- \(h\) is the step size.
- \(f(t_n,y_n)\) is the rate of change at the current point.

## 2. Mathematical Concepts

### 2.1 Newton's Law of Cooling

Newton's law of cooling describes how the temperature of an object changes as it approaches the surrounding temperature.

It is expressed as:

\[
\frac{dT}{dt}=-k(T-T_{\text{ambient}})
\]

Where:

- \(T\) is the object's temperature.
- \(T_{\text{ambient}}\) is the surrounding temperature.
- \(k\) is the cooling constant.
- \(t\) is time.

### 2.2 Euler's Method

Euler's method estimates the next temperature using the current temperature and its rate of change.

\[
T_{n+1}=T_n+h[-k(T_n-T_{\text{ambient}})]
\]

A smaller step size generally improves the accuracy of Euler's approximation but requires more calculations.

### 2.3 Applications

Euler's method can be applied to:

- Temperature and cooling systems.
- Population growth models.
- Chemical reaction models.
- Motion and velocity calculations.
- Electrical circuit simulations.

## 3. Original Problem: Newton's Law of Cooling

### 3.1 Problem Description

The original program models the cooling of a hot object using Newton's law of cooling.

Euler's method is used to estimate the temperature over 30 minutes and compare the numerical result with the exact mathematical solution.

### 3.2 Input Parameters

| Parameter | Value |
|---|---:|
| Ambient temperature | 25°C |
| Initial temperature | 90°C |
| Cooling constant | 0.12 |
| Step size | 1 minute |
| End time | 30 minutes |

### 3.3 Implementation

The program uses:

- NumPy to generate time values and store temperature estimates.
- A cooling-rate function to calculate the temperature change.
- A loop to apply Euler's method repeatedly.
- The exact mathematical solution for comparison.
- Matplotlib to plot the numerical and exact solutions.

### 3.4 Original Output

```text
Newton's Law of Cooling - Euler Method
Step size: 1.0 minutes
Euler temperature after 30 minutes: 26.4041 °C
Exact temperature after 30 minutes: 26.7760 °C
Absolute error: 0.3720 °C
```

### 3.5 Interpretation

After 30 minutes, Euler's method estimated the temperature as 26.4041°C, while the exact solution gave 26.7760°C.

The absolute error was 0.3720°C.

Euler's method slightly underestimated the final temperature because it approximates the rate of change at discrete time intervals.

The graph showed the temperature decreasing towards the ambient temperature.

## 4. Parameter Modification and Experiment

### 4.1 Modification

The original step size was:

`h = 1.0`

It was changed to:

`h = 0.5`

All other parameters remained unchanged.

This reduced the time interval between calculations from one minute to half a minute.

### 4.2 Modified Output

```text
Newton's Law of Cooling - Euler Method
Step size: 0.5 minutes
Euler temperature after 30 minutes: 26.5870 °C
Exact temperature after 30 minutes: 26.7760 °C
Absolute error: 0.1890 °C
```

### 4.3 Interpretation

Reducing the step size improved the accuracy of Euler's method.

The absolute error decreased from 0.3720°C to 0.1890°C.

The exact temperature remained unchanged because it is calculated independently of the numerical step size.

This experiment demonstrates that smaller step sizes generally produce more accurate Euler approximations, although they require more computational steps.

## 5. Real-World Application: Campus Server Room Temperature Monitoring

### 5.1 Problem Description

Computer servers and networking equipment generate heat during operation.

A campus server room requires cooling to maintain suitable operating temperatures.

This application uses Euler's method to estimate how the server room temperature decreases towards the surrounding temperature.

### 5.2 Assumptions

- The initial room temperature is 35°C.
- The surrounding temperature is 24°C.
- The cooling constant is 0.08.
- The cooling rate follows Newton's law of cooling.
- The temperature is estimated over 20 minutes.
- The cooling constant and ambient temperature remain constant during the simulation.

### 5.3 Mathematical Model

\[
\frac{dT}{dt}=-0.08(T-24)
\]

The initial temperature is:

\[
T(0)=35^\circ C
\]

### 5.4 Implementation

The program uses:

- NumPy to generate time values and store temperature estimates.
- Euler's method to calculate successive temperatures.
- The exact solution to evaluate numerical accuracy.
- Matplotlib to compare the estimated and exact temperature curves.

### 5.5 Output

```text
Campus Server Room Temperature Monitoring
Initial temperature: 35.00 °C
Ambient temperature: 24.00 °C
Euler temperature after 20 minutes: 26.0756 °C
Exact temperature after 20 minutes: 26.2209 °C
Absolute error: 0.1452 °C
```

### 5.6 Interpretation

The initial server room temperature was 35°C, while the ambient temperature was 24°C.

After 20 minutes, Euler's method estimated the room temperature as 26.0756°C.

The exact solution gave 26.2209°C, producing an absolute error of 0.1452°C.

The results demonstrate how Euler's method can approximate temperature changes in a simplified server room cooling model.

The graph showed the room temperature gradually approaching the ambient temperature.

## 6. Comparison of Results

| Experiment | Step Size | Euler Temperature | Exact Temperature | Absolute Error |
|---|---:|---:|---:|---:|
| Original cooling model | 1.0 min | 26.4041°C | 26.7760°C | 0.3720°C |
| Modified cooling model | 0.5 min | 26.5870°C | 26.7760°C | 0.1890°C |
| Server room application | 1.0 min | 26.0756°C | 26.2209°C | 0.1452°C |

## 7. Conclusion

This task demonstrated how Euler's method can be used to approximate solutions to ordinary differential equations.

Newton's law of cooling was used to model temperature changes over time.

The parameter experiment demonstrated that reducing the step size from 1.0 to 0.5 minutes reduced the numerical error.

The real-world application showed how Euler's method can be used to estimate temperature changes in a campus server room.

Euler's method is useful for modelling real-world systems whose behaviour can be described using differential equations.