#!/usr/bin/env python3
"""
Nomad-T Chassis Generator v5 — Phase 1 "Skid-Steer" (Code-as-CAD)
===================================================================
Generates a STEP assembly matching the APPROVED design:
  HM-CAT-001  Master Design       HM-CAT-012  Integration
  HM-CAT-010  Drivetrain          HM-CAT-013  Frame (Rigid)
  HM-CAT-014  Electrical          HM-CAT-015  Custom Parts (NMT-MP-001)

Coordinate system — Origin: center of rear axle at ground level
  +X = forward,  +Y = left,  +Z = up

Changes from v4:
  - Removed: suspension arms, shocks, differentials, belt drive, pulley adapters
  - Added:   4x G30 hub motors (direct drive), 4x NMT-MP-001 motor plates
  - Added:   DiBond shear panels, brake resistor, 4x VESCs
  - Changed: Frame 320mm wide, Apache 3800, WitMotion WT901 IMU, 10S3P battery

Usage:   python3 generate_chassis.py
Output:  04_ASSETS/cad/HM-AST-006_nomad_t_chassis.step
"""

import sys, os, math
sys.path.append(os.path.expanduser("~/.local/lib/python3.12/site-packages"))
import cadquery as cq

# =============================================================================
# PROJECT ROOT  (resolve from script location → 06_ENGINEERING/00_TOOLS/)
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
OUT_PATH = os.path.join(PROJECT_ROOT, "04_ASSETS", "cad", "HM-AST-006_nomad_t_chassis.step")

# =============================================================================
# DIMENSIONS  (HM-CAT-013 / HM-CAT-012 / HM-CAT-010 / HM-CAT-015)
# =============================================================================

# ── Frame (HM-CAT-013) ──
EX = 20.0                        # 2040 extrusion profile (20×40 → using 20×20 faces)
FRAME_L = 700.0                  # side rail length
RAIL_Y = 160.0                   # half-width: 320mm outer-to-outer
RAIL_X_START = 0.0               # rail starts at origin
RAIL_X_END = RAIL_X_START + FRAME_L

# Crossbeam positions (4× per cut list: Front, Center-Fwd, Center-Aft, Rear)
XB_POS = [0, 233, 467, 700]
XB_LEN = 240.0                   # inner width (HM-CAT-013 §5)

# Rail vertical position — axle at 125mm, rails clear above
WHEEL_RADIUS = 125.0             # 10" tire / 2  (HM-CAT-012 §5)
AXLE_Z = WHEEL_RADIUS            # axle height from ground
RAIL_Z = AXLE_Z + 20.0           # rail bottom 20mm above axle center = 145mm
                                  # gives ~125mm ground clearance (HM-CAT-012: ~89mm under rail bottom
                                  # at 85mm, but we raise slightly for hub motor clearance)

# ── Shear Panels (HM-CAT-013 §2) ──
PANEL_L = 700.0
PANEL_H = 120.0
PANEL_T = 3.0                    # 3mm DiBond

# ── Motor Plates NMT-MP-001 (HM-CAT-015) ──
MP_SIZE = 80.0                   # ~80×80mm
MP_THICK = 6.0                   # 6mm 6061-T6

# ── Hub Motor: Ninebot G30 (HM-CAT-010) ──
HUB_OD = 250.0                   # 10" tire outer diameter
HUB_WIDTH = 65.0                 # motor+tire width
HUB_AXLE_D = 12.0                # axle diameter

# ── Wheelbase & Track ──
WHEELBASE = 700.0                # front axle to rear axle = rail length
TRACK_W = 450.0                  # center-to-center wheel spacing (wider than frame)

# ── Apache 3800 Case (HM-CAT-012 §1) ──
CASE_L = 415.0
CASE_W = 328.0
CASE_H = 173.0

# ── Unified Thermal Deck (HM-CAT-012 §3 / CDR-4) ──
DECK_THICK = 6.0                 # 6mm aluminum
DECK_L = CASE_L
DECK_W = CASE_W

# ── Vibration Isolation Bobbins ──
BOBBIN_H = 15.0                  # M5 rubber bobbin height (Shore 40A)

# ── Battery 10S3P (HM-CAT-012 §2) ──
BAT_L = 200.0; BAT_W = 80.0; BAT_H = 70.0

# ── VESC: Flipsky 75100 (HM-CAT-014 §3) ──
VESC_L = 110.0; VESC_W = 66.0; VESC_H = 30.0

# ── RPLiDAR C1 (HM-CAT-006) ──
LIDAR_D = 50.0; LIDAR_H = 40.0
LIDAR_MAST_H = 200.0            # mast to get >300mm from ground

