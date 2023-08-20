import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from my_functions import csTimer_exp

f1 = "csTimer_export/edge1.csv"
f2 = "csTimer_export/edge2.csv"
f3 = "csTimer_export/edge3.csv"
f4 = "csTimer_export/edge4.csv"
t1 = csTimer_exp(f1)
t2 = csTimer_exp(f2)
t3 = csTimer_exp(f3)
t4 = csTimer_exp(f4)

plt.figure()
plt.title("Edge only solves, alternating parity")

bins = 50  # Adjust the number of bins as needed
hist_range = (-25, 25)  # Set the range for bins

plt.hist(t1, density=True, alpha=0.5, bins=bins, range=hist_range, label="Week 1")
plt.hist(t2, density=True, alpha=0.5, bins=bins, range=hist_range, label="Week 2")
plt.hist(t3, density=True, alpha=0.5, bins=bins, range=hist_range, label="Week 3")
plt.hist(t4, density=True, alpha=0.5, bins=bins, range=hist_range, label="Week 4")
plt.xticks(list(range(-25,-9))+ list(range(10,26)))
plt.legend()

# Now everithing together

t = np.concatenate([t1,t2,t3,t4])
plt.figure()

plt.hist(t, bins=bins, range=hist_range, edgecolor = 'black', linewidth = 0.5)

plt.xticks(list(range(-25,-9))+ list(range(10,26)))

# Now we divide odd and even parity solves

t_odd = t[0::2]
t_even = t[1::2]

plt.figure()
solves = str(len(t))
succ_rate = str(round(len(t[t>0])/len(t)*100, 1))
succ_rate_odd = str(round(len(t_odd[t_odd>0])/len(t_odd)*100, 1))
succ_rate_even = str(round(len(t_even[t_even>0])/len(t_even)*100, 1))
plt.title("Odd vs even parity on " + solves + " edges only solves (" + succ_rate + "% success rate)")
plt.hist(t_odd, bins=bins, range=hist_range, edgecolor = 'black', linewidth = 0.5, alpha = 0.5, color='red', label="Odd (" + succ_rate_odd + "% success rate)")
plt.hist(t_even, bins=bins, range=hist_range, edgecolor = 'black', linewidth = 0.5, alpha = 0.5, color='blue', label="Even (" + succ_rate_even + "% success rate)")

plt.xticks(list(range(-25,-9))+ list(range(10,26)))
plt.axvline(np.average(t_odd[t_odd>0]), color='red', label="Odd average")
plt.axvline(np.average(t_even[t_even>0]), color='blue', label="Even average")
plt.xlim(9,25)
plt.legend()
plt.show()