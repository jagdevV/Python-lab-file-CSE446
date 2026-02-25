#Scatter plot static
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.array([5, 7, 8, 7, 6, 9, 11, 10, 12, 14])
y = np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78])

# Create Figure
plt.figure(figsize=(8, 5))

# Create Scatter Plot
plt.scatter(
    x, y,
    color="#4A90E2",
    edgecolor="black",
    s=100,          # Marker size
    alpha=0.8
)

# Title and Labels
plt.title("Static Scatter Plot", fontsize=16, fontweight='bold')
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Add Grid
plt.grid(True, linestyle='--', alpha=0.5)

# Remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()