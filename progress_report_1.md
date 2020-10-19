# Progress Report 1 (Oct 5th)


## Current progress

### (1) Getting hardware
We have purchased Raspberry Pi and sensors (GPS module and MPU-6050 six-axis accelerometers) from [Taobao](https://www.taobao.com/).

### (2) Set up the test environment
We have built the sensors (including GPS module and MPU-6050 six-axis accelerometers) and written Python codes to monitor the parameters based on the tutorials.

#### GPS module test results

  - Hardware connection
Connect L76X GPS module to the board. Four pins are available for use: VCC, GND, TX, and RX.

| L76X GPS Module  | Raspberry Pi (Board)  | Raspberry Pi (BCM) |
| :----: | :----: | :----:|
| VCC | 5v | 5 |
| GND | GND | GND |
| TX | 10 | P15 |
| RX | 8 | P14 |

<div align="left"><img width="400" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/GPS.png"/></div>

- Running code

Run the test code [GPS.py](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/code/GPS.py). The test results are shown as follows:


<div align="left"><img width="600" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/gps_test1.png"/></div>

<div align="left"><img width="600" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/gps_test2.png"/></div>

<div align="left"><img width="600" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/gps_test3.png"/></div>


#### MPU 6050 sensor test results

  - Hardware connection
  
Connect MPU 6050 sensor to the board. Four pins are available for use: VCC, GND, SDA, and SCL.

| MPU 6050  | Raspberry Pi (Board)  |
| :----: | :----: |
| VCC | 3.3v |
| GND | GND |
| SDA | P3 |
| SCL | P5 |

<div align="left"><img width="400" src="https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu6050.jpeg"/></div>

- Running code

Run the test code [Acceleration.py](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/code/Acceleration.py). The test results are shown as follows:

![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu_test1.png)

![image](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh1-pages/Images/mpu_test2.png)

## Future Plan
- Complie all sensors together and test the system under indoor environments.
