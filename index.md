# IoT based Bridge Health Monitoring and Evaluating System

• [Pengkun Liu](pengkunl@andrew.cmu.edu); [Ruoxin Xiong](ruoxinx@andrew.cmu.edu)

### video link:


## 1 Introduction


![](/Images/background.png)

The deteriorating and aging infrastructures continue to challenge transportation authorities as they align maintenance and replacement priorities with decreasing funds. According to the 2020 bridge reports from the Federal Highway Administration, more than one third (37 percent) of U.S. bridges—nearly 231,000 spans, need repair work. More than 46,000 bridges are rated in poor condition and classified as “structurally deficient.” [1]. Our project uses an Internet of Things (IoT) based monitoring system for bridge health evaluation and maintenance. We expect this system can detect changes in the bridge superstructure and, in some cases, predict impending failures.

### 1.1 Motivation

Bridge engineers need a reliable way to assess structural integrity of bridges to maintain the continuous operation of the road network while ensuring the safety of the public. Traditional visual inspection techniques are both time consuming, subjective and costly. They can only assess visual appearance [2]. The internal damages may be unnoticed for a long period of time. To address these issues, our project applies an Internet of Things (IoT) based structural health monitoring system. IoT technologies offer the ability to combine several sensors to obtain a more complete assessment. Currently, these methods will provide a better picture of the overall bridge condition.

### 1.2 Goals

The main goal of this project is to establish and calibrate an IoT based bridge health monitoring and evaluation system. This system enable the integration of distributed sensors for continuous, portable, and real-time monitoring for bridges.

- integrate multiple sensors to monitor the vibration, climatic conditions, and traffic flow signals;

- apply de-noise algorithms to detect and remove anomaly signals from the sensors;

- identify the alarming signals from sensors and issue an alarm with the buzzer.

## 2 For Progress Reports

#### [Progress Report_Oct 5th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/progress_report_1.md)


## 3 Methodology

### 3.1 Phenomena of Interest

The general monitoring metrics intended to measure bridge condition and performance including:

1. Vibration - the instantaneous rate at which the velocity of a point in a vibrating bridge is changing with time. Acceleration is the most common measure taken to characterize vibrations. The frequencies and modes can be compared to values obtained from previous acceleration measurements to determine if the bridge has deteriorated or has been damaged.

2. Climatic Conditions - pertains to the environmental conditions in the area of the bridge that may relate to bridge performance. Parameters that can be measured include: air temperature and relative humidity.

3. Traffic flow - the total vehicles passing over a particular area of a bridge. This measure can be useful to enforce weight restrictions, as well as to define the range (i.e., spectrum) of typical traffic loads.

### 3.2 Sensor(s) Used
![](/Images/sensor_all.png)


(1) Gyro + Accelerometer: MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS

The MPU-6050 parts are the world’s first MotionTracking devices designed for the low power, low cost, and high-performance requirements of smartphones, tablets and wearable sensors. It combines a 3-axis gyroscope and a 3-axis accelerometer on the same silicon die.

```markdown
Features and Specifications:

- Tri-Axis angular rate sensor with a sensitivity up to 131 LSBs/dps and a full-scale range of ±250, ±500, ±1000, and ±2000dps
- Tri-Axis accelerometer with a programmable full scale range of ±2g, ±4g, ±8g and ±16g
- VDD Supply voltage range of 2.375V – 3.46V 
- VLOGIC (MPU-6050) at 1.8V ± 5% or VDD
- Gyro operating current: 3.6mA (full power, gyro at all rates)
- 400kHz Fast Mode I²C or up to 20MHz SPI serial host interfaces 




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
