# Progress Report 1 (Oct 5th)


## Current progress

### (1) Getting hardware
We have purchased Raspberry Pi and sensors (GPS module and MPU-6050 six-axis accelerometers) from [Taobao](https://www.taobao.com/).
![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/Images/Sensors.png)

### (2) Set up the test environment
We have built the sensors (including GPS module and MPU-6050 six-axis accelerometers) and written Python codes to monitor the parameters based on the tutorials.

#### GPS module test results

(a)Hardware connection
Connect L76X GPS module to the board. Four pins are available for use: VCC, GND, TX, and RX.

| L76X GPS Module  | Raspberry Pi (Board)  | Raspberry Pi (BCM) |
| :----: | :----: | :----:|
| VCC | 5v | 5 |
| GND | GND | GND |
| TX | 10 | P15 |
| RX | 8 | P14 |

#### Camera sensor test results

We have learned how to connect the Raspberry Pi Camera Module to the Raspberry Pi and take pictures, record video, and apply image effects.

<div align="center"><img width="800" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/Images/camera_test.png"/></div>

<div align="center"><img width="800" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/Images/Motion_detector.png"/></div>

#### SW-420 vibration sensor test results

The working volatage of vibration sensor is 3.3V-5V and this project use the 3.3V as power supply.When there is no vibration,it output low level voltage and the light signal turns on;When there is any vibration, it output high-level voltage and the light signal turns off.

![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/Images/sw40.png)

### (3) Sensor Placement Plan
We designed a preliminary plan for sensor placement. The camera is placed at the entrance of the bridge to monitor and detect the traffic flow. The vibration sensor, temperature and humidity sensor are both set in the middle of the bridge to reflect the typical measurements of the bridges. Meanwhile, the buzzer is also placed in the middle of the bridge to issue the safety alarms if the measurements exceed the predefined thresholds.

![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/Images/Sensor_pla.png)

## Problems Encountered

### (1) How to set up the experiment environments?
We can set up our experiments on real scenarios or simulated bridges. Collecting real bridge data may require some restricted safety permissions from the bridge management institutes. So we may establish simulated experimental environments to collect sensor data. We have chosen some bridge models online, as shown in the Figure. We then must figure out how to add different vehicle loads on the bridge to simulate the vibration features of bridges?

![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/Images/bridge%20model.png)

### (2) How to choose the proper thresholds for safety alarms?
One of the goals of this project is to issue safety alarms to the drivers and pedestrian when the measurements exceed the defined threshold. One possible way is to look up the bridge standards regarding vibrations and traffic flows.

### (3) How to detect and remove the anomaly signals from sensors?
During the continuous data collection process, there may be abnormal values, including zero values, null values, or no changes in the data within a certain time range, or abnormal values. These abnormal data will have a great impact on future data mining work. Therefore, in order to improve data quality, simple judgment and processing of these abnormal signals are required.

### (4) How to unify the time scale of the multi-data for each channel?
The data in the bridge monitoring system is collected by various sensors such as temperature and humidity, acceleration sensor. Because the working principle of the sensor and the working performance of the instrument are different, the sampling frequency of each sensor cannot be completely consistent. However, for bridge monitoring, it is necessary to understand the structural response of each part of the same period in order to clearly understand the mechanical properties of the overall structure.

### (5) How to achieve optimal sensor placement of bridges?
We have designed a preliminary sensor placement plan. However, it remains to be answered if this plan can achieve the optimal collection of reliable and comprehensive health information for structural state change information.

### (6) Incorrect sensors for vibration measurements.
At first, we tried to use vibration sensor in the KOOKYE Smart Home Sensor Kit to measure the vibration of bridges. However, we didn't realize the vibration sensor only output binary signals until we conduct experiments on the sensor. The vibration sensor will output high level voltage when it detect vibration and output low level voltage when no vibration. So we have purchased MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS to measure the virbration signals of bridges this week.

## Future Plan
- Build the simulated physical models of the bridge and install the sensors on the suitable locations of the bridge.
- determine the appropriate sampling frequencies for both sensors and finish the control part of the codes.
- Connect all sensors to OpenChirp and remove the anomaly signals.
- Analyze the collected signals and identify the alrmaing cases.
