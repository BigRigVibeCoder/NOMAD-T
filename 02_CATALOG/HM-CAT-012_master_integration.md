---
ID: HM-CAT-012
Status: ACTIVE
Role: Master Integration Specification
Date: 2026-02-07
Linked: HM-CAT-001, HM-CAT-009, HM-CAT-014
---

# Master Integration Specification

> [!NOTE]
> **Updated for Phase 1.** Defines the physical integration of all subsystems into the Apache 3800 chassis.

## 1. Primary Enclosure: Apache 3800 (CDR-3)

*   **Model:** Apache 3800 Water-Resistant Protective Case (Black)
*   **Dimensions (Ext):** 415 × 328 × 173 mm
*   **Dimensions (Int):** 378 × 268 × 154 mm (Base Depth: 105mm)
*   **Modifications:**
    *   Lid removed and replaced with **Unified Thermal Deck** (6mm Al Plate).
    *   Base drilled for wire glands (cable ingress) and mounting bobbins.
*   **Mounting:** 4x M5 Vibration Isolation Bobbins (Shore 40A).

## 2. Power Source: 10S3P Li-Ion (36V)

*   **Architecture:** 10 Series, 3 Parallel
*   **Cell Type:** 18650 High-Discharge (Samsung 25R or similar)
*   **Capacity:** ~7.5Ah - 9.0Ah (depending on cell) -> **Updated Target: 10Ah+**
*   **Dimensions:** ~200mm × 80mm × 70mm block
*   **Connector:** XT90-S Anti-Spark
*   **Placement:** Floor of Apache 3800 (Right Side), secured with strap plate (CDR-9).

## 3. Unified Thermal Deck (CDR-4)

The "Lid" of the case is a functional heatsink.

| Component | Mounting | Notes |
| :--- | :--- | :--- |
| **Odroid H4 Ultra** | Inverted | CPU contacts Copper Pedestal (15mm) -> Thermal Pad -> Deck |
| **VESC 75100 (x4)** | Inverted | Flat side bolted to Deck bottom |
| **Status LEDs** | Panel Mount | Rear facing on box edge or separate panel |

## 4. Sensor Placement

*   **RPLiDAR C1:** Mounted on short mast or direct to front deck. Height: >300mm from ground.
*   **OAK-D Lite:** Camera mast or bracket.
*   **GPS/Compass:** Mast (keep away from Motors/High Current wires).

## 5. Ground Clearance

*   **Wheel Radius:** 125mm (10" Tire)
*   **Axle Height:** 125mm
*   **Frame Rail Bottom:** Axle Height - 40mm (Profile) = ~85mm
*   **Result:** **~89mm** clearance under rails. Excellent for gravel/grass.

## 6. Mass Estimate

| Subsystem | Mass |
| :--- | :--- |
| **Structure (Rails/Plate)** | 4.0 kg |
| **Drivetrain (Motors x4)** | 8.8 kg (2.2kg ea) |
| **Battery (10S3P)** | 2.5 kg |
| **Electronics + Case** | 3.5 kg |
| **Total** | **~18.8 kg** |

Within the 20-25kg target for manageable field deployment.
