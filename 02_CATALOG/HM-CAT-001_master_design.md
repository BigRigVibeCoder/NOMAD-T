# Nomad-T / Badger-M "Hybrid" Design Specification
**The "goBILDA Edition" Recipe**

> [!WARNING]
> **SUPERSEDED** by [HM-CAT-010 (Traxxas-Class Drivetrain)](HM-CAT-010_drivetrain_spec.md). This document is retained for historical reference only. The drivetrain has shifted from goBILDA to Arrma Kraton transplant with Flipsky 6374 motors.

## 1. Executive Summary
This design synthesizes the **Battle-Hardened Physics** of the "Badger-M" (UGV Whitepaper) with the **Modular Convenience** of the goBILDA build system.

**Objective:** Build a ~20kg, 4WD, off-road autonomous rover.
**Primary Constraint:** Use goBILDA parts for structure and drivetrain interfacing to minimize custom machining.

---

## 2. Core Architecture: The "Open-Channel flat" Chassis
Instead of welded steel (UGV Whitepaper) or 2020 extrusion (Nomad-T original), we will use **goBILDA 1120 Series U-Channel**.

### Why goBILDA Channel?
- **Strength:** The "U" profile provides excellent torsion resistance, comparable to the steel tubing for this scale.
- **Mounting:** The 8mm grid pattern allows us to mount motors, axles, and electronics anywhere without drilling.
- **Protection:** Electronics sit *inside* the channel, protected from debris.

### Chassis Recipe
*   **Main Rails:** 2x `1120-0001-0432` (17 Hole U-Channel) - ~432mm long.
*   **Crossbeams:** 4x `1120-0001-0288` (11 Hole U-Channel) - ~288mm wide.
*   **Corners:** 4x `1132-0006-0001` (45 Degree Pattern Mount) or `1134-0004-0001` (Inside Corner Connector) for rigid 90° joints.

---

## 3. Drivetrain: "The Hybrid Axle"
**Critical Issue Resolved:** The research correctly identified that standard RC shafts don't fit industrial motors, and industrial NEMA gearboxes don't fit RC parts.
**Solution:** We use goBILDA as the "Universal Translator".

### The Motor Problem
*   **Requirement:** ~4Nm per wheel (Post-gearing) for 24kg robot.
*   **goBILDA Yellow Jacket:** ~1.4Nm continuous (too weak for direct drive 1:1, okay if heavily geared but slow).
*   **Decision:** We strive to keep the **6384 Brushless Outrunners** from the research because they offer 3000W+ of power, which is necessary for "Rasputitsa" mud conditions.

### The Motor Mount Recipe (Per Corner)
*   **Motor:** 6384 Brushless Outrunner (Non-goBILDA).
*   **Mounting Plate:** `1111-0001-0062` (Flat Pattern Bracket) - * Requires drilling 4 holes for 6384 bolt pattern (44mm dia).*
*   **Transmission:** **Belt Drive** (Quieter, handles shock better than gears).
    *   **Motor Pulley:** HTD 5M 15T (8mm bore for 6384 shaft).
    *   **Wheel Pulley:** goBILDA `3400-0014-0060` (60 Tooth HTD 5M Zone Pulley) adapted to 14mm bore.
    *   **Belt:** HTD 5M 9mm width.

### The Axle & Wheel Recipe (Per Corner)
*   **Axle:** `2100-0014-0100` (14mm Stainless Steel Shaft). This is HUGE (0.55") - strong enough for a 20kg bot.
*   **Bearings:** 2x `1611-0005-0014` (14mm Bore Flanged Ball Bearing).
*   **Hub:** `1310-0014-0002` (14mm HyperHub).
*   **Wheel:** `3606-0500-0190` (190mm / 7.5" Pneumatic Tire).
    *   *Note: goBILDA sells "Rhino Wheels" (140mm), but for the "7-10 inch" requirement, we might need to adapt generic pneumatic tires using the HyperHub.*

---

## 4. Subsystem Breakdown

### 4.1 Steering
*   **Type:** **Skid Steer** (Tank driving).
*   **Rationale:** Simplest mechanical design (UGV Whitepaper recommendation). No steering rack to break.

### 4.2 Suspension (Optional but Recommended)
*   The goBILDA "Strafer Chassis" is rigid. For off-road, we can build a **Bogie** or **Rocker-Bogie** suspension using `1121 Series` Low-Side U-Channel as pivot arms.
*   *For Phase 1 (MVP)*: We stick to **Rigid Chassis + Big Pneumatic Tires** (Low pressure absorbs bumps). This is the standard "Badger-M" approach.

### 4.3 Electronics (The "Brain Box")
*   **Housing:** `1120-0001-0288` (U-Channel) covered with `1111-0001-0288` (Flat Plate).
*   **Mounting:** `1200-0001-0002` (Pattern Spacers) to lift the VESC/Odroid off the metal to prevent shorts (and thermal bridging issues discussed in research).

---

## 5. Bill of Materials (BOM) - Draft v1

| Part Name | goBILDA SKU | Qty | Notes |
| :--- | :--- | :--- | :--- |
| **Structure** | | | |
| 17 Hole U-Channel | 1120-0001-0432 | 2 | Main Rails |
| 11 Hole U-Channel | 1120-0001-0288 | 4 | Crossbeams |
| Inside Corner | 1134-0004-0001 | 8 | Frame Joinery |
| **Drivetrain** | | | |
| 14mm Shaft (100mm) | 2100-0014-0100 | 4 | Axles |
| 14mm Flanged Bearing | 1611-0005-0014 | 8 | Axle Support |
| 14mm HyperHub | 1310-0014-0002 | 4 | Wheel Mount |
| Clamping Motor Mount | 3220-0001-0001 | 4 | *Modify for 6384* |
| **Motion** | | | |
| 60T Pulley (14mm) | 3400-0014-0060 | 4 | Wheel Side |
| 5M Belt | 3406-0005-00xx | 4 | Length TBD |
| **Wheels** | | | |
| 10" Pneumatic Tire | (Generic) | 4 | *Purchase from 3rd party* |

---

## 6. Next Steps
1.  **Select Tires:** The 14mm HyperHub is our interface. We need a tire that can bolt to the goBILDA visual pattern (16mm hole pattern).
    *   *Action:* Search for "goBILDA compatible pneumatic tire" or design a 3D printed adapter for standard hand-truck wheels.
2.  **Confirm Motor Mount:** Verify if we can drill a standard goBILDA plate for 6384 motors.
