---
ID: HM-CAT-013
Status: ACTIVE
Role: Frame Specification
Date: 2026-02-07
Linked: HM-CAT-010, HM-CAT-012
---

# Frame Specification (2040 Rigid)

> [!NOTE]
> **Simplicity First.** The suspension design was rejected due to complexity and weight. We use a rigid "skid" frame relying on large pneumatic tires for damping.

## 1. Main Structure

*   **Profile:** 2040 V-Slot Aluminum Extrusion (Silver or Black)
*   **Length:** 700mm (Side Rails)
*   **Width:** 320mm (Outer-to-Outer rail spacing)
*   **Crossmembers:**
    *   2040 Profile for rigidity.
    *   Positioned at Front, Rear, and Center (Battery/Load support).
*   **Joinery:** Interior Corner Brackets + T-Plates for rigidity.

## 2. Shear Panels (CDR-9)

*   **Material:** 3mm DiBond (Aluminum Composite Panel)
*   **Role:** Structural "Shear Web" to prevent parallelogramming.
*   **Mounting:** Bolted to the side of the 2040 rails.
*   **Aesthetics:** Dark Gray / Black matte finish.

## 3. Motor Interface (NMT-MP-001)

*   **Plates:** 6mm Aluminum (6061-T6)
*   **Location:** Bolted to the *front and rear faces* of the side rails.
*   **Function:** Holds the G30 axle flats (CDR-2). Doubles as a structural corner gusset.

## 4. Vibration Isolation (CDR-3)

*   **Mounts:** 4x M5 Rubber Bobbins (Shore 40A)
*   **Location:** Top of the 2040 rails.
*   **Payload:** Carries the Apache 3800 case.
*   **Purpose:** Decouples high-frequency chassis vibration (motor/terrain) from sensitive electronics (Odroid/HDD).

## 5. Cut List (Phase 1)

| Part | Profile | Length | Qty |
| :--- | :--- | :--- | :--- |
| **Side Rails** | 2040 | 700mm | 2 |
| **Crossbeams** | 2040 | 240mm | 4 |
| **Motor Plates** | 6mm Al | Custom | 4 |
| **Shear Panels** | 3mm DiBond | 700x120mm | 2 |
