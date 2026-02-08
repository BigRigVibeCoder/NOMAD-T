#!/usr/bin/env python3
"""
Nomad-T Chassis Generator v6 — Phase 1 "Skid-Steer" (Code-as-CAD)
===================================================================
Full robot assembly — every part named and placed per approved specs.

Uses simplified geometry (boxes/cylinders) for COTS parts to keep OCCT
kernel performance manageable. High-fidelity detail is in generate_parts.py
which produces individual manufacturing-ready STEP files.

Specs:  HM-CAT-001/010/012/013/014/015
Origin: center of rear axle at ground level
  +X = forward,  +Y = left,  +Z = up

Usage:   python3 generate_chassis.py
Output:  04_ASSETS/cad/HM-AST-006_nomad_t_chassis.step
"""

import sys, os
sys.path.append(os.path.expanduser("~/.local/lib/python3.12/site-packages"))
import cadquery as cq

# =============================================================================
# PATHS
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
OUT_PATH = os.path.join(PROJECT_ROOT, "04_ASSETS", "cad", "HM-AST-006_nomad_t_chassis.step")

# =============================================================================
# DIMENSIONS
# =============================================================================

# Frame (HM-CAT-013)
EX = 20.0
FRAME_L = 700.0
RAIL_Y = 160.0                    # 320mm outer-to-outer
XB_POS = [0, 233, 467, 700]      # 4 crossbeams
XB_LEN = 240.0

# Heights
WHEEL_R = 125.0                   # 10" tire radius
AXLE_Z = WHEEL_R
RAIL_Z = AXLE_Z + 20.0

# Shear Panels (HM-CAT-013 §2)
PANEL_L = 700.0; PANEL_H = 120.0; PANEL_T = 3.0

# Motor Plates NMT-MP-001 (HM-CAT-015)
MP = 80.0; MP_T = 6.0

# Hub Motor G30 (HM-CAT-010)
TIRE_OD = 250.0; TIRE_W = 65.0
MOT_OD = 140.0; MOT_W = 45.0
AXLE_D = 12.0; AXLE_L = 25.0
TRACK_W = 450.0

# Apache 3800 (HM-CAT-012 §1)
CASE_L = 415.0; CASE_W = 328.0; CASE_H = 173.0

# Thermal Deck (CDR-4)
DECK_T = 6.0

# Bobbins
BOB_H = 15.0; BOB_OD = 16.0

# Battery 10S3P (HM-CAT-012 §2)
BAT_L = 200.0; BAT_W = 80.0; BAT_H = 70.0

# VESC 75100 (HM-CAT-014)
VESC_L = 110.0; VESC_W = 66.0; VESC_H = 30.0

# Sensors
LIDAR_D = 50.0; LIDAR_H = 40.0; MAST_H = 200.0
OAKD_L = 91.0; OAKD_W = 28.0; OAKD_H = 17.5
IR_L = 44.0; IR_W = 18.0; IR_H = 13.0
IMU_L = 51.0; IMU_W = 36.0; IMU_H = 15.0

# Electrical
BRAKE_L = 60.0; BRAKE_W = 20.0; BRAKE_H = 20.0
DCDC_L = 120.0; DCDC_W = 40.0; DCDC_H = 27.0
NANO_L = 45.0; NANO_W = 18.0; NANO_H = 8.0

# E-Stop (CDR-6)
ESTOP_D = 30.0; ESTOP_H = 25.0

# Distribution Bus
DBUS_L = 80.0; DBUS_W = 30.0; DBUS_H = 20.0

# Contactor (HM-DWG-001)
CONT_L = 40.0; CONT_W = 35.0; CONT_H = 35.0

# Status LEDs (3x)
LED_D = 8.0; LED_H = 10.0

