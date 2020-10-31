# Progress Report 4 (Oct 17th)


## Current progress


### (1) Outdoor Testing Preparation

Install the remote control application Anydeck on the mobile phone to control the Raspberry Pi outdoor.

<div align="center"><img width="1500" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/screenshot.jpg"/></div>


### (2) Outdoor Testing Results

<div align="center"><img width="1500" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/outdoor_5.png"/></div>

There are three kinds of defeats: Cracking, Pot Holes, and Upheaval.

Smooth road (SM): Good road conditions with smooth road surface.

Potholes (PH): Missing chunks of the road surface.

Upheaval (UH): Localized upward swelling on the roads.

Cracking (CR): Road cracks often result from frequent vehicle movements and temperature changes.

<div align="center"><img width="1500" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/outdoor_7.png"/></div>

<div align="center"><img width="1500" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/pot_holes_upheaval.png"/></div>

<div align="center"><img width="1500" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/cracking.png"/></div>


After collecting and cleaning all the sets of data, we make the figures of three kinds of defects. The figures are about the X-axis acceleration, Y-axis acceleration, Z-axis acceleration, and the corresponding moving averages. 95 % confidence interval of the Z-axis acceleration of three kinds of defects are also drawn. Different defects have different data distributions and patterns. As for the duration of acceleration, the Pot Holes have the shortest period, especially multiple massive changes in amplitude in a short time. The durations of acceleration of the Cracking last for the longest time, but the variation range of acceleration is more moderate compared to the Pot Holes. The changing pattern of acceleration for the Upheaval is somewhere between the Pot Holes and Cracking.


### (3) Interfacing the GPS Unit 


<div align="center"><img width="1500" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/interfacing_GPS.png"/></div>


