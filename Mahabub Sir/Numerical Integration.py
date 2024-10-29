import random
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**3

n = 0  # Total points generated
m = 0  # Points under the curve

# Set the range for x and y values
x_min, x_max = 2.0, 5.0
y_max = 140  # Maximum y value to cover the range of y = x^3

# Monte Carlo simulation with scatter plot
for i in range(100):
    rx = random.uniform(x_min, x_max)
    ry = random.uniform(0, y_max)
    n += 1
    if ry <= func(rx):
        m += 1
        plt.scatter(rx, ry, color="green")  # Point is below or on the curve
    else:
        plt.scatter(rx, ry, color="blue")   # Point is above the curve

# Plot the actual function curve
x_vals = np.arange(x_min, x_max, 0.1)
y_vals = [func(x) for x in x_vals]
plt.plot(x_vals, y_vals, color="red", label="y = x^3")

# Display the result
estimated_area = (m / n) * (x_max - x_min) * y_max
print(f"Estimated Area under y = x^3 from x = {x_min} to x = {x_max}: {estimated_area}")

# Show plot with labels
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Monte Carlo Integration for y = x^3")
plt.show()