# =============================================================================
# COLORS
# =============================================================================
C_ALU   = cq.Color(0.78, 0.78, 0.80, 1)
C_XBEAM = cq.Color(0.70, 0.72, 0.82, 1)
C_PANEL = cq.Color(0.18, 0.18, 0.20, 0.95)
C_PLATE = cq.Color(0.82, 0.73, 0.50, 1)
C_TIRE  = cq.Color(0.06, 0.06, 0.06, 0.95)
C_MOTOR = cq.Color(0.15, 0.15, 0.15, 1)
C_AXLE  = cq.Color(0.60, 0.60, 0.60, 1)
C_BATT  = cq.Color(0.85, 0.12, 0.12, 0.9)
C_XT90  = cq.Color(0.90, 0.80, 0.10, 1)
C_VESC  = cq.Color(0.08, 0.45, 0.08, 0.95)
C_CASE  = cq.Color(0.12, 0.12, 0.12, 0.85)
C_DECK  = cq.Color(0.82, 0.82, 0.85, 0.7)
C_LIDAR = cq.Color(0.0, 0.55, 0.85, 1)
C_OAKD  = cq.Color(0.0, 0.0, 0.75, 1)
C_IR    = cq.Color(1.0, 0.5, 0.0, 1)
C_IMU   = cq.Color(0.85, 0.0, 0.85, 1)
C_BRAKE = cq.Color(0.75, 0.75, 0.20, 0.95)
C_DCDC  = cq.Color(0.50, 0.50, 0.50, 0.95)
C_NANO  = cq.Color(0.0, 0.35, 0.65, 0.95)
C_BOB   = cq.Color(0.25, 0.25, 0.25, 1)
C_ESTOP = cq.Color(0.90, 0.05, 0.05, 1)
C_DBUS  = cq.Color(0.70, 0.50, 0.20, 1)
C_CONT  = cq.Color(0.30, 0.30, 0.35, 1)
C_LED_G = cq.Color(0.0, 0.85, 0.0, 1)
C_LED_Y = cq.Color(0.95, 0.85, 0.0, 1)
C_LED_R = cq.Color(0.95, 0.05, 0.05, 1)
C_HNDL  = cq.Color(0.25, 0.25, 0.25, 1)

# =============================================================================
# BUILD
# =============================================================================
print("🔧 Generating Nomad-T v6 (Phase 1 Skid-Steer, Full Assembly)...")
asm = cq.Assembly()
cx = FRAME_L / 2  # center X of frame

# ── FRAME RAILS (2×) ──
rail = cq.Workplane("XY").box(FRAME_L, EX, EX)
for tag, y in [("rail_L", RAIL_Y), ("rail_R", -RAIL_Y)]:
    asm.add(rail, name=tag,
        loc=cq.Location(cq.Vector(cx, y, RAIL_Z + EX/2)), color=C_ALU)

# ── CROSSBEAMS (4×) ──
xb = cq.Workplane("XY").box(EX, XB_LEN, EX)
for i, x in enumerate(XB_POS):
    asm.add(xb, name=f"xbeam_{i+1}",
        loc=cq.Location(cq.Vector(x, 0, RAIL_Z + EX/2)), color=C_XBEAM)

# ── SHEAR PANELS (2×) ──
panel = cq.Workplane("XY").box(PANEL_L, PANEL_T, PANEL_H)
for tag, y in [("shear_L", RAIL_Y - EX/2 - PANEL_T/2),
               ("shear_R", -RAIL_Y + EX/2 + PANEL_T/2)]:
    asm.add(panel, name=tag,
        loc=cq.Location(cq.Vector(cx, y, RAIL_Z + PANEL_H/2)), color=C_PANEL)

# ── MOTOR PLATES (4×) ──
mp = cq.Workplane("XY").box(MP, MP, MP_T)
# Add center hole for axle
mp = mp.faces(">Z").workplane().hole(AXLE_D)
corners = [("motor_plate_FL", FRAME_L, RAIL_Y), ("motor_plate_FR", FRAME_L, -RAIL_Y),
           ("motor_plate_RL", 0, RAIL_Y),       ("motor_plate_RR", 0, -RAIL_Y)]
for tag, x, y in corners:
    asm.add(mp, name=tag,
        loc=cq.Location(cq.Vector(x, y, AXLE_Z)), color=C_PLATE)

# ── G30 HUB MOTORS (4× — tire + motor body + axle) ──
tire = cq.Workplane("XY").cylinder(TIRE_W, TIRE_OD/2)
mot = cq.Workplane("XY").cylinder(MOT_W, MOT_OD/2)
axle = cq.Workplane("XY").cylinder(AXLE_L, AXLE_D/2)
whl = [("g30_hub_FL", FRAME_L,  TRACK_W/2), ("g30_hub_FR", FRAME_L, -TRACK_W/2),
       ("g30_hub_RL", 0,         TRACK_W/2), ("g30_hub_RR", 0,       -TRACK_W/2)]
for tag, x, y in whl:
    rot = cq.Location(cq.Vector(x, y, AXLE_Z), cq.Vector(1,0,0), 90)
    asm.add(tire, name=f"{tag}_tire", loc=rot, color=C_TIRE)
    asm.add(mot, name=f"{tag}_motor", loc=rot, color=C_MOTOR)
    sgn = 1 if y > 0 else -1
    asm.add(axle, name=f"{tag}_axle",
        loc=cq.Location(cq.Vector(x, y - sgn*(TIRE_W/2 + AXLE_L/2), AXLE_Z),
                        cq.Vector(1,0,0), 90), color=C_AXLE)

