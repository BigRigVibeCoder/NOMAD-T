---
ID: HM-CAT-015
Status: ACTIVE
Role: Custom Parts — Pulley Adapter Plate
Linked: HM-CAT-010 (Drivetrain), HM-CAT-013 (Frame)
---

# Custom Parts: Pulley Adapter Plate

## 1. Problem

Arrma Kraton 8S diff expects a spur gear input. We need an adapter that mounts to the diff's spur gear bolt pattern and accepts a 60T HTD 8M pulley.

---

## 2. Diff Input Face (Arrma Kraton 8S)

| Feature | Dimension |
|:---|:---|
| Bolt circle diameter | 32mm |
| Bolt pattern | 8× M3 threaded, 45° spacing |
| Center spline OD | 8mm |
| Center spline ID | 6mm |
| Spline teeth | 14 |

---

## 3. Adapter Plate Drawing

### Top View

```
         Overall Ø50mm
        ╱‾‾‾‾‾‾‾‾‾‾‾‾╲
       ╱ ○   ○   ○      ╲    ○ = M3 clearance (3.2mm) × 8
      │                    │      on 32mm bolt circle
      │ ○      ┌──┐    ○  │
      │        │12│       │  ← 12mm pilot boss
      │ ○      └──┘    ○  │      (press fit into pulley bore)
       ╲ ○   ○   ○      ╱
        ╲_____________ ╱
```

### Side View (Cross-Section)

```
    ◄──────── 50mm ────────►
    ┌────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░│ ← 6mm plate
    └───────┬────────┬───────┘
            │████████│         ← 10mm tall pilot boss (Ø12mm)
            └────────┘
```

---

## 4. Dimensions Table

| Feature | Dimension | Tolerance |
|:---|:---|:---|
| Overall diameter | 50mm | ±0.5mm |
| Plate thickness | 6mm | ±0.1mm |
| Pilot boss diameter | 12mm | +0.00/−0.02 (press fit) |
| Pilot boss height | 10mm | ±0.2mm |
| Bolt circle diameter | 32mm | ±0.1mm |
| M3 clearance holes | 3.2mm × 8 | ±0.1mm |
| Hole angular spacing | 45° | ±0.5° |

**Material:** 6061-T6 Aluminum
**Manufacturing:** CNC mill or waterjet + lathe for pilot

---

## 5. Assembly

1. **Adapter → Diff:** 8× M3 × 8mm SHCS, 1.5 Nm, blue threadlocker
2. **Pulley → Adapter:** Press fit pilot into 12mm bore, or 2× M4 set screws 120° apart (alt: Loctite 638 retaining compound)
3. **Verify:** Belt runs true, <1mm offset, pulley spins freely unpowered

---

## 6. 3D-Printed Prototype Option

| Change from Al version | Value |
|:---|:---|
| Material | PETG or Nylon PA12 |
| Infill | 100% solid |
| Plate thickness | 6mm → **10mm** |
| Add ribs | Between bolt holes |
| Bolt holes | Brass heat-set inserts |
| Max torque | ~10 Nm (vs 50+ Al) |
| Lifespan | ~50 hours |
| Cost | ~$5 vs ~$30 machined |

> [!TIP]
> Print for initial testing, upgrade to aluminum for final build.
