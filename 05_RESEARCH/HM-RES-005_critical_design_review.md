---
ID: HM-RES-005
Status: ACTIVE
Date: 2026-02-07
Role: Independent Critical Design Review
Architecture: Nomad-T G30 Standard (Rev 3.2)
Linked: HM-RES-003, HM-RES-004, HM-CAT-016
Reviewer: Engineering Partner (adversarial review)
---

# Critical Design Review — Nomad-T

> [!CAUTION]
> **This is an adversarial review.** Everything below challenges decisions that were previously marked "✅ ANSWERED." Some of these are serious. None are personal — they exist because a robot that falls apart in the field teaches nothing.

---

## CDR-1: Skid-Steer Bearing Abuse (RQ-1.1, 1.2) 🟡 CONFIRMED

**The problem nobody talked about:**

The G30 motor bearings are designed for a scooter rolling forward. We're using them in a skid-steer robot that **drags wheels sideways during every turn.** The consultant analyzed cantilever bending (radial load) — correct. But skid-steer generates **lateral scrubbing forces** that the G30 bearings were never designed for.

- During a zero-radius turn, each wheel is dragged perpendicular to its rolling axis.
- Scrub force per wheel: ~6 kg × 9.81 × μ ≈ **35N laterally.**
- This lateral force is applied at the tire contact patch, 55mm from the nearest bearing.
- **This is a thrust load on a radial bearing.** Deep-groove ball bearings can handle some axial load (~50% of radial rating), but repeated lateral impacts (curbs, rocks, ruts) during skid turns will accelerate bearing wear.

**Consultant response (CONFIRMED):** The delivery robot community (using similar hub motors in 4WD skid-steer) has identified the weak points: **internal snap rings and bearing seats** fail first under sustained grit/impact duty cycles. No formal whitepaper, but field-validated.

**Required actions:**

1. **Seal upgrade:** Verify the G30 uses high-quality **2RS seals** (rubber contact seals). If factory seals are generic, upgrade to **SKF or NSK equivalent** to keep grit out of the races. This is the #1 life extension.
2. **Maintenance schedule:** Check for **"wheel click" (axial play)** every **50 km of operation.** Test: grab the tire and wiggle side-to-side. Any detectable play = bearings approaching fatigue limit. Budget ~$20 for replacement bearing set.
3. **Spares:** Procure one spare set of G30 bearings (likely 6001-2RS, 12×28×8mm) during Phase 0. **Verify exact bearing model after disassembling first motor.**

---

## CDR-2: Fatigue on the Cantilever Axle (RQ-1.2) 🟡 CONFIRMED

The consultant's Factor of Safety >20 is for **static** loading. The robot will hit curbs, roots, and rocks. Each impact is a shock load on a cantilevered 12mm axle, and every shock cycle counts toward fatigue.

- Steel fatigue endurance limit is ~40-50% of yield strength. The G30 axle is likely low-carbon steel (~250 MPa yield), so fatigue limit ≈ 125 MPa.
- At 3.5 Nm static, the bending stress is ~4.3 MPa. FoS >20 for static. But a 5G shock (hitting a curb at speed) → 17.5 Nm → 21.5 MPa. Still safe, but **the D-flat slot in the mounting plate is a stress concentrator.** Sharp corners in the D-flat cutout multiply local stress by 2-3×.

**Consultant response (CONFIRMED):** Fatigue is the "silent killer" of robotic chassis in cantilever designs. Every curb strike is a high-amplitude stress cycle.

**Required actions:**

1. **CAD rule — fillet radii:** When drawing the D-shape axle hole, **do NOT let the flat lines meet the circle at a sharp point.** Use the Fillet tool to round all four intersection points to **≥ 2mm radius.** This is a SendCutSend requirement.

2. **Material upgrade (consultant recommendation):**

   | Material | Pros | Cons | Recommendation |
   |:---|:---|:---|:---|
   | 6061-T6 Aluminum (6mm) | Light, easy to machine | Lower fatigue strength, corrodes in mud | Original spec — adequate for Phase 1 |
   | **304 Stainless Steel (4mm)** | **Rust-proof in mud/snow, higher fatigue limit** | Heavier, harder to machine | **Recommended for field duty** |
   | AR400/500 Steel (4mm) | Extreme impact hardness, "battle-hardened" | Difficult to machine, heavy, rusts | Overkill unless extreme impacts expected |

   > [!TIP]
   > **SendCutSend offers both 304 SS and AR400 as standard materials.** If upgrading from 6mm aluminum to 4mm 304 SS, the plate rigidity is similar (steel E-modulus is 3× aluminum, offsetting the thinner gauge) and it won't corrode in wet field conditions.

---

## CDR-3: No Vibration Isolation for Electronics (RQ-2.1, 5.1) 🔴 CONFIRMED — CRITICAL

