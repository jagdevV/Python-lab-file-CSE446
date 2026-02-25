#Moving circle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create circle
circle = plt.Circle((0, 5), 0.5, color="#4A90E2")
ax.add_patch(circle)

# Animation function
def update(frame):
    circle.center = (frame, 5)   # Move horizontally
    return circle,

# Create animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 100),
    interval=50,
    blit=True
)

plt.title("Moving Circle Animation", fontsize=14, fontweight="bold")
plt.grid(alpha=0.3)
plt.show()