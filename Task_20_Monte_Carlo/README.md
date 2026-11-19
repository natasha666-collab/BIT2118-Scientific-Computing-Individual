# Task 20: Random Numbers and Monte Carlo Methods

## 1. Introduction

This task explores random numbers and Monte Carlo methods using Python.

Monte Carlo methods use repeated random sampling to estimate probabilities and study problems involving uncertainty.

The task demonstrates how random simulations can estimate the probability of network server overload and how the estimated probability changes as simulation parameters are modified.

## 2. Mathematical Concept

Monte Carlo methods estimate quantities by performing many random experiments.

If an event occurs in a certain proportion of simulations, its estimated probability is:

\[
P(\text{event})=\frac{\text{Number of successful events}}{\text{Total simulations}}
\]

A larger number of simulations generally produces a more stable probability estimate.

## 3. Original Program: Server Overload Probability

### Problem Description

A network administrator wants to estimate the probability that incoming network demand exceeds the server's available capacity.

The simulation generates random demand values using a normal distribution and counts how many exceed server capacity.

### Parameters

| Parameter | Value |
|---|---:|
| Server capacity | 1,000 |
| Mean demand | 850 |
| Standard deviation | 120 |
| Number of simulations | 100,000 |
| Random seed | 42 |

### Actual Output

```text
Estimated overload probability: 10.6160%
Number of overload cases: 10616 out of 100000
```

### Interpretation

The simulation generated 100,000 random network demand scenarios.

Out of these, 10,616 exceeded the server capacity of 1,000.

The estimated probability of overload was therefore 10.6160%.

The convergence graph illustrates how the estimated probability stabilizes as the number of simulations increases.

## 4. Parameter Modification

The average demand was increased from 850 to 900 while keeping all other parameters unchanged.

### Modified Output

```text
Estimated overload probability: 20.2210%
Number of overload cases: 20221 out of 100000
```

### Comparison

| Measurement | Original | Modified |
|---|---:|---:|
| Server capacity | 1,000 | 1,000 |
| Mean demand | 850 | 900 |
| Standard deviation | 120 | 120 |
| Simulations | 100,000 | 100,000 |
| Overload cases | 10,616 | 20,221 |
| Overload probability | 10.6160% | 20.2210% |

### Interpretation

Increasing the average demand from 850 to 900 increased the estimated overload probability from 10.6160% to 20.2210%.

This demonstrates that higher average demand increases the likelihood of exceeding available server capacity.

Monte Carlo simulation helps evaluate how uncertainty and changing conditions affect system reliability.

## 5. Real-World Application: Campus Network Service Reliability Estimation

### Problem Description

A university wants to estimate the probability that its campus network demand exceeds its available bandwidth during peak usage periods.

This information can help network administrators assess service reliability and plan bandwidth resources.

### Assumptions

| Parameter | Value |
|---|---:|
| Available bandwidth | 500 Mbps |
| Average network demand | 400 Mbps |
| Standard deviation | 65 Mbps |
| Number of simulations | 100,000 |
| Random seed | 42 |

These are illustrative planning values.

### Method Used

The application generates 100,000 random network demand scenarios using NumPy's normal distribution function.

Each scenario is compared against available bandwidth.

The probability of network overload is estimated by dividing the number of scenarios exceeding available bandwidth by the total number of simulations.

A convergence graph displays how the estimated probability changes as more simulations are performed.

### Actual Output

```text
Campus Network Service Reliability Estimation
Available bandwidth: 500.00 Mbps
Average network demand: 400.00 Mbps
Estimated overload probability: 6.1940%
Number of overload cases: 6194 out of 100000
```

### Interpretation

Out of 100,000 simulated network demand scenarios, 6,194 exceeded the available bandwidth of 500 Mbps.

The estimated probability of network overload was 6.1940%.

This indicates that even when average demand is below available bandwidth, fluctuations in network usage can cause occasional capacity overload.

The simulation provides a useful estimate that can support network capacity planning and reliability assessment.

## 6. Conclusion

This task demonstrated how random numbers and Monte Carlo methods can estimate probabilities in systems involving uncertainty.

The original program estimated network server overload probability. Changing the average demand showed how increased demand affects overload risk.

The real-world application extended the concept to campus network bandwidth planning.

Monte Carlo simulation is useful in network reliability analysis, risk assessment, capacity planning and other situations where repeated random sampling can help estimate uncertain outcomes.

## 7. Technologies Used

- Python
- NumPy
- Matplotlib
- NumPy random number generation
- Monte Carlo simulation

