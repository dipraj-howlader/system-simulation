import math
import random
import matplotlib.pyplot as plt

def func(x):
    val = 1 - (x ** 2)
    return math.sqrt(val)

m = 0  # Points under the curve
n = 0  # Total points generated

# Monte Carlo simulation
for i in range(100):
    rx = random.randint(0, 1000) / 1000
    ry = random.randint(0, 1000) / 1000
    n += 1

    if ry <= func(rx):
        m += 1
        plt.scatter(rx, ry, color="green")  # Point under the curve
    else:
        plt.scatter(rx, ry, color="blue")   # Point above the curve

# Plot the actual function curve
x = []
y = []
i = 0
h = 0.01
while i <= 1:
    x.append(i)
    y.append(round(func(i), 5))
    i += h
    i = round(i, 2)
plt.plot(x, y, color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Simulation for Estimating π/4")
plt.show()

# Area estimation
estimated_area = (m / n) * 4
actual_value = 3.1416
error_percentage = abs((actual_value - estimated_area) / actual_value) * 100

# Display results
print(f"Estimated Area: {estimated_area}")
print(f"Actual Value (π): {actual_value}")
print(f"Error Percentage: {error_percentage:.2f}%")
print(f"Points under curve (m): {m}, Total points (n): {n}")