# ── OAK-D Lite (HM-CAT-003) ──
OAKD_L = 91.0; OAKD_W = 28.0; OAKD_H = 17.5

# ── Sharp IR Range Finders (HM-CAT-005) ──
IR_L = 44.0; IR_W = 18.0; IR_H = 13.0

# ── WitMotion WT901SDCL IMU (HM-CAT-008) ──
IMU_L = 51.0; IMU_W = 36.0; IMU_H = 15.0

# ── Brake Resistor (CDR-5 / HM-CAT-014 §3) ──
BRAKE_L = 60.0; BRAKE_W = 20.0; BRAKE_H = 20.0

# ── DC-DC Converter: Mean Well DDR-60L-15 (HM-CAT-014 §2) ──
DCDC_L = 120.0; DCDC_W = 40.0; DCDC_H = 27.0

# ── Arduino Nano (Watchdog — HM-CAT-014 §3) ──
NANO_L = 45.0; NANO_W = 18.0; NANO_H = 8.0

# =============================================================================
# COLORS
# =============================================================================
C_FRAME   = cq.Color(0.75, 0.75, 0.75, 1)      # silver aluminum
C_XBEAM   = cq.Color(0.65, 0.65, 0.80, 1)      # light blue-gray
C_PANEL   = cq.Color(0.20, 0.20, 0.22, 0.9)     # dark gray DiBond
C_MPLATE  = cq.Color(0.80, 0.70, 0.50, 1)       # gold aluminum
C_HUB     = cq.Color(0.06, 0.06, 0.06, 0.9)     # black tire/motor
C_BATT    = cq.Color(0.85, 0.10, 0.10, 0.85)    # red battery
C_VESC    = cq.Color(0.10, 0.50, 0.10, 0.9)     # green PCB
C_CASE    = cq.Color(0.20, 0.20, 0.20, 0.7)     # dark case
C_DECK    = cq.Color(0.80, 0.80, 0.80, 0.5)     # light aluminum
C_LIDAR   = cq.Color(0.0, 0.6, 0.9, 1)          # cyan sensor
C_OAKD    = cq.Color(0.0, 0.0, 0.8, 1)          # blue camera
C_IR      = cq.Color(1.0, 0.5, 0.0, 1)          # orange IR
C_IMU     = cq.Color(0.9, 0.0, 0.9, 1)          # magenta IMU
C_BRAKE   = cq.Color(0.7, 0.7, 0.2, 0.9)        # yellow resistor
C_DCDC    = cq.Color(0.5, 0.5, 0.5, 0.9)        # gray converter
C_NANO    = cq.Color(0.0, 0.4, 0.7, 0.9)        # teal Arduino

# =============================================================================
# BUILD ASSEMBLY
# =============================================================================
print("🔧 Generating Nomad-T v5 (Phase 1 Skid-Steer, Rigid Frame)...")
asm = cq.Assembly()

rail_cx = (RAIL_X_START + RAIL_X_END) / 2

# ── FRAME RAILS (2× side rails along X) — HM-CAT-013 §1 ──
rail = cq.Workplane("XY").box(FRAME_L, EX, EX)
for tag, ys in [("rail_L", RAIL_Y), ("rail_R", -RAIL_Y)]:
    asm.add(rail, name=tag,
        loc=cq.Location(cq.Vector(rail_cx, ys, RAIL_Z + EX/2)),
        color=C_FRAME)

# ── CROSSBEAMS (4× along Y) — HM-CAT-013 §5 ──
xbeam = cq.Workplane("XY").box(XB_LEN, EX, EX)
for i, xp in enumerate(XB_POS):
    asm.add(xbeam, name=f"xbeam_{i+1}",
        loc=cq.Location(cq.Vector(xp, 0, RAIL_Z + EX/2), cq.Vector(0,0,1), 90),
        color=C_XBEAM)

# ── SHEAR PANELS (2× DiBond side skins) — HM-CAT-013 §2 ──
panel = cq.Workplane("XY").box(PANEL_L, PANEL_T, PANEL_H)
for tag, ys in [("shear_L", RAIL_Y - EX/2 - PANEL_T/2),
                ("shear_R", -RAIL_Y + EX/2 + PANEL_T/2)]:
    asm.add(panel, name=tag,
        loc=cq.Location(cq.Vector(rail_cx, ys, RAIL_Z + PANEL_H/2)),
        color=C_PANEL)

