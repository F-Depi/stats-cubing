import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from my_functions import csTimer_exp

filename = "csTimer_export\csTimerExport_20230630_221423.csv"
t = csTimer_exp(filename)

#binlimits = [-60] + list(range(-49, -18, 3)) + list(range(22, 52, 3)) + [60]

plt.figure
hist, bins, _ = plt.hist(t, density=True, bins=50, edgecolor='black', linewidth=0.5)

for i in range(len(bins)):
    if bins[i] < 0:
        plt.gca().get_children()[i].set_facecolor('red')

plt.xlim(-60, 60)

# Create dummy bars for legend handles
successi_bar = plt.bar([], [], color='blue', label='Successi')
dnf_bar = plt.bar([], [], color='red', label='DNF')

# Create the legend using the dummy bars as handles
plt.legend(handles=[successi_bar, dnf_bar])

plt.xticks(range(-60,65,5))
plt.xlabel("Time [s], if DNF the time is negative")
plt.ylabel("Frequency")
plt.legend(["Successi","DNF"])
solves = str(len(t))
succ_rate = str(round(len(t[t>0])/len(t)*100))
mean = str(round(np.mean(t[t>0]),2))
title =  solves + " solves, " + succ_rate + "% success rate, " + mean + " mean"
plt.title(title)

plt.show()