**Consultant verdict: Hard-mounting the Apache case is REJECTED.**

A skid-steer robot on gravel generates sustained **high-frequency vibration** (hundreds of Hz) from tire treads and scrubbing. A rigid monocoque transmits this with zero damping directly into the electronics.

### Failure Modes (Consultant Analysis):

1. **Connector fretting (RAM/SSD):** High-frequency micro-motion wears through gold contact plating → oxidation → intermittent connections. Result: random reboots and data corruption in the field.

2. **Nylon standoff creep (THERMAL CATASTROPHE):** This is the killer.
   - Nylon has high CTE and creeps under constant load + heat.
   - Vibration acts as an impact driver — it **will** back nylon screws out.
   - If the copper pedestal shifts 1mm, it slides off the 10×10mm CPU die.
   - **Thermal resistance → infinity. CPU fries instantly.**

### The Fix: Vibration Isolation Bobbins

Decouple the "sprung mass" (Apache case + electronics) from the "unsprung mass" (chassis + motors).

| Bobbin Spec | Value |
|:---|:---|
| Type | Cylindrical male-male studs (one end into T-nut, other through case floor) |
| Thread | **M5 or M6** |
| Dimensions | ~15–20mm diameter, 15–20mm height |
| Durometer | **Shore 40A–50A** (do NOT exceed 60A — too stiff for high-freq) |
| Material | Neoprene or Silicone |
| Fastening | **Nyloc nuts** inside case (NO Loctite near ABS — causes stress cracking) |
| Frame side | Split washer on T-nut side |
| Quantity | **4× minimum** |
| Cost | **~$8 total** |

> [!CAUTION]
> **NO LOCTITE NEAR PLASTIC.** Liquid threadlocker (Loctite Blue 243) attacks ABS/polycarbonate (stress cracking) and degrades rubber. Use Nyloc nuts only.

### Environmental Sealing (Three-Way Consensus) ✅

Drilling bobbin holes voids IP65. The following sealing protocol restores it:

1. **Outside (between bobbin flange and case floor):** **M5 bonded sealing washer** (rubber-backed metal washer) — compresses into a gasket under the bobbin stud head.
2. **Inside (before fender washer and Nyloc nut):** Bead of **marine-grade RTV silicone** around the stud hole.
3. Result: Each penetration is double-sealed (mechanical + chemical).

### Wire Routing Across Isolation Boundary (Three-Way Consensus) ✅

Stiff wires bridging the bobbin gap short-circuit the vibration isolation.

**Assembly rule (mandatory):**
1. Secure wire bundle tightly to 2040 frame with P-clip **before** the case.
2. Leave a **50mm flexible service loop** (S-shape or C-shape) that can flex freely.
3. Secure wire bundle tightly **inside** the Apache case immediately after entry.
4. Use high-strand-count **silicone-jacketed wire** for motor phase leads. **PVC-jacketed wire is not acceptable.**

### CDR-3 Status: ✅ RESOLVED

All three parties agree. BOM additions: 4× M5 Shore 40A bobbins ($8), 4× bonded sealing washers ($2), RTV silicone ($5), Nyloc nuts + fender washers ($2). **Total: ~$17.**

---

## CDR-4: Thermal Deck CTE Mismatch & Paste Pump-Out (RQ-5.1) 🟡 CONFIRMED — RESOLVED

**Consultant verdict: Thermal interface strategy revised. Hybrid TIM approach required.**

Over a 60°C operating cycle, the aluminum beneath the 40mm copper block expands ~15 µm more than the copper. This creates a pumping action that migrates thermal paste out of the gap over hundreds of cycles → dry spots → thermal failure.

### The Fix: Hybrid TIM Strategy (Consultant + Engineering Partner Consensus)

| Interface | Location | Material | Spec | Why |
|:---|:---|:---|:---|:---|
| **A** | Copper → Aluminum plate | **Thermal Pad** | 0.5mm, **≥ 6.0 W/m·K** | Absorbs 15µm CTE shear without migration |
| **B** | Copper → CPU die | **Thermal Paste** | **≥ 8.0 W/m·K** | Minimum bond line for fragile bare die |

**Recommended products:**
- **Interface A (pad):** Fujipoly Sarcon XR-series or Laird Tflex HP (~$8 for a sheet)
- **Interface B (paste):** Thermal Grizzly Kryonaut or Arctic MX-6 (~$8 tube)

> [!IMPORTANT]
> **Bolt type clarification — two different bolt sets, two different rules:**
> - **Cu-to-Al plate bolts:** Use **metal bolts** (M3 or M4 steel), torqued to pad manufacturer's recommended pressure for full wet-out. Metal is fine here — the pad absorbs CTE differential.
> - **Cu-to-CPU die clamp (through Odroid board):** Use **nylon standoffs** at **0.3–0.5 Nm max.** The die is 10×10mm exposed silicon — metal bolts over-torqued here will crack it. These are NOT the same bolts.

