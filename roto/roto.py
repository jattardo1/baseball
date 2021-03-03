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
global combos
combos = [10,10,10,10,10,10,10,10,10,10]
global doi
doi = 100
x = 0
lineup = [0,0,0,0,0,0,0,0,0,0]
price = [0,0,0,0,0,0,0,0,0,0,]
def printCombination(arr, n, r): 
    data = [0]*r
    stat = [0]*r
    combinationUtil(arr, data, 0,  n - 1, 0, r,stat)

def combinationUtil(arr, data, start, end, index, r,stat): 
    if (index == r): 
        #for j in range(r):
        #    print(data[j], end = " ")
        #print()
        return; 
    i = start;  
    while(i <= end and end - i + 1 >= r - index):
        stat[index] = proj[i]
        data[index] = arr[i]
        tot = 0
        for j in range(r):
            tot = tot + stat[j]
        y = 0; 
        global doi
        global combos
        if(tot >= doi):
            v = 1
            combos = stat
            doi = sum(combos)
        if (sum(data) <=136 and (tot >= doi or combos[9] == 10)):
            print(combos)
            if((index == 7 or index == 6 or index == 9 or index ==8)  and pos[i] == 7):
                combinationUtil(arr, data, i + 1,  end, index + 1, r,stat); 
            elif((index == 5)  and (pos[i] == 6)):
                combinationUtil(arr, data, i + 1,  end, index + 1, r,stat)
            elif((index == 4)  and (pos[i] == 5)):
                combinationUtil(arr, data, i + 1,  end, index + 1, r,stat)
            elif((index == 3)  and (pos[i] == 4)):
                combinationUtil(arr, data, i + 1,  end, index + 1, r,stat)
            elif((index == 2)  and (pos[i] == 3)):
                combinationUtil(arr, data, i + 1,  end, index + 1, r,stat)
            elif((index == 1)  and (pos[i] == 2)):
                combinationUtil(arr, data, i + 1,  end, index + 1, r,stat)
            elif((index == 0)  and (pos[i] == 2)):
                combinationUtil(arr, data, i + 1,  end, index + 1, r,stat)
        i += 1; 
arr = val; 
r = 10
n = len(arr)
printCombination(arr, n, r)