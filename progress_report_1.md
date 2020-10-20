# Progress Report 1 (Oct 5th)


## Current progress

### Narrow down the goal of project
Due to monitoring the bridge vibration requiring high sampling frequencies, the sampling frequencies of Raspberry Pi is not sufficient. We would focus on part of the bridge health monitoring, for example, the bridge road surface monitoring. 

We investigates an application of mobile sensing: detecting and reporting the surface conditions of roads. We describe a system and associated algorithms to monitor this important bridge using a collection of sensor-equipped vehicles. In specific, uses the inherent mobility of the participating vehicles, opportunistically gathering data from vibration and GPS sensors, and processing the data to assess road surface conditions.

### New developed theme with same sensors: Automatic detection of road pothole

The monitoring of bridge vibration requires high-frequency acquisition systems.

#### Goals:

- Identify the road potholes and records its locations;
- Classify the relative scale of potholes.

#### Phenomena of Interest

- Acceleration - the moving objects will show different features acceleration when entering the road potholes;
- GPS - record the locations of road potholes.

#### Sensors
- Accelerometer: MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS 
MPU allows a sample rate of 8kHz only for the gyrometer, the accelerometer allows only 1kHz.

- GPS module (1 Hz)
Resulting in the following information:
<time,location,speed,heading,3-axis acceleration>

#### Reference:
https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi
https://www.electronicwings.com/raspberry-pi/gps-module-interfacing-with-raspberry-pi