### CDR-4 Status: ✅ RESOLVED

BOM additions: 1× thermal pad sheet ($8), 1× thermal paste tube ($8). **Total: ~$16.**

---

## CDR-5: Regen Braking with Full Battery = Loss of Control (RQ-3.4) 🔴 CONFIRMED — CRITICAL SAFETY

> [!CAUTION]
> **My original software-only fix was WRONG.** Setting `battery_cut_end = 42V` saves the battery but **kills all braking force.** On a hill, the robot free-wheels uncontrollably. The consultant correctly identified this as a safety-critical failure.

**Consultant verdict: The Flipsky 75100 does NOT protect the battery from regen overvoltage.** Its protections are designed to save the VESC (cuts at ~70V), not the cells. Software voltage limits cause instant loss of braking torque.

### The Failure Sequence (Software-Only):

1. Robot descends steep hill with 100% charged battery (42V).
2. Driver brakes → VESCs regen → bus voltage pushes past 42V.
3. VESC firmware hits `battery_cut_end` → **stops regenerating instantly.**
4. **ZERO braking force.** Robot free-wheels downhill.

### The Fix: Hardware Brake Shunt (Rheostatic Braking)

A power resistor + switch dumps excess regen energy as heat, allowing the VESC to maintain braking torque without over-volting the battery.

| Component | Spec | Cost |
|:---|:---|:---|
| Power Resistor | **200W, 8Ω chassis-mount wirewound** (100W insufficient for sustained braking — see math below) | ~$15 |
| DC Solid State Relay | **60V DC, ≥25A continuous** (Fotek SSR-25 DD or equivalent) | ~$15 |
| Wiring | Resistor + SSR in series, across battery P+ and P- | — |
| Control | VESC Master GPIO pin → SSR control input | — |

**VESC Configuration (VESC Tool):**
1. App Settings → Nrf/UART/Brake → External Brake Resistor
2. Select GPIO pin connected to SSR control
3. Set brake threshold: **43.0V** (just above full charge)
4. When bus voltage hits 43V during braking, VESC fires GPIO → SSR activates → current dumps into resistor → voltage drops → braking force maintained.

**Mounting:** Resistor bolted to aluminum frame rail (NOT near the Apache case — resistor surface exceeds 100°C). Frame acts as heatsink.

### Resistor Sizing Validation (Three-Way Consensus) ✅

Peak dump power at 43V across 8Ω: P = V²/R = 43²/8 = **231W.** A 100W resistor handles 5-second bursts (wirewound thermal mass), but a sustained 30-second downhill brake at full charge will burn it out — and an open-circuit resistor puts you back to square one (no brakes or over-volted battery). **200W provides adequate margin.**

**Thermal clearance (mandatory):** Resistor surface can exceed **250°C** under full load. Maintain **≥100mm clearance** from:
- Apache case (ABS softens >105°C)
- DiBond panels (PE core melts >120°C)
- Any wiring insulation

Bolt resistor to bare 2040 aluminum rail with **thermal paste** at the mounting pad. Frame acts as heatsink.

### CDR-5 Status: ✅ RESOLVED (Hardware fix required)

BOM additions: 1× 200W 8Ω wirewound resistor ($15), 1× 60V/25A DC SSR ($15), wiring + connectors ($5). **Total: ~$35.**

---

## CDR-6: No Hardware Watchdog / E-Stop Path (RQ-3.3, 4.1) 🔴 CONFIRMED — CRITICAL SAFETY

> [!CAUTION]
> **The current design is UNSAFE.** There is no positive method to disconnect high voltage during a software failure. A kernel panic, segfault, or frozen ROS node could result in a full-speed runaway robot. This is mandatory before any field operation.

**Consultant verdict:** No physical kill switch exists in the design. VESC CAN timeout is not sufficient — a crashing Odroid can spew garbage CAN data that resets the timeout, or hardware CAN buffers can re-transmit the last valid frame indefinitely ("zombie state"), locking the robot at its last speed until battery death or impact.

### The Fix: Hardware Safety Chain

The main contactor coil must pass through **two hardware safety devices in series.** If either link breaks, the contactor opens and all motor power is cut.

```
[+12V Source] → [E-Stop NC] → [Watchdog Relay NO] → [Contactor Coil +]
                                                      [Contactor Coil -] → [GND]
```

**Contactor engages ONLY IF:** (E-Stop is NOT pressed) **AND** (Watchdog is receiving heartbeat)

#### Link 1: Physical E-Stop (Kill Switch)

| Spec | Value |
|:---|:---|
| Type | **Industrial mushroom-head pushbutton** |
| Action | Push-to-lock, twist-to-reset |
| Rating | **IP65/IP67** (sealed against rain/mud) |
| Contacts | **NC (Normally Closed)** — in series with contactor coil supply |
| Cost | ~$8 |

