---
ID: HM-CAT-011
Status: ACTIVE
Role: Component Selection Rationale & Trade Studies
Linked: HM-CAT-010 (Drivetrain Spec)
---

# COTS Component Selection: Trade Studies

This document records the **why** behind each component choice in [HM-CAT-010](HM-CAT-010_drivetrain_spec.md).

---

## 1. Wheel/Tire Trade Study

### Requirements

| Req | Target | Rationale |
|:---|:---|:---|
| Diameter | 150–200mm | Ground clearance vs gear ratio |
| Width | 60–80mm | Stability vs scrub |
| Load Rating | >15kg/wheel | 20kg ÷ 4 × 2.5 SF |
| Hub | Standard pattern | No custom adapters |

### Candidates

| Option | Ø | Width | Hub | Cost/4 | Verdict |
|:---|:---|:---|:---|:---|:---|
| goBILDA 5203 96mm | 96mm | 40mm | 8mm D | $48 | ❌ Too small |
| goBILDA Rhino 152mm | 152mm | 58mm | 8mm hex | $80 | ⚠️ Marginal |
| Pololu 120mm Scooter | 120mm | 50mm | 8mm bore | $36 | ❌ Plastic hub |
| Traxxas X-Maxx 7772 | 180mm | 85mm | 24mm hex | $120 | ⚠️ Heavy |
| **Arrma Kraton 8S** | **182mm** | **75mm** | **17mm hex** | **$90** | **✅ Selected** |
| 10" Hand Truck Pneumatic | 254mm | 65mm | 16mm bore | $50 | ❌ Too heavy, no suspension |

### Decision: Arrma Kraton 8S (ARA510120)

- 17mm hex is an industry standard with massive aftermarket
- Belted construction won't balloon at speed
- Foam inserts = no punctures
- Proven in 30+ lb RC trucks — directly validated for our weight class

> [!IMPORTANT]
> **Hub Interface:** 17mm hex mates directly to Kraton diff output. No adapter needed when using Kraton diff modules.

---

## 2. Motor Trade Study

### Candidates

| Motor | KV | Peak Power | Torque | Shaft | Weight | Cost |
|:---|:---|:---|:---|:---|:---|:---|
| **Flipsky 6374 190KV** | 190 | 3,000W | 3.8 Nm | 8mm key | 850g | **$65** |
| Flipsky 6384 190KV | 190 | 3,500W | 4.2 Nm | 8mm key | 1.0kg | $70 |
| Turnigy SK8 6374 | 192 | 2,500W | 3.4 Nm | 10mm | 900g | $55 |
| goBILDA Yellow Jacket | N/A | 45W | 0.18 Nm | 6mm D | 250g | $30 |
| Hoverboard Hub Motor | ~16 | 350W | ~12 Nm | Integrated | 2.5kg | $25 |

### Decision: Flipsky 6374 190KV (Sensored)

**Why 6374 over 6384:**
- 150g lighter per motor (300g total savings)
- 4mm shorter (easier packaging)
- Better aftermarket mount availability
- Still provides 1.53× safety factor on torque

**Why not Yellow Jacket:** Yellow Jacket delivers 45W vs 3,000W — it's designed for 1–5kg robots, not 20kg.

---

## 3. Reduction Architecture Trade Study

| Option | Method | Pros | Cons |
|:---|:---|:---|:---|
| **A: Belt → RC Diff** | HTD belt to Kraton diff input | Proven diff, adjustable, cheap | Needs adapter plate |
| B: Belt → Live Axle | HTD belt to locked axle | Simplest | No diff = tire scrub in turns |
| C: Planetary Gearbox | Bolt-on gearbox to motor | Compact | Expensive ($150+), heavy |

### Decision: Option A — Belt to RC Differential

The Arrma Kraton rear diff assembly (ARA310940) provides a proven, oil-filled bevel gear differential for $45. One custom adapter plate (laser-cut aluminum) bridges the HTD 60T pulley to the diff spur gear mount.

---

## 4. Differential Detail

**Part:** Arrma Kraton 8S Rear Diff (ARA310940)

| Spec | Value |
|:---|:---|
| Type | Bevel gear, oil-filled |
| Internal Ratio | ~1.1:1 |
| Output | 2× CV cups (17mm hex) |
| Width | 65mm |
| Weight | 280g |
| Cost | ~$45 (eBay) |

**Adapter Required:** Pulley-to-diff plate (6mm aluminum, laser cut)
- Input: M4 holes matching 60T pulley
- Output: M3 holes matching diff spur gear mount

---

## 5. CV Axle Options

| Option | Angle Tolerance | Durability | Cost |
|:---|:---|:---|:---|
| Stock Dog Bones (ARA310448) | ±25° | Medium | $15/pair |
| CVD Shafts (ARA310945) | ±35° | High | $35/pair |

**Decision:** Start with stock dog bones. Upgrade to CVD if binding at suspension extremes.
