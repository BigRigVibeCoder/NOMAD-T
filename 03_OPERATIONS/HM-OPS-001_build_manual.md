---
ID: HM-OPS-001
Status: ACTIVE
Date: 2026-02-08
Role: Assembly & Build Manual
Linked: HM-DWG-001, HM-CAT-002, HM-CAT-015
---

# Nomad-T Phase 1 — Build Manual

> [!CAUTION]
> **Read HM-OPS-002 (Safety Manual) before beginning.** Li-Ion batteries and 36V systems can cause burns, fire, and electrical shock if mishandled.

---

## Required Tools

| Tool | Size | Purpose |
|:---|:---|:---|
| Hex Key Set | 2.5, 3, 4, 5mm | Frame bolts, motor plates |
| Torque Wrench | M5 range (4-8 Nm) | Critical fasteners |
| Wire Strippers | 10-22 AWG | Wiring harness |
| Crimping Tool | Ferrules + Ring Terminals | Power connections |
| Multimeter | DC Volts + Continuity | Verification |
| Heat Gun | — | Heat shrink, cable management |
| Drill + Bits | 5mm, 8mm | Mounting holes (if needed) |
| Thread Locker | Loctite 243 (Medium) | Anti-vibration bolts |

---

## Phase 1: Frame Assembly

### Step 1.1 — Cut Extrusion

| Part | Profile | Length | Qty |
|:---|:---|:---|:---|
| Side Rails | 2040 | 700mm | 2 |
| Crossbeams | 2040 | 240mm | 4 |

**Verification:** Measure each piece ±1mm. Deburr all cuts.

### Step 1.2 — Assemble Frame

1. Lay both 700mm rails parallel, 240mm apart (inside edge to inside edge).
2. Insert M5 T-Nuts into the rail channels (top and side slots).
3. Bolt crossbeams at front, rear, and two intermediate positions using M5 × 10mm BHCS.
4. **Torque:** 5 Nm for all frame bolts.
5. **Square Check:** Measure diagonals. Must be equal ±2mm.

### Step 1.3 — Install Shear Panels

1. Cut 3mm DiBond to 700mm × 120mm (2 panels).
2. Drill M5 clearance holes at 100mm intervals along the panel edges.
3. Bolt panels to the **outer face** of the side rails using M5 × 15mm + T-Nuts.
4. **Purpose:** Prevents frame parallelogramming under torque steer.

**✅ CHECKPOINT:** Frame is rigid, square, and panels are flush.

---

## Phase 2: Drivetrain Installation

### Step 2.1 — Install Motor Plates (NMT-MP-001)

> **Reference:** [HM-CAT-015](../02_CATALOG/HM-CAT-015_custom_parts.md) for plate drawing.

1. Attach one motor plate to each end of each side rail (4 total).
2. Bolt pattern: 4× M5 × 15mm into rail end-face tapped holes.
3. **Torque:** 6 Nm + **Loctite 243** (vibration-critical joint).
4. Verify the "Double-D" slot is oriented with flats **vertical**.

### Step 2.2 — Mount Hub Motors

1. Slide Ninebot G30 axle into the motor plate slot.
2. Apply axle nut and torque washer on the outboard side.
3. **Torque:** Per OEM spec (typically 25-30 Nm for M12 axle nuts).
4. **Spin Test:** Each wheel must rotate freely with no wobble or grinding.

**✅ CHECKPOINT:** All 4 wheels spin freely. Robot sits level on flat surface.

---

## Phase 3: Electrical — Power System

> **Reference:** [HM-DWG-001](../06_ENGINEERING/01_SCHEMATICS/HM-DWG-001_wiring_harness.md)

### Step 3.1 — Install Main Fuse

1. Bolt 60A MIDI Fuse Holder to the Apache 3800 case base (near battery bay).
2. Connect Battery XT90-S (+) → Fuse Input with **10 AWG Red** wire.
3. Connect Fuse Output → Distribution Bus Bar with **10 AWG Red** wire.
4. **Wire Length:** Keep battery-to-fuse run **<200mm** (CDR-13).

### Step 3.2 — Wire Distribution Bus

1. Mount positive and negative bus bars inside the Apache 3800 case base.
2. Connect Battery (-) to Negative Bus Bar with **10 AWG Black** wire.
3. Wire bus bar outputs per HM-DWG-001 Section 2A.

### Step 3.3 — Install DC-DC Converter (CDR-8)

