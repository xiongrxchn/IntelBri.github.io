#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:48:47 2020

@author: pi
"""

#! /usr/bin/python
from gps import *
import time, inspect
import numpy as np
 
 
f = open(time.strftime("%Y%m%d-%H%M%S")+'_GSPData.csv','w')
 
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
 
print 'GPStime utc\t\t\tlatitude\tlongitude\tspeed\tsats in view' # '\t' = TAB to try and output the data in columns.
 
f.write("GPStime utc,latitude,longitude,speed,sats in view\n")

data  =   []

try:
 
    while True:
        report = gpsd.next() #
        if report['class'] == 'TPV':
            GPStime =  str(getattr(report,'time',''))
            lat = str(getattr(report,'lat',0.0))
            lon = str(getattr(report,'lon',0.0))
            speed =  str(getattr(report,'speed','nan'))
            sats = str(len(gpsd.satellites))
            
            GPStime1 =  getattr(report,'time','')
            lat1 = getattr(report,'lat',0.0)
            lon1 = getattr(report,'lon',0.0)
            speed1 =  getattr(report,'speed','nan')
            sats1 = len(gpsd.satellites)
 
            print  GPStime,"\t",
            print  lat,"\t",
            print  lon,"\t",
            print  speed,"\t",
            print  sats,"\t"
 
            f.write(GPStime + ',' + lat +',' + lon + ',' + speed + ',' + sats + '\n')
            
            data.append((time.time, GPStime1, lat1, lon1, speed1, sats1))
            np.save ('data_gps.npy',  np.array (data))
 
            time.sleep(1)
 
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "Done.\nExiting."
    f.close()