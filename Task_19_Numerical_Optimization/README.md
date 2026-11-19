# Task 19: Numerical Optimization

## 1. Introduction

This task explores numerical optimization using Python and SciPy. Numerical optimization is the process of finding the best solution to a problem while satisfying specified constraints.

The assignment demonstrates how optimization techniques can minimize costs while meeting resource requirements.

## 2. Original Program: Server Resource Allocation

### Objective

The original program uses SciPy's `minimize()` function with the SLSQP method to minimize the cost of allocating two types of server capacity.

### Mathematical Model

Let:

- x = allocation of Type A
- y = allocation of Type B

Objective function:

Minimize:

C(x, y) = 12x + 18y

Subject to:

100x + 170y ≥ 1000

x ≥ 0, y ≥ 0

### Original Output

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

### Interpretation

The continuous optimization solution allocates approximately 5.882 units of Type B capacity and no Type A capacity.

This achieves the required capacity of 1,000 at a minimum cost of approximately 105.88.

The best whole-unit solution uses six Type B units, achieving 1,020 capacity at a cost of 108.

## 3. Parameter Modification

The required capacity was increased from 1,000 to 1,200.

### Modified Output

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 7.059
Total capacity: 1200.00
Minimum planning cost: 127.06
Best nearby integer solution: (132, 2, 6, 1220)
```

### Comparison

| Measurement | Original | Modified |
|---|---:|---:|
| Required capacity | 1,000 | 1,200 |
| Type A allocation | 0.000 | 0.000 |
| Type B allocation | 5.882 | 7.059 |
| Minimum continuous cost | 105.88 | 127.06 |
| Integer solution cost | 108 | 132 |

### Interpretation

Increasing the required capacity increased the allocation of Type B and the minimum planning cost.

The continuous solution allows fractional allocations, whereas the integer solution represents whole units.

This demonstrates how changing a constraint affects an optimization result.

## 4. Real-World Application: Campus IT Lab Server Capacity Planning

### Problem Description

A university needs to plan its IT server resources to support students accessing computer laboratory systems simultaneously.

The objective is to minimize monthly server costs while ensuring enough capacity for at least 1,500 simultaneous users.

### Assumptions

| Parameter | Type A | Type B |
|---|---:|---:|
| Monthly cost | KSh 15,000 | KSh 22,000 |
| Capacity | 120 users | 200 users |

Required capacity: 1,500 simultaneous users.

These are illustrative planning values.

### Mathematical Model

Let:

- x = number of Type A servers
- y = number of Type B servers

Objective function:

Minimize:

C(x, y) = 15000x + 22000y

Subject to:

120x + 200y ≥ 1500

x ≥ 0, y ≥ 0

The practical solution also requires whole-number server quantities.

### Method Used

The application uses SciPy's `linprog()` function with the HiGHS solver to find the minimum-cost continuous solution.

A separate enumeration method checks whole-server combinations to identify the least expensive practical allocation.

### Actual Output

```text
Campus IT Lab Server Capacity Planning
Optimization success: True
Type A servers: 0.000
Type B servers: 7.500
Total capacity: 1500.00 users
Minimum monthly cost: KSh 165,000.00

Whole-Server Optimization
Type A servers: 1
Type B servers: 7
Total capacity: 1520 users
Minimum monthly cost: KSh 169,000.00
```

### Interpretation

The continuous solution requires 7.5 Type B servers and achieves exactly 1,500 users of capacity at a monthly cost of KSh 165,000.

However, physical servers cannot be purchased in fractional quantities.

The whole-server solution therefore uses one Type A server and seven Type B servers. It provides capacity for 1,520 users at a monthly cost of KSh 169,000.

This provides a practical allocation that meets the university's capacity requirement.

## 5. Conclusion

This task demonstrated how numerical optimization can be used to minimize costs while satisfying resource constraints.

The original program used SciPy's SLSQP optimization method, while the real-world application used linear programming through `scipy.optimize.linprog()`.

The experiments showed that increasing resource requirements increases the minimum cost. They also demonstrated the difference between continuous mathematical solutions and practical integer solutions.

Numerical optimization is useful in server allocation, network planning, resource management and other decision-making problems.

## 6. Technologies Used

- Python
- NumPy
- SciPy
- SciPy Optimize (`minimize()` and `linprog()`)

