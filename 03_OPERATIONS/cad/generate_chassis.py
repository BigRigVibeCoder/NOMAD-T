#!/usr/bin/env python3
"""
HM-OPS-001: Nomad-T Chassis Generator v4 (Code-as-CAD)
========================================================
Full robot from HM-CAT-013 (frame/suspension) + HM-CAT-012 (integration).

Coordinate system — Origin: center of rear axle at ground level
  +X = forward, +Y = left, +Z = up

Usage:  python3 generate_chassis.py
Output: nomad_t_chassis_v4.step
"""

import sys, os, math
sys.path.append(os.path.expanduser("~/.local/lib/python3.12/site-packages"))
import cadquery as cq

# =============================================================================
# DIMENSIONS  (HM-CAT-013 / HM-CAT-012 / HM-CAT-010)
# =============================================================================

# -- Frame --
EX = 20.0
FRAME_L = 700.0              # total rail length
RAIL_Y = 150.0               # left rail at +150, right at -150
FRAME_W_OUT = 300.0           # outer rail-to-rail
FRAME_W_IN = 260.0            # inner
RAIL_Z = 120.0                # rail bottom from ground
RAIL_X_START = -50.0          # extends 50mm behind rear axle
RAIL_X_END = 650.0

# Crossbeam X positions (from origin = rear axle)
XB_POS = [0, 170, 350, 530, 650]
XB_LEN = 300.0               # crossbeam length

# Upper deck
DECK_Z = 180.0                # deck plate bottom from ground
DECK_POST_H = 60.0            # 180 - 120 = 60
DECK_L = 250.0
DECK_W = 200.0
DECK_THICK = 3.0

# -- Wheelbase & Track --
WHEELBASE = 650.0             # XB#1 (X=0) to XB#5 (X=650)
TRACK_W = 648.0

# -- Motor: Flipsky 6374 --
MOT_D = 63.0
MOT_L = 74.0

# -- Belt Drive --
M2D = 230.0                  # motor-to-diff center distance

# -- Diff: Arrma Kraton 8S --
DIFF_W = 65.0; DIFF_H = 55.0; DIFF_D = 55.0

# -- Wheel: Arrma Kraton 8S --
WHL_D = 182.0; WHL_W = 75.0
WHL_CENTER_Z = 91.0          # wheel radius = center height

# -- Suspension: Trailing Arm --
ARM_L = 150.0                # pivot to axle
ARM_W = 50.0
ARM_THICK = 6.0
PIVOT_Z = 100.0              # from ground
STATIC_ANGLE = -6.0          # degrees from horizontal

# -- Shock: Traxxas GTR 7461 --
SHOCK_EXTENDED = 221.0
SHOCK_STATIC = 195.0
SHOCK_DIA = 16.0
SHOCK_UPPER_Z = 170.0        # from ground
SHOCK_LOWER_FROM_PIVOT = 80.0

# -- Battery: Zeee 6S 14Ah --
BAT_L = 168.0; BAT_W = 68.0; BAT_H = 56.0

# -- VESC: Flipsky 75100 --
VESC_L = 110.0; VESC_W = 66.0; VESC_H = 30.0

# -- Apache 2800 (Odroid case) --
CASE_L = 241.0; CASE_W = 188.0; CASE_H = 108.0

# -- RPLiDAR C1 --
LIDAR_D = 50.0; LIDAR_H_BODY = 40.0
LIDAR_MAST = 189.0

# -- OAK-D Lite --
OAKD_L = 91.0; OAKD_W = 28.0; OAKD_H = 17.5

# -- Sharp IR --
IR_L = 44.0; IR_W = 18.0; IR_H = 13.0

# -- IMU --
IMU_SZ = 25.0; IMU_H = 3.0

# -- Pulley Adapter --
ADAPTER_D = 50.0; ADAPTER_T = 6.0