# ── BOBBINS (4×) ──
bob = cq.Workplane("XY").cylinder(BOB_H, BOB_OD/2)
bz = RAIL_Z + EX + BOB_H
for tag, x, y in [("bobbin_FL", cx+CASE_L/2-30,  CASE_W/2-30),
                  ("bobbin_FR", cx+CASE_L/2-30, -CASE_W/2+30),
                  ("bobbin_RL", cx-CASE_L/2+30,  CASE_W/2-30),
                  ("bobbin_RR", cx-CASE_L/2+30, -CASE_W/2+30)]:
    asm.add(bob, name=tag,
        loc=cq.Location(cq.Vector(x, y, RAIL_Z + EX + BOB_H/2)), color=C_BOB)

# ── APACHE 3800 CASE ──
case = cq.Workplane("XY").box(CASE_L, CASE_W, CASE_H)
asm.add(case, name="apache_3800",
    loc=cq.Location(cq.Vector(cx, 0, bz + CASE_H/2)), color=C_CASE)

# Handle
handle = cq.Workplane("XY").box(120, 15, 20)
asm.add(handle, name="case_handle",
    loc=cq.Location(cq.Vector(cx, 0, bz + CASE_H + 10)), color=C_HNDL)

# ── BATTERY 10S3P ──
batt = cq.Workplane("XY").box(BAT_L, BAT_W, BAT_H)
asm.add(batt, name="battery_10s3p",
    loc=cq.Location(cq.Vector(cx, -CASE_W/4, bz + BAT_H/2 + 4)), color=C_BATT)
xt90 = cq.Workplane("XY").box(15, 20, 12)
asm.add(xt90, name="battery_xt90",
    loc=cq.Location(cq.Vector(cx + BAT_L/2 + 7.5, -CASE_W/4, bz + BAT_H/2 + 4)),
    color=C_XT90)

# ── THERMAL DECK ──
tdz = bz + CASE_H
deck = cq.Workplane("XY").box(CASE_L, CASE_W, DECK_T)
asm.add(deck, name="thermal_deck",
    loc=cq.Location(cq.Vector(cx, 0, tdz + DECK_T/2)), color=C_DECK)

# ── VESCs (4×) ──
vesc = cq.Workplane("XY").box(VESC_L, VESC_W, VESC_H)
for tag, x, y in [("vesc_FL", cx+80, 60), ("vesc_FR", cx+80, -60),
                  ("vesc_RL", cx-80, 60), ("vesc_RR", cx-80, -60)]:
    asm.add(vesc, name=tag,
        loc=cq.Location(cq.Vector(x, y, tdz - VESC_H/2)), color=C_VESC)

# ── RPLiDAR C1 + MAST ──
mast = cq.Workplane("XY").cylinder(MAST_H, EX/2)
lidar = cq.Workplane("XY").cylinder(LIDAR_H, LIDAR_D/2)
mast_z = tdz + DECK_T
asm.add(mast, name="lidar_mast",
    loc=cq.Location(cq.Vector(cx+100, 0, mast_z + MAST_H/2)), color=C_ALU)
asm.add(lidar, name="rplidar_c1",
    loc=cq.Location(cq.Vector(cx+100, 0, mast_z + MAST_H + LIDAR_H/2)), color=C_LIDAR)

# ── OAK-D LITE (−15° tilt) ──
oakd = cq.Workplane("XY").box(OAKD_L, OAKD_W, OAKD_H)
asm.add(oakd, name="oakd_lite",
    loc=cq.Location(cq.Vector(FRAME_L+20, 0, RAIL_Z+EX+OAKD_H/2+10),
                    cq.Vector(0,1,0), -15), color=C_OAKD)
# 3 lenses
lens = cq.Workplane("XY").cylinder(3, 5)
for tag, ly in [("oakd_lens_L", 25), ("oakd_lens_C", 0), ("oakd_lens_R", -25)]:
    asm.add(lens, name=tag,
        loc=cq.Location(cq.Vector(FRAME_L+20+OAKD_W/2, ly, RAIL_Z+EX+OAKD_H/2+10),
                        cq.Vector(0,1,0), -15), color=cq.Color(0.1,0.1,0.1,1))

# ── SHARP IR WHISKERS (4×) ──
ir = cq.Workplane("XY").box(IR_L, IR_W, IR_H)
iz = RAIL_Z + EX/2
for tag, x, y, a in [("ir_FL", FRAME_L+20, RAIL_Y-10, 45),
                     ("ir_FR", FRAME_L+20, -RAIL_Y+10, -45),
                     ("ir_FC", FRAME_L+20, 0, 0),
                     ("ir_RC", -20, 0, 180)]:
    asm.add(ir, name=tag,
        loc=cq.Location(cq.Vector(x, y, iz), cq.Vector(0,0,1), a), color=C_IR)

