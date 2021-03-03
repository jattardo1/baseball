import pandas as pd
import csv
import numpy as np
import math
import matplotlib.pyplot as plt

df = pd.read_csv('roto.csv', index_col=0)

runs = np.array(df["R"])
hrs = np.array(df["HR"])
rbi = np.array(df["RBI"])
sb = np.array(df["SB"])
avg = np.array(df["AVG"])
val = np.array(df["AUC VAL"])
proj = np.array(df["VAL"])
pos = np.array(df["POS"])

