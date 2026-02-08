---
ID: HM-ALPHA-002
Status: ACTIVE
Version: Mk.0 "Scrapper"
Date: 2026-02-08
Role: Alpha Prototype Bill of Materials
Linked: HM-ALPHA-001
---

# Mk.0 "Scrapper" — Shopping List

> **Target: <$500.** Junkyard motors + AliExpress hardware + reusable electronics.

---

## 1. Salvaged Parts (Facebook Marketplace / Craigslist / Thrift)

| Item | What You're Harvesting | Qty | Est. Cost |
|:--|:--|:--|:--|
| **Broken Hoverboard** | 2× motors + tires + Hall cables | 2 boards | **$40** |
| **Hoverboard Battery** (Optional) | 36V 10S2P Li-Ion pack + BMS | 1 | **$0** (from board) |

> [!TIP]
> **How to spot a good donor board:**
> - Listing says "won't turn on" or "won't charge" = dead battery or BMS. Motors are fine.
> - Listing says "one side doesn't work" = dead gyro board. Motors are fine.
> - Listing says "motor grinding" = **SKIP** (actual motor damage, rare).
> - Bonus: Some boards include chargers. The charger is 42V (10S) — you can reuse it.

---

## 2. Frame & Hardware (AliExpress)

| Item | Spec | Qty | Est. Cost |
|:--|:--|:--|:--|
| 2040 V-Slot Extrusion | 700mm length | 2 | $12 |
| 2040 V-Slot Extrusion | 1000mm (cut to 240mm) | 1 | $6 |
| M5 × 10 BHCS + T-Nuts | 2040 fasteners (bag of 50) | 1 | $6 |
| Interior Corner Brackets | 2040 L-bracket | 12 | $5 |
| M4 × 15 SHCS | Motor mounting bolts | 16 | $3 |

**Subtotal: ~$32**

---

## 3. Motor Mounting (Choose One)

### Option A: 3D Printed (Fastest, $2)
- Print 4× L-brackets in PETG, 100% infill
- Bolt motor M4 face to bracket, bolt bracket to 2040 T-slot
- **Lifespan:** ~50 hours of testing

### Option B: Aluminum Flat Bar ($10)
- Buy 25mm × 3mm aluminum flat bar from hardware store
- Cut and drill 4× L-brackets
- More durable, slightly more effort

---

## 4. Electronics (Reusable — Carries to Mk.1)

| Item | Spec | Qty | Est. Cost | Source |
|:--|:--|:--|:--|:--|
| **VESCs** | Flipsky 75100 | 4 | $260 | Flipsky / AliExpress |
| **DC-DC** | Mean Well DDR-60L-15 | 1 | $35 | DigiKey |
| **USB-CAN** | TouCAN or similar | 1 | $30 | Amazon |
| **Odroid H4 Ultra** | Already purchased | 1 | $0 | — |
| **RAM** | 16GB DDR5 SO-DIMM | 1 | $0 | Already purchased |

**Subtotal: ~$325**

---

## 5. Safety & Wiring

| Item | Spec | Qty | Est. Cost | Source |
|:--|:--|:--|:--|:--|
| E-Stop Button | NC Mushroom, panel mount | 1 | $8 | AliExpress |
| Blade Fuse + Holder | 40A ATC | 1 | $3 | Auto parts / Amazon |
| XT60 Connectors | Battery disconnect | 2 pairs | $3 | AliExpress |
| 12 AWG Silicone Wire | Red + Black (2m each) | 1 | $5 | AliExpress |
| 18 AWG Wire | Signal / Logic (assorted) | 1 | $4 | AliExpress |
| Arduino Nano | Watchdog + LED driver | 1 | $5 | AliExpress |

**Subtotal: ~$28**

---

## 6. Optional but Recommended

| Item | Spec | Qty | Est. Cost | Notes |
|:--|:--|:--|:--|:--|
| RC Receiver + Transmitter | FlySky FS-i6X | 1 | $45 | Manual override / teleop |
| Joystick (USB) | Logitech F710 | 1 | $30 | ROS 2 teleop_twist_joy |
| Anti-tip Casters | 1" swivel caster | 2 | $5 | Prevents face-plants on hard braking |

---

## Grand Total

| Category | Cost |
|:--|:--|
| Salvaged Parts | $40 |
| Frame & Hardware | $32 |
| Motor Mounting | $5 |
| Electronics (Reusable) | $325 |
| Safety & Wiring | $28 |
| **Total (Required)** | **~$430** |
| Optional (RC/Joystick) | +$80 |
| **Total (Full Kit)** | **~$510** |

> [!IMPORTANT]
> **$325 of this carries forward to Mk.1 unchanged.** The actual "throwaway" cost of the Alpha is only ~$105 (motors + frame hardware + brackets).