#### Link 2: Hardware Watchdog Timer

| Spec | Value |
|:---|:---|
| MCU | **Arduino Nano** or ATtiny85 (~$3) |
| Relay | Small logic-level relay or MOSFET ($2) — controls contactor coil circuit |
| Heartbeat | Odroid must send a signal every ~100ms |
| Timeout | If no signal for **500ms**, watchdog drops relay → contactor opens |
| Cost | ~$8 total |

### 🔍 My Pushback: The Odroid Has No GPIO

The consultant's design says "toggle a GPIO pin." **The Odroid H4 Ultra does NOT have a GPIO header.** It's an x86 SBC, not a Raspberry Pi. Its interfaces are:
- 4× USB 3.0, 1× USB 2.0
- 2× Ethernet (2.5GbE)
- HDMI, DisplayPort
- M.2 slots
- **No user-accessible GPIO pins**

**Fix: USB-serial heartbeat instead of GPIO.**

1. Connect the Arduino Nano to the Odroid via **USB cable** (the Nano appears as `/dev/ttyUSB0`).
2. The Odroid runs a lightweight daemon that writes a keep-alive byte (`0xA5`) to the serial port every 100ms. This is a 10-line Python script or systemd service.
3. The Arduino validates byte value and timing. If no valid byte for 500ms → kill the relay.
4. **Why this works:** If the Odroid kernel panics, the serial daemon dies, no bytes are sent, the watchdog fires. If USB hardware hangs, same result — no bytes flow, watchdog fires.

> [!IMPORTANT]
> The USB-serial approach is actually **more reliable** than GPIO for watchdog purposes. A GPIO pin can be held high by a crashed process if the pin was set before the crash. A serial byte stream requires the daemon to be actively running — if ANY part of the software stack dies (kernel, Python runtime, systemd), the stream stops.

### E-Stop Mounting Location (Three-Way Consensus) ✅

**Location: DiBond side panel, top edge (left or right side).**

- **Accessibility:** In a runaway, the operator runs alongside and hits the button from standing — no reaching down toward wheels or leaning over the chassis.
- **Visibility:** Most prominent location on the robot.
- **Rigidity:** DiBond is rigid. Mounting to the vibration-isolated Apache case makes it a "moving target" on rough terrain.
- **Wiring:** Through M22 waterproof panel mount. Wire runs inside frame rail channel.

### CDR-6 Status: ✅ RESOLVED (Hardware safety chain required)

BOM additions: 1× IP65 mushroom e-stop ($8), 1× Arduino Nano ($3), 1× 5V relay module ($3), 1× USB cable ($2), wiring ($2). **Total: ~$18.**

---

## CDR-7: CAN Bus Single Point of Failure (RQ-3.2, 4.1) 🟡 CONFIRMED — RESOLVED

All 4 VESCs on a single CAN bus daisy chain is a single point of failure. If one transceiver fails shorted, the entire bus dies.

### The Fix: Proper CAN Hygiene (Consultant + Engineering Partner Consensus)

**For Phase 1, accept single CAN bus but implement it correctly:**

| Requirement | Spec |
|:---|:---|
| Topology | **Daisy-chain only** — no star, no stubs |
| Wiring | **Shielded Twisted Pair (STP)** — NOT loose wires |
| Termination | **120Ω resistor at each physical end** of the bus (first VESC and last VESC) |
| Bus order | Odroid CAN adapter → VESC1 → VESC2 → VESC3 → VESC4 |
| Shield grounding | Shield grounded at **one end only** (Odroid side) to prevent ground loops |

**Phase 2 upgrade path:** Split into dual CAN buses (left pair + right pair) using two USB-CAN adapters. If one bus dies, opposite-side motors still function for a limp-home mode.

### CDR-7 Status: ✅ RESOLVED

BOM additions: STP cable (~$5), 2× 120Ω termination resistors ($0.20). **Total: ~$5.**

---

## CDR-8: Mean Well DC-DC Voltage Mismatch (RQ-3.4) 🔴 CONFIRMED — BOM CHANGE REQUIRED

**Consultant verdict: The SD-50B-24 is REJECTED.** Minimum trim output is 21V — exceeds Odroid's 20V max input. Would destroy the board.

**Consultant solution: Switch to SD-50B-12 and trim UP to 16V.**

| Spec | SD-50B-24 ❌ REJECTED | SD-50B-12 ✅ PROPOSED |
|:---|:---|:---|
| Output | 24V (trim 21–28V) | 12V (trim **11–16V**) |
| Target | 19V — **unreachable** | **16V — at top of trim range** |
| Odroid safe? | ❌ 21V > 20V max | ✅ 16V in 14–20V range |
| Power at target | 50W at 24V = 2.08A | 50W at 16V = **3.125A** |
| Odroid max draw | 34W / 16V = 2.125A | **Within 3.125A limit** ✅ |

