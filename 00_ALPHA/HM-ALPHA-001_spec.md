---
ID: HM-ALPHA-001
Status: ACTIVE
Version: Mk.0 "Scrapper"
Date: 2026-02-08
Role: Alpha Prototype Specification
Linked: HM-CAT-001 (Mk.1 Master)
---

# Nomad-T Mk.0 "Scrapper" — Alpha Prototype Specification

> [!NOTE]
> **Purpose:** Cheapest possible skid-steer testbed to prove the ROS 2 control stack, VESC CAN bus, and autonomy software BEFORE committing to the $1,500 Mk.1 field build.
>
> **Constraints:** Pavement only. No weatherproofing. Budget: **<$500.**

---

## 1. System Overview

| Parameter | Mk.0 "Scrapper" | Mk.1 "Nomad" (Future) |
|:---|:---|:---|
| **Motors** | 4× Hoverboard 6.5" (Salvaged) | 4× Ninebot G30 |
| **Tires** | 6.5" Solid Rubber | 10" Pneumatic |
| **Frame** | 2040 V-Slot (700×320mm) | Same |
| **Voltage** | 36V (10S) | Same |
| **VESCs** | 4× Flipsky 75100 | Same |
| **Compute** | Odroid H4 Ultra | Same |
| **Enclosure** | Open-top (no case) | Apache 3800 (IP65) |
| **Waterproofing** | ❌ None | ✅ IPX5 |
| **Ground Clearance** | ~50mm | ~89mm |
| **Weight** | ~14 kg | ~19 kg |
| **Budget** | **~$458** | ~$1,500 |

---

## 2. Motor: Hoverboard 6.5" BLDC (Salvaged)

### Sourcing
**Buy 2× broken hoverboards** from Facebook Marketplace, Craigslist, or thrift stores.

- **Target price:** $10-20 per board = **$20-40 total for 4 motors**
- **What breaks on hoverboards:** Battery (dead cells), main board (blown FETs), charger port. **Motors almost never fail.**
- **What you harvest:** 2× BLDC hub motors with tires, Hall sensor cables, phase wires

### Specs

| Spec | Value |
|:---|:---|
| **Type** | Brushless DC (BLDC), direct drive |
| **Power** | 250–350W rated |
| **Voltage** | 36V (10S) — Native! |
| **Torque** | ~12 Nm per motor |
| **Tire** | 6.5" solid rubber (bonded) |
| **Hall Sensors** | Yes (5-wire: VCC, GND, HA, HB, HC) |
| **Phase Wires** | 3× (Match or auto-detect in VESC Tool) |
| **Weight** | ~2.3 kg per motor+tire |

### VESC Compatibility

> [!TIP]
> Hoverboard motors are one of the most common VESC targets. VESC Tool has built-in motor detection that auto-configures phase order and Hall sensor mapping. **No manual configuration needed** — just run "Detect Motor" wizard.

---

## 3. Mounting Strategy

Hoverboard motors have **no external axle**. They bolt directly to a frame via 4× M4 threaded holes on the motor face.

### Option A: 3D Printed Bracket (Fastest)
- **Material:** PETG or Nylon (100% infill)
- **Design:** L-bracket bolting motor face to 2040 rail side slot
- **Lifespan:** ~50 hours. Fine for prototyping.
- **Cost:** ~$2 in filament

### Option B: Flat Aluminum Bracket (Durable)
- **Material:** 3mm aluminum flat bar
- **Design:** Bent L-bracket, drilled on both ends
- **Cost:** ~$5 from hardware store
- **Upgradeable:** Can use same bracket concept for Mk.1 motor plates

---

## 4. Electrical (Simplified)

The Mk.0 uses the **same 36V architecture** as Mk.1 but with simplified wiring:

| System | Mk.0 Approach | Mk.1 Equivalent |
|:---|:---|:---|
| **Battery** | Salvaged hoverboard 36V pack OR cheap e-bike 10S pack | Custom 10S3P |
| **Main Fuse** | 40A blade fuse (cheaper) | 60A MIDI fuse |
| **DC-DC** | DDR-60L-15 (17V) | Same |
| **Safety** | E-Stop + basic relay | Full safety chain |
| **CAN Bus** | Daisy chain (same) | Same |
| **Contactor** | Optional (can use E-Stop direct for <40A) | 100A Contactor |

### Simplified Wiring

```
Battery (36V) → Blade Fuse (40A) → E-Stop → Bus Bar
  ├── VESC 1 (Front Left)
  ├── VESC 2 (Front Right)
  ├── VESC 3 (Rear Left)
  ├── VESC 4 (Rear Right)
  └── DC-DC (17V) → Odroid H4 Ultra
```

---

## 5. What to Test on Mk.0

| Test | Goal | Pass Criteria |
|:---|:---|:---|
| **VESC Motor Detection** | All 4 motors detected | Spin freely, correct direction |
| **CAN Bus Daisy Chain** | All 4 VESCs communicate | `ros2 topic echo` shows all 4 |
| **Teleop (RC)** | Joystick controls skid steer | Smooth forward, reverse, turn |
| **Turn-in-Place** | Zero-radius turn on pavement | Completes 360° without slipping |
| **Odometry** | Hall sensor ticks = distance | Straight line ±5% over 10m |
| **E-Stop** | Kill switch works | Motors stop within 0.5s |
| **Watchdog** | Software crash = motors off | Unplug USB → motors stop |

---

## 6. Upgrade Path: Mk.0 → Mk.1

When Mk.0 has proven the software stack:

1. **Unbolt** hoverboard motors + 3D printed brackets
2. **Bolt on** G30 motor plates (NMT-MP-001)
3. **Slide in** G30 hub motors
4. **Swap** blade fuse → MIDI fuse holder
5. **Add** Apache 3800 case on bobbins
6. **Add** Contactor + full safety chain
7. **Replace** salvaged battery → proper 10S3P pack

**Everything else stays.** Frame, VESCs, Odroid, DC-DC, CAN — all identical.
