import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return 0.5 * x**2

# Generate x values
x = np.linspace(-10, 10, 400)

# Generate y values
y = f(x)

# Create the plot
plt.figure(figsize=(6, 4))
plt.plot(x, y, label='f(x) = 0.5*x^2')
plt.title('Plot of the function f(x) = 0.5*x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

