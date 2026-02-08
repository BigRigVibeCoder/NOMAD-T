---
ID: HM-AST-007
Status: ACTIVE
Role: CAD Assembly Manifest
Date: 2026-02-08
Generator: 06_ENGINEERING/00_TOOLS/generate_chassis.py (v5)
Output: 04_ASSETS/cad/HM-AST-006_nomad_t_chassis.step
Linked: HM-CAT-001, HM-CAT-010, HM-CAT-012, HM-CAT-013, HM-CAT-014, HM-CAT-015
---

# CAD Assembly Manifest — Nomad-T Phase 1

> [!NOTE]
> **This document lives alongside the STEP file** and serves as its table of contents, traceability map, and regeneration guide. If the STEP looks wrong, check here first.

## 1. Quick Start

### View the Model
Drag `HM-AST-006_nomad_t_chassis.step` into any of these:
- **[3dviewer.net](https://3dviewer.net)** — Zero install, browser-based
- **FreeCAD** — `File → Import → STEP`
- **Fusion 360** — `Insert → Insert Mesh / Upload`
- **SolidWorks** — `File → Open → STEP`

### Regenerate the Model
```bash
cd <project-root>
python3 06_ENGINEERING/00_TOOLS/generate_chassis.py
```
**Requires:** Python 3.12 + CadQuery (`~/.local/lib/python3.12/site-packages/cadquery`)

---

## 2. Assembly Parts Map

Every named part in the STEP file is listed below with its source spec.

### Structure (HM-CAT-013)
| STEP Name | Description | Spec |
|:---|:---|:---|
| `rail_L`, `rail_R` | 2040 V-Slot side rails, 700mm | §1 |
| `xbeam_1` – `xbeam_4` | 2040 crossbeams, 240mm | §5 |
| `shear_L`, `shear_R` | 3mm DiBond side panels, 700×120mm | §2 |

### Drivetrain (HM-CAT-010 / HM-CAT-015)
| STEP Name | Description | Spec |
|:---|:---|:---|
| `g30_hub_FL/FR/RL/RR` | Ninebot G30 hub motors + 10" tires | HM-CAT-010 §1–2 |
| `motor_plate_FL/FR/RL/RR` | NMT-MP-001 custom 6mm Al plates | HM-CAT-015 |

### Electronics Enclosure (HM-CAT-012)
| STEP Name | Description | Spec |
|:---|:---|:---|
| `apache_3800` | Apache 3800 protective case | §1 |
| `thermal_deck` | 6mm Al unified thermal plate (lid replacement) | §3 / CDR-4 |
| `bobbin_FL/FR/RL/RR` | M5 vibration isolation bobbins (Shore 40A) | §1 |
| `battery_10s3p` | 10S3P Li-Ion pack, 36V | §2 |

### Power & Control (HM-CAT-014)
| STEP Name | Description | Spec |
|:---|:---|:---|
| `vesc_FL/FR/RL/RR` | 4× Flipsky 75100 motor controllers | §3 |
| `brake_resistor` | 200W 8Ω regenerative brake resistor | §3 / CDR-5 |
| `dcdc_meanwell` | Mean Well DDR-60L-15 (36V → 17V) | §2 |
| `arduino_nano` | Watchdog heartbeat monitor | §3 |

### Sensors
| STEP Name | Description | Spec |
|:---|:---|:---|
| `rplidar_c1` + `lidar_mast` | RPLiDAR C1, mast-mounted >300mm | HM-CAT-006 |
| `oakd_lite` | OAK-D Lite depth camera, -15° tilt | HM-CAT-003 |
| `ir_FL/FR/FC/RC` | 4× Sharp IR range finders | HM-CAT-005 |
| `imu_wt901` | WitMotion WT901SDCL 9-axis AHRS | HM-CAT-008 |

---

## 3. Coordinate System

| Axis | Direction | Reference |
|:---|:---|:---|
| **+X** | Forward | 0 = rear axle center |
| **+Y** | Left | 0 = centerline |
| **+Z** | Up | 0 = ground plane |

---

## 4. Key Dimensions (Quick Reference)

| Parameter | Value | Source |
|:---|:---|:---|
| Frame Length | 700mm | HM-CAT-013 §1 |
| Frame Width | 320mm (outer-to-outer) | HM-CAT-013 §1 |
| Wheelbase | 700mm | HM-CAT-010 |
| Track Width | 450mm (center-to-center) | Layout |
| Wheel OD | 250mm (10" pneumatic) | HM-CAT-010 §2 |
| Ground Clearance | ~125mm (under rails) | HM-CAT-012 §5 |
| Total Mass | ~18.8 kg | HM-CAT-012 §6 |

---

## 5. Version History

| Version | Date | Changes |
|:---|:---|:---|
| **v5** | 2026-02-08 | Phase 1 approved design: rigid frame, 4× G30 direct drive, Apache 3800, WT901 IMU |
| v4 | 2026-02-07 | *Obsolete:* Trailing arm suspension, Arrma diffs, belt drive, Apache 2800 |

---

## 6. What This Model Does NOT Include

These are intentionally omitted from the parametric model:

- **Wiring harness** — See [HM-DWG-001](file:///home/bdavidriggins/Documents/Nomad-T/06_ENGINEERING/01_SCHEMATICS/HM-DWG-001_wiring_harness.md)
- **Fasteners** (bolts, T-nuts, brackets) — See [HM-OPS-001 Build Manual](file:///home/bdavidriggins/Documents/Nomad-T/03_OPERATIONS/HM-OPS-001_build_manual.md)
- **Internal PCB layouts** — VESC/Odroid are bounding boxes only
- **Tire tread pattern** — Simplified cylinder geometry
