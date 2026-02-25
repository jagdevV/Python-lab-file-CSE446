#Static pie chart

import matplotlib.pyplot as plt

# Sample Data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [35, 25, 20, 20]

# Colors
colors = ['#4A90E2', '#50E3C2', '#F5A623', '#D0021B']

# Create figure
plt.figure(figsize=(7, 7))

# Create Pie Chart
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Title
plt.title("Programming Language Usage", fontsize=16, fontweight='bold')

# Make circle perfect
plt.axis('equal')

plt.tight_layout()
plt.show()