**Why 16V is ideal:** Sits in the middle of the Odroid's 14–20V range, provides 2V buffer above 14V minimum against sag during heavy CPU+GPU loads.

**Assembly rule:** Before connecting Odroid, power up SD-50B-12 and use multimeter + screwdriver to adjust V_ADJ trim pot clockwise to **16.0V.** Verify with multimeter under no-load. **Never connect without verifying.**

### 🔴 My Pushback: Input Voltage Range Mismatch

**Neither I nor the consultant caught this initially.** The SD-50B-12 input range is **19V – 36V.** Our 10S battery hits **42V at full charge** — 6V over the max input. The SD-50C-12 (36–72V) drops out below 36V, losing the Odroid with 20%+ battery remaining. **Neither B nor C covers 30V–42V.**

### ✅ FINAL SOLUTION: Mean Well DDR-60L-15 (Three-Way Consensus)

The consultant located the correct part family: **wide-input "4:1" industrial DIN-rail DC-DC converters.**

> [!WARNING]
> **Do NOT use cheap Amazon/AliExpress buck modules (XL4016, LTC3780).** They are electrically noisy (corrupts USB peripherals, sensors), have poor thermal management, and degrade under vibration. Do not power the robot's brain with hobby-grade electronics.

| Spec | DDR-60L-15 ✅ SELECTED |
|:---|:---|
| Input range | **18V – 75V DC** (covers 30V LVC to 42V full charge with massive headroom) |
| Output | 15V nominal, trim **13.5V – 18V** |
| Target output | **17.0V** (centered in Odroid 14–20V range, 3V buffer each side) |
| Power | **60W** (4A at 15V) — Odroid max 34W = **2.0A at 17V** ✅ |
| Form factor | Ultra-slim DIN rail mount |
| Mounting | 100mm segment of 35mm DIN rail on DiBond electronics panel |

**Assembly procedure:**
1. Mount 100mm DIN rail segment to DiBond panel (2× screws).
2. Clip DDR-60L-15 onto rail (better vibration resistance than old chassis-mount).
3. Power from battery **unloaded** (Odroid disconnected).
4. Adjust front-panel trim pot to **17.0V** — verify with multimeter.
5. Connect Odroid only after confirming 17.0V ± 0.5V.

### CDR-8 Status: ✅ RESOLVED (Third iteration)

| Iteration | Part | Result |
|:---|:---|:---|
| 1 | SD-50B-24 | ❌ Output min 21V > Odroid 20V max |
| 2 | SD-50B-12 | ❌ Input max 36V < battery 42V full |
| 3 | **DDR-60L-15** | ✅ **18–75V input, 15V out → trim to 17V** |

BOM change: Remove SD-50B-24, add **Mean Well DDR-60L-15** + 100mm DIN rail segment. Cost delta: ~$10 more than original.

---

## CDR-9: Mass Retention — Case + Battery (RQ-2.1) 🔴 CONFIRMED — CRITICAL SAFETY

Two heavy masses are unrestrained in the current design. In a 10G impact (hitting a wall at 4 m/s, ~40mm crush distance):

| Item | Mass | Force at 10G | Current Retention | Risk |
|:---|:---|:---|:---|:---|
| Apache 3800 case | 1.8 kg | **176N** | Bobbins (CDR-3) | ✅ Solved |
| **10S Li-Ion battery** | **~5 kg** | **490N** | **None** | 🔴 **Arc flash / fire** |

> [!WARNING]
> **The battery is a kinetic weapon deployed against your own robot.** If it shifts and a terminal contacts the aluminum frame → hundreds of amps short circuit → welds to frame → immediate thermal runaway (fire).

### Part A: Apache Case Retention ✅ CLOSED

CDR-3 vibration bobbins (4× M5 studs + Nyloc nuts) provide positive retention in X, Y, and Z. No additional work needed.

### Part B: Battery Retention (Three-Way Consensus)

#### 1. Battery Floor Plate (Consultant Addition — Critical)

**You cannot strap a battery directly across open 2040 rails.** The battery sags in the middle, and vibration causes sharp V-slot inner edges to saw through the PVC shrink wrap like an orbital sander.

| Spec | Value |
|:---|:---|
| Material | Scrap DiBond piece or 3mm aluminum plate |
| Mounting | Bolted to V-slots via T-nuts, bridging the two bottom rails |
| Padding | **3mm adhesive neoprene foam** on top surface (anti-slip + shock absorption) |

#### 2. Strap System