# =============================================================================
# COLORS
# =============================================================================
C_FRAME  = cq.Color(0.75, 0.75, 0.75, 1)
C_XBEAM  = cq.Color(0.65, 0.65, 0.80, 1)
C_DECK   = cq.Color(0.80, 0.80, 0.80, 0.5)
C_MOTOR  = cq.Color(0.12, 0.12, 0.12, 1)
C_DIFF   = cq.Color(0.40, 0.40, 0.40, 1)
C_WHEEL  = cq.Color(0.06, 0.06, 0.06, 0.9)
C_BATT   = cq.Color(0.85, 0.10, 0.10, 0.85)
C_VESC   = cq.Color(0.10, 0.50, 0.10, 0.9)
C_CASE   = cq.Color(0.20, 0.20, 0.20, 0.7)
C_LIDAR  = cq.Color(0.0, 0.6, 0.9, 1)
C_OAKD   = cq.Color(0.0, 0.0, 0.8, 1)
C_IR     = cq.Color(1.0, 0.5, 0.0, 1)
C_IMU    = cq.Color(0.9, 0.0, 0.9, 1)
C_SHOCK  = cq.Color(0.9, 0.9, 0.0, 0.9)
C_ARM    = cq.Color(0.6, 0.4, 0.2, 1)
C_ADAPT  = cq.Color(0.8, 0.6, 0.0, 1)

# =============================================================================
# BUILD
# =============================================================================
print("🔧 Generating Nomad-T v4 (full engineering spec)...")
asm = cq.Assembly()

rail_cx = (RAIL_X_START + RAIL_X_END) / 2   # center of rail along X

# ── FRAME RAILS (2× along X) ──
rail = cq.Workplane("XY").box(FRAME_L, EX, EX)
for tag, ys in [("rail_L", RAIL_Y), ("rail_R", -RAIL_Y)]:
    asm.add(rail, name=tag,
        loc=cq.Location(cq.Vector(rail_cx, ys, RAIL_Z + EX/2)),
        color=C_FRAME)

# ── CROSSBEAMS (5× along Y) ──
xbeam = cq.Workplane("XY").box(XB_LEN, EX, EX)
for i, xp in enumerate(XB_POS):
    asm.add(xbeam, name=f"xb_{i+1}",
        loc=cq.Location(cq.Vector(xp, 0, RAIL_Z + EX/2), cq.Vector(0,0,1), 90),
        color=C_XBEAM)

# ── UPPER DECK ──
# 4 vertical posts
post = cq.Workplane("XY").box(EX, EX, DECK_POST_H)
post_positions = [
    (XB_POS[2] - DECK_L/2 + EX/2,  RAIL_Y - EX),
    (XB_POS[2] - DECK_L/2 + EX/2, -RAIL_Y + EX),
    (XB_POS[2] + DECK_L/2 - EX/2,  RAIL_Y - EX),
    (XB_POS[2] + DECK_L/2 - EX/2, -RAIL_Y + EX),
]
for j, (px, py) in enumerate(post_positions):
    asm.add(post, name=f"post_{j}",
        loc=cq.Location(cq.Vector(px, py, RAIL_Z + EX + DECK_POST_H/2)),
        color=C_FRAME)

# Deck plate
deck = cq.Workplane("XY").box(DECK_L, DECK_W, DECK_THICK)
asm.add(deck, name="deck_plate",
    loc=cq.Location(cq.Vector(XB_POS[2], 0, DECK_Z + DECK_THICK/2)),
    color=C_DECK)

# ── MOTORS (2×, at XB#2 and XB#4 positions) ──
motor = cq.Workplane("XY").cylinder(MOT_L, MOT_D/2)
mot_y = 80.0   # motor offset from centerline (per spec: Y=+80mm)
for tag, xp in [("mot_R", XB_POS[1]), ("mot_F", XB_POS[3])]:
    asm.add(motor, name=tag,
        loc=cq.Location(cq.Vector(xp, mot_y, RAIL_Z), cq.Vector(1,0,0), 90),
        color=C_MOTOR)

