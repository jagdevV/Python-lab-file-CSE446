#Subplot
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2
y4 = np.sqrt(x)

# Create figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 7))

# Plot 1 - Sine
axs[0, 0].plot(x, y1, color="#4A90E2")
axs[0, 0].set_title("Sine Wave")

# Plot 2 - Cosine
axs[0, 1].plot(x, y2, color="#50E3C2")
axs[0, 1].set_title("Cosine Wave")

# Plot 3 - Square
axs[1, 0].plot(x, y3, color="#F5A623")
axs[1, 0].set_title("x² Graph")

# Plot 4 - Square Root
axs[1, 1].plot(x, y4, color="#D0021B")
axs[1, 1].set_title("√x Graph")

# Adjust spacing
plt.tight_layout()

plt.show()