---
ID: HM-CAT-001
Status: ACTIVE
Role: Master Design Specification (Phase 1)
Date: 2026-02-07
Linked: HM-CAT-010, HM-CAT-012, HM-CAT-013, HM-CAT-014
---

# Nomad-T Phase 1 "Skid-Steer" Specification

> [!NOTE]
> **APPROVED DESIGN.** This document supersedes all previous concepts (Badger-M, Arrma, Suspension).
> **Objective:** Build a rugged, weatherproof, skid-steer field robot using mass-produced scooter components.

## 1. System Overview

*   **Architecture:** 4WD Skid-Steer (Tank Drive)
*   **Chassis:** Rigid 2040 Aluminum Extrusion with DiBond Shear Panels
*   **Drivetrain:** 4× Direct-Drive Hub Motors (Ninebot G30 Gen 2)
*   **Power:** 36V 10S3P Li-Ion (Swappable)
*   **Compute:** Odroid H4 Ultra (x86) + OAK-D Lite + RPLiDAR C1
*   **Target Mass:** ~18–22kg
*   **Payload:** ~10kg (Flat Deck)
*   **Speed:** ~25 km/h (Software limited)

## 2. Core Directives (from CDR)

1.  **"Golden Unit" Sourcing:** Use verified OEM/refurb parts for critical drivetrain components (G30 motors), not generic clones.
2.  **Unified Thermal Deck:** The Odroid and VESCs share a common 6mm aluminum armor plate for cooling and protection (CDR-4).
3.  **Vibration Isolation:** The electronics case (Apache 3800) is "floated" on rubber bobbins to protect components (CDR-3).
4.  **Hardware Safety:** Physical E-Stop loop, independent status LEDs, and hardware watchdog (CDR-6, CDR-12).

## 3. Subsystem Breakdown

### 3.1 Structure (HM-CAT-013)
*   **Rails:** 700mm long 2040 V-Slot (Silver).
*   **Width:** 320mm outer-to-outer.
*   **Panels:** 3mm DiBond (Aluminum Composite) side skins for shear strength.
*   **Waterproofing:** IP65 desired for case (IPX5 for motors).

### 3.2 Drivetrain (HM-CAT-010)
*   **Motors:** 4× Ninebot Max G30 Rear Hub Motors (350W nom / 800W peak).
*   **Tires:** 10" Pneumatic (60/70-6.5) Pre-installed.
*   **Mounting:** Custom 6mm Aluminum plates with 2mm fillet radii slots (CDR-2).

### 3.3 Electronics (HM-CAT-014 & HM-DWG-001)
*   **Voltage:** 36V Nominal (10S).
*   **Protection:** 60A MIDI Fuse (Main), 10A (Charge), 5A (DC-DC).
*   **Logic:** 17V regulated for Odroid (CDR-8).
*   **Control:** 4× Flipsky 75100 VESC via CAN Bus.

## 4. Bill of Materials Summary (Phase 1)

| Subsystem | Est. Cost | Status |
| :--- | :--- | :--- |
| **Drivetrain** (Motors, Plates) | ~$350 | Sourcing |
| **Structure** (Rails, Case, DiBond) | ~$150 | Sourcing |
| **Power** (Battery, Fuse, Wiring) | ~$200 | Sourcing |
| **Compute** (Odroid, RAM, WiFi) | ~$400 | Purchased |
| **Control** (VESCs, Arduino) | ~$300 | Sourcing |
| **Sensors** (LiDAR, Camera) | ~$250 | Sourcing |
| **Total** | **~$1,650** | **Under Budget ($2k)** |
