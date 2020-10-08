# Progress Report 2 (Oct 8th)


## Current progress

### Narrow down the goal of project

Due to monitoring the bridge vibration requiring high sampling frequencies, the sampling frequencies of Raspberry Pi is not sufficient.
We would focus on part of the bridge health monitoring, for example, the bridge road surface monitoring.

The main goal of this project is to establish and calibrate an IoT based bridge health monitoring and evaluation system. This system enable the integration of distributed sensors for continuous, portable, and real-time monitoring for bridges.

- integrate multiple sensors to monitor the vibration, climatic conditions, and traffic flow signals;

- apply de-noise algorithms to detect and remove anomaly signals from the sensors;

- identify the alarming signals from sensors and issue an alarm with the buzzer.


## Problems Encountered

### (1) How to set up the experiment environments?
We can set up our experiments on real scenarios or simulated bridges. Collecting real bridge data may require some restricted safety permissions from the bridge management institutes. So we may establish simulated experimental environments to collect sensor data. We have chosen some bridge models online, as shown in the Figure. We then must figure out how to add different vehicle loads on the bridge to simulate the vibration features of bridges?




## Future Plan
- Build the simulated physical models of the bridge and install the sensors on the suitable locations of the bridge.
- determine the appropriate sampling frequencies for both sensors and finish the control part of the codes.
- Connect all sensors to OpenChirp and remove the anomaly signals.
- Analyze the collected signals and identify the alrmaing cases.
