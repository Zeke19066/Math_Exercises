"""
Building a Logarithmic Spiral Generator [METAL RATIOS]
(Fibonacci + More)

"the Silver Ratio - numberphile"
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000) # Otherwise the recursive limit would be 1000

cycle_limit = 20          # How many datapoints do we want to generate? (for the plot to be accurate)
cycle_show = 10             # How many numbers in this infinite series do we wish to print out to show?
ratio_multiple = 1          # Fibonacci/Golden Ratio = 1, Pell Sequence/Silver Ratio = 2, etc.

log_sequence = {0:0, 1:1}   # Starting dictionary that will store the completed sequence.

def log_generator(cycle = 1, left_num = 0, right_num = 1):
    
    if cycle < cycle_limit-1:
        log_sequence[right_num + 1] = (log_sequence.get(left_num) + (ratio_multiple * log_sequence.get(right_num)))
        left_num += 1
        right_num += 1
        cycle += 1
        log_generator(cycle, left_num, right_num)
    else:
        show_sequence = {} # This is the abridged sequence that will be shown
        for i in log_sequence.keys():
            if i < cycle_show:
                show_sequence[i] = log_sequence[i] # This is how we copy key/value pairs from one dictionary to another.
                
        print(show_sequence)

log_generator()


# The plotter function
plt.style.use('dark_background') 
for x, y in log_sequence.items():
    if y > 0: #let's avoid that zero at our first index\
        m, b = np.polyfit(x, np.log(y), 1)
        print(f'{m} ,  {b}')
        plt.polar(x, np.log(y), 'r-o')# np.log(y) processes y values to grant logarithmic scale to polar graph.

"""
# SECOND TEST PLOT
plt.style.use('dark_background') 
for x, y in log_sequence.items():
    if y > 0: #let's avoid that zero at our first index\
        plt.plot(x, np.log(y), 'r-o')# np.log(y) processes y values to grant logarithmic scale to polar graph.

"""

plt.show()