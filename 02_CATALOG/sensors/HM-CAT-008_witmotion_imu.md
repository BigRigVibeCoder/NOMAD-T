---
ID: HM-CAT-008
Status: ACTIVE
Source: github.com/BigRigVibeCoder/HiveMind
---

# Inertial Measurement Unit (IMU) - WitMotion WT901SDCL

**Role:** Proprioception & Balance (The Inner Ear)

**Hardware:** WitMotion WT901SDCL (USB-C Version)

**Interface:** USB 2.0 (Virtual Serial / TTL)

## 1. Hardware Overview

The WT901SDCL is a high-performance Attitude and Heading Reference System (AHRS). Unlike raw sensor chips, it contains an internal **Cortex-M4 Core** running a high-speed Kalman Filter to fuse raw data into stable orientation data on-device before sending it to the host.

### 1.1 Core Specifications

- **Sensors:** 9-Axis (3-axis Gyroscope, 3-axis Accelerometer, 3-axis Magnetometer).

- **Processor:** Internal Cortex-M4 (Running Dynamic Kalman Fusion).

- **Output Frequency:** Default 10Hz, Configurable up to **200Hz** (Recommended for K9) or 1000Hz.

- **Baud Rate:** Supports 115200 (Default) up to 921600.

- **Casing:** CNC Aluminum (Shields against RF interference from motors).

## 2. The Output Schema (Data Structure)

The device outputs data in two formats: **Raw Hexadecimal Packets** (at the serial level) which are converted into **ROS 2 Messages**.

### 2.1 The Serial Protocol (Raw Byte Stream)

If you inspect the raw USB data (`cat /dev/ttyUSB0`), you will see a stream of 11-byte packets starting with the header `0x55`.

| Header | Flag | Data Payload (8 Bytes) | Checksum | Meaning |
| --- | --- | --- | --- | --- |
| `0x55` | `0x51` | `axL axH ayL ayH azL azH TL TH` | `Sum` | **Acceleration** (g) & Temp |
| `0x55` | `0x52` | `wxL wxH wyL wyH wzL wzH TL TH` | `Sum` | **Angular Velocity** (deg/s) |
| `0x55` | `0x53` | `RolL RolH PitL PitH YawL YawH TL TH` | `Sum` | **Euler Angles** (Roll/Pitch/Yaw) |
| `0x55` | `0x54` | `HxL HxH HyL HyH HzL HzH TL TH` | `Sum` | **Magnetometer** (uT) |
| `0x55` | `0x59` | `Q0L Q0H Q1L Q1H Q2L Q2H Q3L Q3H` | `Sum` | **Quaternion** (Orientation) |

**Key Takeaway:** The "Angle" packet (`0x53`) and "Quaternion" packet (`0x59`) are the most valuable. They represent the *solved* math from the internal Kalman filter.

### 2.2 The ROS 2 Topic Schema (`sensor_msgs/Imu`)

The driver converts the raw hex into standard ROS 2 topics.

**Topic:** `/imu/data`\
**Message Type:** `sensor_msgs/msg/Imu`

```
header:
  stamp: {sec: 164000, nanosec: 500}
  frame_id: "imu_link"
orientation:             # Fused Data (From 0x59 Packet)
  x: 0.001
  y: 0.045
  z: -0.002
  w: 0.999
angular_velocity:        # Raw Gyro (From 0x52 Packet)
  x: 0.01
  y: -0.05
  z: 0.00
linear_acceleration:     # Raw Accel (From 0x51 Packet)
  x: 0.12
  y: 0.05
  z: 9.81 (Gravity)

```

**Topic:** `/imu/mag` (Optional)\
**Message Type:** `sensor_msgs/msg/MagneticField`

- Contains the raw X/Y/Z magnetic field data (From `0x54` Packet).

## 3. Integration Strategy

### 3.1 Physical Mounting (Critical)

- **Location:** Center of Mass (Middle of Bottom Plate).

- **Orientation:** \* **Label Up:** Z-axis points to sky.

  - **USB Port Back:** Ensure X-Axis arrow points to Robot Forward.

- **Fastening:** M2.5 or M3 screws + Loctite. Vibration damping is handled internally by the algorithm, but rigid mounting is preferred to prevent "sensor lag."

### 3.2 Software Setup (Ubuntu)

Because it uses a standard CH340 or CP2102 USB chip, Linux recognizes it instantly.

```
ls /dev/ttyUSB*
# Output: /dev/ttyUSB0 (or USB1)

```

## 4. ROS 2 Integration

### 4.1 Driver Installation

We use the standard driver which handles the hex parsing automatically.

```
sudo apt install ros-jazzy-witmotion-ros

```

### 4.2 Configuration Parameters

Set these in `imu_params.yaml`:

```
witmotion_imu:
  ros__parameters:
    port: "/dev/ttyUSB0"
    baud_rate: 115200   # Must match hardware setting
    poll_rate: 200      # 200Hz is ideal for walking robots
    frame_id: "imu_link"
    use_native_orientation: true # Use the internal Kalman filter (Better/Faster)

```

### 4.3 Calibration Procedure

**Do this ONCE before installing on the robot.**

1. Plug into Windows PC using WitMotion software.

2. Perform **Accelerometer Calibration** (Place flat, wait 3 sec).

3. Perform **Magnetic Calibration** (Rotate sensor in all 3 axes like a figure-8).

4. **Save to Flash.** The calibration is now stored on the device hardware.

## 5. Engineering Verdict

The **WT901SDCL** provides a pre-solved orientation vector. By subscribing to `/imu/data`, the Balance Controller knows exactly how much the robot is tilting without doing any trigonometry on the Main CPU.