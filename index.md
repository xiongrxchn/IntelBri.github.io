# IoT based Bridge Health Monitoring Evaluating System

• [Pengkun Liu](pengkunl@andrew.cmu.edu); [Ruoxin Xiong](ruoxinx@andrew.cmu.edu)

### video link:


## Introduction


![](/Images/background.png)

Increases in traffic have puts more and more strain on the bridge networks than was originally intended. According to the 2020 bridge reports from the Federal Highway Administration, more than one third (37 percent) of U.S. bridges—nearly 231,000 spans—need repair work. More than 46,000 bridges are rated in poor condition and classified as “structurally deficient.” A total of 81,000 bridges should be replaced. Our project is to use an Internet of Things (IoT) based structural health monitoring system for bridge health evaluation and maintenance. These systems can detect changes in the bridge superstructure and, in some cases, predict impending failures.

### Motivation

Bridge engineers need a reliable way to assess structural integrity of bridges to maintain the continuous operation of the road network while ensuring the safety of the public. Traditional visual inspection techniques are both time consuming and expensive. They are also qualitative and can only assess outward appearance. Any internal damage may go unnoticed for a long period of time. How does a bridge engineer keep track of these problems? A possible solution to these issues is the use of an Internet of Things (IoT) based structural health monitoring system. These systems can detect changes in the bridge superstructure and, in some cases, predict impending failures.

The challenges of a deteriorating and aged infrastructure continue to challenge transportation authorities as they align maintenance and replacement priorities with decreasing funds.

No single structural health monitoring (SHM) method exists that is capable of completely determining the condition of a bridge. Current assessment methods provide critical information about the condition of a bridge, but the data obtained must be interpreted by a skilled professional and are typically limited to local metrics.

IoT technologies offer the ability to combine several methods to obtain a more complete assessment. Currently, these methods will provide a better picture of the overall bridge condition.

### Goals

The goal of IoT based structural monitoring is to enable the integration of distributed sensors for continuous, portable, and real-time monitoring for bridges. 


## For Progress Reports

#### [Progress Report_Oct 5th](https://github.com/xiongrxchn/IntelBri.github.io/blob/gh-pages/progress_report_1.md)

## Methodology

### Phenomena of Interest

Describe the physical phenomena of interest, e.g. physical principles, static and dynamic behavior, and signal characteristics

The general monitoring metrics intended to measure bridge condition and performance including:

1. Acceleration - the instantaneous rate at which the velocity of a point in a vibrating bridge is changing with time. Acceleration is the most common measure taken to characterize vibrations. It is possible to define the frequencies and shapes of the different modes of vibration from a single acceleration trace. The frequencies and modes can be compared to values obtained from previous acceleration measurements to determine if the bridge has deteriorated or has been damaged.

2. Climatic Conditions - pertains to the environmental conditions in the area of the bridge that may relate to bridge performance. Parameters that can be measured include: air temperature and relative humidity.

3. Traffic flow - the total load of objects passing over a particular area of a bridge. This measure can be useful to enforce weight restrictions, as well as to define the range (i.e., spectrum) of typical traffic loads.

### Sensor(s) Used

Camera:

![](https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/daaa041609e59f61893be36888d21d5888bcc3fb/en/images/pi-camera-attached.jpg)

Temperature and humidity sensor:
DHT11 Temperature-Humidity Sensor Module is a cheap and reliable sensor using an ADC to convert analog values of humidity and temperature. It comes with an 8-bit microcontroller and provides reliable output results.[2]
Parameters:
```markdown
- Power supply: 3.3 - 5 V
- Current: 2.5 mA max use of current during conversion (when data request)
- Humidity: 20 - 90 % ± 5 %
- Temperature: 0 - 50º ± 2 %
- Sampling rate: ≤ 1 Hz
```

Vibration: vibration sensor
Vibration Sensor Module Features & Specifications
```markdown
- Operating Voltage: 3.3V to 5V DC
- Operating Current: 15mA
- Using SW-420 normally closed type vibration sensor
- LEDs indicating output and power
- LM393 based design
- Easy to use with Microcontrollers or even with normal Digital/Analog IC
- With bolt holes for easy installation
- Small, cheap and easily available
```

Buzzer
The team use buzzer to warn drivers when the window is fogging. A buzzer can be sorted as a passive or active buzzer. An active buzzer has a built-in oscillating source. Thus, it will make sounds when electrified. But a passive buzzer does not have such a source, so it will not tweet if DC signals are used; instead, you need to use square waves whose frequency is between 2K and 5K to drive it. The active buzzer is often more expensive than the passive one because of multiple built-in oscillating circuits. Its detailed characteristics and connection information are shown below:

Buzzer Features and Specifications
```markdown
- Rated Voltage: 6V DC
- Operating Voltage: 4-8V DC
- Rated current: <30mA
- Sound Type: Continuous Beep
- Resonant Frequency: ~2300 Hz 
- Small and neat sealed package
- Breadboard and Perf board friendly
```

### Signal Conditioning and Processing

Describe the signal conditioning and processing procedures
According to the sampling principle, the sampling frequency (fs) needs to be at least twice the measured signal frequency (fh): fs>2fh. If the sampling frequency was chosen to be too small, not only the raw signal could not be described clearly and correctly, but also aliasing would occur, which block the way to attain the useful data information.

Accelerometer:
The accelerator sensor is installed under the middle of the bridge to test its vibration on the z-axis. It is hard for us to calculate the frequency response of the deck. To find the appropriate sampling rate, a 1 kHz frequency was used at first and a host of pre-experiments were conducted. 

## Experiments and Results

Describe the experiments you did and present the results; Use tables and plots if possible

## Discussion

Discuss the insights from the project

## References

[1] Andrew Gastineau, Tyler Johnson, Arturo Schultz, Bridge Health Monitoring and Inspections – A Survey of Methods, September 2009. http://www.lrrb.org/pdf/200929.pdf.

[2] 2020 Bridge Reports, American Road and Transportation Builders Association, 
https://artbabridgereport.org/reports/2020%20ARTBA%20Bridge%20Report.pdf.

[3] Ahlborn, Tess & Shuchman, Robert & Sutter, Larry & Harris, Devin & Brooks, Colin & Burns, Joseph. (2013). Bridge Condition Assessment Using Remote Sensors. https://www.mtu.edu/mtri/research/project-areas/transportation/infrastructure/bridge-condition/final-report-main-body.pdf
