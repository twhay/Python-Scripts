# Python Exercise - Random Number Generation - Dice Generator
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
r = np.random.rand()
print(r)

# Use randint() to simulate a dice
dice = np.random.randint(1,7)
print(dice)

# Starting step
step = 50

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)