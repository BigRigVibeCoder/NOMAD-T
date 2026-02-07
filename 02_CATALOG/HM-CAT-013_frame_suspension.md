---
ID: HM-CAT-013
Status: ACTIVE
Role: Frame & Suspension Engineering Specification
Linked: HM-CAT-010 (Drivetrain), HM-CAT-012 (Integration)
---

# Frame & Suspension Engineering Specification

## Coordinate System

```
Origin: Center of rear axle, at ground level
+X = Forward    +Y = Left    +Z = Up
All dimensions in mm.
```

---

## 1. Primary Frame Rails

| Param | Value |
|:---|:---|
| Qty | 2 (left + right) |
| Profile | 2020 V-slot aluminum extrusion |
| Length | 700mm |
| Left rail Y | +150mm |
| Right rail Y | −150mm |
| Z (bottom face) | 120mm from ground |
| X extent | −50mm to +650mm (50mm behind rear axle) |
| Rail spacing (inner) | 260mm |
| Rail spacing (outer) | 300mm |

---

## 2. Crossbeams

| # | X | Purpose | Special Features |
|:---|:---|:---|:---|
| 1 | 0 | Rear axle | Diff bracket, M8 shock mounts at Y=±50mm |
| 2 | 170 | Rear motor | Motor clamp (Y=+80mm), VESC mount (Y=−60mm) |
| 3 | 350 | Center/CG | Battery tray (168×140mm below), IMU at center |
| 4 | 530 | Front motor | Motor clamp, VESC mount (mirrors #2) |
| 5 | 650 | Front axle | Diff bracket, shock mounts, bumper |

All crossbeams: 2020 V-slot, 300mm long, attached with M5 T-nuts.

---

## 3. Upper Deck

| Param | Value |
|:---|:---|
| Z height | 180mm from ground (60mm above base rail top) |
| Vertical posts | 4× 2020 extrusion, 60mm tall |
| Deck plate | 250 × 200mm, 3mm aluminum |
| X extent | 250–500mm (centered over battery bay) |
| Carries | Apache 2800 case (Odroid + PDU) + LiDAR mast |

---

## 4. Suspension: Trailing Arm

### 4.1 Architecture

Semi-independent trailing arm with coil-over shock per wheel. Diff is chassis-mounted; dog bones connect diff output to wheel hub through trailing arm.

### 4.2 Key Geometry

| Param | Value |
|:---|:---|
| Arm length (pivot → axle) | 150mm |
| Arm width | 50mm |
| Arm pivot Z | 100mm from ground |
| Static arm angle | −6° from horizontal |
| Shock mount distance from pivot | 80mm |
| Shock upper mount Z | 170mm from ground |
| Shock angle (static) | 65° from horizontal |

### 4.3 Travel

| Condition | Arm Angle | Wheel Travel |
|:---|:---|:---|
| Full droop | −31° | −62mm |
| Static | −6° | 0mm |
| Full bump | +9° | +39mm |
| **Total** | | **101mm (4.0")** |

### 4.4 Shock: Traxxas GTR 7461

| Param | Value |
|:---|:---|
| Extended | 221mm |
| Compressed | 176mm |
| Stroke | 46mm |
| Static | 195mm (27mm preloaded) |
| Bore | 16mm |
| Mounting | M4 rod ends, 8mm OD |
| Cost | $25/pair |

### 4.5 Trailing Arm Construction

Sandwich build: 150mm 2020 extrusion spine + 2× 6mm aluminum side plates bolted via T-nuts.

| Feature | Distance from Pivot | Hole Size |
|:---|:---|:---|
| Pivot bushings | 0mm | 8mm (2×, 30mm spacing) |
| Shock clevis | 80mm | 8mm |
| Axle/Hub carrier | 150mm | 17mm hex |

Bronze bushings: 8mm ID × 16mm OD × 10mm flanged.

---

## 5. Frame BOM

| Qty | Part | Length/Size | Purpose |
|:---|:---|:---|:---|
| 2 | 2020 V-slot | 700mm | Main rails |
| 5 | 2020 V-slot | 300mm | Crossbeams |
| 4 | 2020 V-slot | 60mm | Deck posts |
| 1 | 2020 V-slot | 189mm | LiDAR mast |
| 4 | 2020 V-slot | 150mm | Trailing arm spines |
| 8 | 6mm Al plate | 180×50mm | Trailing arm side plates |
| 1 | 3mm Al plate | 250×200mm | Upper deck |
| 1 | 3mm Al plate | 180×150mm | Battery tray |
| 4 | Traxxas GTR 7461 | — | Shocks (2 pairs) |
| 16 | Bronze bushing | 8mm ID × 16mm OD | Arm pivots |
| 40+ | M5 × 10 BHCS | — | Frame assembly |
| 40+ | M5 T-nut (drop-in) | — | Frame assembly |
| 8 | M5 × 25 BHCS | — | Deck posts |
| 4 | 90° corner bracket | — | Reinforcement |

**Total extrusion:** 2×700 + 5×300 + 4×60 + 189 + 4×150 = **4,029mm ≈ 4.1m**
