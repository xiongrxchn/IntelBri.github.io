#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:10:21 2020

@author: pi
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pandas import Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  math


def interpolate(y):
    xp = y.nonzero()[0]
    yp = y[xp]
    x = np.arange(len(y))
    y = np.interp(x, xp, yp)
    return y


def split(y):
    rows, cols = len(y), len(y[0])
    y1 = [0] * rows
    y2 = [0] * rows
    y3 = [0] * rows
    y4 = [0] * rows
    y5 = [0] * rows
    y6 = [0] * rows

    
    for row in range(0, rows - 1):
        y1[row] = y[row][0]
        y2[row] = y[row][1]
        y3[row] = y[row][2]
        y4[row] = y[row][3]
        y5[row] = y[row][4]

        
    return y1, y2, y3, y4, y5, y6

def Movingaverage(y, n):
    Series(y)
    return pd.Series(y).rolling(window=n).mean()


y = np.load('data_gps.npy')
df = pd.DataFrame(y)
                  
data = split(y)

time = np.array(data[0])
GPStime = np.array(data[1])  
lat = np.array(data[2])  
lon = np.array(data[3])  

speed = np.array(data[4])  
sats = np.array(data[5])  



data1 = interpolate(lat)
data2 = interpolate(lon)

xave = []
for i in range(2, len(data2)-2):
    m = 0
    for j in range(i - 2, i + 3):
        m = m + data2[j]
    xave.append(m/5)
print(xave)

result = 0

for i in range(len(xave)):

    result = result + (data2[i+2] - xave[i])**2
    #print(result)

variance = result / len(data2)
print(variance)

dataAve1 = Movingaverage(data1, 5)
dataAve2 = Movingaverage(data2, 5)
x = np.arange(len(data1))



plt.xlabel('Time')
plt.ylabel('lat')
plt.title('lat')

plt.plot(x, data1, label='Raw Data')
plt.plot(x, dataAve1,label='Moving Average')
plt.legend()

plt.show()


plt.xlabel('Time')
plt.ylabel('lon')
plt.title('lon')

plt.plot(x, data2, label='Raw Data')
plt.plot(x, dataAve2,label='Moving Average')
plt.legend()

plt.show()


linecolor = 'g'
fillcolor = 'g'


mean = xave
std = pow(variance, 0.5)
t = 2

std = np.ones_like(mean)*std

plt.plot(np.arange(len(mean)), mean, color = linecolor)
plt.fill_between(np.arange(len(mean)), mean-t*std, mean+t*std, alpha = 0.2, color = fillcolor)
plt.xlabel('Time')
plt.ylabel('lon')
plt.title('lon')
plt.show()