# Beautiful Histogram Program

import matplotlib.pyplot as plt

# Sample Data
data = [12, 15, 13, 17, 19, 21, 22, 25, 23, 20, 18, 16, 14, 19, 24]

# Set figure size
plt.figure(figsize=(8, 5))

# Create Histogram with styling
plt.hist(
    data,
    bins=6,
    color="#4A90E2",        # Soft blue color
    edgecolor="black",
    linewidth=1.2,
    alpha=0.8
)

# Title and Labels with styling
plt.title("Static Histogram", fontsize=16, fontweight='bold')
plt.xlabel("Value Range", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Add grid with transparency
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Remove top and right borders for clean look
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust layout
plt.tight_layout()

plt.show()