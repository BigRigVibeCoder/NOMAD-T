---
ID: HM-CAT-016
Status: ACTIVE
Date: 2026-02-07
Role: OEM Datasheet Extract — Odroid H4 Ultra
Source: Hardkernel "ODROID H4 Series Introduction" PDF (2024)
Linked: HM-CAT-009
---

# Odroid H4 Ultra — OEM Specification Extract

> [!NOTE]
> This document extracts the **engineering-critical specifications** from the official Hardkernel datasheet PDF. Full benchmarks and marketing content are omitted. Refer to the original PDF for complete data.

---

## 1. Processor

| Spec | Value |
|:---|:---|
| **CPU** | Intel Core i3 Processor N305 |
| **Codename** | Alder Lake-N |
| **Microarchitecture** | Gracemont |
| **Cores / Threads** | 8C / 8T |
| **Cache** | 6 MB |
| **AVX2** | Yes |
| **TDP (Balanced Mode)** | **15W** |
| **Single-Thread Burst** | **3.8 GHz** |
| **All-Core Boost (UP Mode)** | **3.0 GHz** |
| **Tj (Max Junction Temp)** | ~105°C (throttle begins at Tj − 5°C) |

---

## 2. Power Consumption (MEASURED by Hardkernel)

> [!CAUTION]
> **These are the authoritative numbers.** All thermal design calculations must use these values, NOT the 65W figure used in earlier analysis.

| Condition | Power Draw |
|:---|:---|
| Power Off | 0.2W |
| Suspend to RAM | 0.9–1.2W |
| Headless Idle (ASPM Auto) | **2.8W** |
| Desktop GUI Idle | **6.2W** |
| 4K YouTube Playback | 15.4W |
| WebGL Demo | 16.4W |
| CPU Stress (Balanced, PL4=30000) | **20.5W** |
| CPU + GPU Stress (Balanced) | **19–22W** |
| WebGL + CPU Stress | 21.6W |
| **UP Mode Max (PL4=0, active load)** | **34+W** |
| UP Mode Idle | Same as Balanced idle |

**Key insight:** In Unlimited Performance mode, idle power is identical to Balanced. The 34W max occurs ONLY during sustained all-core turbo boost under load.

---

## 3. Thermal Behavior

| Parameter | Value |
|:---|:---|
| Passive heatsink (Balanced mode) | **Sufficient — no fan needed** |
| Active cooling (UP mode) | Fan required to prevent throttle |
| Fan temp reduction | **25–30°C** below passive-only |
| Throttle behavior | CPU auto-throttles ~5°C below Tj max |
| Fan connector | 12V PWM 4-pin (standard PC) |
| Compatible fans | 92×15mm slim OR 92×25mm thick |

> [!IMPORTANT]
> **Hardkernel explicitly states:** "You do not need a fan in Balanced mode." The stock passive heatsink is designed to handle 15W TDP without active cooling. UP mode (34W) requires a fan to avoid thermal throttling.

---

## 4. Physical Dimensions

| Parameter | Value |
|:---|:---|
| **Board dimensions** | **120mm × 120mm** (4.7" × 4.7") |
| **Board + heatsink height** | **~47mm** |
| **Form factor change** | +10mm per side vs H3 series (was 110×110mm) |

> [!WARNING]
> HM-CAT-009 and HM-CAT-012 reference 110×110mm board dimensions — those are the H3 series. The H4 Ultra is **120×120mm**. The Unified Thermal Deck plate must accommodate this larger footprint.

---

## 5. Power Input

| Parameter | Value |
|:---|:---|
| DC Jack | 5.5mm outer / 2.1mm inner (positive center) |
| **Input voltage range** | **14V – 20V** |
| Recommended PSU (no HDDs) | 15V / 4A (60W) |
| Recommended PSU (with HDDs) | 19V / 7A (133W) |

**For Nomad-T:** Our DC-DC targets 19V output from 36V battery. The Odroid accepts 14–20V. At 19V, current draw at max load (34W UP) = 34/19 = **1.8A.** At 22W balanced stress = **1.16A.** Wire gauge requirements are minimal.

---

## 6. Memory

| Parameter | Value |
|:---|:---|
| Slots | 1× DDR5 SO-DIMM (single channel) |
| Speed | Up to 4800 MT/s (5600 MT/s modules run at 4800) |
| **Max validated** | **48 GB** (DDR5 SO-DIMM) |
| DDR4 compatible? | **No** — DDR5 only |

---

## 7. Storage

| Parameter | Value |
|:---|:---|
| M.2 NVMe | 1× PCIe Gen 3 x4 (NGFF-2280) |
| M.2 SATA | Compatible (uses 1 PCIe lane) |
| SATA III | 4 ports (H4 Ultra) |
| eMMC | 1× socket (bootable) |

---

## 8. I/O Ports

| Port | Count | Notes |
|:---|:---|:---|
| USB 3.0 | 2 | |
| USB 2.0 | 2 + 3 (on expansion header) | |
| 2.5 GbE Ethernet | 2 | Intel I226-V |
| HDMI 2.0 | 1 | 4K@60Hz |
| DisplayPort 1.2 | 2 | 4K@60Hz each |
| Audio out/in | 3.5mm jacks | |
| SPDIF out | 1 | |

---

## 9. Expansion Header (24-pin, 2.54mm pitch)

| Signal | Count |
|:---|:---|
| I2C | 2× (SCL/SDA, 3.3V IO) |
| UART | 1× (TXD/RXD/RTS/CTS, 3.3V IO) |
| USB 2.0 | 3× |
| HDMI-CEC | 1× |
| External Power Button | 1× |
| DC 5V | 1× |
| DC 3.3V | 1× |
| GND | 5× |

---

## 10. Other Features

| Feature | Detail |
|:---|:---|
| **Dual BIOS** | Yes (H4 Ultra) — backup via jumper |
| **TPM 2.0** | fTPM enabled |
| **Certifications** | FCC / CE / KC / RoHS |
| **Price** | $239 (board only) |

---

## 11. Connector Heights (Critical for Thermal Deck)

The board's tallest components are the I/O connectors on the rear edge:

| Component | Approximate Height |
|:---|:---|
| RJ45 Ethernet × 2 (stacked) | **~15mm** |
| USB 3.0 × 2 | **~15mm** |
| USB 2.0 × 2 | **~13mm** |
| HDMI 2.0 | **~11mm** |
| DisplayPort × 2 | **~10mm** |
| DC Jack | **~11mm** |
| CPU Die (exposed) | **~1mm** above PCB |

**Gap to bridge:** When board is inverted, the Ethernet/USB jacks create a **~14mm gap** between the CPU die and the cooling plate. This is why the Unified Thermal Deck requires a **15mm copper thermal pedestal** (see RQ-5.1 in HM-RES-003).

---

*Extracted from Hardkernel official PDF, "Introducing the ODROID-H4, H4+ and H4 Ultra" (April 2024)*
*Catalog document prepared: 2026-02-07*
