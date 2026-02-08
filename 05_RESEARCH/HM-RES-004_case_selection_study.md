---
ID: HM-RES-004
Status: ACTIVE
Date: 2026-02-07
Role: Electronics Volume Analysis & Case Selection Study
Architecture: Nomad-T G30 Standard (Rev 3.2)
Linked: HM-RES-003, HM-CAT-009, HM-CAT-016
---

# Electronics Volume Analysis & Case Selection

> [!CAUTION]
> **FINDING: The Apache 2800 is too small.** The Odroid H4 Ultra alone is 120×120mm. The Apache 2800 internal width is 229mm. Fitting the Odroid + 4× VESCs on a single thermal deck plate inside the 2800 lid is physically impossible. This analysis recommends the **Apache 3800** as the optimal upgrade.

---

## 1. Complete Electronics Inventory with Dimensions

Every electronic component that must be protected in the enclosure:

### 1.1 Thermal Deck Components (Mounted to Lid)

| Component | L × W × H (mm) | Mass (g) | Notes |
|:---|:---|:---|:---|
| **Odroid H4 Ultra** (board only) | 120 × 120 × 47 | 450 | 47mm includes stock heatsink (will be replaced by pedestal) |
| **Copper Thermal Pedestal** | 40 × 40 × 15 | 215 | On top of CPU die |
| **Flipsky 75100 VESC × 4** | 103 × 58 × 28 each | 280 each | Aluminum tube body |

**Thermal Deck plate minimum footprint:**

```
┌─────────────────────────────────────────────────┐
│               THERMAL DECK PLATE                │
│                                                 │
│  ┌───────────┐  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │  ODROID   │  │VESC│ │VESC│ │VESC│ │VESC│   │
│  │  120×120  │  │ #1 │ │ #2 │ │ #3 │ │ #4 │   │
│  │           │  │103 │ │103 │ │103 │ │103 │   │
│  │           │  │×58 │ │×58 │ │×58 │ │×58 │   │
│  └───────────┘  └────┘ └────┘ └────┘ └────┘   │
│                                                 │
│  ← 120mm →  gap  ← 4 × 58mm = 232mm →         │
│  TOTAL WIDTH: 120 + 10 + 232 = ~362mm           │
│  TOTAL DEPTH: max(120, 103) = ~120mm + margin   │
└─────────────────────────────────────────────────┘
```

> [!WARNING]
> **In-line layout: 362mm wide.** The Apache 2800 lid is only **302mm** internal length. **The VESCs don't fit alongside the Odroid in a 2800.**

**Alternative: 2×2 VESC layout (stacked pairs):**

```
┌──────────────────────────────────────────┐
│            THERMAL DECK PLATE            │
│                                          │
│  ┌───────────┐  ┌────┐ ┌────┐           │
│  │  ODROID   │  │ V1 │ │ V2 │           │
│  │  120×120  │  │103 │ │103 │           │
│  │           │  │×58 │ │×58 │           │
│  └───────────┘  ├────┤ ├────┤           │
│                 │ V3 │ │ V4 │           │
│                 │103 │ │103 │           │
│                 │×58 │ │×58 │           │
│                 └────┘ └────┘           │
│                                          │
│  WIDTH: 120 + 10 + 116 = ~246mm         │
│  DEPTH: max(120, 206) = ~210mm          │
└──────────────────────────────────────────┘
```

**2×2 layout: 246mm × 210mm.** Still doesn't fit the Apache 2800 (302 × 229mm) — the depth (210mm) is nearly at limit (229mm), but it's extremely tight with wiring. And lid depth is only **30mm** — the VESCs alone are **28mm tall.** Zero clearance.

### 1.2 Case Body Components

