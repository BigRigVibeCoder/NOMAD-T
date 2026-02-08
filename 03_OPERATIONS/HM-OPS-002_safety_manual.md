---
ID: HM-OPS-002
Status: ACTIVE
Date: 2026-02-08
Role: Safety Manual & Emergency Procedures
Linked: HM-RES-005 (CDR-6, CDR-11, CDR-13), HM-DWG-001
---

# Nomad-T Safety Manual

> [!CAUTION]
> **MANDATORY READING** before any work on the robot. This document defines the safety systems, emergency procedures, and handling protocols for a 36V Li-Ion powered mobile robot.

---

## 1. Hazard Summary

| Hazard | Source | Severity | Mitigation |
|:---|:---|:---|:---|
| **Electrical Shock** | 36V Battery (42V Max) | Moderate | XT90-S disconnect, MIDI fuse, E-Stop |
| **Thermal Burns** | VESCs under load, Brake Resistor | Low | Enclosed in case, thermal deck dissipates |
| **Pinch/Crush** | Moving wheels (30Nm torque) | High | E-Stop, Watchdog, Never reach under while powered |
| **Battery Fire** | Li-Ion thermal runaway | Severe | BMS protection, fuse, charge port fuse, steel cells |
| **Tip-Over** | Off-camber terrain, CG shift | Moderate | Speed limits, payload centering |

---

## 2. Safety Systems Architecture

### 2.1 Emergency Stop (CDR-6)

*   **Type:** Red Mushroom Button, Normally-Closed (NC)
*   **Location:** Rear panel, accessible without reaching over wheels
*   **Action:** Pressing E-Stop breaks the contactor coil circuit → Contactor opens → **All motor power is cut instantly**
*   **Reset:** Twist/Pull to release button → Power cycle Arduino → Watchdog re-asserts → Contactor closes
*   **Design Principle:** The E-Stop does NOT switch high current directly. It interrupts the low-current coil circuit.

### 2.2 Watchdog (CDR-6)

*   **Controller:** Arduino Nano (USB connected to Odroid)
*   **Heartbeat:** ROS node sends serial heartbeat every 500ms
*   **Timeout:** If no heartbeat for 2 seconds → Arduino de-asserts D2 → Relay opens → Contactor opens
*   **Fail-Safe:** Loss of USB, Odroid crash, or software hang = motors OFF

### 2.3 Main Fuse (CDR-13)

*   **Rating:** 60A MIDI Fuse, **≥58V DC Rated** (Littelfuse 498 series or equivalent)
*   **Location:** Immediately after battery XT90-S (<200mm wire length)
*   **Replacement:** Turn off battery (disconnect XT90-S) → Wait 30 seconds → Unbolt fuse → Replace with identical rating → Reconnect.
*   **Spare Fuses:** Carry 2× spares in the Apache 3800 case lid pocket.

> [!WARNING]
> **NEVER substitute a higher-rated fuse.** The 60A rating protects 10 AWG wire from fire. A higher fuse defeats the protection.

### 2.4 Charging Safety (CDR-11)

*   **Port:** Weipu SP17 (Rear Panel), fused at **10A**
*   **Charger:** 42V Li-Ion charger (10S), ≤5A output
*   **Procedure:**
    1. Press E-Stop (motors disabled)
    2. Connect charger to Weipu port
    3. Monitor BMS LED (if visible) or battery voltage via Arduino/Odroid
    4. Disconnect when BMS balance LED goes solid or voltage reaches 41.5V
    5. **Never charge unattended overnight**

---

## 3. First Power-On Protocol

> [!IMPORTANT]
> Perform this sequence for **every** first assembly or after any wiring change.

1. **Visual Inspection:**
   - [ ] All wires routed away from moving parts
   - [ ] No bare copper visible (all terminals insulated)
   - [ ] Fuse installed and correct rating visible
   - [ ] E-Stop is PRESSED (locked out)

2. **Cold Resistance Checks** (Battery NOT connected):
   - [ ] Battery (+) to Frame: > 1 MΩ (no short to chassis)
   - [ ] Battery (-) to Frame: > 1 MΩ
   - [ ] CAN Bus end-to-end: ~60Ω (with both terminators)

3. **Connect Battery:**
   - [ ] Plug XT90-S Anti-Spark connector slowly (expect small spark on anti-spark pin)
   - [ ] Red LED ON = Safety chain active (correct)
   - [ ] Measure Bus Bar voltage: 30-42V DC

4. **Logic Power Verify:**
   - [ ] DC-DC output: 17.0V ± 0.2V
   - [ ] Odroid power LED: ON

5. **Release E-Stop:**
   - [ ] Twist button to release
   - [ ] Power-cycle Arduino (disconnect/reconnect USB or reset button)
   - [ ] Listen for contactor CLICK (confirming closure)
   - [ ] Red LED OFF, Green LED behavior TBD

---

## 4. Emergency Procedures

### 4.1 Runaway Robot
1. **Press E-Stop** (if reachable)
2. If E-Stop not reachable: **pull the XT90-S battery connector**
3. If neither: **tip the robot on its side** (wheels off ground)

### 4.2 Battery Smoke / Swelling
1. **Disconnect battery immediately** (XT90-S)
2. Move battery to open air (concrete/dirt, NOT inside building)
3. Do NOT use water. Use **dry sand** or **Class D fire extinguisher**
4. Call emergency services if fire develops

### 4.3 Electrical Shock
1. **Do NOT touch the victim and the robot simultaneously**
2. Disconnect XT90-S using insulated gloves or a dry wooden stick
3. Administer first aid. Call 911 if needed.

---

## 5. Personal Protective Equipment (PPE)

| Item | When Required |
|:---|:---|
| **Safety Glasses** | All wiring and assembly work |
| **Insulated Gloves** | Battery connection/disconnection |
| **Closed-Toe Shoes** | All operations (robot weighs 19kg) |
| **Hearing Protection** | Not required (hub motors are silent) |
