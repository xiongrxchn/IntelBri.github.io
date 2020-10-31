# Progress Report 1 (Oct 5th)


## Current progress

### Narrow down the goal of project

We design a system named Patrolman to monitor the road surface conditions. In specific, the team makes use of the inherent mobility of the vehicles to gather signals from the accelerometer and GPS sensors.

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
