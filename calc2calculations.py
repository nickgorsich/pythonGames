# calc2calculations.py

import os
import numpy as np
from scipy.integrate import quad

'''-----------------------BOUNDS-------------------------'''
b = np.pi/2   # Upper bound

a = 0    # Lower bound
'''------------------------------------------------------'''

'6.5 ARC LENGTH CALCULATOR'
# def arc_length_integrand(x):
#     # Example: y = tan(x), so dy/dx = sec^2(x)
#     derivative = 1 / np.cos(x)**2  # sec^2(x)
#     return np.sqrt(1 + derivative**2)# 

'6.6 SURFACE AREA OF A SOLID OF REVOLUTION CALCULATOR'
def surface_area_integrand(x):
    radius = 4*np.sin(x)  
    derivative_squared = (       4*np.cos(x)        )**2 
    return radius * np.sqrt(1 + derivative_squared)

# Compute integrals
# arc_length, arc_error = quad(arc_length_integrand, a, b)
surface_area, sa_error = quad(surface_area_integrand, a, b)
surface_area *= 2 * np.pi  # Multiply by 2π for surface area


os.system('cls')

# Output
print(f"--- Arc Length Calculator ---")
# print(f"Arc length from {a:.4f} to {b:.4f} ≈ {arc_length:.6f}")
#print(f"Estimated error: {arc_error:.2e}\n")

print(f"--- Surface Area Calculator (Revolution about x-axis) ---")
print(f"Surface area from {a:.4f} to {b:.4f} ≈ {surface_area:.6f} square units")
#print(f"Estimated error: {sa_error:.2e}")







import numpy as np
from scipy.integrate import quad
from sympy import symbols, integrate, sin, pprint # type: ignore

# ' === Numerical Integral ==='
# def f(x):
#     return np.sin(x**2)

# a, b = 6,13
# numerical_result, _ = quad(f, a, b)
# print(f"Numerical integral from {a} to {b} ≈ {numerical_result:.6f}")


# '=== Symbolic Integral ==='
# x = symbols('x')
# expr = sin(x**2)
# print("\nSymbolic indefinite integral:")
# pprint(integrate(expr, x))
