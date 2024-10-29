import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Given data
mean_time_between_waves = 100
lambda_wave = 1 / mean_time_between_waves  # λ = 1 / mean
threshold_days = 120

# Probability calculation using the exponential distribution's CDF
# P(X > threshold_days) = 1 - P(X <= threshold_days) = 1 - CDF(threshold_days)
prob_more_than_120_days = 1 - expon.cdf(threshold_days, scale=1/lambda_wave)

print(f"Probability that it will take more than 120 days for the next wave to occur: {prob_more_than_120_days:.4f}")

# Simulation for various rate parameters
rate_params = [0.5, 1.0, 2.0, 4.0]
x_values = np.linspace(0, 5, 500)  # x-axis for plotting (scaled to visualize curves)

plt.figure(figsize=(12, 6))

for rate in rate_params:
    y_values = expon.pdf(x_values, scale=1/rate)
    plt.plot(x_values, y_values, label=f"λ = {rate}")

plt.title('Exponential Distributions for Different Rate Parameters')
plt.xlabel('Time')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
