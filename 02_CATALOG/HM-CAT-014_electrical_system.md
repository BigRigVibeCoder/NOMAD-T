---
ID: HM-CAT-014
Status: ACTIVE
Role: Electrical System Design
Linked: HM-CAT-012 (Integration), HM-CAT-010 (Drivetrain)
---

# Electrical System Design

## 1. Power Architecture

Star topology from central PDB. CAN bus daisy-chain for motor control.

```
BATT1 ──┐              ┌── VESC #1 (Rear) ── Motor #1
         ├── PDB ──────┤
BATT2 ──┘   │          └── VESC #2 (Front) ── Motor #2
             │
             └── DC-DC ─┬── 12V → Odroid, Fan
                        └── 5V  → RPLiDAR, OAK-D, IR×4, IMU
```

### PDB Components (inside Apache 2800)

| Component | Spec | Purpose |
|:---|:---|:---|
| 150A ANL fuse | 150A | Main overcurrent protection |
| 100A contactor | 12V coil, N.C. | E-Stop relay |
| XT90 inputs ×2 | 90A rated | Battery connections |
| XT60 outputs ×2 | 60A rated | VESC feeds |
| Terminal blocks | 30A | DC-DC, accessories |

---

## 2. Wire Gauge Table

| Circuit | V | Max A | Gauge | Color | Length |
|:---|:---|:---|:---|:---|:---|
| Battery → PDB | 22.2 | 200 | 8 AWG | Red/Black | 300mm |
| PDB → VESC (×2) | 22.2 | 100 | 10 AWG | Red/Black | 400–500mm |
| VESC → Motor (×2) | 22.2 | 80 | 12 AWG | Y/B/G (3 phase) | 200mm |
| PDB → DC-DC | 22.2 | 10 | 16 AWG | Red/Black | 150mm |
| DC-DC → Odroid | 12 | 6 | 18 AWG | Red/Black | 200mm |
| 5V sensor bus | 5 | 2 | 22 AWG | Red/Black | Various |
| CAN bus | Signal | — | 22 AWG twisted | Yellow/Green | Daisy |
| E-Stop | 5 | 0.1 | 22 AWG | White | 1000mm |

---

## 3. Motor Phase Wiring

Each VESC → Motor connection uses 3× 12 AWG phase wires + 6-pin JST Hall sensor cable.

| VESC Pin | Wire | Motor Pin |
|:---|:---|:---|
| Phase A | Yellow 12AWG, 6.5mm bullet | Phase A |
| Phase B | Blue 12AWG, 6.5mm bullet | Phase B |
| Phase C | Green 12AWG, 6.5mm bullet | Phase C |
| Hall 5V/GND/A/B/C/Temp | 6-pin JST | Hall sensor |

> [!IMPORTANT]
> Phase wires must be equal length (±10mm). Route away from sensor wires.

---

## 4. CAN Bus

Daisy-chain: **Odroid → USB-CAN adapter → VESC #1 → VESC #2 → 120Ω terminator**

| Param | Value |
|:---|:---|
| Baud rate | 500 kbps |
| Cable | 22 AWG twisted pair |
| Termination | 120Ω at end of chain |
| Connector | JST-PH 4-pin |
| CAN-H | Yellow |
| CAN-L | Green |

---

## 5. Sensor Connections to Odroid

### USB Ports

| Port | Device |
|:---|:---|
| USB 3.0 #1 | OAK-D Lite (USB-C) |
| USB 3.0 #2 | RPLiDAR C1 |
| USB 2.0 #3 | USB-CAN adapter (→ VESCs) |
| USB 2.0 #4 | Arduino Nano (I/O expander) |

### Arduino Nano I/O Expander

| Pin | Device |
|:---|:---|
| I2C (SDA/SCL) | BNO085 IMU |
| A0 | Sharp IR #1 (Front-Left) |
| A1 | Sharp IR #2 (Front-Right) |
| A2 | Sharp IR #3 (Front-Center) |
| A3 | Sharp IR #4 (Rear-Center) |
| D2 | E-Stop status (LOW = pressed) |

Arduino communicates to Odroid via USB-Serial.

---

## 6. E-Stop Circuit

1. Red mushroom button (N.C., panel-mount)
2. Controls 100A contactor coil (12V from DC-DC)
3. Button pressed → coil de-energized → relay opens → **all power cut**
4. Requires manual reset: release button + power cycle
5. Arduino monitors status on D2 for software awareness

---

## 7. Electrical BOM

| Qty | Part | Cost |
|:---|:---|:---|
| 1 | 150A ANL fuse + holder | $8 |
| 1 | 100A contactor (12V coil) | $25 |
| 1 | E-Stop mushroom button | $8 |
| 1 | DC-DC 22V→12V (10A) | $15 |
| 1 | DC-DC 22V→5V (5A) | $10 |
| 2 | XT90 connector pair | $6 |
| 2 | XT60 connector pair | $4 |
| 1 | USB-CAN adapter | $25 |
| 1 | Arduino Nano | $12 |
| 1 | 120Ω CAN terminator | $2 |
| 1 | Terminal block strip | $5 |
| 1 | Wire kit (8–22 AWG) | $30 |
| 4 | 6.5mm bullet connectors (sets) | $8 |
| | **Subtotal** | **~$158** |
