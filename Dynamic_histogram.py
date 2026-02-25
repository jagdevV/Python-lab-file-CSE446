#Dynamic histogram
# Dynamic Histogram Program

import matplotlib.pyplot as plt

# Taking input from user
data = list(map(int, input("Enter numbers separated by space: ").split()))

# Number of bins
bins = int(input("Enter number of bins: "))

# Create Histogram
plt.hist(data, bins=bins)

# Title and Labels
plt.title("Dynamic Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

plt.grid(True)
plt.show()