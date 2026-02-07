---
ID: HM-CAT-012
Status: ACTIVE
Role: Master Integration & Placement Specification
Linked: HM-CAT-009 (Compute), HM-CAT-010 (Drivetrain), HM-CAT-003–008 (Sensors)
---

# Component Integration & Placement Specification

All dimensions in mm. All weights in grams. All costs in USD.

---

## 1. Compute Module: Odroid H4 Ultra

| Param | Value |
|:---|:---|
| PCB | 110 × 110mm |
| Height (with active cooler) | 58mm |
| Mounting | M3 × 4, 104mm square pattern |
| TDP | 35–65W configurable |
| Weight | 450g (with cooler) |

### Enclosure

| Option | Internal (mm) | Rating | Cost |
|:---|:---|:---|:---|
| Apache 1800 | 153 × 127 × 76 | IP65 | $12 |
| **Apache 2800** (selected) | 241 × 188 × 108 | IP65 | **$25** |

> [!TIP]
> Apache 2800 fits Odroid + DC-DC converter + terminal blocks in one waterproof box.

---

## 2. Battery: Zeee 6S 14Ah 100C (×2)

| Param | Value |
|:---|:---|
| Voltage | 22.2V nom / 25.2V full |
| Capacity | 14Ah × 2 = **28Ah total** |
| Discharge | 100C = 1,400A |
| Dimensions | 168 × 68 × 56 each |
| Weight | 1.7kg each |
| Connector | EC5 (switch to XT90) |
| Cost | ~$180 each |

**Placement:** Side-by-side at geometric center (168 × 136 × 56mm bay).

---

## 3. VESC: Flipsky FSESC 75100 (×2)

| Param | Value |
|:---|:---|
| Voltage | 14–75V |
| Continuous | 100A / Peak 200A |
| Dimensions | 110 × 66 × 30 |
| Weight | 280g |
| Comms | USB, CAN bus, UART |
| Cost | ~$150 each |

**Placement:** Each VESC adjacent to its motor (short phase wires). Two singles > one dual for redundancy and heat distribution.

---

## 4. Sensor Placement

### 4.1 RPLiDAR C1 — 300mm Mast

| Param | Value |
|:---|:---|
| Body | Ø50 × 40mm |
| Mount | M2.5 × 4, 44mm pattern |
| Weight | 125g |
| **Height from ground** | **300mm** |
| Mast length | 189mm (2020 extrusion) |

### 4.2 OAK-D Lite — Front, -15° Tilt

| Param | Value |
|:---|:---|
| Body | 91 × 28 × 17.5mm |
| Mount | M4 × 2 (or ¼"-20 tripod) |
| Weight | 61g |
| **Tilt** | **-15°** (ground visible from 0.5m ahead) |
| Height | ~250mm (chassis top) |

### 4.3 Sharp IR "Whiskers" (×4) — Bumper Level

| Position | Orientation | Purpose |
|:---|:---|:---|
| Front-Left | 45° outward | Turn collision |
| Front-Right | 45° outward | Turn collision |
| Front-Center | Forward | Low obstacle |
| Rear-Center | Backward | Backup safety |

Mount height: 100–150mm (below LiDAR scan plane).

### 4.4 IMU (BNO085) — Center of Mass

| Param | Value |
|:---|:---|
| Board | 25 × 25 × 3mm |
| Weight | 2.5g |
| Interface | I2C / SPI / UART |
| **Location** | 400mm from rear axle, centered, on chassis floor (~115mm height) |

---

## 5. Ground Clearance

| Condition | Value |
|:---|:---|
| Nominal (ride height) | **100mm** |
| Minimum (full compression) | 80mm |
| Maximum (full extension) | 120mm |
| Approach / Departure angle | ~25° |
| Breakover angle | ~20° |

---

## 6. Master BOM Summary

| Subsystem | Components | Subtotal |
|:---|:---|:---|
| Compute | Odroid + RAM + SSD + WiFi + Case + Fan + PSU | $580 |
| Power | Batteries ×2 + VESCs ×2 + Power Distro | $680 |
| Sensors | RPLiDAR + OAK-D + IR ×4 + IMU + GNSS | $340 |
| Drivetrain | Motors ×2 + Diffs ×2 + Belts + Wheels ×4 + Hardware | $625 |
| Structure | 2020 Extrusion + Plates + Mounts | $100 |
| | **GRAND TOTAL** | **~$2,325** |

---

## 7. Decision Confirmation Checklist

| # | Decision | Selection | Status |
|:---|:---|:---|:---|
| 1 | Wheel/Tire | Arrma Kraton 8S, 182mm, 17mm hex | ☐ |
| 2 | Motor | Flipsky 6374 190KV, 8mm shaft | ☐ |
| 3 | Gear Ratio | 4:1 belt (15T:60T HTD 8M) | ☐ |
| 4 | VESC | 2× Flipsky 75100 (separate) | ☐ |
| 5 | Battery | 2× Zeee 6S 14Ah 100C | ☐ |
| 6 | LiDAR Height | 300mm from ground | ☐ |
| 7 | OAK-D Angle | -15° tilt down | ☐ |
| 8 | IR Sensors | 4× Sharp GP2Y0A21, whisker config | ☐ |
| 9 | IMU | BNO085, center of mass | ☐ |
| 10 | Ground Clearance | 100mm nominal | ☐ |
| 11 | Enclosure | Apache 2800 (brain + power) | ☐ |
