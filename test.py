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
path_data_long2 = '/home/cami/Desktop/verbrennungsmotoren/data/long2.csv'
path_data_ufpe1 = '/home/cami/Desktop/verbrennungsmotoren/data/ufpe1.csv'

# Read all the data
data_drive1 = pd.read_csv(path_data_drive1)
data_idle1 = pd.read_csv(path_data_idle1)
data_live1 = pd.read_csv(path_data_live1)
data_long1 = pd.read_csv(path_data_long1)
data_long2 = pd.read_csv(path_data_long2)
data_ufpe1 = pd.read_csv(path_data_ufpe1)



rpm_drive1 = data_drive1['ENGINE_RPM ()']
rpm_idle1 = data_idle1['ENGINE_RPM ()']
rpm_live1 = data_live1['ENGINE_RPM ()']
rpm_long1 = data_long1['ENGINE_RPM ()']
rpm_long2 = data_long2['ENGINE_RPM ()']
rpm_ufpe1 = data_ufpe1['ENGINE_RPM ()']

print(max(rpm_drive1))
print(max(rpm_idle1))
print(max(rpm_live1))
print(max(rpm_long1))
print(max(rpm_long2))
print(max(rpm_ufpe1))


torque_drive1 = data_drive1['ENGINE_RPM ()']
torque_idle1 = data_idle1['ENGINE_RPM ()']
torque_live1 = data_live1['ENGINE_RPM ()']
torque_long1 = data_long1['ENGINE_RPM ()']
torque_long2 = data_long2['ENGINE_RPM ()']
torque_ufpe1 = data_ufpe1['ENGINE_RPM ()']

print(max(rpm_drive1))
print(max(rpm_idle1))
print(max(rpm_live1))
print(max(rpm_long1))
print(max(rpm_long2))
print(max(rpm_ufpe1))