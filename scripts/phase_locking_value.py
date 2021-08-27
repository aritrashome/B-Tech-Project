#!pip install spectral_connectivity

from statsmodels.tsa.stattools import grangercausalitytests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

from spectral_connectivity import Multitaper, Connectivity
def phase_locking_value(x,y):
    m = Multitaper(time_series=np.array([x,y]).transpose(),sampling_frequency=250, n_fft_samples=125)
    c = Connectivity.from_multitaper(m)
    matrix = c.phase_locking_value()
    matrix = np.nan_to_num(matrix, nan=0)
    return matrix[0,:,0,1].mean()

#files = ['C_high','C_low','C_medium','D_high','D_low','D_medium','In_low','In_high','In_medium',            # List of 18 files
#         'Ir_high','Ir_low','Ir_medium','Jay_high','Jay_low','Jay_medium','Su_high','Su_low','Su_medium']

files = ['C_high']    				# Files for which granger sausality is to be calculated

for file in files:
    print(file)
    data = np.load('data/preprocess/' +file+ '.npy')    # Replace with Loctaion of file on drive
    plv = []
    for i in range(20): 
        print(i,end=' ')
        arr = np.zeros(shape=(1596), dtype=complex)
        cnt = 0
        for j in range(56):
            #print(i,j, end=' ')
            for k in range(j+1):
                arr[cnt] = phase_locking_value( data[i][j], data[i][k] )
                cnt += 1
        plv.append(arr)
    np.save('data/parameter/'+file+'_plv.npy',plv, allow_pickle=True)   # CHange to location where the file is to be save
    #print(np.load('data/parameter/'+file+'_plv.npy').shape)