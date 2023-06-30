import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = "csTimer_export\csTimerExport_20230630_221423.csv"
data = pd.read_csv(filename, delimiter=";")

t = data['Time']

t = pd.to_numeric(t, errors='coerce')
t = t.fillna(-1)
    
plt.hist(t)
plt.show()
