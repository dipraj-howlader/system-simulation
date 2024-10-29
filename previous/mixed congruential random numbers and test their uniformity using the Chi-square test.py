import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

def mixed_congruential_generator(seed, a1, c1, m1, a2, c2, m2, n):
    """
    Generates a sequence of random numbers using a mixed congruential method.
    
    Parameters:
    - seed: Initial seed value
    - a1, c1, m1: Parameters for the first LCG
    - a2, c2, m2: Parameters for the second LCG
    - n: Number of random numbers to generate
    
    Returns:
    - random_numbers: List of generated random numbers
    """
    random_numbers = []
    x1 = seed
    x2 = seed
    
    for _ in range(n):
        x1 = (a1 * x1 + c1) % m1
        x2 = (a2 * x2 + c2) % m2
        mixed_number = (x1 + x2) % m1  # Combine the two sequences
        random_numbers.append(mixed_number / m1)  # Normalize to [0, 1]
    
    return random_numbers

# Parameters for mixed congruential generator
seed = 42
a1, c1, m1 = 1664525, 1013904223, 2**32
a2, c2, m2 = 1103515245, 12345, 2**31
n = 1000  # Number of random numbers to generate

# Generate random numbers
random_numbers = mixed_congruential_generator(seed, a1, c1, m1, a2, c2, m2, n)

# Plot histogram of generated random numbers
plt.figure(figsize=(12, 6))
plt.hist(random_numbers, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Histogram of Mixed Congruential Random Numbers')
plt.xlabel('Random Number')
plt.ylabel('Density')
plt.grid()
plt.show()

# Chi-square test for uniformity
# Prepare bins and observed frequencies
bins = np.linspace(0, 1, 21)  # Create 20 bins for [0, 1]
observed_frequencies, bin_edges = np.histogram(random_numbers, bins=bins)

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
