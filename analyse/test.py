# importing of libaries
import numpy as np                      #functions for scientific computing, faster arrays
import pandas as pd                     #easy import and export of data, fast and easy-to-use datastructure
import math                             #mathematical functions
import matplotlib.pyplot as plt         #generation of Graphs
from scipy.constants import pi, g       #fundamental Constants
# Path for every data set
path_data_drive1 = '/home/cami/Desktop/verbrennungsmotoren/data/drive1.csv'
path_data_idle1 = '/home/cami/Desktop/verbrennungsmotoren/data/idle1.csv'
path_data_live1 = '/home/cami/Desktop/verbrennungsmotoren/data/live1.csv'
path_data_long1 = '/home/cami/Desktop/verbrennungsmotoren/data/long1.csv'
path_data_ufpe1 = '/home/cami/Desktop/verbrennungsmotoren/data/ufpe1.csv'

# Read all the data
data_drive1 = pd.read_csv(path_data_drive1)
data_idle1 = pd.read_csv(path_data_idle1)
data_live1 = pd.read_csv(path_data_live1)
data_long1 = pd.read_csv(path_data_long1)
data_ufpe1 = pd.read_csv(path_data_ufpe1)



speed_data_drive1 = data_drive1['VEHICLE_SPEED ()']
throttle_data_drive1 = data_drive1['THROTTLE ()']
purge_data_drive1 = data_drive1['COMMANDED_EVAPORATIVE_PURGE ()']


purge_drive1 = purge_data_drive1
speed_drive1 = speed_data_drive1
throttle_drive1 = throttle_data_drive1

plt.scatter(purge_drive1,speed_drive1, label='Speed')
plt.scatter(purge_drive1, throttle_drive1, label='Throttle')


print(data_drive1['COMMANDED_EVAPORATIVE_PURGE ()'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()