| Spec | Value |
|:---|:---|
| Quantity | **2× separate straps** |
| Width | 1 inch (25mm) nylon webbing |
| Buckles | **Metal cam buckles** (plastic buckles break under vibration) |
| Routing | Under the battery floor plate, over the top of the battery |
| Cost | ~$5 |

**Abrasion check:** File/deburr any sharp edges where straps pass through 2040 extrusion slots.

#### 3. Terminal Safety — "No Sparks" Rule (Consultant Override)

> [!CAUTION]
> **Kapton tape is insufficient** — it wears through and falls off under vibration. My original recommendation was wrong.

**Requirement:** The main battery power leads must terminate in a **fully shrouded, high-amperage connector:**
- **XT90-S Anti-Spark** (preferred — built-in pre-charge resistor prevents arc on plug-in)
- Anderson Powerpole PP75 (acceptable alternative)

**Rule:** No exposed conductive metal (ring terminals, spade connectors, bare bullet connectors) is permitted on the battery side of the connection. **Ever.**

### CDR-9 Status: ✅ RESOLVED

BOM additions: 1× DiBond/Al floor plate (scrap), 1× neoprene foam sheet ($3), 2× cam buckle straps ($5), XT90-S connectors ($4 pair). **Total: ~$12.**

---

## CDR-10: No Graceful Shutdown Path (RQ-4.1) 🟡 CONFIRMED — RESOLVED

**Hard-cutting power to an Ubuntu NVMe system is Russian Roulette with your data.** ext4 journal corruption will eventually brick the OS, requiring manual filesystem repair in the field (keyboard + monitor on a muddy robot).

### My Original Proposals — Both Rejected:

| Option | Verdict | Why |
|:---|:---|:---|
| Read voltage via VESC CAN bus | ❌ Rejected | Violates defense-in-depth — relies on ROS + CAN drivers staying alive to save themselves |
| Hardware ADC on Odroid | ❌ Rejected | Odroid H4 Ultra is x86 — **no analog input pins** |

### ✅ The Fix: Leverage the CDR-6 Arduino Watchdog (Consultant Solution)

The Arduino Nano from CDR-6 is already connected to the Odroid via USB serial and monitoring heartbeats. **Add battery voltage sensing to this existing hardware** — no new components needed beyond two resistors.

#### 1. Voltage Divider Circuit (add to Arduino Nano)

```
Battery (+) → [R1: 100kΩ] → Arduino A0 → [R2: 10kΩ] → Battery GND
```

- **Max measurable:** 5V × (100+10)/10 = **55V** (safe for 42V 10S pack)
- **Components:** 2× ¼W resistors ($0.20 total)

#### 2. Arduino Firmware Update

The watchdog sketch now does double duty:
- **Heartbeat watchdog** (CDR-6): Kill relay if no `0xA5` byte for 500ms
- **Voltage reporting** (CDR-10): Read A0, calculate real voltage, send `V:38.4\n` over serial every second

#### 3. Odroid Daemon Update

The existing Python watchdog daemon now also parses voltage telemetry:
- If voltage < **32.0V** (3.2V/cell) for **>5 consecutive seconds** → execute `shutdown -h now`
- This gives the OS ~60 seconds to halt cleanly before the BMS hard-cuts at ~30V (3.0V/cell)

> [!IMPORTANT]
> **Why this is superior to CAN bus monitoring:** The shutdown daemon is a 20-line Python script running as a systemd service, completely independent of ROS 2. If ROS crashes AND the battery is low, this daemon still runs and triggers a clean shutdown. Defense in depth.

### CDR-10 Status: ✅ RESOLVED

BOM additions: 2× resistors ($0.20). Firmware + software update only. **Total: ~$0.20.**

---

## CDR-11: Charging Port Design (missing entirely) 🟡 CONFIRMED — RESOLVED

Opening the sealed Apache case every charge cycle wears latches, breaks IP65, and exposes electronics to the environment. An external charge port is mandatory.

### My Original Proposal — Rejected:

I proposed an XT60 panel mount ($3). **The consultant correctly identified this creates a live 42V dead-short risk on the exterior of the robot.** Hobby connectors lack sealing caps, are easily fouled by mud, and have exposed pins.

### ✅ The Fix: Industrial IP68 Charge Connector + Fuse (Consultant Solution)

#### 1. Connector Specification

| Spec | Value |
|:---|:---|
| Part | **Weipu SP13 or SP17 series (2-pin)** mated pair |
| Rating | **IP68 when capped** — true waterproof, not just splash-resistant |
| Features | Threaded coupling (vibration-proof), shrouded contacts (short-proof), tethered cap |
| Mounting | Female panel-mount receptacle in Apache case side wall, with included rubber gasket |
| Cost | ~$12 per mated pair |

**The tethered cap MUST be installed whenever not charging.**

#### 2. Dedicated Charge Fuse (Consultant Addition — Critical)

