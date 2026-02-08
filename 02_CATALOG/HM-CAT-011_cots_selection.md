---
ID: HM-CAT-011
Status: ACTIVE
Role: Component Selection Rationale (Phase 1)
Date: 2026-02-07
Linked: HM-CAT-010, HM-RES-005
---

# Component Selection Rationale (Phase 1)

> [!NOTE]
> **Why we changed everything.**
> The initial "Badge-M" concept (RC Truck parts) was rejected during Research for being water-permeable, complex, and maintenance-heavy. The Phase 1 design prioritizes **Reliability** and **Sealing**.

## 1. Drivetrain: Hub Motors vs. Belt Drive

| Feature | G30 Hub Motor (Selected) | RC Belt Drive (Rejected) |
| :--- | :--- | :--- |
| **Sealing** | IPX5 (Sealed Drum) | Open (Belts collect mud) |
| **Complexity** | 1 Moving Part | ~20 Parts (Pulley, Belt, Mount, Axle, Bearings) |
| **Torque** | 30Nm (Direct) | ~4Nm (Gearing required) |
| **Maintenance** | Zero | High (Belt tension, debris clearing) |
| **Cost** | $60/corner | ~$120/corner |

**Decision:** **Ninebot G30 Hub Motors.** They solve the "Rasputitsa" mud problem by having no external linkage to jam.

## 2. Chassis: 2040 Extrusion vs. Suspension

| Feature | Rigid 2040 "Skid" (Selected) | Trailing Arm Susp (Rejected) |
| :--- | :--- | :--- |
| **Simplicity** | Bolt-together | Complex geometry, pivots, shocks |
| **Rigidity** | Extreme (Box frame) | Flexible (Compliance issues) |
| **Payload** | High (Static load) | Limited by spring rates |
| **Terrain** | "Tank" style | Baja style |

**Decision:** **Rigid 2040 Frame.** For a slow-moving (25km/h) field robot, pneumatic tires provide sufficient damping. Suspension adds unwarranted complexity for Phase 1.

## 3. Power: 36V (10S) vs. 22V (6S)

| Feature | 36V Architecture (Selected) | 22.2V RC LiPo (Rejected) |
| :--- | :--- | :--- |
| **Efficiency** | Higher (Lower current for same power) | Lower (High current heat) |
| **Compatibility** | Native to G30 components | Requires boost or specialized motors |
| **Availability** | Massive e-bike/scooter ecosystem | RC Hobby specific |
| **Safety** | Steel-cased 18650s | Soft-pouch LiPos (Fire risk) |

**Decision:** **36V System.** Aligns with industrial/scooter standards and reduces I²R losses in the wiring.

## 4. Compute: Odroid H4 Ultra vs. Jetson

**Decision:** **Odroid H4 Ultra.**
*   **Why x86?** Superior compatibility with ROS 2, Docker, and standard Linux tools compared to ARM (Jetson).
*   **Why Ultra?** 8 Cores provide headroom for heavy V-SLAM (Visual SLAM) and navigation stacks without bogging down.
