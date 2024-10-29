import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

def arithmetic_congruential_generator(seed, a, c, m, n):
    """
    Generates a sequence of random numbers using an arithmetic congruential method.
    
    Parameters:
    - seed: Initial seed value
    - a: Multiplier
    - c: Increment
    - m: Modulus
    - n: Number of random numbers to generate
    
    Returns:
    - random_numbers: List of generated random numbers
    """
    random_numbers = []
    x = seed
    
    for _ in range(n):
        x = (a * x + c) % m
        random_numbers.append(x / m)  # Normalize to [0, 1]
    
    return random_numbers

def calculate_autocorrelation(data, lag):
    """Calculates the autocorrelation of a data series at a given lag."""
    n = len(data)
    mean = np.mean(data)
    c0 = np.var(data) * (n - 1)  # Variance of the original series

    autocorr = np.correlate(data - mean, data - mean, mode='full')
    return autocorr[n - 1 + lag] / c0  # Return normalized autocorrelation

# Parameters for arithmetic congruential generator
seed = 42
a = 1664525
c = 1013904223
m = 2**32
n = 1000  # Number of random numbers to generate

# Generate random numbers
random_numbers = arithmetic_congruential_generator(seed, a, c, m, n)

# Plot histogram of generated random numbers
plt.figure(figsize=(12, 6))
plt.hist(random_numbers, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Histogram of Arithmetic Congruential Random Numbers')
plt.xlabel('Random Number')
plt.ylabel('Density')
plt.grid()
plt.show()

# Chi-square test for uniformity
# Prepare bins and observed frequencies
bins = np.linspace(0, 1, 21)  # Create 20 bins for [0, 1]
observed_frequencies, _ = np.histogram(random_numbers, bins=bins)

# Calculate expected frequency
expected_frequency = len(random_numbers) / len(observed_frequencies)

# Filter out any bins that have 0 observed frequency to prevent issues with Chi-square test
non_zero_bins = observed_frequencies > 0
observed_frequencies = observed_frequencies[non_zero_bins]
expected_frequencies = [expected_frequency] * len(observed_frequencies)

# Calculate Chi-square statistic if there are non-zero frequencies
if len(observed_frequencies) > 1:
    chi_square_stat, p_value = chisquare(observed_frequencies, f_exp=expected_frequencies)

    print(f'Chi-square statistic: {chi_square_stat:.4f}')
    print(f'p-value: {p_value:.4f}')

    # Interpretation of the results
    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis: The random numbers are not uniformly distributed.")
    else:
        print("Fail to reject the null hypothesis: The random numbers are uniformly distributed.")
else:
    print("Insufficient data for Chi-square test.")

# Calculate and print autocorrelation for different lags
lags = range(10)  # Calculate autocorrelation for lags 0 to 9
autocorrelations = [calculate_autocorrelation(random_numbers, lag) for lag in lags]

# Plot autocorrelation
plt.figure(figsize=(12, 6))
plt.stem(lags, autocorrelations, basefmt=" ", use_line_collection=True)
plt.title('Autocorrelation of Arithmetic Congruential Random Numbers')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.grid()
plt.show()
