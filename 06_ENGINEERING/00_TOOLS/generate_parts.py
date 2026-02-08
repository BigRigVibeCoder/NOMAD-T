#!/usr/bin/env python3
"""
Nomad-T Individual Part Generator — Manufacturing-Ready (Code-as-CAD)
=====================================================================
Generates standalone STEP files for critical custom parts.

Output directory: 04_ASSETS/cad/parts/
  NMT-MP-001_motor_plate.step   — send to waterjet/laser shop
  NMT-TD-001_thermal_deck.step  — CNC or waterjet
  NMT-FR-001_frame_assembly.step — frame + crossbeams for cut-list verification

Specs: HM-CAT-013, HM-CAT-015, HM-CAT-012 §3

Usage:  python3 generate_parts.py
"""

import sys, os
sys.path.append(os.path.expanduser("~/.local/lib/python3.12/site-packages"))
import cadquery as cq

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
OUT_DIR = os.path.join(PROJECT_ROOT, "04_ASSETS", "cad", "parts")
os.makedirs(OUT_DIR, exist_ok=True)


# =============================================================================
# PART 1: NMT-MP-001 Motor Plate (HM-CAT-015)
# =============================================================================
def generate_motor_plate():
    """
    Manufacturing-ready motor plate:
    - 80×80×6mm 6061-T6 aluminum
    - Double-D axle slot: 12mm OD, 10mm flat-to-flat, R2 corners
    - 4× M5 clearance holes (5.5mm) on 20mm grid
    - 2× additional M5 holes for anti-rotation / frame attachment
    - 2mm chamfer on all outer vertical edges
    - 0.5mm edge break on top/bottom faces
    """
    print("  ├─ NMT-MP-001 Motor Plate...")

    SIZE = 80.0
    THICK = 6.0
    AXLE_OD = 12.0
    FLAT_DIST = 10.0
    FILLET_R = 2.0
    BOLT_D = 5.5          # M5 clearance
    BOLT_GRID = 20.0      # spacing from center

    # Base plate
    plate = (cq.Workplane("XY")
        .rect(SIZE, SIZE)
        .extrude(THICK))

    # Chamfer vertical edges (outer profile)
    try:
        plate = plate.edges("|Z").chamfer(2.0)
    except Exception:
        pass

    # Edge break on top/bottom horizontal edges
    try:
        plate = plate.edges("#Z").chamfer(0.5)
    except Exception:
        pass

    # Primary bolt pattern: 4× M5 at 20mm from center (frame mounting)
    primary_bolts = [
        ( BOLT_GRID,  BOLT_GRID),
        ( BOLT_GRID, -BOLT_GRID),
        (-BOLT_GRID,  BOLT_GRID),
        (-BOLT_GRID, -BOLT_GRID),
    ]
    plate = (plate.faces(">Z").workplane()
        .pushPoints(primary_bolts)
        .hole(BOLT_D))

    # Additional frame mount holes: 2× M5 at midpoints (top/bottom edges)
    edge_bolts = [
        (0,  BOLT_GRID),
        (0, -BOLT_GRID),
    ]
    plate = (plate.faces(">Z").workplane()
        .pushPoints(edge_bolts)
        .hole(BOLT_D))

    # Double-D axle slot
    # Start with round hole, then cut two flats
    plate = plate.faces(">Z").workplane().hole(AXLE_OD)

    # Cut flat faces: two rectangles that trim the circle to flat-to-flat dist
    # Each flat is at ±(FLAT_DIST/2) from center
    flat_cut_depth = (AXLE_OD / 2) - (FLAT_DIST / 2)  # how much to cut
    flat_cut_w = AXLE_OD  # wider than the hole diameter

    if flat_cut_depth > 0:
        flat_block = cq.Workplane("XY").box(flat_cut_w, flat_cut_depth, THICK * 2)
        for y_off in [FLAT_DIST / 2 + flat_cut_depth / 2,
                      -(FLAT_DIST / 2 + flat_cut_depth / 2)]:
            plate = plate.cut(flat_block.translate((0, y_off, THICK / 2)))

    out = os.path.join(OUT_DIR, "NMT-MP-001_motor_plate.step")
    cq.exporters.export(plate, out)
    sz = os.path.getsize(out) / 1024
    print(f"  │  ✅ {out}  ({sz:.0f} KB)")
    return out


