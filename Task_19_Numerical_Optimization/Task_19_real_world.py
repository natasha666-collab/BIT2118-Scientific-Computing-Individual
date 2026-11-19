
"""
Campus IT Lab Server Capacity Planning
Numerical Optimization using SciPy
"""

from scipy.optimize import linprog

# Monthly server costs in Kenya Shillings
COST_A = 15000
COST_B = 22000

# Server capacity in simultaneous users
CAPACITY_A = 120
CAPACITY_B = 200

# Minimum required capacity
REQUIRED_CAPACITY = 1500


# Objective function: minimize total monthly cost
# x = number of Type A servers
# y = number of Type B servers

solution = linprog(
    c=[COST_A, COST_B],
    A_ub=[[-CAPACITY_A, -CAPACITY_B]],
    b_ub=[-REQUIRED_CAPACITY],
    bounds=[(0, None), (0, None)],
    method="highs"
)


print("Campus IT Lab Server Capacity Planning")
print("Optimization success:", solution.success)

if solution.success:
    x, y = solution.x

    total_capacity = CAPACITY_A * x + CAPACITY_B * y

    print(f"Type A servers: {x:.3f}")
    print(f"Type B servers: {y:.3f}")
    print(f"Total capacity: {total_capacity:.2f} users")
    print(f"Minimum monthly cost: KSh {solution.fun:,.2f}")

else:
    print("Optimization failed:", solution.message)


# Find the best whole-server combination
best_integer = None

for a in range(0, 20):
    for b in range(0, 20):

        capacity = CAPACITY_A * a + CAPACITY_B * b

        if capacity >= REQUIRED_CAPACITY:

            cost = COST_A * a + COST_B * b

            if best_integer is None or cost < best_integer[0]:
                best_integer = (cost, a, b, capacity)


print("\nWhole-Server Optimization")

if best_integer is not None:
    cost, a, b, capacity = best_integer

    print(f"Type A servers: {a}")
    print(f"Type B servers: {b}")
    print(f"Total capacity: {capacity} users")
    print(f"Minimum monthly cost: KSh {cost:,.2f}")