# ── DIFFS (2×, at XB#1 and XB#5 centerline) ──
diff = cq.Workplane("XY").box(DIFF_W, DIFF_D, DIFF_H)
for tag, xp in [("diff_R", XB_POS[0]), ("diff_F", XB_POS[4])]:
    asm.add(diff, name=tag,
        loc=cq.Location(cq.Vector(xp, 0, RAIL_Z - DIFF_H/2)),
        color=C_DIFF)

# ── PULLEY ADAPTERS (2×, on diffs) ──
adapter = cq.Workplane("XY").cylinder(ADAPTER_T, ADAPTER_D/2)
for tag, xp in [("adapt_R", XB_POS[0]), ("adapt_F", XB_POS[4])]:
    asm.add(adapter, name=tag,
        loc=cq.Location(cq.Vector(xp, DIFF_D/2 + ADAPTER_T/2 + 2, RAIL_Z - DIFF_H/2),
                        cq.Vector(1,0,0), 90),
        color=C_ADAPT)

# ── TRAILING ARMS (4×) + WHEELS (4×) + SHOCKS (4×) ──
arm = cq.Workplane("XY").box(ARM_L, ARM_W, ARM_THICK)
wheel = cq.Workplane("XY").cylinder(WHL_W, WHL_D/2)
shock = cq.Workplane("XY").cylinder(SHOCK_STATIC, SHOCK_DIA/2)

rad = math.radians(STATIC_ANGLE)
arm_end_x_off = ARM_L * math.cos(rad)
arm_end_z_off = ARM_L * math.sin(rad)

corners = [
    ("FL", XB_POS[4],  RAIL_Y + ARM_L/2 + 10),
    ("FR", XB_POS[4], -RAIL_Y - ARM_L/2 - 10),
    ("RL", XB_POS[0],  RAIL_Y + ARM_L/2 + 10),
    ("RR", XB_POS[0], -RAIL_Y - ARM_L/2 - 10),
]
for label, ax, ay in corners:
    ysign = 1 if ay > 0 else -1

    # Arm (tilted at static angle)
    arm_cx = ax
    arm_cz = PIVOT_Z + arm_end_z_off/2
    asm.add(arm, name=f"arm_{label}",
        loc=cq.Location(cq.Vector(arm_cx, ay, arm_cz),
                        cq.Vector(0, 1, 0), STATIC_ANGLE),
        color=C_ARM)

    # Wheel at end of arm
    whl_y = ysign * TRACK_W / 2
    asm.add(wheel, name=f"whl_{label}",
        loc=cq.Location(cq.Vector(ax, whl_y, WHL_CENTER_Z),
                        cq.Vector(1, 0, 0), 90),
        color=C_WHEEL)

    # Shock (simplified cylinder, vertical-ish)
    shock_base_z = PIVOT_Z + SHOCK_LOWER_FROM_PIVOT * math.sin(rad)
    shock_cz = (SHOCK_UPPER_Z + shock_base_z) / 2
    asm.add(shock, name=f"shock_{label}",
        loc=cq.Location(cq.Vector(ax, ysign * (RAIL_Y - 30), shock_cz)),
        color=C_SHOCK)

# ── BATTERIES (2×, centered at XB#3) ──
batt = cq.Workplane("XY").box(BAT_L, BAT_W, BAT_H)
bat_z = RAIL_Z - BAT_H/2  # hanging under frame
for tag, yoff in [("bat_1", BAT_W/2 + 2), ("bat_2", -BAT_W/2 - 2)]:
    asm.add(batt, name=tag,
        loc=cq.Location(cq.Vector(XB_POS[2], yoff, bat_z)),
        color=C_BATT)

