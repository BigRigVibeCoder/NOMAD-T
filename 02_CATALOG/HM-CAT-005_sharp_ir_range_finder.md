---
ID: HM-CAT-005
Status: ACTIVE
Source: github.com/BigRigVibeCoder/HiveMind
---

# Component Specification: IR Proximity Sensors (The "Whiskers")

**Role:** Close-Range Blind Spot Detection (Chin/Side/Rear)\
**Hardware:** Sharp GP2Y0A21YK0F (10-80cm)\
**Interface:** Analog Voltage (Requires ADC Adapter)\
**Status:** **APPROVED**

## 1. Core Concept: "The Virtual Bumper"

While the LIDAR sees walls and the OAK-D sees people, neither can see a table leg 5cm from the robot's hip. IR Proximity sensors act as "Whiskers."

- **Technology:** Infrared Triangulation.

- **Range:** 10cm to 80cm.

- **Behavior:** It outputs a voltage (0.4V - 3.1V) proportional to distance.

- **Why not Ultrasonic?** Ultrasonic is slow (speed of sound latency) and has wide cones (ghost echoes). IR is a tight beam and instant.

## 2. Hardware Architecture

### 2.1 The Sensor (Sharp IR)

- **Part:** **Sharp GP2Y0A21YK0F**.

- **Beam Width:** Narrow.

- **Refresh Rate:** \~25Hz (40ms).

- **Connection:** 3-Wire (VCC, GND, Signal).

### 2.2 The Interface (The ADC Bridge)

**Hardware:** **NOYITO USB 10-Channel 12-Bit AD Data Acquisition Module** (STM32 based).

- **Chipset:** STM32F103C8T6 + CH340 (USB Serial).

- **Channels:** 10 Analog Inputs (IN0 - IN9).

- **Resolution:** 12-Bit (0-4096 values).

- **Voltage Range:** 0V - 3.3V (Matches Sharp IR output perfectly).

**Wiring Diagram:**

| Sharp Sensor Wire | Connection Point | NOYITO Pin |
| --- | --- | --- |
| **Red (VCC)** | Power Rail | **5V / 3.3V** (Use 5V for Sharp) |
| **Black (GND)** | Ground Rail | **GND** |
| **Yellow (Signal)** | Analog Input | **IN0 - IN3** |

*Note:* The Sharp sensor requires 5V power, but outputs &lt;3.3V signal. Verify the NOYITO board passes 5V from USB to a VCC pin, or wire the Red wires to the robot's 5V rail (from the Power Server or Odroid USB 5V line).

### 2.3 Proposed Placement (x4)

1. **Chin (Down/Forward):** Detects stair edges (backup to ToF). -&gt; **IN0**

2. **Left Hip:** Detects doorframes during strafing. -&gt; **IN1**

3. **Right Hip:** Detects doorframes during strafing. -&gt; **IN2**

4. **Rear (Tail):** Detects obstacles when backing up. -&gt; **IN3**

## 3. Data Interface & Protocol

### 3.1 The "Voltage-to-Distance" Curve

The Sharp sensor is **Non-Linear**.

- 80cm = 0.4V

- 10cm = 3.1V

- **Math:** We use a lookup table or a power function in software to convert Voltage -&gt; Meters.

  - *Formula:* $Distance (cm) = 27.86 \\times (Voltage)^{-1.15}$

### 3.2 The Serial Output (NOYITO Protocol)

The module streams data as text lines containing raw ADC values.

- *Example Output:* `1024, 2048, 450, 12, ... \n`

- *Parsing:* Split string by comma -&gt; Map index to Sensor Location.

## 4. ROS 2 Integration

We write a simple Python Node (`proximity_node.py`) to read the ADC and publish `Range` messages.

### 4.1 The Node Logic (Python)

```
import serial
import math

# Configuration
PORT = '/dev/ttyUSB0'
BAUD = 115200 # Standard for STM32 USB dumps

def adc_to_cm(adc_value):
    # 1. Convert 12-bit Int (0-4096) to Voltage (0-3.3V)
    voltage = (adc_value * 3.3) / 4096.0
    
    # 2. Prevent divide by zero / math errors at extreme low voltage
    if voltage < 0.4: return 80.0
    
    # 3. Apply Sharp IR Formula
    distance = 27.86 * (voltage ** -1.15)
    return max(10.0, min(80.0, distance)) # Clamp to sensor limits

def read_loop():
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        while True:
            line = ser.readline().decode('utf-8').strip()
            # Expecting CSV: "val1, val2, val3..."
            if line:
                values = [int(x) for x in line.split(',') if x.isdigit()]
                if len(values) >= 4:
                    chin_dist = adc_to_cm(values[0])
                    left_dist = adc_to_cm(values[1])
                    right_dist = adc_to_cm(values[2])
                    rear_dist = adc_to_cm(values[3])
                    
                    # Publish to ROS Topic /sensor/ir_range/...
```

### 4.2 Nav2 Integration

We add these to the **Local Costmap**.

- **Layer:** `RangeSensorLayer`.

- **Behavior:** If the Rear IR sees an object at 20cm, it marks a "Lethal Obstacle" behind the robot. The planner will refuse to back up.

## 5. Bill of Materials (The Kit)

| Component | Source | Est. Cost |
| --- | --- | --- |
| **Sharp GP2Y0A21YK0F (x4)** | Amazon / Pololu | $40 ($10 ea) |
| **JST-PH Cables** | Included with Sensor | $0 |
| **NOYITO 10-CH USB ADC** | Amazon | $15 |
| **3D Printed Mounts** | Custom (Simple bracket) | $0 |

**Total:** \~$55 for 360-degree close-range protection.

## 6. Engineering Verdict: APPROVED

This fills the "Blind Spot" gap left by the OAK-D (min range 20cm) and LIDAR (can't see glass/black surfaces well). It is cheap insurance for your expensive legs.