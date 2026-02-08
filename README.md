# NOMAD-T

**Autonomous Off-Road UGV — Engineering Design Package**

A field-hardened, 4WD skid-steer robot built from mass-produced scooter components. Designed for outdoor autonomy in unstructured terrain.

> **Architecture Lock (Rev 4.0):** Rigid 2040 frame, 4× Ninebot G30 hub motors, 36V Li-Ion, Odroid H4 Ultra.

---

## Versions

| Version | Codename | Purpose | Motors | Budget | Status |
|:---|:---|:---|:---|:---|:---|
| **Mk.0 "Scrapper"** | Alpha | Cheap pavement testbed | 4× Hoverboard 6.5" | ~$460 | **ACTIVE** |
| **Mk.1 "Nomad"** | Release | Field-hardened, weatherproof | 4× Ninebot G30 | ~$1,500 | Design Complete |

---

## Key Specifications

| Parameter | Value |
|:---|:---|
| **Drivetrain** | 4× Ninebot Max G30 Rear Hub Motors (Direct Drive) |
| **Frame** | 2040 V-Slot Aluminum Extrusion, 700 × 320mm |
| **Wheels** | 10" G30 Pneumatic (60/70-6.5), Tubeless |
| **Suspension** | None (Rigid) — Pneumatic tires provide damping |
| **Compute** | Odroid H4 Ultra (Intel i3-N305, 8C, DDR5) |
| **Sensors** | RPLiDAR C1, OAK-D Lite, 4× Sharp IR, BNO085 IMU |
| **Power** | 10S3P Li-Ion (36V), DDR-60L-15 DC-DC (17V Logic) |
| **Safety** | 60A MIDI Fuse, E-Stop, Arduino Watchdog, Contactor |
| **Enclosure** | Apache 3800 (IP65) on Vibration Isolation Bobbins |
| **Weight** | ~19 kg |
| **Est. Cost** | ~$1,600 |

---

## Project Structure

```
00_ALPHA/          Mk.0 "Scrapper" prototype specs & BOM
01_PROTOCOLS/      Documentation standards & naming conventions (HM-PRO)
02_CATALOG/        Mk.1 component specs, BOMs, trade studies (HM-CAT)
03_OPERATIONS/     Build guides, safety manual, checklists (HM-OPS)
04_ASSETS/         Images, renders, CAD models (HM-AST)
05_RESEARCH/       Analysis, whitepapers, CDR findings (HM-RES)
06_ENGINEERING/    Schematics, tools, source code (HM-DWG/SRC)
```

---

## Document Index

### Alpha (Mk.0 "Scrapper")
| ID | Title |
|:---|:---|
| HM-ALPHA-001 | [Alpha Prototype Spec](00_ALPHA/HM-ALPHA-001_spec.md) |
| HM-ALPHA-002 | [Alpha BOM / Shopping List](00_ALPHA/HM-ALPHA-002_bom.md) |

### Protocols
| ID | Title |
|:---|:---|
| HM-PRO-001 | [Documentation Standards](01_PROTOCOLS/HM-PRO-001_doc_standards.md) |

### Specifications (Catalog)
| ID | Title |
|:---|:---|
| HM-CAT-001 | [Master Design (Phase 1)](02_CATALOG/HM-CAT-001_master_design.md) |
| HM-CAT-002 | [Shopping List](02_CATALOG/HM-CAT-002_shopping_list.md) |
| HM-CAT-003–008 | Sensor Datasheets (OAK-D, PZEM, IR, LiDAR, GNSS, IMU) |
| HM-CAT-009 | [Brain Core (Odroid H4 Ultra)](02_CATALOG/HM-CAT-009_brain_core_compute.md) |
| HM-CAT-010 | [Drivetrain (G30 Hub Motors)](02_CATALOG/HM-CAT-010_drivetrain_spec.md) |
| HM-CAT-011 | [Component Trade Studies](02_CATALOG/HM-CAT-011_cots_selection.md) |
| HM-CAT-012 | [Master Integration (Apache 3800)](02_CATALOG/HM-CAT-012_master_integration.md) |
| HM-CAT-013 | [Frame (Rigid 2040)](02_CATALOG/HM-CAT-013_frame_suspension.md) |
| HM-CAT-014 | [Electrical System (36V)](02_CATALOG/HM-CAT-014_electrical_system.md) |
| HM-CAT-015 | [Custom Parts (Motor Plate NMT-MP-001)](02_CATALOG/HM-CAT-015_custom_parts.md) |
| HM-CAT-016 | [Odroid H4 Ultra Datasheet](02_CATALOG/HM-CAT-016_odroid_h4_ultra_datasheet.md) |

### Operations
| ID | Title |
|:---|:---|
| HM-OPS-001 | [Build Manual](03_OPERATIONS/HM-OPS-001_build_manual.md) |
| HM-OPS-002 | [Safety Manual](03_OPERATIONS/HM-OPS-002_safety_manual.md) |
| HM-OPS-003 | [Pre-Flight Checklist](03_OPERATIONS/HM-OPS-003_preflight_checklist.md) |

### Research
| ID | Title |
|:---|:---|
| HM-RES-001 | [Nomad-T Concept Analysis](05_RESEARCH/HM-RES-001_nomad_t_analysis.md) |
| HM-RES-002 | [UGV Whitepaper](05_RESEARCH/HM-RES-002_ugv_whitepaper.md) |
| HM-RES-003 | [Pre-Build Research Questions (Rev 4.0)](05_RESEARCH/HM-RES-003_pre_build_research_questions.md) |
| HM-RES-004 | [Case Selection Study](05_RESEARCH/HM-RES-004_case_selection_study.md) |
| HM-RES-005 | [Critical Design Review (13 CDRs)](05_RESEARCH/HM-RES-005_critical_design_review.md) |
| HM-RES-006 | [Hub Motor Trade Study](05_RESEARCH/HM-RES-006_hub_motor_trade_study.md) |

### Engineering
| ID | Title |
|:---|:---|
| HM-DWG-001 | [Wiring Harness Schematic](06_ENGINEERING/01_SCHEMATICS/HM-DWG-001_wiring_harness.md) |

---

## Status

**Phase 1 Hardware Design: COMPLETE**
- All 13 Critical Design Reviews resolved
- Wiring harness schematic issued
- Documentation synchronized
- Ready for procurement and assembly
