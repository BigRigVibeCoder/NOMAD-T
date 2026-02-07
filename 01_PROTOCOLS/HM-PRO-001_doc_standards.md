# Protocol: HiveMind Documentation Standard
**ID:** HM-PRO-001
**Status:** ACTIVE
**Classification:** OPEN INTERNAL

## 1. Purpose
To establish a high-assurance, "Deep Tech" documentation framework that ensures traceability, version control compatibility, and ease of cognitive retrieval for the Nomad-T project.

## 2. Directory Structure (Johnny Decimal + Diataxis)
The project structure determines the *type* of information stored.

*   **01_PROTOCOLS (Reference - Laws)**
    *   Standards, conventions, and defining rigid rules.
    *   *Example:* This document (`HM-PRO-001`).
*   **02_CATALOG (Reference - Specs)**
    *   System Specifications, Bill of Materials (BOM), and "Recipes".
    *   *Example:* Master Design Specs, Shopping Lists.
*   **03_OPERATIONS (How-to - Guides)**
    *   Step-by-step instructions, assembly guides, and tutorials.
    *   *Example:* "How to mount the motor", "Wiring Guide".
*   **04_ASSETS (Media)**
    *   Binary assets, Images, CAD files, Drawings.
*   **05_RESEARCH (Explanation)**
    *   Whitepapers, Trade Studies, Analysis, and theoretical groundwork.

## 3. Identification System (HM-ID-XXX)
All documentation files must have a unique identifier in their filename to ensure traceability despite refactors.

**Format:** `HM-[TYPE]-[SEQ]_[snake_case_title].md`

### Types
*   **PRO:** Protocol (Standards, Rules)
*   **CAT:** Catalog (Specs, Parts)
*   **OPS:** Operations (Guides, Manuals)
*   **RES:** Research (Theory, Analysis)
*   **AST:** Asset (Images, Models) - *Mandatory for release candidates*

### Sequence
*   3-Digit Integer (e.g., `001`, `002`).
*   Sequences are unique *per Type*.

## 4. Maintenance
*   **Docs-as-Code:** All docs are stored in the repo with the code/designs.
*   **Traceability:** Changes to design must reference the Protocol or Catalog ID they affect.
*   **Assets:** All assets must be numbered (HM-AST-XXX) to be referenced in specs.