> [!CAUTION]
> You cannot wire an external port directly to the battery. If someone (or debris) shorts the exposed pins, you get an arc flash from the full battery pack.

| Spec | Value |
|:---|:---|
| Fuse | **10A automotive blade fuse** in inline fuse holder |
| Location | On the positive line, **immediately inside the Apache case** between the Weipu connector and the BMS charge port |
| Purpose | If the external port is shorted, 10A fuse blows instantly — main battery and wiring remain protected |

#### 3. Wiring Path

```
External Weipu Port → [10A Fuse] → BMS Charge Terminals (C+/C-)
```

- Charge path **bypasses the main contactor** — allows charging while robot is powered off
- **Charging feedback:** Rely on the charger brick's LED indicator (Red = charging, Green = complete). Do NOT add displays or LEDs to the robot exterior — each penetration is another potential leak path

### CDR-11 Status: ✅ RESOLVED

BOM additions: 1× Weipu SP17 2-pin pair ($12), 1× 10A inline fuse holder ($3), 10A blade fuses ($1). **Total: ~$16.**

---

## CDR-12: No Status Indicators (missing entirely) 🟢

## CDR-12: No Status Indicators (missing entirely) 🟢 CONFIRMED — RESOLVED

The Odroid is headless. WiFi is the only interface. If WiFi drops, you're completely blind.

### My Original Proposal — Rejected:

I proposed NeoPixels driven by the Odroid. **The consultant caught me forgetting my own CDR-6 finding:**
1. **No GPIO:** The Odroid H4 Ultra has no GPIO header to drive NeoPixels.
2. **Software-dependent:** NeoPixels need precise timing. A kernel panic during boot = no LEDs = zero information.

### ✅ The Fix: Industrial "Traffic Light" (Consultant Solution)

Three separate panel-mount LED indicators driven by existing hardware — no software dependency for basic health.

| LED | Color | Driven By | Logic | Meaning |
|:---|:---|:---|:---|:---|
| **Green** | 🟢 | Arduino Nano (USB command from Odroid) | ON only when Odroid daemon confirms all critical ROS nodes are running. Odroid crash → heartbeat stops → Arduino kills green. | **Software stack healthy** |
| **Yellow** | 🟡 | Arduino Nano (**autonomous**) | Blink if battery < 34V. Solid if < 32V. Uses CDR-10 voltage divider data. Works even if Odroid is dead. | **Battery warning** |
| **Red** | 🔴 | **Hardwired to safety chain** | Wired in parallel with contactor coil or watchdog relay. If safety chain broken (e-stop or watchdog), Red lights up. No software involved. | **Robot is safed / will not move** |

**Hardware:** 3× industrial 12mm panel-mount LED indicators (5V, integrated resistor), drilled into rear DiBond panel.

> [!IMPORTANT]
> **Defense in depth:** Red LED works with no software at all (pure hardware). Yellow LED works with only the Arduino alive (no Odroid needed). Green LED requires the full stack. If you see Red + Yellow + no Green, you know exactly what layer failed.

### CDR-12 Status: ✅ RESOLVED

BOM additions: 3× panel-mount LEDs ($3 total), wiring ($1). **Total: ~$4.**

---

## CDR-13: No Main Fuse on HV Bus (NEW) 🔴 CONFIRMED — CRITICAL SAFETY

> [!CAUTION]
> **There is no fuse anywhere between the battery and the VESCs.** This is arguably the most basic electrical safety requirement in any high-current system, and it is completely absent from the design. The BMS is the *backup*; the fuse is the *primary* defense.

### The Failure Mode

Without a fuse, the only overcurrent protection is the BMS internal MOSFET (which may or may not have a fast enough trip curve) and the wire insulation itself. In a hard short (e.g., a motor phase wire chafes through insulation against the aluminum frame):

1. Short circuit current: **hundreds of amps** (limited only by battery internal resistance and wire resistance)
2. 10-12 AWG wire at 200A+ → insulation melts in **<2 seconds**
3. If the BMS doesn't trip fast enough → **the wire IS the fuse** → arc flash → fire

This is how garage fires start in the e-bike and RC community.

### The Fix: High-Voltage MIDI Fuse Assembly (Consultant Validated)

#### Load Analysis (justifying 60A rating):

| Condition | Per Motor | 4× Motors Total |
|:---|:---|:---|
| Nominal driving (~350W @ 36V) | ~10A | **~40A continuous** |
| Peak stall/skid-turn (~700W @ 36V) | ~20A | **~80A peak** |

A 60A MIDI fuse is **slow-blow**: holds 60A indefinitely, holds ~90A (150%) for several seconds before blowing. This handles brief 80A skid-turn peaks without nuisance blowing.

#### Fuse Specification:

| Spec | Value |
|:---|:---|
| Fuse type | **Bolt-down MIDI / AMI fuse** (positive mechanical connection, won't vibrate loose) |
| Rating | **60A** (consultant validated — slow-blow handles 80A peaks) |
| Voltage | **≥58V DC rated — CRITICAL** |
| Recommended part | **Littelfuse 498 series** or equivalent industrial/marine grade |
| Holder | Inline MIDI fuse holder with protective cover, 10AWG ring terminals |
| Placement | **Immediately after the battery XT90-S connector** |
| Cost | ~$5 (fuse) + ~$8 (holder) = **$13** |

> [!CAUTION]
> **DO NOT buy standard auto parts store MIDI fuses.** Most automotive MIDI fuses are rated for **32V DC only** (car electrical systems). At 42V full charge, a 32V-rated fuse trying to interrupt a dead short **may not extinguish the arc** — the fuse blows but electricity jumps the gap, sustaining the fault. **Specify ≥58V DC rated fuses explicitly.**

#### Wire Gauge Constraint:

A fuse protects the *wire*, not the electronics. To safely use a 60A fuse:
- Main battery feeder wires must be **≥10AWG high-strand silicone wire (200°C rated)**
- If using thinner 12AWG wire, the wire might overheat before the fuse blows in a partial short

**Carry spares:** Keep 3× spare fuses in the maintenance kit. If a fuse blows, it means something else is broken — don't just replace the fuse without finding the root cause.

> [!IMPORTANT]
> **Fuse placement rule:** The fuse must be the FIRST component after the battery connector. The wiring path is:
> `Battery → XT90-S → MIDI Fuse → Bus Bar / Distribution → VESCs + DC-DC + Contactor`
>
> If the fuse is downstream of any junction, an unfused branch can still short.

### CDR-13 Status: ✅ RESOLVED

BOM additions: 1× 60A MIDI fuse ≥58V rated ($5), 1× inline holder ($8), 3× spare fuses ($10). **Total: ~$23.**

---

## Summary: Final Priority Triage

| # | Issue | Severity | Status | Cost | Resolution |
|:---|:---|:---|:---|:---|:---|
| CDR-1 | Bearing wear | 🟡 | ✅ | $0 | SKF 2RS seals + 50km maintenance |
| CDR-2 | Axle fatigue | 🟡 | ✅ | $0 | ≥2mm fillet radii + 304 SS option |
| CDR-3 | Vibration isolation | 🔴 | ✅ | $17 | Shore 40A bobbins + bonded washers + service loops |
| CDR-4 | CTE mismatch | 🟡 | ✅ | $16 | Hybrid TIM: pad at Cu-Al, paste at Cu-die |
| CDR-5 | Regen braking | 🔴 | ✅ | $35 | 200W 8Ω brake resistor + 60V/25A SSR |
| CDR-6 | No E-stop/watchdog | 🔴 | ✅ | $18 | Safety chain + USB-serial Arduino heartbeat |
| CDR-7 | CAN bus SPOF | 🟡 | ✅ | $5 | Daisy-chain STP + 120Ω termination |
| CDR-8 | DC-DC mismatch | 🔴 | ✅ | $10Δ | DDR-60L-15 (18–75V in, trim to 17V) |
| CDR-9 | Mass retention | 🔴 | ✅ | $12 | Battery floor + straps + XT90-S |
| CDR-10 | No graceful shutdown | 🟡 | ✅ | $0.20 | Arduino voltage divider + daemon |
| CDR-11 | No charge port | 🟡 | ✅ | $16 | Weipu SP17 IP68 connector + 10A fuse |
| CDR-12 | No status LEDs | 🟢 | ✅ | $4 | R/Y/G traffic light driven by Arduino + safety chain |
| CDR-13 | No main fuse | 🔴 | ✅ | $23 | 60A MIDI fuse ≥58V DC (Littelfuse 498) |

**Total cost of all fixes: ~$156.** No architectural changes required.

**The Arduino Nano ($3) is now the single most critical component** — it runs:
- Heartbeat watchdog (CDR-6)
- Contactor relay control (CDR-6)
- Battery voltage monitoring (CDR-10)
- Graceful shutdown triggering (CDR-10)
- Green + Yellow LED control (CDR-12)

---

## ⚠️ FINAL BLOCKER: Integrated Wiring Harness Diagram

> [!CAUTION]
> **Do NOT begin assembly without a complete wiring diagram.** Every subsystem from these 13 CDRs (safety chain, HV bus, CAN bus, voltage monitoring, charge port, status LEDs) must be drawn on one sheet to ensure correct interaction and proper ground management.

---

*Independent Critical Design Review — Engineering Partner*
*Date: 2026-02-07*
*Methodology: Adversarial failure mode analysis across all subsystems*
*13 CDRs identified, analyzed, and resolved through three-way review*
*CDR-13 added at consultant recommendation — main fuse missing from HV bus*