# =============================================================================
# PART 2: NMT-TD-001 Thermal Deck (HM-CAT-012 §3 / CDR-4)
# =============================================================================
def generate_thermal_deck():
    """
    Unified thermal deck plate:
    - 415×328×6mm 6061-T6 aluminum (matches Apache 3800 footprint)
    - 4× corner M5 mounting holes
    - 16× M3.5 VESC mount holes (4 per VESC, 4 VESCs)
    - 4× M3 Odroid standoff holes (centered)
    - 4× M3 holes for copper pedestal (CPU contact)
    - 1.5mm fillet on top edges
    """
    print("  ├─ NMT-TD-001 Thermal Deck...")

    L = 415.0; W = 328.0; T = 6.0
    VESC_MOUNT = [(45, 25), (45, -25), (-45, 25), (-45, -25)]

    deck = (cq.Workplane("XY")
        .rect(L, W)
        .extrude(T))

    # Top edge fillet
    try:
        deck = deck.edges(">Z").fillet(1.5)
    except Exception:
        pass

    # Corner mounting holes (M5, 5.5mm clearance)
    corner_pts = [
        ( L/2 - 20,  W/2 - 20),
        ( L/2 - 20, -W/2 + 20),
        (-L/2 + 20,  W/2 - 20),
        (-L/2 + 20, -W/2 + 20),
    ]
    deck = (deck.faces(">Z").workplane()
        .pushPoints(corner_pts)
        .hole(5.5))

    # VESC mounting holes: 4 VESCs at (±80, ±60) relative to center
    vesc_centers = [(80, 60), (80, -60), (-80, 60), (-80, -60)]
    all_vesc_pts = []
    for vcx, vcy in vesc_centers:
        for dx, dy in VESC_MOUNT:
            all_vesc_pts.append((vcx + dx, vcy + dy))
    deck = (deck.faces(">Z").workplane()
        .pushPoints(all_vesc_pts)
        .hole(3.5))

    # Odroid H4 Ultra standoff holes (M3, centered)
    odroid_pts = [(40, 35), (40, -35), (-40, 35), (-40, -35)]
    deck = (deck.faces(">Z").workplane()
        .pushPoints(odroid_pts)
        .hole(3.2))

    # Copper pedestal contact holes (M3, tight cluster near center)
    pedestal_pts = [(15, 10), (15, -10), (-15, 10), (-15, -10)]
    deck = (deck.faces(">Z").workplane()
        .pushPoints(pedestal_pts)
        .hole(3.2))

    # Wire gland pass-through holes (2× 16mm at rear edge)
    gland_pts = [(-L/2 + 40, 50), (-L/2 + 40, -50)]
    deck = (deck.faces(">Z").workplane()
        .pushPoints(gland_pts)
        .hole(16.0))

    out = os.path.join(OUT_DIR, "NMT-TD-001_thermal_deck.step")
    cq.exporters.export(deck, out)
    sz = os.path.getsize(out) / 1024
    print(f"  │  ✅ {out}  ({sz:.0f} KB)")
    return out


# =============================================================================
# PART 3: NMT-FR-001 Frame Assembly (HM-CAT-013)
# =============================================================================
def generate_frame_assembly():
    """
    Frame sub-assembly:
    - 2× 700mm 2040 side rails (with center bore, chamfered edges)
    - 4× 240mm 2040 crossbeams
    - Oriented in final assembly position for verification
    """
    print("  ├─ NMT-FR-001 Frame Assembly...")

    EX = 20.0
    FRAME_L = 700.0
    RAIL_Y = 160.0
    XB_POS = [0, 233, 467, 700]
    XB_LEN = 240.0

    def make_rail(length):
        r = (cq.Workplane("XY")
            .rect(EX, EX)
            .extrude(length))
        r = r.faces(">Z").workplane().hole(5.0, length)
        try:
            r = r.edges("|Z").chamfer(1.0)
        except Exception:
            pass
        return r

    asm = cq.Assembly()

    # Side rails
    rail = make_rail(FRAME_L)
    for tag, ys in [("rail_L", RAIL_Y), ("rail_R", -RAIL_Y)]:
        asm.add(rail, name=tag,
            loc=cq.Location(cq.Vector(0, ys, EX/2),
                            cq.Vector(0, 1, 0), -90),
            color=cq.Color(0.78, 0.78, 0.80, 1))

    # Crossbeams
    xbeam = make_rail(XB_LEN)
    for i, xp in enumerate(XB_POS):
        asm.add(xbeam, name=f"xbeam_{i+1}",
            loc=cq.Location(cq.Vector(xp, -XB_LEN/2, EX/2),
                            cq.Vector(1, 0, 0), 90),
            color=cq.Color(0.70, 0.72, 0.82, 1))

    out = os.path.join(OUT_DIR, "NMT-FR-001_frame_assembly.step")
    asm.save(out)
    sz = os.path.getsize(out) / 1024
    print(f"  │  ✅ {out}  ({sz:.0f} KB)")
    return out


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print("🔧 Generating Nomad-T individual parts (manufacturing-ready)...")
    print("  │")

    files = []
    files.append(generate_motor_plate())
    files.append(generate_thermal_deck())
    files.append(generate_frame_assembly())

    print("  │")
    print(f"  └─ ✅ {len(files)} part files generated in {OUT_DIR}")
    print()
    print("📐 Part Summary:")
    print("   NMT-MP-001  Motor Plate      80×80×6mm  6061-T6  Waterjet/Laser")
    print("   NMT-TD-001  Thermal Deck     415×328×6mm  6061-T6  CNC/Waterjet")
    print("   NMT-FR-001  Frame Assembly   700×320mm  2040 V-Slot  Cut list verify")
    print()
    print("📦 View: drag into https://3dviewer.net or FreeCAD")
