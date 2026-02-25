#line chart

import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Create Line Chart
plt.plot(x, y)

# Add Title and Labels
plt.title("Simple Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Show Grid (optional but good for lab)
plt.grid(True)

# Display the chart
plt.show()