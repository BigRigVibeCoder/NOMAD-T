---
ID: HM-CAT-006
Status: ACTIVE
Source: github.com/BigRigVibeCoder/HiveMind
---

# Component Specification: Slamtec RPLIDAR C1

Role: Primary Indoor Localization & Mapping Sensor

Architecture: DTOF (Direct Time-of-Flight) Laser Scanner

Interface: USB 2.0 (via CP210x Bridge)

Scanning Frequency: 10 Hz (Adjustable 5-12 Hz)

## 1. Core Concept: "The 360° Ruler"

The RPLIDAR C1 is a significant upgrade from the older A1/A2 series. Instead of using a camera to triangulate a laser dot (which is bulky and sensitive to light), the C1 measures the time it takes for a laser pulse to bounce back.

- **Technology:** Direct Time-of-Flight (DTOF).

- **Field of View:** 360° (Full rotation).

- **Range:** 0.05m to 12m.

- **Resolution:** &lt; 2cm accuracy.

- **Environment:** **Outdoor Ready** (40,000 Lux resistance). This is the key reason we chose the C1 over the A1—it won't go blind on a sunny driveway.

**Engineering Implication:** Unlike the A1, the C1 is a sealed, compact unit with no external belt. This makes it far more durable for a walking robot that experiences vibration and dust.

## 2. Hardware Architecture

### 2.1 Physical Characteristics

- **Dimensions:** 55.6mm x 59.8mm x 41.3mm. (Tiny footprint).

- **Weight:** 110g. (Minimal impact on the robot's center of gravity).

- **Motor:** Brushless (Long lifespan, low noise).

### 2.2 Data Output

- **Sample Rate:** 5,000 points per second.

- **Angular Resolution:** 0.72° (at 10Hz).

- **Safety:** Class 1 Laser (Eye Safe).

## 3. Data Interface & Protocol

The C1 connects via a standard USB-Serial adapter (CP2102) included in the box.

### 3.1 The "Scan" Packet

The device outputs a continuous stream of polar coordinates.

- **Format:** `[Quality, Angle, Distance]`

  - `Quality`: Signal strength (0-255). Helps filter out dust/ghosts.

  - `Angle`: 0° to 360°.

  - `Distance`: Millimeters.

### 3.2 Power Requirements

- **Voltage:** 5V DC (Powered directly via USB).

- **Current:** \~200mA (Very efficient).

## 4. ROS 2 Integration (`sllidar_ros2`)

Slamtec provides an official, well-maintained ROS 2 driver.

### 4.1 Installation

We do not write the driver. We compile the official package in our `deploy_k9.sh` script.

```
sudo apt install ros-jazzy-sllidar-ros2

```

### 4.2 Topics & Messages

<table style="min-width: 75px;">
<colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><td colspan="1" rowspan="1"><p><strong>ROS 2 Topic</strong></p></td><td colspan="1" rowspan="1"><p><strong>Message Type</strong></p></td><td colspan="1" rowspan="1"><p><strong>Description</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>/scan</code></p></td><td colspan="1" rowspan="1"><p><code>sensor_msgs/LaserScan</code></p></td><td colspan="1" rowspan="1"><p>The raw 2D slice of the world. Used by <code>Nav2</code> and <code>SLAM Toolbox</code>.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>/rpms</code></p></td><td colspan="1" rowspan="1"><p><code>std_msgs/UInt16</code></p></td><td colspan="1" rowspan="1"><p>Motor speed telemetry.</p></td></tr></tbody>
</table>

### 4.3 Configuration (`sllidar_node`)

We must set specific parameters in our launch file to match the C1.

```
channel_type: serial
serial_port: /dev/ttyUSB0  # (Or specific by-id path)
serial_baudrate: 460800    # C1 specific high-speed baud
frame_id: laser_frame
inverted: false
angle_compensate: true
scan_mode: Standard

```

## 5. Integration Strategy

### 5.1 Mechanical Mounting

- **Location:** **Top Rear Spine**.

- **Clearance:** It must be the highest point on the back to see over the "shoulders" of the robot.

- **Blind Spots:** The robot's own head (OAK-D) will create a small blind spot in the front. This is acceptable because the OAK-D covers that area with depth vision.

### 5.2 Interference Management

- **LIDAR vs. Vision:** The C1 uses infrared light (905nm). It operates on a different frequency than the OAK-D's ToF/Stereo sensors, so **no interference** is expected.

## 6. Summary for Engineers

The RPLIDAR C1 is the **"Localization Anchor."**

- **Input:** Laser pulses.

- **Output:** Precise distance to walls.

- **Usage:** It stops the map from drifting. While Odometry (Motor encoders) drifts by meters over time, the LIDAR snaps the robot back to the correct inch by matching the wall geometry.