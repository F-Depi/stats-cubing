def csTimer_exp(filename):
    """
    This function is designed to extract an array of times from a csTimer session.
    The DNFs are kept and the time is negative (e.g. DNF(2:34.56) --> -154.56)
    I didn't find an elegant way to keep track of which times had a +2, so I just removed the "+"
    
    ~ Depi 2023/06/30

    """
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    data = pd.read_csv(filename, delimiter=";")

    t = data['Time']
    t = t.str.replace("+","")
    t = t.str.replace("DNF","-")
    t = t.str.replace("(","")
    t = t.str.replace(")","")

    for ii in range(len(t)):
        if ":" in t[ii]:
            min_sec = t[ii].split(":")
            min = int(min_sec[0])
            sec = float(min_sec[1])
            t[ii] = min*60 + sec*np.sign(min)        # il sign() serve perchè ai DNF ho messo un - davanti, il meno però se lo prende solo min

            #print(ii, min_sec ,min, sec, t[ii])      #check

    t = pd.to_numeric(t)

    return(t)