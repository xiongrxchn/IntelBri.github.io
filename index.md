# Patrolman: Using Raspberry Pi for Road Pothole Inspection

• [Pengkun Liu](pengkunl@andrew.cmu.edu); [Ruoxin Xiong](ruoxinx@andrew.cmu.edu)

### video link:


## 1 Introduction

Road potholes are a common nuisance experienced by the vehicle drivers or commuters. In the United Kingdom, more than half a million potholes were reported in 2017, an increase of 44% on the 2015 [1]. The self-proclaimed pothole capital, Edmonton, Alberta, Canada reportedly spends $4.8 million on 450,000 potholes annually, as of 2015 [2]. Serious road accidents can occur as a direct result from surface potholes, especially under high speed or low visibility conditions. Every year India loses approximately 1,100 people to accidents caused by potholes [3]. This project designs and implement a mobile Raspberry Pi system, which is called Patrolman, for road pothole inspection.

<div align="center"><img width="800"src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/background.png"/></div>

(Image source: Pothole - Wikipedia https://en.wikipedia.org/wiki/Pothole#cite_note-13)

### 1.1 Motivation

Reliable and cost-effective routine monitoring of road conditions can lead to timely preventive action. The traditional approach to road damage detection is to use manual reporting of the presence of potholes on the roads. Due to the sheer size of the roadway networks, manual inspections are typically unavailable in terms of labor and cost. Road conditions are naturally sensed from a moving entity that can measure vibrations and impulses during a drive [4]. We design a mobile Raspberry Pi system - Patrolman, for road pothole inspection. Patrolman uses the six-axis accelerometer and GPS sensor deployed on Raspberry Pi system, relying on the mobility of cars (we use a toy car) to sense the vibration response of the roads being monitored.

### 1.2 Goals

This project presents an alternative system – Patrolman, using Raspberry Pi to detect and report road potholes with their georeferenced locations. It uses the mobility of the participating vehicles, gathering data from the six-axis accelerometer and GPS sensors, and processing the data to assess road surface conditions. This project will provide an affordable sensing method to conduct pavement condition assessments.

## 2 For Progress Reports

#### [Progress Report_Oct 5th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/progress_report_1.md)
#### [Progress Report_Oct 8th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/progress_report_2.md)
#### [Progress Report_Oct 15th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/progress_report_3.md)
#### [Progress Report_Oct 17th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/progress_report_4.md)


## 3 Methodology

### 3.1 Phenomena of Interest

Road conditions are naturally sensed from a moving entity that can measure vibrations and impulses during a drive [4]. The general monitoring metrics intended to measure road condition and performance including:

1. Vibration - Acceleration is the most common measure taken to characterize vibrations. When the vehicle drive on flat road conditions, the three x, y, and z gravity of acceleration values (g) were steady while the three x, y, and z gravity of acceleration values (g) reflect pulse signals on road with potholes.

2. Georeferenced locations - GPS is linked to each accelerometer for data to be georeferenced. Therefore, we record the locations of detected road potholes.

### 3.2 Sensor(s) Used

The Patrolman system consists of Raspberry Pi, MPU-6050 six-axis accelerometers, GPS, and a battery. In this project, the team collect driving data of vehicles (we use a toy car instead), and leverages sensors mounted on a testing vehicle.

  - Accelerometer: MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS

MPU6050 sensor module is complete 6-axis Motion Tracking Device. It combines 3-axis Gyroscope, 3-axis Accelerometer and Digital Motion Processor all in small package. Also, it has additional feature of on-chip Temperature sensor. It has I2C bus interface to communicate with the microcontrollers.

#### Features and Specifications
```markdown
  - Tri-Axis angular rate sensor with a sensitivity up to 131 LSBs/dps and a full-scale range of ±250, ±500, ±1000, and ±2000dps
  - Tri-Axis accelerometer with a programmable full scale range of ±2g, ±4g, ±8g and ±16g
  - VDD Supply voltage range of 2.375V – 3.46V 
  - VLOGIC (MPU-6050) at 1.8V ± 5% or VDD
  - Gyro operating current: 3.6mA (full power, gyro at all rates)
  - 400kHz Fast Mode I²C or up to 20MHz SPI serial host interfaces
  - Gyroscope readings are in degrees per second (dps) unit; Accelerometer readings are in g unit.
```
#### Accelerometer Placement

图和方向

  - GPS sensor: L76X GPS Module

L76X GPS Module is a general Global Navigation Satellite System (GNSS) module which supports Multi-GNSS systems: GPS, BDS, and QZSS, with advantages such as small size, fast positioning, high accuracy, and low power consumption.

#### Features
```markdown
  - Supports Multi-GNSS systems: GPS, BDS, and QZSS
  - EASY™, self track prediction technology, help quick positioning
  - AlwaysLocate™, intelligent controller of periodic mode for power saving
  - Supports DGPS, SBAS (WAAS/EGNOS/MSAS/GAGAN)
  - UART communication baudrate: 4800~115200bps (9600bps by default)
  - Onboard rechargeable Li battery MS621FE, for preserving ephemeris information and hot starts
  - 2x LEDs for indicating the module working status
  - Comes with development resources and manual (examples for Raspberry Pi/Arduino/STM32)
```

#### GNSS Specifications
```markdown
  - Band: GPS L1(1575.42Mhz), BD2 B1 (1561.098MHz)
    - Channels: 33 tracking ch, 99 acquisition ch, 210 PRN ch
    - C/A code
    - SBA: WAAS, EGNOS, MSAS, GAGAN
  - Horizontal position accuracy:
    - Autonomous: <2.5mCEP
  - Time-To-First-Fix @-130dBm (EASY™ enabled):
    - Cold starts: <15s
    - Warm starts: <5s
    - Hot starts: <1s
  - Sensitivity:
    - Acquisition: -148dBm
    - Tracking: -163dBm
    - Re-acquisition: -160dBm
  - Dynamic performance:
    - Altitude (max): 18000m
    - Velocity (max): 515m/s
    - Acceleration (max): 4G
```

#### General Specifications
```markdown
  - Communication interface: UART
  - Baudrate: 4800~115200bps (9600bps by default)
  - Update rate: 1Hz (default), 10Hz (max)
  - Protocols: NMEA 0183, PMTK
  - Power supply voltage: 5V / 3.3V
  - Operating current: 11mA
  - Operating temperature: -40℃ ~ 85℃
  - Dimensions: 32.5mm x 25.5mm
```

#### Applications
```markdown
  - Vehicle tracking
  - Asset tracking
  - Security system
  - Industrial PDA
  - GIS application
```
#### Development Resources
Wiki : www.waveshare.com/wiki/L76X_GPS_Module

### 3.3 Signal Conditioning and Processing

#### Sampling frequency

According to the sampling principle, the sampling frequency (fs) needs to be at least twice the measured signal frequency (fh): fs > 2fh. If the sampling frequency was chosen to be too small, not only the raw signal could not be described clearly and correctly, but also aliasing would occur, which block the way to attain the useful data information.

  - Accelerometer: The accelerator sensor is installed on the moving cars to test its vibration on the z-axis. Due to the limitation of Raspberry Pi, the team uses  10 Hz frequency at first and a host of pre-experiments were conducted.
  
  - GPS sensor: The max frequency of GPS module is 10Hz, and the default frequency is 1 Hz. Here, the team uses the default frequency.

#### Absent value of sensors

GPS receivers often encounter missing signals, especially when the GPS receiver is moving and encounter various obstructions such as bridges, buildings, tunnels, etc. The receiver cannot receive GPS signals with sufficient signal-to-noise ratio, and the positioning may be interrupted. In most cases, this positioning interruption lasts for a short time. In our experiments, we can use the linear interpolation between GPS readings as the georeferenced locations due to the low speed of the testing cars.

For the zero readings of the accelerometer, the team also ﬁlls the missing values with linear interpolation.

#### Signal smoothing

To discover important patterns in our data while leaving out things that are unimportant (i.e. noise), the teams apply moving average to smooth the accelerometer signals. The goal of smoothing is to produce slow changes in value so that it's easier to see trends in our data.

### 3.4 Pavement defect patterns

The team focused on collecting a diverse set of samples, including the following event classes:

  - Smooth road (SM): Segments of road surface that are considered smooth.
  
  - Potholes (PH): Missing chunks of pavement, severely sunk in or protruding manhole covers, other signiﬁcant road surface anomalies.
  
  - Upheaval (UH): Upheaval is a localized upward movement in a pavement due to swelling of the subgrade.

(Figure!!! 实地和信号图)

## 4 Experiments and Results

### Data collection

  - Getting hardware
We have purchased Raspberry Pi and sensors (GPS module and MPU-6050 six-axis accelerometers) from [Taobao](https://www.taobao.com/).

  - Set up the test environment
We have built the sensors (including GPS module and MPU-6050 six-axis accelerometers) and written Python codes to monitor the parameters based on the tutorials.

<div align="center"><img width="400" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/sensor_all_1.jpg"/></div>

  - GPS module test results

    - Hardware connection
    
Connect L76X GPS module to the board. Four pins are available for use: VCC, GND, TX, and RX.

| L76X GPS Module  | Raspberry Pi (Board)  | Raspberry Pi (BCM) |
| :----: | :----: | :----:|
| VCC | 5v | 5 |
| GND | GND | GND |
| TX | 10 | P15 |
| RX | 8 | P14 |

<div align="center"><img width="400" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/GPS.png"/></div>

  - Running code

Run the test code [GPS.py](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/code/GPS.py). The test results are shown as follows:

<center class="half">
    <img src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/gps_test1.png" width="300"/><img src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/gps_test3.png" width="300"/>
</center>

- MPU 6050 sensor test results

  - Hardware connection
  
Connect MPU 6050 sensor to the board. Four pins are available for use: VCC, GND, SDA, and SCL.

<div align="center"><img width="400" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu6050.jpeg"/></div>

| MPU 6050  | Raspberry Pi (Board)  |
| :----: | :----: |
| VCC | 3.3v |
| GND | GND |
| SDA | P3 |
| SCL | P5 |

  - Running code

Run the test code [Acceleration.py](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/code/Acceleration.py). The test results are shown as follows:

![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu_test1.png)

![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu_test2.png)

### Indoor experiments


### (1) Getting the toy car
We have purchased the toy car from [Taobao](https://www.taobao.com/).

<div align="center"><img width="600" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/car.png"/></div>

### (2) Install the raspberry pi and sensors on the toy car

We have installed the raspberry pi，the sensor MPU-6050 Six-Axis (Gyro + Accelerometer) and GPS module on the toy car.

<div align="center"><img width="600" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/sensor_all_2.png"/></div>


### (3) Indoor Testing results

<div align="center"><img width="600" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/indoor_situation.png"/></div>

Test results of Z-axis acceleration show significant patterns when the car crosses over the road obstacle compared to the smooth road surface.


<div align="center"><img width="1000" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu_indoor_test.png"/></div>

<div align="center"><img width="800" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu_indoor_test_2.png"/></div>

<div align="center"><img width="800" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu_indoor_test_3.png"/></div>


### Outdoor experiments

The team collectes the hand-labeled data by repeatedly driving down several known stretches of roads, and continuously recording raw accelerometer traces. Traces were post-processed to select out only the sample windows containing a corresponding event that appeared signiﬁcant, in order to eliminate delay and inaccuracy in the human-recorded annotations.

<div align="center"><img width="400" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/sensor_all.png"/></div>

### Pothole detection

The intuition behind our algorithm is that anomalous road conditions are reﬂected in features of the acceleration data. The problem of identifying potholes from accelerometer data is challenging because of the broad variation in road conditions (e.g., various types of road surfaces and anomalies such as potholes, manholes, curbs, railroad crossings, and expansion joints). While most anomalies can be characterized as high-energy events in the acceleration signal, signal energy content alone is not sufﬁcient as a detection criterion, because many high-energy events should not be considered road anomalies.



## 5 Discussion

Discuss the insights from the project

## References

[1] Editor, Swindonian (30 December 2018). "More than half a million potholes were reported last year throughout the UK". The Swindonian. Retrieved 2 January 2019.

[2] Hingston, Michael (April 2015). "Asphalt Nerds The alchemy of pavement in Canada's pothole capital". The Walrus. Retrieved 20 March 2015.

[3] S, Kamaljit Kaur; DelhiJuly 24, hu; July 24, 2018UPDATED; Ist, 2018 00:37. "Over 9300 deaths, 25000 injured in 3 years due to potholes". India Today. Retrieved 4 August 2019.

[4] Eriksson, J., Girod, L., Hull, B., Newton, R., Madden, S., & Balakrishnan, H. (2008). The Pothole Patrol: Using a mobile sensor network for road surface monitoring. In MobiSys’08 - Proceedings of the 6th International Conference on Mobile Systems, Applications, and Services (pp. 29–39).

[5] L76X GPS Module User Manual. https://www.waveshare.com/w/upload/5/5b/L76X_GPS_Module_user_manual_en.pdf.

[6] 13 PAVEMENT DEFECTS AND FAILURES YOU SHOULD KNOW. https://www.pavemanpro.com/article/identifying_asphalt_pavement_defects/.

