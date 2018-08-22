# Python Exercise - Plotting a Random Walk Distribution
# Initialization
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)

# Initialize all_walks
all_walks = []

# Simulate random walk 10 times (change 10 to the number of times to simulate)
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Transpose np_aw: np_aw_t in order to make the plot make sense
# Without transposing, the 2D Numpy array is rendered by matplotlib
# It will not be able to show the results for the 100 iterations over 10 random walks
# Transposing allows for the results over 100 iterations to be displayed
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Find the number of ends that are above a certain amount
np.where(ends > 60)

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
