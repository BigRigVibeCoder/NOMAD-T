---
ID: HM-CAT-014
Status: ACTIVE
Role: Electrical System Specification
Date: 2026-02-07
Linked: HM-DWG-001 (Schematic)
---

# Electrical System Specification

> [!CAUTION]
> **Safety Critical.** Follow HM-DWG-001 Schematic exactly.

## 1. High Voltage (HV) Bus

*   **Nominal Voltage:** 36V DC
*   **Chemistry:** Li-Ion (10S)
*   **Max Voltage:** 42.0V
*   **Min Voltage:** 30.0V (Cutoff)
*   **Main Fuse:** 60A MIDI Fuse (Bolt-down, >58V Rated)
*   **Connector:** XT90-S Anti-Spark

## 2. Low Voltage / Logic

*   **Source:** Mean Well DDR-60L-15 DC-DC Converter
*   **Input:** 18-75V DC
*   **Output:** 15V (Trimmed to **17V** per CDR-8)
*   **Capacity:** 60W (4A)
*   **Loads:**
    *   Odroid H4 Ultra (17V)
    *   USB Peripherals (5V via Odroid)
    *   Arduino Nano (5V via USB)

## 3. Safety Systems (CDR-6)

*   **Emergency Stop:**
    *   Physical mushroom button (NC).
    *   Breaks the **coil circuit** of the main contactor.
    *   Does NOT switch high current directly.
*   **Watchdog:**
    *   Arduino Nano monitors heartbeat from ROS.
    *   If lost, kills relay -> kills contactor.
*   **Braking:**
    *   200W 8Ω Brake Resistor on HV Bus.
    *   Triggered by VESC over-voltage protection (CDR-5).

## 4. Communication

*   **CAN Bus:**
    *   Daisy-chain topology (CDR-7).
    *   Shielded Twisted Pair (STP).
    *   120Ω Terminator at last node.
*   **USB:**
    *   Internal USB 2.0 to Arduino.
    *   External USB 3.0 to Sensors.

## 5. Wiring Standards

*   **HV (Battery -> Dist):** 10 AWG Silicone (Red/Black)
*   **HV (Dist -> VESC):** 14 AWG Silicone
*   **Motor Phase:** 16 AWG (or OEM Motor Wire)
*   **Logic Power:** 18-20 AWG
*   **Signal/CAN:** 22-24 AWG Twisted
