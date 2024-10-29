import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

def multiplicative_congruential_generator(seed, a, m, n):
    """
    Generates a sequence of random numbers using a multiplicative congruential method.
    
    Parameters:
    - seed: Initial seed value
    - a: Multiplier
    - m: Modulus
    - n: Number of random numbers to generate
    
    Returns:
    - random_numbers: List of generated random numbers
    """
    random_numbers = []
    x = seed
    
    for _ in range(n):
        x = (a * x) % m
        random_numbers.append(x / m)  # Normalize to [0, 1]
    
    return random_numbers

def poker_test(random_numbers, hand_size=5):
    """Performs the poker test on the generated random numbers."""
    n_hands = len(random_numbers) // hand_size  # Number of complete hands
    hands = np.array_split(random_numbers[:n_hands * hand_size], n_hands)  # Split into hands
    distinct_counts = [len(np.unique(hand)) for hand in hands]  # Count distinct values in each hand
    
    return distinct_counts

# Parameters for multiplicative congruential generator
seed = 42
a = 1664525
m = 2**32
n = 1000  # Number of random numbers to generate

# Generate random numbers
random_numbers = multiplicative_congruential_generator(seed, a, m, n)

# Plot histogram of generated random numbers
plt.figure(figsize=(12, 6))
plt.hist(random_numbers, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Histogram of Multiplicative Congruential Random Numbers')
plt.xlabel('Random Number')
plt.ylabel('Density')
plt.grid()
plt.show()

# Poker test
hand_size = 5  # Size of each hand
distinct_counts = poker_test(random_numbers, hand_size)

# Prepare data for Chi-square test
max_distinct = hand_size  # Maximum distinct values in a hand
observed_frequencies = np.zeros(max_distinct + 1)  # Count frequencies of distinct counts

# Count frequencies of distinct counts
for count in distinct_counts:
    observed_frequencies[count] += 1

# Chi-square test for uniformity of the observed frequencies
expected_frequency = len(distinct_counts) / max_distinct
expected_frequencies = [expected_frequency] * (max_distinct + 1)

chi_square_stat, p_value = chisquare(observed_frequencies, f_exp=expected_frequencies)

print(f'Chi-square statistic: {chi_square_stat:.4f}')
print(f'p-value: {p_value:.4f}')

# Interpretation of the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The random numbers do not pass the poker test.")
else:
    print("Fail to reject the null hypothesis: The random numbers pass the poker test.")
