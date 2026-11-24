import matplotlib.pyplot as plt
import numpy as np

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
results = ([die.roll() for roll_num in range(1000)]) # list comprehension

# Analyze the results
frequencies = []
frequencies = ([results.count(value) for value in range(1, die.num_sides+1)])

plt.style.use('_mpl-gallery')

# make data:
x = 0.5 + np.arange(die.num_sides)
y = frequencies

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, die.num_sides), xticks=np.arange(1, die.num_sides+1),
       ylim=(min(frequencies), max(frequencies)), yticks=np.arange(min(frequencies)-10, max(frequencies)))

plt.show()