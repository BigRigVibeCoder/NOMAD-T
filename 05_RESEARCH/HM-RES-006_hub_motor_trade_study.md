---
ID: HM-RES-006
Status: ACTIVE
Date: 2026-02-08
Role: Hub Motor Trade Study & Drivetrain Architecture Analysis
Linked: HM-CAT-010, HM-CAT-011, HM-RES-003 (RQ-1.1)
---

# Hub Motor Trade Study

> [!NOTE]
> **Gap Identified:** RQ-1.1 selected the G30 without a formal competition matrix. This document retroactively fills that gap with a proper engineering analysis.

---

## 1. Competition Matrix

| Spec | **Ninebot G30** (Gen 2) | **Xiaomi M365 Pro** | **Hoverboard 6.5"** | **Generic 10" E-Bike** (48V) |
|:---|:---|:---|:---|:---|
| **Rated Power** | 350W | 300W | 350W | 500W |
| **Peak Power** | 700–850W | 600W | ~500W | 800W |
| **Voltage** | **36V** (10S) | 36V (10S) | 36V (10S) | **48V** (13S) |
| **Torque (est.)** | ~18 Nm | ~14 Nm | ~12 Nm | ~21-50 Nm |
| **Tire Size** | **10"** Pneumatic | 8.5" Solid/Pneumatic | **6.5"** Solid | **10"** Pneumatic |
| **Tire OD** | ~250mm | ~215mm | ~170mm | ~250mm |
| **Weight (w/ tire)** | 3.2 kg | 3.5 kg | **2.3 kg** | 3.5–4.5 kg |
| **Waterproofing** | **IPX5** (Factory) | IPX4 | **None** | Varies |
| **Axle Type** | 12mm Double-D | 12mm Round | **Integrated** (no axle) | 12mm Keyed |
| **VESC Compatible** | ✅ Yes (Hall + Phase) | ✅ Yes | ⚠️ Needs adapter | ✅ Yes |
| **Tire Replaceable** | ✅ Standard tubeless | ⚠️ Difficult (8.5") | ❌ Bonded solid | ✅ Standard |
| **Cost (Refurb/Used)** | $50–$70 | $30–$50 | **$15–$25** | $60–$100 |
| **Availability** | Excellent (Millions sold) | Excellent | **Oversupplied** | Good (AliExpress) |

---

## 2. Power-to-Weight Analysis

| Motor | Power (Peak) | Weight | **P/W Ratio** | **Torque/kg** |
|:---|:---|:---|:---|:---|
| **Ninebot G30** | 850W | 3.2 kg | **266 W/kg** | 5.6 Nm/kg |
| **M365 Pro** | 600W | 3.5 kg | 171 W/kg | 4.0 Nm/kg |
| **Hoverboard 6.5"** | 500W | 2.3 kg | **217 W/kg** | **5.2 Nm/kg** |
| **Generic 10" E-Bike** | 800W | 4.0 kg | 200 W/kg | 5.3 Nm/kg |

**Observations:**
- G30 has the **best P/W ratio** and highest peak power
- Hoverboard is lightest but has the worst ground clearance (6.5" = only 83mm tire radius)
- E-bike motors are powerful but require **48V**, adding battery complexity and cost

---

## 3. The "Do We Need 4 Motors?" Analysis

### 3.1 Traction Force Calculation

| Config | Total Torque | Traction Force (at tire) | Grade (20kg Robot) |
|:---|:---|:---|:---|
| **4WD G30** | 4 × 18 = **72 Nm** | ~576 N | **>100% grade** |
| **2WD G30** | 2 × 18 = **36 Nm** | ~288 N | ~60% grade |
| **4WD Hoverboard** | 4 × 12 = **48 Nm** | ~565 N* | ~80% grade |
| **2WD Hoverboard** | 2 × 12 = **24 Nm** | ~282 N* | ~50% grade |

*\*Hoverboard has smaller tire radius (85mm vs 125mm), so force at ground is higher per Nm.*

### 3.2 The Real Reason for 4WD: Skid Steering

> [!IMPORTANT]
> **It's not about power — it's about steering.**
>
> Skid-steer (tank drive) works by running left and right sides at different speeds. With **2WD**, only the rear wheels drive. The front wheels are passive casters or fixed. This creates two problems:
>
> 1. **Turn-in-place requires dragging 2 unpowered tires sideways.** This demands enormous force on loose surfaces and is impossible on high-friction surfaces (pavement).
> 2. **Loss of traction on one driven wheel = total loss of steering.** If one rear wheel lifts off a bump, you're a unicycle.
>
> **4WD solves both:** All 4 wheels contribute to turning force and there's always redundancy.

### 3.3 Could We Do 2WD with Steering?

| Architecture | Pros | Cons |
|:---|:---|:---|
| **2WD + Front Casters** | Cheaper (2 motors), simpler | Can't turn in place, terrible off-road |
| **2WD + Ackermann Steering** | Car-like handling | Needs servo + linkage, complex fabrication |
| **4WD Skid Steer** (Selected) | Zero turn radius, simple drivetrain, redundant | 4 motors, 4 VESCs, higher cost |

**Decision: 4WD is mandatory for a skid-steer field robot.** 2WD is only viable with a dedicated steering mechanism, which adds complexity we don't want in Phase 1.

---

## 4. Why NOT Each Alternative?

### 4.1 Hoverboard Motor — ❌ REJECTED

Despite the lowest cost ($15) and lightest weight (2.3kg):
- **6.5" tire = 83mm radius = 50mm ground clearance** after mounting. A curb kills it.
- **No waterproofing.** Open motor with exposed magnets and Hall sensors. One puddle = dead motor.
- **Solid tire only.** No pneumatic option = zero damping, resonance vibration destroys electronics.
- **No standard axle.** Motor bolts directly to a frame. Requires custom bracket per motor.
- Used in: Indoor warehouse robots, educational platforms. **Not field-rated.**

### 4.2 Xiaomi M365 Pro — ⚠️ VIABLE BUT INFERIOR

- **8.5" tire** is barely adequate for ground clearance (~108mm radius)
- Tire changes on 8.5" M365 rims are notoriously difficult (the tire is extremely tight on the rim)
- Lower power (300W rated) means less margin
- **Could work** for a lighter robot (<15kg) on paved surfaces
- Used in: Urban delivery robots (sidewalk-only)

### 4.3 Generic 48V E-Bike Motor — ⚠️ VIABLE BUT COMPLICATES POWER

- **48V requires 13S battery.** This means more cells, higher cost, higher BMS complexity.
- Fewer VESC options rated for 48V continuous
- Heavier (4+ kg per motor)
- **Would make sense** if we needed >25 km/h or >30kg payload
- Good option for **Phase 2** if more power is needed

---

## 5. Final Verdict

| Criterion | Winner |
|:---|:---|
| **Best All-Around** | **Ninebot G30** |
| **Cheapest** | Hoverboard 6.5" (~$60 for 4) |
| **Lightest** | Hoverboard 6.5" (~9.2 kg for 4) |
| **Most Powerful** | Generic 48V E-Bike |
| **Best Sealed** | **Ninebot G30** (IPX5) |
| **Best Tire** | **Ninebot G30** (10" pneumatic, field-replaceable) |

> [!TIP]
> **The G30 wins on the criteria that matter most for a field robot:** waterproofing, tire quality, VESC compatibility, and parts availability. It's not the cheapest or the lightest — but it's the one that won't die in mud.

**Configuration: 4× G30 @ 36V (10S) = CONFIRMED.**
- Total motor mass: 12.8 kg (51% of robot weight — this is normal for a hub-motor platform)
- Total peak power: 3,400W
- Total peak torque: 72 Nm
- Gradeability: >100% loaded

---

## Appendix: The "Chinesium Hoverboard" Path (Budget Alternative)

If budget is the absolute top priority and the robot will operate **indoors only**:

| Item | Cost |
|:---|:---|
| 4× Hoverboard Motors | $60 |
| 4× Custom Brackets | $40 |
| Frame (2040) | $18 |
| **Total Frame+Drive** | **$118** |

**Savings:** ~$260 vs G30 path. **Tradeoff:** No waterproofing, no ground clearance, solid tires, custom brackets.
