---
ID: HM-CAT-010
Status: ACTIVE
Role: Drivetrain Specification
Date: 2026-02-07
Linked: HM-CAT-001 (Master), HM-CAT-013 (Frame)
---

# Drivetrain Specification

> [!NOTE]
> **Design Change:** Shifted from "Belt Drive Outrunner" to **Direct Drive Hub Motor** for reliability, waterproofing, and simplicity.

## 1. Selected Motor: Ninebot Max G30 (Gen 2)

*   **Type:** Brushless Direct Drive Hub Motor
*   **Position:** Rear Wheel (Drum brake compatible, though brake not strictly required)
*   **Voltage:** 36V Nominal (10S)
*   **Power:** 350W Nominal / 700W Peak
*   **Torque:** ~30 Nm peak per wheel (×4 = 120 Nm total)
*   **KV:** ~14 KV (High torque, low speed)
*   **Speed:** ~30 km/h unloaded at 36V

### 1.1 Sourcing Rules (The "Golden Unit" - CDR-1)
*   **Target:** OEM or High-Quality Refurb (MonsterScooterParts, reputable eBay pulls).
*   **Avoid:** "Front" wheels (no motor), "Lite" versions (G30L/LP).
*   **Connector:** 3× Phase (Bullet/Spade) + 5/6 pin Hall Sensor.
    *   *Action:* Likely need to re-terminate phase wires to 4mm Bullets or MR60 for VESC.

## 2. Tire Specification

*   **Size:** 10 inch (Nominal OD ~250mm)
*   **Format:** 60/70-6.5 Tubeless Pneumatic
*   **Pressure:** ~25-30 PSI (Lower for off-road traction)
*   **Self-Healing:** Many G30 tires come with internal sealant (gel layer). This is a **bonus** for field robustness.

## 3. Mounting Interface (CDR-2 Specification)

> [!CRITICAL]
> **Custom Part Required:** NMT-MP-001 Motor Plate

The G30 axle has a "Double-D" profile. It **cannot** be clamped in standard round mounts.

*   **Plate Material:** 6061-T6 Aluminum (6mm thick).
    *   *Upgrade Option:* 304 Stainless Steel (CDR-2 recommendation for fatigue).
*   **Axle Slot:** 12mm Round with 10mm Flats.
*   **Fillet Radius:** **R2.0mm minimum** in slot corners to prevent stress risers.
*   **Fastening:** Bolted to 2040 Extrusion end-face via 4× M5 screws.
*   **Anti-Rotation:** The tight-tolerance slot + torque washer prevents axle spin.

## 4. Performance Calculations

| Param | Value |
| :--- | :--- |
| **Simulated Speed** | ~25 km/h (Loaded) |
| **Traction Force** | ~400N (continuous) / ~1000N (peak) |
| **Climbing Grade** | >30% (Skid steer traction limited) |
| **Turn-in-Place** | Excellent (High torque, rigid chassis) |

## 5. Maintenance Schedule (CDR-1)

*   **Bearings:** 6001-2RS (Standard sealed).
    *   *Interval:* Check for play every 50km. Replace if gritty.
*   **Axle Nuts:** Check torque (tightness) every 10 hours of operation.
*   **Tire Pressure:** Check weekly.
