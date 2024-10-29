import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the distributions
mean_sample = 100
std_dev_sample = 20
mean_blood_pressure = 80
std_dev_blood_pressure = 20
sample_size = 200

# Generate random samples for unimodal distributions
sample_data = np.random.normal(mean_sample, std_dev_sample, sample_size)
blood_pressure_data = np.random.normal(mean_blood_pressure, std_dev_blood_pressure, sample_size)

# Generate random samples for a multimodal distribution
multimodal_data = np.concatenate([
    np.random.normal(60, 10, int(sample_size / 3)),
    np.random.normal(100, 15, int(sample_size / 3)),
    np.random.normal(140, 20, int(sample_size / 3))
])

# Plotting
plt.figure(figsize=(14, 6))

# Unimodal Distribution Plot
plt.subplot(1, 2, 1)
sns.histplot(sample_data, bins=15, kde=True, color="skyblue", label=f"Sample (mean={mean_sample}, sd={std_dev_sample})", stat="density")
sns.histplot(blood_pressure_data, bins=15, kde=True, color="salmon", label=f"Blood Pressure (mean={mean_blood_pressure}, sd={std_dev_blood_pressure})", stat="density")
plt.title('Unimodal Normal Distributions')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Multimodal Distribution Plot
plt.subplot(1, 2, 2)
sns.histplot(multimodal_data, bins=15, kde=True, color="purple", label="Multimodal Data", stat="density")
plt.title('Multimodal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()
