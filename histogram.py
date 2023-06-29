import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("csTimer_export\csTimerExport_20230630_001011.csv", delimiter=";")

t = data['Time']

t = pd.to_numeric(t, errors='coerce')
t = t.fillna(-1)
    
plt.hist(t)
plt.show()
