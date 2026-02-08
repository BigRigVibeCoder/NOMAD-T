---
ID: HM-AST-007
Status: ACTIVE
Role: CAD Assembly Manifest
Date: 2026-02-08
Generator: 06_ENGINEERING/00_TOOLS/generate_chassis.py (v6)
Parts: 06_ENGINEERING/00_TOOLS/generate_parts.py
Output: 04_ASSETS/cad/
Linked: HM-CAT-001, HM-CAT-010, HM-CAT-012, HM-CAT-013, HM-CAT-014, HM-CAT-015
---

# CAD Assembly Manifest — Nomad-T Phase 1

> [!NOTE]
> **This document lives alongside the STEP files** and serves as their table of contents, traceability map, and regeneration guide.

## 1. Quick Start

### View Any Model
Drag any `.step` file into:
- **[3dviewer.net](https://3dviewer.net)** — Zero install, browser-based
- **FreeCAD** — `File → Import → STEP`
- **Fusion 360** — `Insert → Upload`
- **SolidWorks** — `File → Open → STEP`

### Regenerate
```bash
# Full assembly (59 parts)
python3 06_ENGINEERING/00_TOOLS/generate_chassis.py

# Individual manufacturing parts
python3 06_ENGINEERING/00_TOOLS/generate_parts.py
```
**Requires:** Python 3.12 + CadQuery (`~/.local/lib/python3.12/site-packages/cadquery`)

---

## 2. File Inventory

| File | Size | Description |
|:---|:---|:---|
| `HM-AST-006_nomad_t_chassis.step` | 393 KB | Full robot assembly (59 named parts) |
| `parts/NMT-MP-001_motor_plate.step` | 146 KB | Motor plate — **send to waterjet/laser shop** |
| `parts/NMT-TD-001_thermal_deck.step` | 173 KB | Thermal deck plate — CNC or waterjet |
| `parts/NMT-FR-001_frame_assembly.step` | 73 KB | Frame rails + crossbeams — cut-list verification |

---

## 3. Assembly Parts Map (59 Parts)

### Structure (HM-CAT-013)
| STEP Name | Description |
|:---|:---|
| `rail_L`, `rail_R` | 700mm 2040 V-Slot side rails |
| `xbeam_1` – `xbeam_4` | 240mm 2040 crossbeams |
| `shear_L`, `shear_R` | 3mm DiBond side panels (700×120mm) |

### Drivetrain (HM-CAT-010 / HM-CAT-015)
| STEP Name | Description |
|:---|:---|
| `g30_hub_FL/FR/RL/RR_tire` | 250mm 10" pneumatic tires |
| `g30_hub_FL/FR/RL/RR_motor` | 140mm motor body (inside tire) |
| `g30_hub_FL/FR/RL/RR_axle` | 12mm Double-D axle stub |
| `motor_plate_FL/FR/RL/RR` | NMT-MP-001 6mm Al plates with axle bore |

### Electronics (HM-CAT-012 / HM-CAT-014)
| STEP Name | Description |
|:---|:---|
| `apache_3800` + `case_handle` | Protective case + handle |
| `thermal_deck` | 6mm Al unified thermal plate |
| `bobbin_FL/FR/RL/RR` | M5 vibration isolation bobbins |
| `battery_10s3p` + `battery_xt90` | 36V pack + XT90-S connector |
| `vesc_FL/FR/RL/RR` | Flipsky 75100 motor controllers |
| `brake_resistor` | 200W 8Ω regen brake |
| `dcdc_meanwell` | DDR-60L-15 (36V→17V) |
| `arduino_nano` | Watchdog heartbeat monitor |
| `distribution_bus` | Power distribution block |
| `main_contactor` | HV switching contactor |

### Sensors
| STEP Name | Description |
|:---|:---|
| `rplidar_c1` + `lidar_mast` | RPLiDAR C1 on mast (>300mm) |
| `oakd_lite` + 3× `oakd_lens_*` | OAK-D Lite with lens bumps |
| `ir_FL/FR/FC/RC` | Sharp IR range finders |
| `imu_wt901` | WitMotion WT901SDCL 9-axis AHRS |

### Safety & UI (CDR-6, CDR-12)
| STEP Name | Description |
|:---|:---|
| `estop_button` | Red mushroom E-Stop (rear) |
| `led_green/yellow/red` | Status LEDs (rear panel) |
| `charge_port` | Weipu SP17 charging connector |

---

## 4. Individual Parts Detail

### NMT-MP-001 Motor Plate (146 KB)
**The linchpin of the design.** Manufacturing-ready with:
- Double-D axle slot (12mm OD, 10mm flats)
- 6× M5 clearance holes (4 primary + 2 edge)
- 2mm chamfered edges
- Material: 6061-T6, 6mm thick
- **Process:** Waterjet or laser cut

### NMT-TD-001 Thermal Deck (173 KB)
- 4× corner M5 mounting holes
- 16× M3.5 VESC mount holes (4 per VESC × 4 VESCs)
- 4× M3 Odroid standoff holes
- 4× M3 copper pedestal contact holes
- 2× 16mm wire gland pass-through holes
- 1.5mm filleted top edges
- **Process:** CNC or waterjet

---

## 5. Coordinate System & Key Dimensions

| Axis | Direction | | Parameter | Value |
|:---|:---|:---|:---|:---|
| **+X** | Forward | | Frame | 700 × 320mm |
| **+Y** | Left | | Wheelbase | 700mm |
| **+Z** | Up | | Track | 450mm |
| Origin | Rear axle, ground | | Wheel OD | 250mm |

---

## 6. Wiring Diagram

See [HM-DWG-002_wiring_visual.png](file:///home/bdavidriggins/Documents/Nomad-T/06_ENGINEERING/01_SCHEMATICS/HM-DWG-002_wiring_visual.png) for color-coded wiring diagram, and [HM-DWG-001](file:///home/bdavidriggins/Documents/Nomad-T/06_ENGINEERING/01_SCHEMATICS/HM-DWG-001_wiring_harness.md) for pin-to-pin netlist.

For formal, editable schematics with DRC: use **[KiCad](https://www.kicad.org/)** (free, open-source EDA).

---

## 7. Version History

| Version | Date | Changes |
|:---|:---|:---|
| **v6** | 2026-02-08 | 59-part assembly, individual part files, wiring diagram |
| v5 | 2026-02-08 | 33-part assembly, first correct design |
| v4 | 2026-02-07 | *Obsolete:* suspension, diffs, belt drive |
