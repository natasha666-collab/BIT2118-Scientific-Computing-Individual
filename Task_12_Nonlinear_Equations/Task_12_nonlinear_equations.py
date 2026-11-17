import numpy as np
from scipy.optimize import root

# Find intersections of:
# Circle: x^2 + y^2 = 4
# Parabola: y = x^2 - 1

def equations(z):
    x, y = z

    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]

# Try two different initial guesses
for guess in ([2.0, 1.5], [-2.0, 1.5]):
    solution = root(equations, guess)

    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()
