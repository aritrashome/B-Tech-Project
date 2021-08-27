import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from os import listdir
import glob

files = ['C_high','C_low','C_medium','D_high','D_low','D_medium','In_low','In_medium',
         'Ir_high','Ir_low','Ir_medium','Jay_high','Jay_low','Jay_medium','Su_high','Su_low','Su_medium'] #'In_high',

for file in files:
    print(file)
    #Loading Data
    filepath = 'data/' + file + '.csv'
    my_data = np.genfromtxt(filepath, delimiter=',')
    #Clipping 15,000
    my_data = my_data[:15000] 
    # Common average reference filter
    for i in range(len(my_data)):
        my_data[i] = my_data[i] - np.mean(my_data[i])
    ####################################
    # 3 Second split
    split = 3*250
    data = []
    for i in range(0, len(my_data), split):
        data.append(my_data[i:i+split].transpose())
    ######################################
    #print(data[0].shape)
    # Saving as file
    np.save('data/preprocess/' +file+ '.npy', data)
