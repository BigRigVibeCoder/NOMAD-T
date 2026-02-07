# NOMAD-T

**Autonomous Off-Road UGV — Engineering Design Package**

A manufacturing-ready design for a ~24kg, 4WD, belt-driven autonomous rover built from COTS components.

## Project Structure

```
01_PROTOCOLS/     Documentation standards & naming conventions
02_CATALOG/       Component specs, BOMs, trade studies (HM-CAT-XXX)
03_OPERATIONS/    Build scripts, CAD generation, assembly guides
04_ASSETS/        Images, renders, reference photos
05_RESEARCH/      Analysis documents, whitepapers
```

## Key Specs

| Parameter | Value |
|:---|:---|
| Drivetrain | 2× Flipsky 6374 → 4:1 HTD belt → Arrma Kraton 8S diffs |
| Frame | 2020 V-slot extrusion, 700 × 300mm |
| Wheels | 182mm Arrma Kraton 8S, 17mm hex |
| Suspension | Trailing arm, Traxxas GTR 7461 shocks, 101mm travel |
| Compute | Odroid H4 Ultra (Intel N305) |
| Sensors | RPLiDAR C1, OAK-D Lite, 4× Sharp IR, BNO085 IMU |
| Power | 2× Zeee 6S 14Ah LiPo, 2× Flipsky FSESC 75100 |
| Weight | ~24 kg |
| Cost | ~$2,325 |

## Code-as-CAD

```bash
cd 03_OPERATIONS/cad
python3 generate_chassis.py    # → nomad_t_chassis.step
```

View the STEP file at [3dviewer.net](https://3dviewer.net).

## Catalog Documents

| ID | Document |
|:---|:---|
| HM-CAT-001 | Master Design (superseded) |
| HM-CAT-002 | Shopping List |
| HM-CAT-003–008 | Sensor Specifications |
| HM-CAT-009 | Brain Core (Odroid H4 Ultra) |
| HM-CAT-010 | Drivetrain Specification |
| HM-CAT-011 | COTS Trade Studies |
| HM-CAT-012 | Master Integration & Placement |
| HM-CAT-013 | Frame & Suspension |
| HM-CAT-014 | Electrical System |
| HM-CAT-015 | Custom Parts (Pulley Adapter) |
