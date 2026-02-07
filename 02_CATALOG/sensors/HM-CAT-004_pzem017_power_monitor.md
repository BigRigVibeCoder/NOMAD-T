---
ID: HM-CAT-004
Status: ACTIVE
Source: github.com/BigRigVibeCoder/HiveMind
---

# Component Specification: Main Power & Energy Monitor

**Role:** Metabolic Analysis (Voltage, Current, Power, Energy Consumption)

**Hardware:** Peacefair PZEM-017 (Industrial DC)

**Interface:** RS485 (via USB Adapter)

## 1. The Problem: Measuring "The Gulp"

The robot's motors draw power in violent spikes (0A to 20A in milliseconds).

- **INA219 (Standard):** Max 3.2A. **REJECTED.** It will burn out.

- **Voltage Dividers:** Inaccurate. Only gives voltage, not current.

We need a sensor that can handle **30A Continuous / 50A Peak** at 16.8V.

## 2. The Solution: PZEM-017 (Industrial DC Meter)

*Best for Phase 2/3 "Coyote". Zero soldering. Includes USB Interface.*

### 2.1 Hardware Overview

- **Type:** DC Communication Box + External Shunt.

- **Range:** 0-300V, 0-300A (Configurable based on shunt).

- **Interface:** RS485 (Modbus-RTU).

- **Isolation:** High voltage side is opto-isolated from the communication side. (Protects the Odroid USB port from spikes).

### 2.2 Integration Strategy

1. **Shunt:** Bolt the **50A / 75mV Shunt** (or 100A) onto the "Dirty" 12V Rail.

   - **Location:** Between the Master Fuse and the Pololu Regulator.

   - **Orientation:** "Load" side goes to motors.

2. **Sense Wires:** Run small wires from the Shunt screws to the PZEM-017 terminals.

3. **Data Link:**

   - **PZEM Side:** Connect wires to A and B terminals.

   - **Odroid Side:** Connect A/B wires to the **USB-to-RS485 Adapter** (Included in kit).

   - **Plug:** Plug USB into Odroid.

4. **Protocol:** Modbus-RTU. (Standard industrial protocol).

### 2.3 Why it wins

- **Robustness:** You can't fry it. The high current never touches the PCB, only the solid metal shunt.

- **Kit Completeness:** The high-end kit includes the USB adapter and the correct shunt.

## 3. Option B: The Embedded Solution (INA226) - DEPRECATED

*Best for Phase 0/1 or if space is extremely tight.* (Kept for reference only).

### 3.1 Hardware Overview

- **Type:** High-Side Current/Power Monitor Chip.

- **Resolution:** 16-Bit (Ultra precise).

- **Range:** Up to 36V. Current depends on the resistor you solder.

- **Interface:** I2C.

### 3.2 The "Ready-to-Roll" Module

Do not buy a bare chip. Buy the **WaveShare INA226 Module**.

- **Connector:** PH2.0 (Easy to wire).

- **Shunt:** usually 0.1 Ohm (Max 2A). **WARNING:** You must Desolder the stock shunt and solder a **0.002 Ohm** shunt to read 50A.

- **Wiring:** Requires connecting SDA/SCL to the Odroid's GPIO headers (Pins 3/5).

## 4. ROS 2 Integration (PZEM-017)

We write a Python Node (`power_monitor_node.py`) using `pymodbus`.

### 4.1 The Node Logic (Python)

```
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
from pymodbus.client import ModbusSerialClient

class PowerMonitor(Node):
    def __init__(self):
        super().__init__('power_monitor')
        self.pub = self.create_publisher(BatteryState, '/sensor/battery', 10)
        # Port depends on your USB adapter (check ls /dev/ttyUSB*)
        self.client = ModbusSerialClient(port='/dev/ttyUSB1', baudrate=9600, timeout=1)
        self.timer = self.create_timer(1.0, self.read_power)

    def read_power(self):
        # Read Input Registers (0x0000 start, 4 registers)
        # Reg 0: Voltage (0.01V)
        # Reg 1: Current (0.01A)
        # Reg 2-3: Power/Energy
        rr = self.client.read_input_registers(0x0000, 4, slave=1)
        
        if not rr.isError():
            msg = BatteryState()
            msg.voltage = rr.registers[0] * 0.01
            msg.current = rr.registers[1] * 0.01
            msg.charge = float('nan') # We don't know % without a curve
            self.pub.publish(msg)
```

### 4.2 Output Topic

- **Topic:** `/sensor/battery`

- **Message:** `sensor_msgs/BatteryState`

  - `voltage`: 16.4 V

  - `current`: 12.5 A

  - `charge`: NaN

## 5. Bill of Materials

### The "Ironclad" Kit (PZEM)

| Component | Source | Est. Cost |
| --- | --- | --- |
| **PZEM-017 Master Kit** (Module + 50A/100A Shunt + USB-RS485) | Amazon / AliExpress | $25 - $35 |
| **12 AWG Wire** | Home Depot / Amazon | $5 |

**Total:** \~$35 for a bulletproof, fire-safe power metering system.

**Recommendation:** **Buy the PZEM-017 Kit.** It is the complete package for high-power monitoring without component hunting.