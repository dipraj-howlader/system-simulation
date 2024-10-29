import numpy as np
import matplotlib.pyplot as plt

def bernoulli_distribution(p, n):
    """
    Generate a Bernoulli distribution.
    
    Parameters:
    p (float): Probability of success (0 <= p <= 1)
    n (int): Number of trials
    
    Returns:
    numpy.array: Array of outcomes (0s and 1s)
    """
    return np.random.binomial(1, p, n)

# Parameters
p = 0.5  # Probability of success (e.g., 0.5 for a fair coin flip)
n = 1000  # Number of trials

# Generate Bernoulli distributed data
data = bernoulli_distribution(p, n)

# Count occurrences of 0 and 1
counts = np.bincount(data)

# Plot the distribution
plt.figure(figsize=(6, 4))
plt.bar([0, 1], counts, color=['skyblue', 'salmon'], tick_label=['0 (Failure)', '1 (Success)'])
plt.title(f'Bernoulli Distribution (p = {p}, n = {n})')
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.show()
