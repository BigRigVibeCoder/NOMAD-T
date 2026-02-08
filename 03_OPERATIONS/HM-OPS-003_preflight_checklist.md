---
ID: HM-OPS-003
Status: ACTIVE
Date: 2026-02-08
Role: Pre-Flight Checklist (Field Operations)
Linked: HM-OPS-002 (Safety), HM-DWG-001
---

# Nomad-T Pre-Flight Checklist

> **Laminate this page and keep it with the robot.**
> Complete EVERY item before EVERY field deployment.

---

## ✅ VISUAL INSPECTION

- [ ] Frame bolts: No loose or missing fasteners
- [ ] Motor plates: Axle nuts tight, no play
- [ ] Wheels: No cuts, bulges, or flat spots on tires
- [ ] Shear panels: No cracks, all bolts present
- [ ] Case: Latches closed, cable glands sealed
- [ ] Wiring: No chafing, exposed copper, or pinched cables

---

## ✅ TIRE PRESSURE

- [ ] All 4 tires inflated to **5-8 PSI** (Low = Off-road, High = Pavement)
- [ ] No visible deflation or soft spots

---

## ✅ BATTERY

- [ ] Battery voltage: **> 34V** (Measured at XT90-S before connecting)
- [ ] If < 34V: **CHARGE BEFORE DEPLOYING** (Yellow LED will warn)
- [ ] If < 32V: **DO NOT DEPLOY** — Deep discharge risk
- [ ] XT90-S connector: Clean, no melting, pins straight

---

## ✅ FUSE CHECK

- [ ] 60A MIDI Fuse: Visually intact (no discoloration or blown indicator)
- [ ] Fuse holder: Bolts tight, no corrosion
- [ ] Spare fuses: 2× stowed in case lid pocket

---

## ✅ SAFETY SYSTEMS

- [ ] E-Stop: **PRESSED** before connecting battery
- [ ] Connect battery → Red LED = ON (Safety Active)
- [ ] DC-DC Output: **17V** (Spot-check with multimeter if first run of the day)
- [ ] Release E-Stop → Contactor CLICKS → Red LED OFF
- [ ] Green LED: ON after ROS boot (wait 30-60 seconds)
- [ ] **Motor Test:** Briefly jog each wheel forward/reverse via teleop. Verify direction.

---

## ✅ COMMS CHECK

- [ ] WiFi connected: `ping <robot_ip>` from laptop
- [ ] SSH access: `ssh user@<robot_ip>`
- [ ] ROS topics: `ros2 topic list` shows expected topics
- [ ] Joystick/RC: Teleop responds to input

---

## ✅ SENSOR CHECK

- [ ] LiDAR: Spinning (audible/visual)
- [ ] Camera: `ros2 topic hz /camera/image_raw` > 0
- [ ] IMU: `ros2 topic echo /imu/data` — values change when tilted
- [ ] IR Sensors: Front/Rear respond to hand wave

---

## 🚀 CLEARED FOR DEPLOYMENT

**Date:** _______________
**Operator:** _______________
**Battery Voltage:** _______ V
**Weather:** _______________
**Notes:** _______________________________________________

---

## 🛑 POST-MISSION

- [ ] Press E-Stop
- [ ] Disconnect XT90-S
- [ ] Record battery voltage: _______ V
- [ ] Inspect tires for debris/damage
- [ ] Wipe down frame and sensors
- [ ] Charge battery if < 36V
- [ ] Log any anomalies: _______________________________________
