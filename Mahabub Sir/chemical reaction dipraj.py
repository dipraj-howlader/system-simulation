import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial concentrations
c1 = [50.0]
c2 = [25.0]
c3 = [0.0]

# Constants
kl = 0.025  # rate constant for reaction 1
k2 = 0.01   # rate constant for reaction 2
time_difference = 0.1
t = 0.0
last_time = 15.0
i = 0

# Set up the plot
fig, ax = plt.subplots()
line_c1, = ax.plot([], [], label='C1')
line_c2, = ax.plot([], [], label='C2')
line_c3, = ax.plot([], [], label='C3')
ax.set_xlim(0, int(last_time / time_difference))
ax.set_ylim(0, max(max(c1), max(c2), max(c3)) + 5)
ax.set_xlabel('Time')
ax.set_ylabel('Concentration')
ax.set_title('Chemical Reaction Simulation')
ax.legend()

# Initialization function for the animation
def init():
    line_c1.set_data([], [])
    line_c2.set_data([], [])
    line_c3.set_data([], [])
    return line_c1, line_c2, line_c3

# Animation function
def animate(frame):
    global t, i, time_difference

    if t <= last_time:
        # Calculate next concentrations
        c1_next = c1[i] + (k2 * c3[i] - kl * c1[i] * c2[i]) * time_difference
        c2_next = c2[i] + (k2 * c3[i] - kl * c1[i] * c2[i]) * time_difference
        c3_next = c3[i] + 2.0 * (kl * c1[i] * c2[i] - k2 * c3[i]) * time_difference

        # Append new concentrations
        c1.append(c1_next)
        c2.append(c2_next)
        c3.append(c3_next)

        # Print concentrations for current time step
        print(f"Time: {t:.2f} | C1: {c1_next:.2f} | C2: {c2_next:.2f} | C3: {c3_next:.2f}")

        i += 1
        t += time_difference

        # Adjust time step
        if t >= 2.0:
            time_difference = 0.2
        if t == 6.0:
            time_difference = 0.4

    # Update the plot
    line_c1.set_data(range(len(c1)), c1)
    line_c2.set_data(range(len(c2)), c2)
    line_c3.set_data(range(len(c3)), c3)
    return line_c1, line_c2, line_c3

# Create the animation
ani = FuncAnimation(fig, animate, frames=int(last_time / time_difference),
                    init_func=init, blit=True, interval=200)

plt.show()
