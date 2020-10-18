# Patrolman: Using Raspberry Pi for Road Pothole Inspection

• [Pengkun Liu](pengkunl@andrew.cmu.edu); [Ruoxin Xiong](ruoxinx@andrew.cmu.edu)

### video link:


## 1 Introduction

Road potholes are a common nuisance experienced by the vehicle drivers or commuters. In the United Kingdom, more than half a million potholes were reported in 2017, an increase of 44% on the 2015 [1]. The self-proclaimed pothole capital, Edmonton, Alberta, Canada reportedly spends $4.8 million on 450,000 potholes annually, as of 2015 [2]. Serious road accidents can occur as a direct result from surface potholes, especially under high speed or low visibility conditions. Every year India loses approximately 1,100 people to accidents caused by potholes [3]. This project designs and implement a mobile Raspberry Pi system, which is called Patrolman, for road pothole inspection.

![](/Images/background.png)

(Image source: Pothole - Wikipedia https://en.wikipedia.org/wiki/Pothole#cite_note-13)

### 1.1 Motivation

Reliable and cost-effective routine monitoring of road conditions can lead to timely preventive action. The traditional approach to road damage detection is to use manual reporting of the presence of potholes on the roads. Due to the sheer size of the roadway networks, manual inspections are typically unavailable in terms of labor and cost. Road conditions are naturally sensed from a moving entity that can measure vibrations and impulses during a drive [4]. We design a mobile Raspberry Pi system - Patrolman, for road pothole inspection. Patrolman uses the three-axis accelerometer and GPS sensor deployed on Raspberry Pi system, relying on the mobility of cars (we use a toy car) to sense the vibration response of the roads being monitored.

### 1.2 Goals

This project presents an alternative system – Patrolman, using Raspberry Pi to detect and report road potholes with their georeferenced locations. It uses the mobility of the participating vehicles, gathering data from the six-axis accelerometer and GPS sensors, and processing the data to assess road surface conditions. This project will provide an affordable sensing method to conduct pavement condition assessments.

## 2 For Progress Reports

#### [Progress Report_Oct 5th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/progress_report_1.md)
#### [Progress Report_Oct 8th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/progress_report_2.md)


## 3 Methodology

### 3.1 Phenomena of Interest

Road conditions are naturally sensed from a moving entity that can measure vibrations and impulses during a drive [4]. The general monitoring metrics intended to measure road condition and performance including:

1. Vibration - Acceleration is the most common measure taken to characterize vibrations. When the vehicle drive on flat road conditions, the three x, y, and z gravity of acceleration values (g) were steady while the three x, y, and z gravity of acceleration values (g) reflect pulse signals on road with potholes.

2. Georeferenced locations - GPS is linked to each accelerometer for data to be georeferenced. Therefore, we record the locations of detected road potholes.

### 3.2 Sensor(s) Used

The Patrolman system consists of Raspberry Pi, MPU-6050 six-axis accelerometers, GPS, and a battery. In this project, the team collect driving data of vehicles (we use a toy car instead), and leverages sensors mounted on a testing vehicle.

![](/Images/sensor_all.png)

(1) Gyro + Accelerometer: MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS

![](/Images/MPU_6050_1.png)

The MPU-6050 parts are the world’s first MotionTracking devices designed for the low power, low cost, and high-performance requirements of smartphones, tablets and wearable sensors. It combines a 3-axis gyroscope and a 3-axis accelerometer on the same silicon die.

```markdown
Features and Specifications:

- Tri-Axis angular rate sensor with a sensitivity up to 131 LSBs/dps and a full-scale range of ±250, ±500, ±1000, and ±2000dps
- Tri-Axis accelerometer with a programmable full scale range of ±2g, ±4g, ±8g and ±16g
- VDD Supply voltage range of 2.375V – 3.46V 
- VLOGIC (MPU-6050) at 1.8V ± 5% or VDD
- Gyro operating current: 3.6mA (full power, gyro at all rates)
- 400kHz Fast Mode I²C or up to 20MHz SPI serial host interfaces 
```
![](/Images/Acceleromete_interfacer.png)


(2) GPS sensor: L76X GPS Module

L76X GPS Module is a module with Global Navigation Satellite System （GNSS）function, supports GPS, BD2 and QZSS positioning systems, and has the advantages of small size, low power consumption, and fast positioning.

```markdown
Features and Specifications:

- Receiving channels: 22 tracking channels, 66 acquisition channels and 210 PRN channels
- Receiving signal: GPS, BD2 and QZSS
- Support SBAS: WAAS, EGNOS, MSAS, GAGAN
- Signal frequency band: GPS L1 (1575.42Mhz) BD2 B1 (1561.098MHz) C/A Code
- Capture time: Cold start: 10S (fastest); Hot start: 1S
- Capture sensitivity: -148dBm
- Tracking sensitivity: -163dBm
- Recapture capture sensitivity: -160dBm
- Positioning accuracy: <2.5mCEP
- The highest altitude: 18000(M)
- Maximum speed: 515m/s
- Logic voltage: 3.3/5V
- Communication interface: UART
- Serial communication baud rate: 4800bps~115200bps (default 9600)
- Update rate: Maximum 10Hz (default 1HZ)
- Communication protocol: NMEA 0183 /PMTK
- Working voltage: 3.3V/5V
- Working current: 11mA (5V)
- Working temperature -40℃ ~ 85℃
- Product size: 32.5X25.5(mm)
```
![](/Images/GPS.png)

![](/Images/GPS_interface.png)


### 3.3 Signal Conditioning and Processing

According to the sampling principle, the sampling frequency (fs) needs to be at least twice the measured signal frequency (fh): fs > 2fh. If the sampling frequency was chosen to be too small, not only the raw signal could not be described clearly and correctly, but also aliasing would occur, which block the way to attain the useful data information.

Accelerometer: The accelerator sensor is installed under the middle of the bridge to test its vibration on the z-axis. It is hard for us to calculate the frequency response of the deck. To find the appropriate sampling rate, a 1 kHz frequency was used at first and a host of pre-experiments were conducted. 

## 4 Experiments and Results

Describe the experiments you did and present the results; Use tables and plots if possible

![](/Images/sensor_all.png)



## 5 Discussion

Discuss the insights from the project

## References

[1] Editor, Swindonian (30 December 2018). "More than half a million potholes were reported last year throughout the UK". The Swindonian. Retrieved 2 January 2019.

[2] Hingston, Michael (April 2015). "Asphalt Nerds The alchemy of pavement in Canada's pothole capital". The Walrus. Retrieved 20 March 2015.

[3] S, Kamaljit Kaur; DelhiJuly 24, hu; July 24, 2018UPDATED; Ist, 2018 00:37. "Over 9300 deaths, 25000 injured in 3 years due to potholes". India Today. Retrieved 4 August 2019.

[4]Eriksson, J., Girod, L., Hull, B., Newton, R., Madden, S., & Balakrishnan, H. (2008). The Pothole Patrol: Using a mobile sensor network for road surface monitoring. In MobiSys’08 - Proceedings of the 6th International Conference on Mobile Systems, Applications, and Services (pp. 29–39).