# ── MOTOR PLATES NMT-MP-001 (4×, one per corner) — HM-CAT-015 ──
mplate = cq.Workplane("XY").box(MP_SIZE, MP_SIZE, MP_THICK)
corners = [
    ("motor_plate_FL", RAIL_X_END,  RAIL_Y),
    ("motor_plate_FR", RAIL_X_END, -RAIL_Y),
    ("motor_plate_RL", RAIL_X_START, RAIL_Y),
    ("motor_plate_RR", RAIL_X_START,-RAIL_Y),
]
for tag, xp, yp in corners:
    asm.add(mplate, name=tag,
        loc=cq.Location(cq.Vector(xp, yp, AXLE_Z)),
        color=C_MPLATE)

# ── G30 HUB MOTORS + TIRES (4× direct drive) — HM-CAT-010 ──
hub = cq.Workplane("XY").cylinder(HUB_WIDTH, HUB_OD/2)
wheel_positions = [
    ("g30_hub_FL", RAIL_X_END,   TRACK_W/2),
    ("g30_hub_FR", RAIL_X_END,  -TRACK_W/2),
    ("g30_hub_RL", RAIL_X_START,  TRACK_W/2),
    ("g30_hub_RR", RAIL_X_START, -TRACK_W/2),
]
for tag, xp, yp in wheel_positions:
    asm.add(hub, name=tag,
        loc=cq.Location(cq.Vector(xp, yp, AXLE_Z), cq.Vector(1,0,0), 90),
        color=C_HUB)

# ── BATTERY 10S3P (inside case, floor-mounted) — HM-CAT-012 §2 ──
batt = cq.Workplane("XY").box(BAT_L, BAT_W, BAT_H)
# Battery sits inside the case, on the right side
case_base_z = RAIL_Z + EX + BOBBIN_H
asm.add(batt, name="battery_10s3p",
    loc=cq.Location(cq.Vector(rail_cx, -CASE_W/4, case_base_z + BAT_H/2)),
    color=C_BATT)

# ── VESCs (4× Flipsky 75100) — HM-CAT-014 ──
# Mounted inverted on thermal deck underside (HM-CAT-012 §3)
vesc = cq.Workplane("XY").box(VESC_L, VESC_W, VESC_H)
thermal_deck_z = case_base_z + CASE_H  # top of case = thermal deck
vesc_positions = [
    ("vesc_FL", rail_cx + 80,   60),
    ("vesc_FR", rail_cx + 80,  -60),
    ("vesc_RL", rail_cx - 80,   60),
    ("vesc_RR", rail_cx - 80,  -60),
]
for tag, xp, yp in vesc_positions:
    asm.add(vesc, name=tag,
        loc=cq.Location(cq.Vector(xp, yp, thermal_deck_z - VESC_H/2)),
        color=C_VESC)

# ── APACHE 3800 CASE (on vibration bobbins) — HM-CAT-012 §1 ──
case_box = cq.Workplane("XY").box(CASE_L, CASE_W, CASE_H)
asm.add(case_box, name="apache_3800",
    loc=cq.Location(cq.Vector(rail_cx, 0, case_base_z + CASE_H/2)),
    color=C_CASE)

# ── UNIFIED THERMAL DECK (6mm Al on top of case) — HM-CAT-012 §3 / CDR-4 ──
deck = cq.Workplane("XY").box(DECK_L, DECK_W, DECK_THICK)
asm.add(deck, name="thermal_deck",
    loc=cq.Location(cq.Vector(rail_cx, 0, thermal_deck_z + DECK_THICK/2)),
    color=C_DECK)

# ── RPLiDAR C1 (on mast, >300mm from ground) — HM-CAT-006 ──
mast = cq.Workplane("XY").box(EX, EX, LIDAR_MAST_H)
lidar = cq.Workplane("XY").cylinder(LIDAR_H, LIDAR_D/2)
mast_base_z = thermal_deck_z + DECK_THICK
asm.add(mast, name="lidar_mast",
    loc=cq.Location(cq.Vector(rail_cx + 100, 0, mast_base_z + LIDAR_MAST_H/2)),
    color=C_FRAME)
asm.add(lidar, name="rplidar_c1",
    loc=cq.Location(cq.Vector(rail_cx + 100, 0, mast_base_z + LIDAR_MAST_H + LIDAR_H/2)),
    color=C_LIDAR)

# ── OAK-D LITE (front-facing, tilted -15°) — HM-CAT-003 ──
oakd = cq.Workplane("XY").box(OAKD_L, OAKD_W, OAKD_H)
asm.add(oakd, name="oakd_lite",
    loc=cq.Location(cq.Vector(RAIL_X_END + 20, 0, RAIL_Z + EX + OAKD_H/2 + 10),
                    cq.Vector(0, 1, 0), -15),
    color=C_OAKD)

