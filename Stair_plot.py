import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.arange(1, 11)
y = [2, 4, 5, 7, 6, 8, 9, 11, 10, 12]

# Create Figure
plt.figure(figsize=(8, 5))

# Create Stair Plot
plt.step(
    x, y,
    where='mid',              # Options: 'pre', 'post', 'mid'
    color="#4A90E2",
    linewidth=2
)

# Add markers
plt.plot(x, y, 'o', color="#D0021B")

# Title and Labels
plt.title("Stair Plot", fontsize=16, fontweight='bold')
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Grid styling
plt.grid(True, linestyle='--', alpha=0.6)

# Clean borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()