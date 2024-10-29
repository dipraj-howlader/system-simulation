import math
import random
import matplotlib.pyplot as plt

# Store each step's X and Y coordinates
past_positions = []

for asa in range(1):
    step = 0
    x = 0
    y = 0
    dotx = []
    doty = []
    direction = []

    F_L_R = [0.5, 0.2, 0.2, 0.1]
    F_L_R = [int(10 * i) for i in F_L_R]

    while step <= 20:
        rn = random.randint(0, 9)

        if rn in range(F_L_R[0]):
            direction.append('F')
            y += 1
        elif rn in range(F_L_R[0], F_L_R[0] + F_L_R[1]):
            direction.append('L')
            x -= 1
        elif rn in range(F_L_R[0] + F_L_R[1], F_L_R[0] + F_L_R[1] + F_L_R[2]):
            direction.append('R')
            x += 1
        else:
            direction.append('B')
            y -= 1

        dotx.append(x)
        doty.append(y)
        past_positions.append((x, y))  # Save the current position

        step += 1

    # Plot the random walk path
    plt.plot(dotx, doty, marker="o")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Random Walk Path")
plt.show()

# Display the past positions along with directions
for i, pos in enumerate(past_positions):
    print(f"Step {i + 1}: Position (X={pos[0]}, Y={pos[1]}) - Direction {direction[i]}")
