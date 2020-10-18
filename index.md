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

The Patrolman system consists of Raspberry Pi, MPU-6050 six-axis accelerometers, GPS, and a battery. In this project, the team collect driving data of vehicles (we use a toy car instead), and leverages sensors including GPS, accelerometer mounted on a testing vehicle.

![](/Images/sensor_all.png)

(1) Gyro + Accelerometer: MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS

![](/Images/MPU_6050.png)

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


(2) GPS

![](/Images/GPS.png)

![](/Images/GPS_interface.png)




(1) Camera sensor: The Raspberry Pi Camera Module v2

```markdown
Features and Specifications:

- Number of Channels: 1
- Maximum Supported Resolution: 3280 x 2464
- Maximum Frame Rate Capture: 30fps
- Dimensions: 3.86 x 25 x 9mm
- Maximum Operating Temperature: +60 °C
- Minimum Operating Temperature: -20 °C
```

(2) Temperature and humidity sensor: DHT11 Temperature-Humidity Sensor Module

The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed).

```markdown
Features and Specifications:

- Power supply: 3.3-5V
- Current: 2.5mA max use of current during conversion (when data request)
- Humidity: 20-90% ± 5%
- Temperature: 0-50°C ± 2%
- Sampling rate: ≤ 1Hz
```

(3) Vibration sensor: SW-420 Vibration Sensor

The SW-420 Vibration sensor can be used to detect vibration from any angle. There is an on-board potentiometer to adjust the threshold of vibration. It outputs logic HIGH when this module not triggered while logic Low when triggered.

```markdown
Features and Specifications:

- Operating Voltage: 3.3V to 5V DC
- Operating Current: 15mA
- Using SW-420 normally closed type vibration sensor
- LEDs indicating output and power
- Easy to use with Microcontrollers or even with normal Digital/Analog IC
```


(5) The team also use buzzer to warn drivers when identifying alarming signals.

As a type of electronic buzzer with integrated structure, buzzers, which are supplied by DC power, are widely used in computers, printers, photocopiers, alarms, electronic toys, automotive electronic devices, telephones, timers and other electronic products for voice devices.

```markdown
Features and Specifications:

- Rated Voltage: 6V DC
- Operating Voltage: 4 - 8V DC
- Rated current: < 30mA
- Sound Type: Continuous Beep
- Resonant Frequency: ~2300Hz 
```

### 3.3 Signal Conditioning and Processing

According to the sampling principle, the sampling frequency (fs) needs to be at least twice the measured signal frequency (fh): fs > 2fh. If the sampling frequency was chosen to be too small, not only the raw signal could not be described clearly and correctly, but also aliasing would occur, which block the way to attain the useful data information.

Accelerometer: The accelerator sensor is installed under the middle of the bridge to test its vibration on the z-axis. It is hard for us to calculate the frequency response of the deck. To find the appropriate sampling rate, a 1 kHz frequency was used at first and a host of pre-experiments were conducted. 

## 4 Experiments and Results

Describe the experiments you did and present the results; Use tables and plots if possible





## 5 Discussion

Discuss the insights from the project

## References

[1] Andrew Gastineau, Tyler Johnson, Arturo Schultz, Bridge Health Monitoring and Inspections – A Survey of Methods, September 2009. [http://www.lrrb.org/pdf/200929.pdf](http://www.lrrb.org/pdf/200929.pdf).

[2] 2020 Bridge Reports, American Road and Transportation Builders Association, 
[https://artbabridgereport.org/reports/2020%20ARTBA%20Bridge%20Report.pdf](https://artbabridgereport.org/reports/2020%20ARTBA%20Bridge%20Report.pdf).

[3] Ahlborn, Tess & Shuchman, Robert & Sutter, Larry & Harris, Devin & Brooks, Colin & Burns, Joseph. (2013). Bridge Condition Assessment Using Remote Sensors. [https://www.mtu.edu/mtri/research/project-areas/transportation/infrastructure/bridge-condition/final-report-main-body.pdf](https://www.mtu.edu/mtri/research/project-areas/transportation/infrastructure/bridge-condition/final-report-main-body.pdf).
