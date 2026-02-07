---
ID: HM-CAT-010
Status: ACTIVE
Supersedes: HM-CAT-001 (goBILDA-only drivetrain)
Architecture: 4WD Belt-to-Diff (Arrma Kraton transplant)
---

# Nomad-T Drivetrain Specification: "Traxxas-Class"

**Scale:** 1/5 RC (Traxxas X-Maxx / Arrma Kraton class)
**Target Weight:** 20 kg (44 lbs) | **Top Speed:** 15 mph | **Architecture:** 4WD Centralized Belt Drive

---

## 1. Weight Budget

| Subsystem | Mass |
|:---|:---|
| Chassis (2020 Al + Plates) | 4.0 kg |
| Motors + Mounts (×2) | 1.7 kg |
| Batteries (2× 6S 16Ah LiPo) | 4.5 kg |
| Electronics (Odroid + Case) | 1.5 kg |
| Sensors (LiDAR/OAK-D/Radio) | 1.0 kg |
| Wheels/Tires (×4) | 1.7 kg |
| Suspension/Axles/Diffs | 3.6 kg |
| **Total** | **~20.0 kg** |

---

## 2. Wheel Physics

| Parameter | Value |
|:---|:---|
| Tire Diameter | 182mm (Arrma Kraton 8S) |
| Circumference | π × 0.182m ≈ 0.572m |
| Target Speed | 15 mph = 6.7 m/s |
| Required Wheel RPM | 6.7 ÷ 0.572 × 60 ≈ **703 RPM** |

---

## 3. Motor & Gearing

### Motor: Flipsky 6374 190KV (Sensored)

| Spec | Value |
|:---|:---|
| KV | 190 RPM/V |
| Voltage | 22.2V (6S) |
| No-Load RPM | 4,218 RPM |
| Loaded RPM (~80%) | 3,374 RPM |
| Stall Torque | 3.8 Nm |
| Peak Power | ~3,000W |
| Shaft | 8mm keyed, 25mm exposed |
| Body | 63mm dia × 74mm long |
| Weight | 850g |
| Cost | ~$65 ea |

### Gear Ratio Selection

| Ratio | Wheel RPM | Top Speed | Wheel Torque (per motor) | Verdict |
|:---|:---|:---|:---|:---|
| 4.75:1 | 711 | 15 mph | 17.1 Nm | Fast, adequate torque |
| 5:1 | 675 | 14.5 mph | 18 Nm | **Sweet spot** |
| 7:1 | 482 | 10 mph | 25 Nm | Hill climber |
| 10:1 | 337 | 7 mph | 36 Nm | Stump puller |

**Selected: ~4.4:1** (belt 4:1 × diff 1.1:1)

### Torque Check ("Stump Puller")

- Motor torque × 4.4 × 0.95 eff = **15.9 Nm** per motor
- Required for 30° slope: 20kg × 9.81 × 0.091m × sin(30°) × 1.5 SF = **10.4 Nm** ✓
- Safety Factor: **1.53×** ✓

---

## 4. Belt Drive Geometry

| Component | Spec | Part |
|:---|:---|:---|
| Motor Pulley | 15T, HTD 8M, 8mm bore | Gates 8M 15T |
| Diff Pulley | 60T, HTD 8M | Gates 8M 60T |
| Belt | 800mm × 15mm wide, HTD 8M | Amazon |
| Tensioner | 608 bearing on M8 bolt | DIY |
| **Belt Ratio** | **4:1** | |
| **Motor-to-Diff Center Distance** | **230mm** | Calculated from belt formula |

```
   Motor (15T)                              Diff (60T)
    ┌───┐                                 ┌─────────┐
    │ ● │═════════════════════════════════│    ●    │
    │   │          HTD 8M Belt            │  KRATON │
    │ M │═════════════════════════════════│  DIFF   │
    └───┘                                 └─────────┘
   Ø38mm          ◄── 230mm ──►            Ø153mm
```

---

## 5. Chassis Dimensions

| Parameter | Value |
|:---|:---|
| **Wheelbase** | 500mm (19.7") |
| **Track Width** (wheel-to-wheel) | 648mm (25.5") |
| **Chassis Deck** | 600mm × 250mm |
| **Ground Clearance** | ~91mm (half wheel dia) |

---

## 6. Drivetrain BOM

| Qty | Part | Spec | Source | Cost |
|:---|:---|:---|:---|:---|
| 2 | Motor | Flipsky 6374 190KV Sensored | Flipsky.net | $130 |
| 2 | Motor Pulley | Gates HTD 8M 15T, 8mm bore | SDP-SI | $24 |
| 2 | Diff Pulley | Gates HTD 8M 60T | SDP-SI | $70 |
| 2 | Belt | HTD 8M 800mm × 15mm | Amazon | $36 |
| 2 | Diff Assembly | Arrma Kraton 8S Rear (ARA310940) | eBay | $90 |
| 2 | CVD Axle Set | Arrma Kraton 8S (ARA310945) | eBay | $70 |
| 4 | Wheel/Tire | Arrma Kraton 8S (ARA510120) | Amazon | $100 |
| 2 | Pulley Adapter | Custom 6mm Al plate | SendCutSend | $40 |
| 2 | Motor Mount | 63mm Clamp | Amazon | $30 |
| 2 | Belt Tensioner | 608 bearing + M8 bolt | Amazon | $10 |
| 1 | Hardware Kit | M3/M4/M5 assortment | Amazon | $25 |
| | | | **TOTAL** | **$625** |

---

## 7. Open Decisions

| Item | Options | Recommendation |
|:---|:---|:---|
| Belt Profile | HTD 5M vs 8M | **8M** (higher torque) |
| Diff Locking | Open vs Limited-Slip | Open first, add LS fluid later |
| Motor Sensor | Sensored vs Sensorless | **Sensored** (low-speed control) |
| Pulley Adapter | Aluminum vs 3D Print | **Aluminum** (durability) |