| Component | L × W × H (mm) | Mass (g) | Notes |
|:---|:---|:---|:---|
| **Mean Well SD-50B-24** (DC-DC) | 159 × 97 × 38 | 320 | Largest single component after Odroid |
| **Battery (10S3P 21700)** | ~200 × 80 × 65 | 1,500 | 30 cells in 10S3P config |
| **PDB (Power Distribution)** | ~80 × 60 × 25 | 100 | Bus bar + fuse holder |
| **100A ANL Fuse + Holder** | ~80 × 40 × 30 | 60 | |
| **E-Stop Contactor** | ~60 × 50 × 50 | 200 | SPST power relay |
| **BMS (10S)** | ~65 × 45 × 10 | 50 | For charging only (Vampire doctrine) |
| **IMU (WitMotion/BNO085)** | ~50 × 35 × 15 | 30 | Must be rigidly mounted to chassis or case |
| **40mm Noctua Stir Fan** | 40 × 40 × 10 | 10 | Internal air circulation |
| **Wiring Bundle Allowance** | — | 300 | Phase wires, CAN bus, power leads |

**Minimum base volume needed:** Stack the largest items:
- DC-DC (159×97×38) is the longest component
- Battery (200×80×65) is the tallest single item
- Total footprint ≈ 220 × 160mm (with wire routing channels)
- Total height ≈ 95mm (battery + PDB stacked, or battery + DC-DC side-by-side)

### 1.3 Externally Mounted Sensors (NOT in case)

| Component | L × W × H (mm) | Mass (g) | Mount |
|:---|:---|:---|:---|
| **RPLiDAR C1** | 56 × 56 × 41 | 110 | Mast-mounted on top of robot, vibration-isolated |
| **OAK-D Lite** | 91 × 28 × 18 | 61 | Front-facing bracket |
| **Sharp IR Sensors × 4** | ~44 × 20 × 13 each | 5 each | Corner-mounted on frame |
| **WiFi 6E Antennas × 2** | ~120 × 20 × 8 each | 10 each | External, pigtails through case |

**These do NOT affect case sizing** — they mount directly to the frame/mast.

---

## 2. Harbor Freight Apache Case Comparison

| Case | Internal L × W × D (mm) | Lid Depth (mm) | Base Depth (mm) | Volume (L) | Weight (g) | Price |
|:---|:---|:---|:---|:---|:---|:---|
| **Apache 1800** | 213 × 149 × 95 | ~20 | ~75 | 3.0 | ~680 | $10 |
| **Apache 2800** | 302 × 229 × 135 | **~30** | **~95** | 9.3 | ~1,100 | $20 |
| **Apache 3800** | 378 × 268 × 156 | **44 ✅ CONFIRMED** | **~105–111** | 15.8 | ~1,800 | $30 |
| **Apache 4800** | 453 × 327 × 168 | **~45** | **~120** | 24.9 | ~2,700 | $40 |
| **Apache 5800** | 515 × 289 × 145 | ~35 | ~110 | 21.6 | ~2,500 | $50 |

---

## 3. Fit Analysis

### Apache 2800 — ❌ DOES NOT FIT

| Check | Required | Available | Status |
|:---|:---|:---|:---|
| Thermal Deck plate width | 246mm (2×2 layout) | 302mm (length) | ✅ Barely |
| Thermal Deck plate depth | 210mm (2×2 layout) | 229mm (width) | ⚠️ 19mm margin (no wiring space) |
| **Lid depth for VESC** | **28mm** | **~30mm** | ❌ 2mm clearance — wires don't fit |
| DC-DC in base | 159mm | 302mm | ✅ |
| Battery in base | 200mm | 302mm | ✅ |
| Base height | 95mm needed | ~95mm | ⚠️ Zero margin |

**Verdict:** The 2800 is physically possible only if we abandon the Unified Thermal Deck (no VESCs in lid) and fold the Odroid into the base instead. This defeats the entire thermal architecture. **The 2800 must be abandoned.**

---

### Apache 3800 — ✅ OPTIMAL FIT

