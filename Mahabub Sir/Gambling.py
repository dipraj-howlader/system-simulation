import random
import numpy as np

total_cost = 0
total_income = 0
games_played = 100
max_flips = 10  # Limit for maximum flips per game before declaring a loss

for game in range(games_played):
    x = 0  # Number of flips in this game
    h = 0  # Count of heads
    t = 0  # Count of tails

    while True:
        x += 1
        total_cost += 1  # Increment total cost with each flip
        r = random.randint(0, 1)
        print(r)
        if r == 0:
            h += 1
        else:
            t += 1
        
        # Calculate the difference between heads and tails
        dif = abs(h - t)

        if dif >= 3:
            print(f"Game {game+1}: Won $8 with cost of ${x}")
            total_income += 8  # Add $8 to total income for a win
            break
        elif x >= max_flips:
            print(f"Game {game+1}: Lost with cost of ${x}")
            break  # Game is lost if it reaches the maximum flip limit

# Print the final totals after all games
print("Total Cost: $", total_cost, "Total Income: $", total_income)
