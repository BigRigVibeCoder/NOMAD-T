---
ID: HM-CAT-009
Status: CRITICAL PATH — Order Immediately
Date: February 2026
---

# Phase 0 Procurement: The Brain Core

**Objective:** Secure the computational heart of the robot.

---

## 1. The Core (Compute)

| Field | Value |
|:---|:---|
| **Item** | ODROID-H4 Ultra |
| **CPU** | Intel Core i3-N305 (8-Core, 3.8GHz Turbo) |
| **GPU** | 32 EUs Intel UHD Graphics |
| **Vendor** | Ameridroid (US) / Hardkernel (Global) |
| **Cost** | ~$230 |
| **Why** | Only SBC with x86 + AVX2 instructions for local LLM inference |

---

## 2. Memory (RAM) — MAXED OUT

| Field | Value |
|:---|:---|
| **Item** | Crucial 48GB DDR5 5600MHz CL46 SO-DIMM |
| **Model** | CT48G56C46S5 (single stick) |
| **Cost** | ~$140 |
| **Constraint** | Maximizes LLM context window |

---

## 3. Storage (SSD) — CONFIRMED

| Field | Value |
|:---|:---|
| **Item** | TEAMGROUP MP44L |
| **Model (1TB)** | TM8FPK001T0C101 |
| **Model (2TB)** | TM8FPK002T0C101 |
| **Cost** | ~$70–$120 |

> [!IMPORTANT]
> **Thermal Note:** The Odroid H4 Ultra M.2 slot supports PCIe Gen 3.0 x4 (~3,500 MB/s). This Gen 4 drive is backward compatible. The MP44L uses TLC NAND and is **DRAM-less** — critical for our sealed enclosure to prevent thermal throttling. Best performance-to-heat ratio available.

---

## 4. Network (WiFi 6E)

| Field | Value |
|:---|:---|
| **Item** | Intel AX210 WiFi 6E M.2 Card (Desktop Kit) |
| **Note** | Must include IPEX4 pigtails and antennas |

---

## 5. Case & Cooling

| Field | Value |
|:---|:---|
| **Case** | ODROID-H4 Case Type 3 |
| **Fan** | Noctua NF-A9x14 HS-PWM chromax.black.swap (slim 14mm) |

---

## 6. Power Supply (Brain Only)

| Field | Value |
|:---|:---|
| **Adapter** | Dtk 19V 4.74A 90W Laptop Charger |
| **Tip Adapter** | 5.5x2.5mm Female → 5.5x2.1mm Male |

---

## 7. Shopping Checklist

| Vendor | Component | Spec Check | Est. Price |
|:---|:---|:---|:---|
| Ameridroid | Odroid H4 Ultra | Verify "Ultra" (i3-N305) | $230.00 |
| Ameridroid | Case Type 3 | Check: "Type 3" | $15.00 |
| Amazon | Crucial 48GB DDR5 | 48GB Single Stick | $140.00 |
| Amazon | TEAMGROUP MP44L | PN: TM8FPK001T0C101 | ~$70–$120 |
| Amazon | Intel AX210 Kit | Includes Antennas | $25.00 |
| Amazon | Noctua NF-A9x14 PWM | 4-Pin PWM | $20.00 |
| Amazon | Dtk 19V 4.74A PSU | 5.5x2.5mm Plug | $20.00 |
| Amazon | DC Adapter Tip | 2.5mm → 2.1mm | $7.00 |
| | | **TOTAL** | **~$530–$580** |

---

## 8. Next Steps (While Shipping)

1. **Download OS:** Get the [Ubuntu 24.04 LTS Server ISO](https://ubuntu.com/download/server).
2. **Prepare Installer:** Flash the ISO to a USB stick using [BalenaEtcher](https://etcher.balena.io/).
