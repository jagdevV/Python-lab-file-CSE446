#Animated line

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [])

def update(frame):
    x_data.append(frame)
    y_data.append(frame**2)
    line.set_data(x_data, y_data)
    ax.relim()
    ax.autoscale_view()
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(10), interval=500)
plt.show()
