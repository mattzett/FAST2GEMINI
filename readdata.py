"""
Created on Fri Sep 10 18:32:11 2021

Date
Time
Electron energy flux (ergs/cm2-s)
Electron number flux (1/cm2-s)
Electron characteristic energy (ergs)
Ion energy flux (ergs/cm2-s)
Ion number flux (1/cm2-s)
Ion characteristic energy (ergs)
Altitude (km)
MLT (decimal hours)
Invariant latitude (degrees)

@author: zettergm
"""

import numpy as np

# read in the data
filename="/Users/zettergm/Dropbox (Personal)/proposals/UNH_GDC/FASTdata/nightside.txt"
file=open(filename,'r')
data=np.loadtxt(file,dtype={
'names': ('ymd','time','JEe_s_AVG1','Je_s_AVG1','E_Char_Energy_AVG1',
'JEi_s_AVG1','Ji_s_AVG1','I_Char_Energy_AVG1','alt','mlt','ilat'), 
'formats': ('S1','S1','float','float','float','float','float','float','float','float','float')})

# sort into parameters
#for k in range(0,data.size):
#    datanow=data[k]
    
