from scipy.optimize import root_scalar

# Illustrative campus ICT equipment replacement cash flows
cash_flows = [-20000, 6000, 7000, 8000, 9000]

# Net Present Value function
def npv(rate):
    return sum(
        cf / (1 + rate)**t
        for t, cf in enumerate(cash_flows)
    )

# Derivative of the NPV function
def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

# Newton-Raphson method
newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.15,
    method="newton",
    xtol=1e-12
)

# Secant method
secant = root_scalar(
    npv,
    x0=0.10,
    x1=0.25,
    method="secant",
    xtol=1e-12
)

print(f"Equipment replacement IRR using Newton-Raphson: {newton.root:.6%}")
print(f"Equipment replacement IRR using Secant: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")
print(f"NPV at Secant solution: {npv(secant.root):.6f}")
