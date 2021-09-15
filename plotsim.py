#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:33:43 2021

plot plasma density from fast simulations

@author: zettergm
"""
##############################################################################
# imports
import gemini3d.read
import os
import matplotlib.pyplot as plt
import numpy as np

# functions    
def plotdata(xg,ne,time):
    z=xg["x1"][2:-2]
    x=xg["x2"][2:-2]
    y=xg["x3"][2:-2]
    ix=x.size//2
    neplot=np.squeeze(ne[:,ix,:])
    
    plt.figure(num=0,dpi=300)
    plt.clf()
    plt.pcolormesh(y/1e3,z/1e3,np.log10(neplot))
    plt.xlabel('N-S distance (km)')
    plt.ylabel('altitude (km)')
    plt.ylim([90,400])
    plt.colorbar(label="$log_{10} ~ n_e$")
    plt.clim([9.5,11.75])
    plt.title(str(time)+" s")
    ax=plt.gca()
    ax.set_aspect("equal")
    #plt.show(block=False)
    return

##############################################################################
# prep
plt.close("all")

# setup output directories
direc="/Users/zettergm/simulations/fast_cusp/"
plotdir=direc+"/customplots/"
if not os.path.isdir(plotdir):
    os.mkdir(plotdir)

# load config and grid
cfg=gemini3d.read.config(direc)
xg=gemini3d.read.grid(direc)
inds=np.arange(0,len(cfg["time"]))

# plots
for k in inds:
    data=gemini3d.read.frame(direc,cfg["time"][k])
    simtime=(cfg["time"][k]-cfg["time"][0]).total_seconds()
    print(cfg["time"][k])
    plotdata(xg,data["ne"],simtime)
    plt.savefig(plotdir+"/"+str(simtime)+"s.png")
    #wait=input("Press a button to continue...")
    
    