| Check | Required | Available | Margin |
|:---|:---|:---|:---|
| Thermal Deck plate width | 246mm (2×2) | **378mm** (length) | ✅ **132mm** spare |
| Thermal Deck plate depth | 210mm (2×2) | **268mm** (width) | ✅ **58mm** for wiring |
| Lid depth: Odroid stack | 32mm (pedestal+PCB+jacks) | **44mm CONFIRMED** | ✅ **12mm** spare |
| Lid depth: VESCs | 33mm (body+wires) | **44mm CONFIRMED** | ✅ **11mm** spare |
| DC-DC in base | 159 × 97mm | 378 × 268mm | ✅ Plenty |
| Battery in base | 200 × 80mm | 378 × 268mm | ✅ Plenty |
| Base depth | 95mm needed | **105–111mm CONFIRMED** | ✅ 10–16mm spare |

**Thermal Deck in the 3800 lid:**

```
┌──────────────────────────────────────────────────────┐
│              APACHE 3800 LID (378 × 268mm)           │
│                                                      │
│  ┌───────────┐  ┌───────┐ ┌───────┐   SPARE AREA    │
│  │  ODROID   │  │ VESC1 │ │ VESC2 │   for wiring,   │
│  │  120×120  │  │103×58 │ │103×58 │   connectors,   │
│  │           │  ├───────┤ ├───────┤   CAN bus,       │
│  │           │  │ VESC3 │ │ VESC4 │   terminal       │
│  └───────────┘  │103×58 │ │103×58 │   blocks         │
│                 └───────┘ └───────┘                  │
│                                                      │
│  Used: 246 × 210mm                                   │
│  Spare: 132 × 58mm (wire routing + strain relief)    │
└──────────────────────────────────────────────────────┘
```

**Base layout:**

```
┌──────────────────────────────────────────────────────┐
│              APACHE 3800 BASE (378 × 268mm)          │
│                                                      │
│  ┌─────────────────┐  ┌───────────────┐              │
│  │    BATTERY       │  │   DC-DC       │              │
│  │   10S3P 21700    │  │  Mean Well    │              │
│  │   200 × 80mm     │  │  159 × 97mm   │              │
│  │   (65mm tall)    │  │  (38mm tall)  │              │
│  └─────────────────┘  └───────────────┘              │
│                                                      │
│  ┌────────┐ ┌────┐ ┌──────────┐ ┌────┐              │
│  │  PDB   │ │FUSE│ │ E-STOP   │ │BMS │              │
│  │80×60mm │ │    │ │ 60×50mm  │ │    │              │
│  └────────┘ └────┘ └──────────┘ └────┘              │
│                                                      │
│  ┌───────────────────────┐                           │
│  │    WIRING CHANNELS    │ (remaining space)         │
│  └───────────────────────┘                           │
│                                                      │
│  Headroom: 110mm base depth − 65mm battery = 45mm    │
│  DC-DC can sit beside battery (38mm tall < 110mm)    │
└──────────────────────────────────────────────────────┘
```

**Verdict:** The 3800 provides comfortable margins on all axes. The Thermal Deck fits the lid with room for wire routing. The base holds the battery, DC-DC, PDB, and all power electronics with 45mm of headroom above the tallest component.

---

### Apache 4800 — ✅ FITS EASILY (Overkill?)

| Check | Required | Available | Margin |
|:---|:---|:---|:---|
| Thermal Deck plate | 246 × 210mm | 453 × 327mm | ✅ 207 × 117mm spare |
| Base components | 220 × 160mm | 453 × 327mm | ✅ Massive spare |
| Weight | — | ~2,700g case | ⚠️ +900g vs 3800 |

**Verdict:** Works perfectly, but adds ~900g and ~10mm to case height. The extra volume could house a second battery pack (10S6P for 2-hour runtime) or expansion hardware. But for Phase 1, it's bigger than necessary.

---

### Apache 5800 — ⚠️ WRONG ASPECT RATIO

