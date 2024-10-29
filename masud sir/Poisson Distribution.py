import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def poisson_pmf(mean_rate, max_calls):
    """
    Computes the Poisson probability mass function for 0 to max_calls.
    
    Parameters:
    mean_rate (float): The average number of events per interval (λ)
    max_calls (int): Maximum number of calls to compute PMF for
    
    Returns:
    list: Probabilities for 0, 1, ..., max_calls events
    """
    return [poisson.pmf(k, mean_rate) for k in range(max_calls + 1)]

# Parameters
mean_rate_1 = 5   # Mean rate for first scenario
mean_rate_2 = 10  # Mean rate for second scenario
mean_rate_3 = 15  # Mean rate for third scenario
max_calls = 10    # Calculate PMF for 0, 1, ..., 10 calls

# Compute PMFs
pmf_5_calls = poisson_pmf(mean_rate_1, max_calls)
pmf_10_calls = poisson_pmf(mean_rate_2, max_calls)
pmf_15_calls = poisson_pmf(mean_rate_3, max_calls)

# Plotting the PMF for different mean rates
x = np.arange(0, max_calls + 1)

plt.figure(figsize=(12, 6))

# Plot for λ = 5 calls per hour
plt.subplot(1, 3, 1)
plt.stem(x, pmf_5_calls, basefmt=" ")
plt.title('Poisson PMF (λ = 5 calls/hour)')
plt.xlabel('Number of Calls')
plt.ylabel('Probability')
plt.ylim(0, max(pmf_5_calls) + 0.05)

# Plot for λ = 10 calls per hour
plt.subplot(1, 3, 2)
plt.stem(x, pmf_10_calls, basefmt=" ", linefmt='C1-', markerfmt='C1o')
plt.title('Poisson PMF (λ = 10 calls/hour)')
plt.xlabel('Number of Calls')
plt.ylabel('Probability')
plt.ylim(0, max(pmf_10_calls) + 0.05)

# Plot for λ = 15 calls per hour
plt.subplot(1, 3, 3)
plt.stem(x, pmf_15_calls, basefmt=" ", linefmt='C2-', markerfmt='C2o')
plt.title('Poisson PMF (λ = 15 calls/hour)')
plt.xlabel('Number of Calls')
plt.ylabel('Probability')
plt.ylim(0, max(pmf_15_calls) + 0.05)

plt.tight_layout()
plt.show()
