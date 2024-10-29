import numpy as np
import matplotlib.pyplot as plt

def binomial_distribution(n, p, trials):
    """
    Generate a Binomial distribution.
    
    Parameters:
    n (int): Number of trials per sample
    p (float): Probability of success in each trial
    trials (int): Number of samples
    
    Returns:
    numpy.array: Array of outcomes (number of successes in each sample)
    """
    return np.random.binomial(n, p, trials)

# Parameters
n = 10      # Number of trials per sample
p = 0.5     # Probability of success
trials = 1000  # Number of samples

# Generate Binomial distributed data
data = binomial_distribution(n, p, trials)

# Plot the distribution
plt.figure(figsize=(10, 6))
plt.hist(data, bins=range(n+2), color='skyblue', edgecolor='black', align='left')
plt.title(f'Binomial Distribution (n = {n}, p = {p}, trials = {trials})')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.xticks(range(n+1))
plt.show()
