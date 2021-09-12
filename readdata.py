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
import matplotlib.pyplot as plt

# read in the data
filename="/Users/zettergm/Dropbox (Personal)/proposals/UNH_GDC/FASTdata/nightside.txt"
file=open(filename,'r')
data=np.loadtxt(file,dtype={
'names': ('ymd','time','JEe_s_AVG1','Je_s_AVG1','E_Char_Energy_AVG1',
'JEi_s_AVG1','Ji_s_AVG1','I_Char_Energy_AVG1','alt','mlt','ilat'), 
'formats': ('S1','S1','float','float','float','float','float','float','float','float','float')})

# sort into parameters
eflux=np.empty( data.shape )
chare=np.empty( data.shape )
invlat=np.empty( data.shape )
for k in range(0,data.size):
    datanow=data[k]
    eflux[k]=datanow[2]
    chare[k]=datanow[4]
    invlat[k]=datanow[-1]
    
# unit conversion, ergs to eV
elchrg=1.6e-19
chare=chare/1e7/elchrg

# smooth data a bit prior to inserting into model
lsmooth=2
efluxsmooth=np.empty(data.shape)
charesmooth=np.empty(data.shape)
for k in range(0,data.size):
    print(chare[k-lsmooth:k+lsmooth])
    charesmooth[k]=np.average(chare[k-lsmooth:k+lsmooth])
    efluxsmooth[k]=np.average(eflux[k-lsmooth:k+lsmooth])

# plot
plt.subplots(2,2,dpi=100)

plt.subplot(2,2,1)
plt.plot(invlat,eflux)
plt.xlabel("latitude (deg.)")
plt.ylabel("energy flux (mW/m$^2$)")

plt.subplot(2,2,2)
plt.plot(invlat,chare)
plt.xlabel("latitude (deg.)")
plt.ylabel("energy (eV)")

plt.subplot(2,2,3)
plt.plot(invlat,efluxsmooth)
plt.xlabel("latitude (deg.)")
plt.ylabel("energy flux (mW/m$^2$)")

plt.subplot(2,2,4)
plt.plot(invlat,charesmooth)
plt.xlabel("latitude (deg.)")
plt.ylabel("energy (eV)")