# ── SHARP IR WHISKERS (4× corner sensors) — HM-CAT-005 ──
ir = cq.Workplane("XY").box(IR_L, IR_W, IR_H)
ir_z = RAIL_Z + EX/2
ir_specs = [
    ("ir_FL", RAIL_X_END + 20,   RAIL_Y - 10,   45),
    ("ir_FR", RAIL_X_END + 20,  -RAIL_Y + 10,  -45),
    ("ir_RC", RAIL_X_START - 20,  0,            180),
    ("ir_FC", RAIL_X_END + 20,   0,              0),
]
for tag, x, y, ang in ir_specs:
    asm.add(ir, name=tag,
        loc=cq.Location(cq.Vector(x, y, ir_z), cq.Vector(0,0,1), ang),
        color=C_IR)

# ── IMU: WitMotion WT901SDCL (center of mass, under deck) — HM-CAT-008 ──
imu = cq.Workplane("XY").box(IMU_L, IMU_W, IMU_H)
asm.add(imu, name="imu_wt901",
    loc=cq.Location(cq.Vector(rail_cx, 0, case_base_z + IMU_H/2 + 5)),
    color=C_IMU)

# ── BRAKE RESISTOR (200W 8Ω, on frame rail) — CDR-5 / HM-CAT-014 §3 ──
brake = cq.Workplane("XY").box(BRAKE_L, BRAKE_W, BRAKE_H)
asm.add(brake, name="brake_resistor",
    loc=cq.Location(cq.Vector(rail_cx - 150, RAIL_Y - EX, RAIL_Z + EX + BRAKE_H/2)),
    color=C_BRAKE)

# ── DC-DC CONVERTER: Mean Well DDR-60L-15 — HM-CAT-014 §2 ──
dcdc = cq.Workplane("XY").box(DCDC_L, DCDC_W, DCDC_H)
asm.add(dcdc, name="dcdc_meanwell",
    loc=cq.Location(cq.Vector(rail_cx + 150, RAIL_Y - EX, RAIL_Z + EX + DCDC_H/2)),
    color=C_DCDC)

# ── ARDUINO NANO (Watchdog) — HM-CAT-014 §3.2 ──
nano = cq.Workplane("XY").box(NANO_L, NANO_W, NANO_H)
asm.add(nano, name="arduino_nano",
    loc=cq.Location(cq.Vector(rail_cx, RAIL_Y - EX, RAIL_Z + EX + NANO_H/2)),
    color=C_NANO)

# ── VIBRATION BOBBINS (4× M5, corners) — HM-CAT-012 §1 ──
bobbin = cq.Workplane("XY").cylinder(BOBBIN_H, 8)  # ~M5 bobbin, 16mm OD
bobbin_positions = [
    ("bobbin_FL", rail_cx + CASE_L/2 - 30,  CASE_W/2 - 30),
    ("bobbin_FR", rail_cx + CASE_L/2 - 30, -CASE_W/2 + 30),
    ("bobbin_RL", rail_cx - CASE_L/2 + 30,  CASE_W/2 - 30),
    ("bobbin_RR", rail_cx - CASE_L/2 + 30, -CASE_W/2 + 30),
]
for tag, xp, yp in bobbin_positions:
    asm.add(bobbin, name=tag,
        loc=cq.Location(cq.Vector(xp, yp, RAIL_Z + EX + BOBBIN_H/2)),
        color=C_FRAME)

# =============================================================================
# EXPORT
# =============================================================================
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
asm.save(OUT_PATH)
sz = os.path.getsize(OUT_PATH) / 1024
print(f"✅ STEP saved: {OUT_PATH}  ({sz:.0f} KB)")
print()
print("📐 Key Dimensions (Phase 1 Approved):")
print(f"   Frame:        {FRAME_L} × {RAIL_Y*2}mm (4 crossbeams, rigid skid)")
print(f"   Rail Z:       {RAIL_Z}mm from ground")
print(f"   Wheelbase:    {WHEELBASE}mm")
print(f"   Track:        {TRACK_W}mm (center-to-center)")
print(f"   Wheels:       4× G30 Hub Motor, {HUB_OD}mm OD, Direct Drive")
print(f"   Case:         Apache 3800 ({CASE_L}×{CASE_W}×{CASE_H}mm)")
print(f"   Thermal Deck: {DECK_THICK}mm Al, Z={thermal_deck_z:.0f}mm")
print(f"   IMU:          WitMotion WT901SDCL")
print()
print("📦 View: drag STEP file into https://3dviewer.net")
print(f"📄 Manifest: 04_ASSETS/cad/HM-AST-007_cad_manifest.md")
