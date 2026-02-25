#User line chart
# Line Graph using User Input

import matplotlib.pyplot as plt

# Taking number of points
n = int(input("Enter number of data points: "))

x = []
y = []

print("Enter X values:")
for i in range(n):
    value = float(input())
    x.append(value)

print("Enter Y values:")
for i in range(n):
    value = float(input())
    y.append(value)

# Plotting
plt.plot(x, y)

# Adding title and labels
plt.title("User Input Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)
plt.show()