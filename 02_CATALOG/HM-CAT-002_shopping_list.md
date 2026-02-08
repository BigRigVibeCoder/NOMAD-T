---
ID: HM-CAT-002
Status: ACTIVE
Role: Master Shopping List (Phase 1)
Date: 2026-02-07
Linked: HM-CAT-001, HM-CAT-012, HM-CAT-014
---

# Nomad-T Phase 1 Shopping List

> [!NOTE]
> **VERIFIED BOM.** This list aligns with the "Rigid 2040 + G30 Hub Motor" architecture. Costs are estimates.

## 1. Drivetrain & Structure (The "Physical" Bot)

> [!TIP]
> **Sourcing Rule:** AliExpress is fine for all structural/hardware parts. Only the G30 motors require OEM sourcing (CDR-1 "Golden Unit" rule).

| Item | Spec | Qty | Est. Cost | Source |
| :--- | :--- | :--- | :--- | :--- |
| **Hub Motors** | Ninebot Max G30 (Gen 2) **Rear** | 4 | $240 ($60 ea) | eBay / MSP (OEM Only) |
| **Frame Rails** | 2040 V-Slot Extrusion (700mm) | 2 | $12 | AliExpress |
| **Crossbeams** | 2040 V-Slot Extrusion (1000mm stick, cut to 240mm) | 1 | $6 | AliExpress |
| **Chassis Main Case** | Apache 3800 (Black) | 1 | $40 | Harbor Freight |
| **Shear Panels** | 3mm DiBond / ACP Sheet (12" x 24") | 2 | $20 | AliExpress / Amazon |
| **Vibration Mounts** | M5 Rubber Bobbin (Shore 40A) | 4 | $5 | AliExpress |
| **Motor Plates** | 6mm Aluminum (Laser/Waterjet Svc) | 4 | $50 | SendCutSend |

**Subtotal: ~$373**

## 2. Power System (36V)

| Item | Spec | Qty | Est. Cost | Source |
| :--- | :--- | :--- | :--- | :--- |
| **Battery** | 36V 10S3P (or 10S4P) Li-Ion | 1 | $120 | Battery Hookup / M365 |
| **Main Fuse** | 60A MIDI Fuse + Holder | 1 | $10 | Amazon / Auto |
| **Connectors** | XT90-S (Anti-Spark) Pair | 2 | $8 | Amazon |
| **DC-DC Converter** | Mean Well DDR-60L-15 | 1 | $35 | DigiKey / Mouser |
| **Wire** | 10 AWG Silicone (Red/Black) | 10ft | $15 | Amazon |

**Subtotal: ~$188**

## 3. Control & Safety

| Item | Spec | Qty | Est. Cost | Source |
| :--- | :--- | :--- | :--- | :--- |
| **VESC** | Flipsky 75100 (Aluminum PCB) | 4 | $260 ($65 ea) | Flipsky / Amazon |
| **E-Stop** | N.C. Mushroom Button | 1 | $10 | Amazon |
| **Relay Module** | 5V Relay (for Watchdog) | 1 | $5 | Amazon |
| **Contactor** | 12V Coil / 100A DC | 1 | $25 | Amazon / Auto |
| **Brake Resistor** | 200W 8Ω Chassis Mount | 1 | $15 | Amazon |

**Subtotal: ~$315**

## 4. Compute & Sensors (The "Brains")

| Item | Spec | Qty | Est. Cost | Source |
| :--- | :--- | :--- | :--- | :--- |
| **SBC** | Odroid H4 Ultra | 1 | $239 | Ameridroid |
| **RAM** | 16GB DDR5 SO-DIMM | 1 | $45 | Amazon |
| **SSD** | 256GB NVMe M.2 | 1 | $30 | Amazon |
| **LiDAR** | RPLiDAR C1 | 1 | $150 | RobotShop |
| **Camera** | OAK-D Lite | 1 | $150 | Luxonis |
| **Interface** | USB-CAN Adapter (TouCAN/Poly) | 1 | $30 | Amazon |

**Subtotal: ~$644**

## 5. Hardware & Misc

| Item | Spec | Qty | Est. Cost | Source |
| :--- | :--- | :--- | :--- | :--- |
| **M5 Screws** | M5x10, M5x15, M5x40 (Box) | 1 | $6 | AliExpress |
| **T-Nuts** | M5 Drop-in for 2020/2040 | 50 | $4 | AliExpress |
| **Thermal Pad** | 100mm x 100mm (0.5mm) | 1 | $3 | AliExpress |
| **Cable Glands** | PG7 / PG9 Assortment | 1 | $4 | AliExpress |
| **Corner Brackets** | 2040 Interior L-Bracket | 20 | $6 | AliExpress |

**Subtotal: ~$23**

---

## Grand Total: ~$1,500 USD

*Note: AliExpress sourcing saves ~$100 vs domestic. Budget includes shipping buffer. Well under $2,000 target.*
