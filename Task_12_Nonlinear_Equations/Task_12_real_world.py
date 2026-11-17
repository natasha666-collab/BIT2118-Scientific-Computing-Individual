from scipy.optimize import root


# Simplified campus network server workload model
# x = normalized workload on Server A
# y = normalized workload on Server B

def workload_equations(z):
    x, y = z

    return [
        x**2 + y - 10,
        x + y**2 - 10
    ]


# Test the solver using two different initial guesses
initial_guesses = ([2.0, 3.0], [3.0, 2.0])

for guess in initial_guesses:
    solution = root(workload_equations, guess)

    x, y = solution.x

    print("Initial guess:", guess)
    print(f"Server A workload: {x:.6f} units")
    print(f"Server B workload: {y:.6f} units")
    print("Residuals:", workload_equations(solution.x))
    print("Converged:", solution.success)
    print()
