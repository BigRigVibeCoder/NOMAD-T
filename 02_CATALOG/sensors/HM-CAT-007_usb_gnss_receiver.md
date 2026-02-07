---
ID: HM-CAT-007
Status: ACTIVE
Source: github.com/BigRigVibeCoder/HiveMind
---

# Component Specification: USB GNSS Receiver (The "Easy Button")

Role: Outdoor Global Localization

Hardware: VFAN USB GPS (UBX-G7020KT Chipset)

Interface: USB 2.0 (Virtual Serial Port)

Status: APPROVED

## 1. Hardware Overview

This unit is a "G-Mouse" style receiver. It encapsulates the antenna and the U-Blox 7 chipset into a single waterproof magnetic puck.

### 1.1 Specifications

- **Chipset:** UBX-G7020KT (U-Blox 7 Series).

- **Constellations:** GPS, GLONASS, QZSS, SBAS (56-Channel).

- **Protocol:** NMEA 0183 (Standard ASCII text).

- **Update Rate:** 1Hz - 10Hz (Default is usually 1Hz).

- **Accuracy:** \~2.5m (Standard Precision).

- **Mounting:** Magnetic Base.

- **Cable:** 2 Meters (6.5 ft).

## 2. Coordinate Systems (State-of-the-Art Standard)

The "Best-in-Class" Standard: WGS84 Decimal Degrees

Modern robotics pipelines (ROS 2, PX4, AutoWare) utilize WGS84 Latitude/Longitude natively.

- **Why it is the best:**

  - **Native Compatibility:** GPS satellites, Google Maps, and OpenStreetMap all speak this language. No conversion errors.

  - **Zero Friction:** The ROS standard message `sensor_msgs/NavSatFix` expects Lat/Long. Using this directly allows you to plug into tools like **Foxglove Studio** or **MapViz** instantly without writing custom adapters.

  - **Precision:** We use **Decimal Degrees** to 7+ decimal places (e.g., `34.052235, -118.243683`). This provides sub-meter resolution without the complexity of grid zones.

The Integration Strategy:

Instead of reading text coordinates (Old School), the SOTA approach is Visual Telemetry.

- **Robot:** Publishes Lat/Long.

- **Mission Control (Foxglove):** Automatically places a 3D robot icon on a streaming Satellite Map tile. You don't read coordinates; you look at the map.

## 3. Python Interfacing (Direct NMEA)

To use this directly in Python (bypassing ROS for testing), we read the raw NMEA stream. We strip away the MGRS conversion to reduce dependencies and latency.

### 3.1 Prerequisites

```
pip install pyserial pynmea2

```

### 3.2 The Parsing Script (`gps_reader.py`)

```
import serial
import pynmea2

# Configuration
PORT = "/dev/ttyACM0"  # or /dev/ttyUSB0
BAUD = 9600

def read_gps():
    try:
        with serial.Serial(PORT, BAUD, timeout=1) as ser:
            print(f"📡 Connected to GPS on {PORT} - Listening for Satellites...")
            while True:
                line = ser.readline().decode('ascii', errors='replace')
                
                # Filter for GNGGA or GPGGA (Global Positioning System Fix Data)
                if "GGA" in line:
                    try:
                        msg = pynmea2.parse(line)
                        lat = msg.latitude
                        lon = msg.longitude
                        sats = msg.num_sats
                        
                        # Output High-Precision Decimal Degrees
                        print(f"📍 Location: {lat:.6f}, {lon:.6f} | Satellites: {sats}")
                        
                    except pynmea2.ParseError:
                        continue
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    read_gps()

```

## 4. ROS 2 Integration

We use the standard NMEA driver. ROS will publish Lat/Long. We can add a custom node later to publish a secondary `/gps/mgrs` topic if needed for other systems.

### 4.1 Installation

```
sudo apt install ros-jazzy-nmea-navsat-driver

```

### 4.2 Launching the Node

Add this to your `system.launch.py`:

```
Node(
    package='nmea_navsat_driver',
    executable='nmea_serial_driver',
    name='gps_driver',
    parameters=[{
        'port': '/dev/ttyACM0',
        'baud': 9600,
        'frame_id': 'gps_link',
        'use_gnss_time': False,
        'time_ref_source': 'gps'
    }]
)

```

### 4.3 Output Data

- **Topic:** `/fix`

- **Message:** `sensor_msgs/NavSatFix` (Latitude, Longitude, Altitude).

## 5. Engineering Verdict: APPROVED

This component works seamlessly with Linux. The transition to MGRS is handled easily in software, giving you the military-grade readout you prefer without complicating the robot's internal math.

**Amazon Search Term:** `VFAN USB GPS Receiver` or `UBX-G7020KT USB GPS`.