# ── VESCs (2×, at motor crossbeams) ──
vesc = cq.Workplane("XY").box(VESC_L, VESC_W, VESC_H)
vesc_y = -60.0  # per spec: VESC at Y=-60mm
for tag, xp in [("vesc_R", XB_POS[1]), ("vesc_F", XB_POS[3])]:
    asm.add(vesc, name=tag,
        loc=cq.Location(cq.Vector(xp, vesc_y, RAIL_Z + EX + VESC_H/2)),
        color=C_VESC)

# ── APACHE 2800 (on upper deck) ──
case_box = cq.Workplane("XY").box(CASE_L, CASE_W, CASE_H)
asm.add(case_box, name="apache_2800",
    loc=cq.Location(cq.Vector(XB_POS[2], 0, DECK_Z + DECK_THICK + CASE_H/2)),
    color=C_CASE)

# ── RPLiDAR MAST + SENSOR ──
mast = cq.Workplane("XY").box(EX, EX, LIDAR_MAST)
lidar = cq.Workplane("XY").cylinder(LIDAR_H_BODY, LIDAR_D/2)
mast_z_base = DECK_Z + DECK_THICK
asm.add(mast, name="lidar_mast",
    loc=cq.Location(cq.Vector(XB_POS[2], 0, mast_z_base + LIDAR_MAST/2)),
    color=C_FRAME)
asm.add(lidar, name="rplidar_c1",
    loc=cq.Location(cq.Vector(XB_POS[2], 0, mast_z_base + LIDAR_MAST + LIDAR_H_BODY/2)),
    color=C_LIDAR)

# ── OAK-D LITE (front of frame, -15° tilt) ──
oakd = cq.Workplane("XY").box(OAKD_L, OAKD_W, OAKD_H)
asm.add(oakd, name="oakd_lite",
    loc=cq.Location(cq.Vector(XB_POS[4] - 20, 0, RAIL_Z + EX + OAKD_H/2 + 5),
                    cq.Vector(0, 1, 0), -15),
    color=C_OAKD)

# ── SHARP IR WHISKERS (4×) ──
ir = cq.Workplane("XY").box(IR_L, IR_W, IR_H)
ir_z = RAIL_Z - IR_H/2
ir_specs = [
    ("ir_FL", XB_POS[4] + 20,  RAIL_Y - 10,  45),
    ("ir_FR", XB_POS[4] + 20, -RAIL_Y + 10, -45),
    ("ir_FC", XB_POS[4] + 20,  0,             0),
    ("ir_RC", XB_POS[0] - 20,  0,           180),
]
for tag, x, y, ang in ir_specs:
    asm.add(ir, name=tag,
        loc=cq.Location(cq.Vector(x, y, ir_z), cq.Vector(0,0,1), ang),
        color=C_IR)

# ── IMU (BNO085, at CG: X=350, Y=0, under deck) ──
imu = cq.Workplane("XY").box(IMU_SZ, IMU_SZ, IMU_H)
asm.add(imu, name="imu_bno085",
    loc=cq.Location(cq.Vector(XB_POS[2], 0, RAIL_Z - EX/2 - IMU_H/2)),
    color=C_IMU)


# =============================================================================
# EXPORT
# =============================================================================
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nomad_t_chassis.step")
asm.save(out)
sz = os.path.getsize(out) / 1024
print(f"✅ STEP saved: {out}  ({sz:.0f} KB)")
print()
print("📐 Key Dimensions (HM-CAT-013):")
print(f"   Frame:       {FRAME_L} × {FRAME_W_OUT}mm (5 crossbeams)")
print(f"   Rail Z:      {RAIL_Z}mm from ground")
print(f"   Wheelbase:   {XB_POS[4] - XB_POS[0]}mm (XB#1→#5)")
print(f"   Track:       {TRACK_W}mm")
print(f"   Suspension:  Trailing arm, {ARM_L}mm, Traxxas GTR shocks")
print(f"   Upper deck:  Z={DECK_Z}mm, carries Apache 2800 + LiDAR")
print()
print("📦 View: drag into https://3dviewer.net")