The 5800 is long and narrow (515 × 289mm) — more of a rifle case shape. Width is only 289mm (marginally better than the 2800's 229mm). Not a good fit for the Thermal Deck's square-ish layout.

---

## 4. Impact Study: Bigger Case → Bigger Robot?

### The Core Question

The Apache 2800 outer dimensions are ~340 × 270 × 155mm.
The Apache 3800 outer dimensions are ~420 × 310 × 175mm.

**Delta: +80mm longer, +40mm wider, +20mm taller.**

### Impact on Robot Frame

| Parameter | Current Design (2800) | Upgraded Design (3800) | Impact |
|:---|:---|:---|:---|
| **Frame inner width** | 270mm | **310mm** | +40mm wider rails → slightly wider track |
| **Frame inner length** | 340mm | **420mm** | +80mm → longer wheelbase → more stable |
| **Frame height** | 155mm | 175mm | +20mm → negligible |
| **Track width** | ~530mm | ~570mm | +40mm → better stability |
| **Wheelbase** | ~500mm | ~580mm | +80mm → longer, more stable at speed |
| **Weight (case only)** | 1,100g | **1,800g** | +700g |
| **Total robot weight** | ~23 kg | **~23.7 kg** | +0.7 kg (3% increase) |
| **Ground pressure** | 1.8 psi | **1.85 psi** | Negligible change |

### Design Impacts

> [!TIP]
> **A bigger case makes the robot BETTER, not worse.**
>
> 1. **Longer wheelbase** (+80mm) = more pitch stability at speed and on slopes
> 2. **Wider track** (+40mm) = better roll stability
> 3. **More internal volume** = room for a second battery, future expansion
> 4. **Better thermal performance** = larger Thermal Deck plate = more surface area
> 5. **Weight increase is trivial** (+700g on a 23 kg platform = 3%)

### What Changes in the Build

| Subsystem | Change Required | Effort |
|:---|:---|:---|
| **Frame rails** | Longer 2040 extrusion: 700mm → 780mm (or 800mm standard cut) | None — buy longer extrusion |
| **DiBond panels** | Larger side panels to match | Trivial — same material, bigger cut |
| **Motor mount spacing** | Wider axle spacing | Move motor plates outboard by 20mm |
| **Thermal Deck plate** | Bigger (378 × 268mm vs 302 × 229mm) | Better — more surface area |
| **Wiring harness** | Slightly longer runs | +$5 in wire |
| **Sensor masts** | Same | No change |
| **Software** | Wheelbase/track params in odometry | One config line change |

### What Does NOT Change

- Motor selection (G30) — unchanged
- VESC selection — unchanged
- Battery chemistry — unchanged
- Sensor suite — unchanged
- DC-DC — unchanged
- Software architecture — unchanged
- Budget — +$10 for the 3800 case

---

## 5. Recommendation

### Primary: Apache 3800 ✅ CONFIRMED

| Reason | Detail |
|:---|:---|
| **Fits all electronics** | Thermal Deck in lid (44mm confirmed), power electronics in base (~110mm confirmed) |
| **Thermal benefit** | Larger plate = lower ΔT at stationary |
| **Growth room** | Can add second battery, additional VESCs, or expansion boards |
| **Weight penalty** | Only +700g (3%) — trivial |
| **Cost** | ~$30 (only $10 more than 2800) |
| **Robot impact** | Longer wheelbase + wider track = MORE stable |

### Fallback: Apache 4800 (if more growth room needed)

The 3800 lid depth (44mm) is confirmed to work. The 4800 is only needed if you want to add significantly more hardware (second battery, dual compute boards, etc). It adds +900g.

### Do NOT Buy

- ❌ **Apache 2800** — physically impossible for Unified Thermal Deck
- ❌ **Apache 5800** — wrong aspect ratio
- ❌ **Apache 1800** — far too small

---

## 6. Phase 0 Action

~~Verify lid depth in-store~~ → **CONFIRMED: 44mm lid depth (1.75").** No blocker.

**Action: Procure Apache 3800 Weatherproof Protective Case, Large, Black from Harbor Freight.**

---

*Document prepared by Engineering Partner — Nomad-T Program*
*Date: 2026-02-07*
*Updated: Lid depth confirmed at 44mm by user measurement. Recommendation locked.*