# ── IMU WT901 ──
imu = cq.Workplane("XY").box(IMU_L, IMU_W, IMU_H)
asm.add(imu, name="imu_wt901",
    loc=cq.Location(cq.Vector(cx, 0, bz + IMU_H/2 + 8)), color=C_IMU)

# ── BRAKE RESISTOR ──
brake = cq.Workplane("XY").box(BRAKE_L, BRAKE_W, BRAKE_H)
asm.add(brake, name="brake_resistor",
    loc=cq.Location(cq.Vector(cx-150, RAIL_Y-EX, RAIL_Z+EX+BRAKE_H/2)), color=C_BRAKE)

# ── DC-DC CONVERTER ──
dcdc = cq.Workplane("XY").box(DCDC_L, DCDC_W, DCDC_H)
asm.add(dcdc, name="dcdc_meanwell",
    loc=cq.Location(cq.Vector(cx+150, RAIL_Y-EX, RAIL_Z+EX+DCDC_H/2)), color=C_DCDC)

# ── ARDUINO NANO ──
nano = cq.Workplane("XY").box(NANO_L, NANO_W, NANO_H)
asm.add(nano, name="arduino_nano",
    loc=cq.Location(cq.Vector(cx, RAIL_Y-EX, RAIL_Z+EX+NANO_H/2)), color=C_NANO)

# ── E-STOP (rear panel, mushroom button) — CDR-6 ──
estop = cq.Workplane("XY").cylinder(ESTOP_H, ESTOP_D/2)
asm.add(estop, name="estop_button",
    loc=cq.Location(cq.Vector(-20, 0, RAIL_Z+EX+ESTOP_H/2)), color=C_ESTOP)

# ── DISTRIBUTION BUS ──
dbus = cq.Workplane("XY").box(DBUS_L, DBUS_W, DBUS_H)
asm.add(dbus, name="distribution_bus",
    loc=cq.Location(cq.Vector(cx-100, -RAIL_Y+EX, RAIL_Z+EX+DBUS_H/2)), color=C_DBUS)

# ── CONTACTOR ──
cont = cq.Workplane("XY").box(CONT_L, CONT_W, CONT_H)
asm.add(cont, name="main_contactor",
    loc=cq.Location(cq.Vector(cx-60, -RAIL_Y+EX, RAIL_Z+EX+CONT_H/2)), color=C_CONT)

# ── STATUS LEDs (3×, rear panel) — CDR-12 ──
led = cq.Workplane("XY").cylinder(LED_H, LED_D/2)
for tag, y, c in [("led_green", 25, C_LED_G), ("led_yellow", 0, C_LED_Y), ("led_red", -25, C_LED_R)]:
    asm.add(led, name=tag,
        loc=cq.Location(cq.Vector(-15, y, RAIL_Z+EX+LED_H/2)), color=c)

# ── CHARGE PORT (Weipu SP17, rear panel) — HM-DWG-001 ──
chg = cq.Workplane("XY").cylinder(15, 10)
asm.add(chg, name="charge_port",
    loc=cq.Location(cq.Vector(-15, -60, RAIL_Z+EX+8)), color=C_DCDC)

# =============================================================================
# EXPORT
# =============================================================================
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
asm.save(OUT_PATH)
sz = os.path.getsize(OUT_PATH) / 1024
print(f"✅ STEP saved: {OUT_PATH}  ({sz:.0f} KB)")
print()
print("📐 Key Dimensions (Phase 1 — v6):")
print(f"   Frame:        {FRAME_L} × {RAIL_Y*2}mm (4 crossbeams, rigid skid)")
print(f"   Rail Z:       {RAIL_Z}mm from ground")
print(f"   Wheelbase:    {FRAME_L}mm")
print(f"   Track:        {TRACK_W}mm (center-to-center)")
print(f"   Wheels:       4× G30 Hub Motor (tire+motor+axle), {TIRE_OD}mm OD")
print(f"   Case:         Apache 3800 ({CASE_L}×{CASE_W}×{CASE_H}mm)")
print(f"   Thermal Deck: {DECK_T}mm Al, Z={tdz:.0f}mm")
print(f"   Motor Plates: NMT-MP-001 ({MP}×{MP}×{MP_T}mm) with axle bore")
print(f"   IMU:          WitMotion WT901SDCL")
print(f"   Parts count:  {len(asm.objects)} named parts")
print()
print("📦 View: drag STEP into https://3dviewer.net")
print("🔩 For manufacturing detail: python3 generate_parts.py")