1. Mount DDR-60L-15 to the case base with M3 screws.
2. Connect Input V+ and V- from Distribution Bus (16 AWG).
3. **Trim Output:** Adjust trim pot to **17.0V** using multimeter.
4. Connect output to Odroid H4 Ultra DC barrel jack (5.5×2.1mm).

### Step 3.4 — Wire Safety Loop

1. Wire E-Stop (NC) in series with the Relay Module output.
2. Connect Relay NO contact to Contactor Coil (+).
3. Connect Contactor Coil (-) to GND.
4. Connect Arduino D2 to Relay Module Signal input.
5. **Test:** Press E-Stop → Contactor should open (click sound). Release → No change until Arduino asserts D2.

### Step 3.5 — Wire VESCs

*Repeat for all 4 VESCs:*
1. Connect VESC V+ to Switched Power (Contactor Load Side) via 14 AWG Red.
2. Connect VESC GND to Negative Bus Bar via 14 AWG Black.
3. Connect 3× Motor Phase Wires (match wire colors, or detect in VESC Tool).
4. Connect Hall Sensor Cable (JST-PH 6-pin).

### Step 3.6 — Wire CAN Bus (CDR-7)

1. Daisy-chain CAN-H and CAN-L from USB-CAN adapter → VESC1 → VESC2 → VESC3 → VESC4.
2. Use **Shielded Twisted Pair** (STP).
3. Ground shield at USB-CAN adapter end **only**.
4. Solder **120Ω resistor** across CAN-H and CAN-L at VESC4 (end of chain).

**✅ CHECKPOINT:** Multimeter shows battery voltage at bus bars. DC-DC outputs 17.0V. E-Stop kills contactor.

---

## Phase 4: Electronics Integration

### Step 4.1 — Prepare Thermal Deck

1. Cut 6mm aluminum plate to Apache 3800 lid dimensions (378 × 268mm).
2. Machine/drill copper pedestal mounting pocket (for Odroid CPU contact).
3. Mount VESCs (×4) inverted on the underside of the plate using M3 screws.
4. Mount Odroid H4 Ultra inverted — CPU die contacts copper pedestal via thermal pad.

### Step 4.2 — Mount Case on Frame

1. Install 4× M5 Rubber Bobbins on the 2040 rail top slots.
2. Place Apache 3800 base on the bobbins.
3. Secure with M5 nuts through bobbin studs.
4. **Bounce Test:** Case should have ~2mm of give when pressed. This is the vibration isolation (CDR-3).

### Step 4.3 — Route External Cables

1. Install cable glands (PG7/PG9) in the Apache 3800 case wall.
2. Route motor phase wires, CAN bus, and sensor cables through glands.
3. Seal each gland finger-tight + ¼ turn with wrench.
4. **IP65 Check:** No cable should be pinched or unsealed.

**✅ CHECKPOINT:** Close case lid (Thermal Deck). All cables routed. No pinch points.

---

## Phase 5: First Power-On

> [!WARNING]
> **Follow HM-OPS-002 (Safety Manual) Section 3 — First Power-On Protocol.**

1. Ensure E-Stop is **pressed** (locked out).
2. Connect battery XT90-S.
3. Verify: Red LED = ON (Safety Active).
4. Use multimeter to check:
   - Bus Bar Voltage: 36-42V DC
   - DC-DC Output: 17.0V ± 0.2V
   - CAN Bus Resistance: ~60Ω (end-to-end, both terminators)
5. Release E-Stop. Assert Arduino watchdog. Contactor should close (click).
6. Verify: Green LED = OFF (ROS not running yet). Yellow LED behavior = TBD.
7. Power on Odroid. Wait for boot. SSH in.

**✅ CHECKPOINT: FIRST LIGHT.** Robot is alive.

---

## Appendix: Torque Specification Table

| Fastener | Location | Torque | Thread Lock |
|:---|:---|:---|:---|
| M5 × 10 BHCS | Frame crossbeams | 5 Nm | None |
| M5 × 15 BHCS | Motor plates to rails | 6 Nm | Loctite 243 |
| M5 × 15 BHCS | Shear panels | 5 Nm | None |
| M5 Bobbin Nut | Case isolation mounts | 4 Nm | Nyloc |
| M3 × 8 SHCS | VESC to Thermal Deck | 1.5 Nm | None |
| M3 × 8 SHCS | Odroid to Thermal Deck | 0.8 Nm | None |
| M12 Axle Nut | Motor axle to plate | 25 Nm | Nyloc |
