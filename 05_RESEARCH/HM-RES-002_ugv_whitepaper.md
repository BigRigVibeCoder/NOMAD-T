# ENGINEERING ARCHITECTURE OF ASYMMETRIC GROUND ROBOTICS (UGV)
**ID:** HM-RES-002
**Status:** REFERENCE (Assimilated into [HM-CAT-001](../02_CATALOG/HM-CAT-001_master_design.md))
**Role:** Technical Theory & Physics Background

---

This design document synthesizes open-source intelligence (OSINT), field engineering reports, and robotics research from the Ukrainian theater (2022–2026). It is structured as a technical white paper for robotics engineers, focusing on the physics, component selection, and "battle-hardened" design patterns that have evolved from the conflict.

# 

---

**WHITE PAPER: ENGINEERING ARCHITECTURE OF ASYMMETRIC GROUND ROBOTICS (UGV)**

**Subject:** Technical Analysis of Ukrainian Combat Robotics (Classes: Loitering Munition, Logistics, ISR)

**Classification:** OPEN SOURCE / TECHNICAL REFERENCE

**Operational Context:** GPS-Denied, EW-Saturated, High-Plasticity Soil (*Chernozem*)

## 

---

**1.0 EXECUTIVE SUMMARY: THE "ATTRITABLE" DOCTRINE**

The conflict in Ukraine has invalidated the Western doctrine of complex, multi-role UGVs (e.g., Rheinmetall Mission Master) in favor of **single-mission, attritable platforms**. The dominant design philosophy is **"Capability per Dollar"**—a platform must cost less than the target it destroys or the logistics chain it replaces.

**Core Engineering Axioms:**

1. **Spectral Silence:** RF emissions are a distinct failure point. Autonomy, frequency hopping, or physical tethering (fiber optics) is mandatory.

2. **Terramechanics First:** The "Rasputitsa" (deep mud) dictates that **Ground Pressure must be &lt; 3.5 psi (24 kPa)**.

3. **The "Garage" Supply Chain:** Designs rely on dual-use COTS (Commercial Off-The-Shelf) components—drone motors, e-bike controllers, and industrial automation sensors—rather than ITAR-restricted defense hardware.

## 

---

**2.0 MECHANICAL ENGINEERING & DYNAMICS**

### **2.1 Terramechanics: Solving for "Rasputitsa"**

Ukrainian black soil (*Chernozem*) behaves as a cohesive-frictional plastic material. Traditional skid-steering requires immense torque to overcome the **Moment of Resistance (**<span data-latex="M_r" data-evaluate="no" data-display="no" data-type="inlineMath">$M_r$</span>**)** during turning, which spikes exponentially in deep mud due to the "bulldozing" effect of lateral soil displacement.

- **Design Constraint (Bekker-Wong Model):**\
  To prevent immobilization, the vehicle's contact patch must satisfy the pressure-sinkage relationship:\
  <span data-latex="p = \left( \frac{k_c}{b} + k_{\phi} \right) z^n" data-evaluate="no" data-display="yes" data-type="inlineMath">$$p = \left( \frac{k_c}{b} + k_{\phi} \right) z^n$$</span>


- *Where:* <span data-latex="p" data-evaluate="no" data-display="no" data-type="inlineMath">$p$</span> is pressure, <span data-latex="b" data-evaluate="no" data-display="no" data-type="inlineMath">$b$</span> is track/wheel width, <span data-latex="z" data-evaluate="no" data-display="no" data-type="inlineMath">$z$</span> is sinkage, and <span data-latex="n" data-evaluate="no" data-display="no" data-type="inlineMath">$n$</span> is the soil deformation exponent (0.3–0.5 for wet clay).

- **Implication:** Narrow wheels create "rut lock." **Wide pneumatic tires (balloon tires)** or **conveyor-belt tracks** are mandatory to increase <span data-latex="b" data-evaluate="no" data-display="no" data-type="inlineMath">$b$</span> and reduce <span data-latex="z" data-evaluate="no" data-display="no" data-type="inlineMath">$z$</span>.


- **Traction Physics (Janosi-Hanamoto Shear):**\
  Slick tires fail instantly. To mobilize soil shear strength, the tread design must use deep paddles (&gt;25mm).


- *Field Hack:* Ukrainian engineers often bolt aluminum U-channel profiles horizontally across rubber conveyor belts to create aggressive grousers that self-clean.

### **2.2 Chassis Topology & Materials**

- **The "Disposable" Class (Kamikaze/Mine-Laying):**


- **Material:** **Mild Steel Square Tubing (20x20mm, 2mm wall)**.

- **Why:** Unlike aluminum, steel absorbs vibration better without fatigue cracking and can be repaired in forward trenches using standard stick welders. Weight is an asset for traction.


- **The "Logistics" Class (Medevac/Resupply):**


- **Material:** **6061-T6 Aluminum** rails with **HDPE (High-Density Polyethylene)** body panels. HDPE is RF-transparent, waterproof, and does not shatter into shrapnel when hit.

- **Armor:** **Hardox 450/500** wear plates (4-6mm) are used *only* to shield the battery and compute core.

## 

---

**3.0 PROPULSION & POWER ELECTRONICS**

### **3.1 Motor Architecture**

- **Tier 1: The "Hoverboard Hack" (Light UGV &lt;100kg):**


- **Source:** Repurposed 10-inch brushless hub motors from hoverboards (350W–1000W).

- **Engineering:** The stock tires are removed. Custom steel flanges are welded or bolted to the magnet bell to drive tracks or mount ATV tires.

- **Pros:** IP54 sealed, high torque density, extremely cheap ($30/unit).


- **Tier 2: The "Professional" (Heavy UGV &gt;150kg):**


- **Source:** Large format brushless outrunners (e.g., **6384 or 80100 size, 130–190 KV**).

- **Transmission:** Direct drive fails in mud. Successful designs use **Planetary Gearboxes** (10:1 to 50:1 reduction) or industrial chain drives (#35 chain).

- **Cooling:** Motors must be **potted** (stator filled with thermal epoxy) and thermally bridged to the aluminum chassis to dissipate heat without airflow.

### **3.2 Electronic Speed Controllers (ESC)**

- **VESC Architecture:** The **VESC 6.0 / 75100** is the gold standard for robotics.


- **Feature:** **Field Oriented Control (FOC)** drives the motor with a sine wave rather than a trapezoidal wave.

- **Tactical Advantage:** **Silent Drive.** FOC eliminates the high-pitched "whine" of brushless motors, reducing the acoustic signature by \~80%.

### **3.3 Energy Storage & The "Vampire" BMS**

- **Chemistry:** **Li-Ion 21700** (Samsung 40T / Molicel P42A) for high discharge rates. **LiFePO4** is used only for logistics mules where fire safety &gt; weight.

- **The Hack:** Standard Battery Management Systems (BMS) cut power during current spikes (e.g., fighting out of a mud pit).


- *Modification:* The discharge path **bypasses the BMS MOSFETs**. The BMS monitors cell health/charging but cannot cut power to the motors. **Destroying the battery is an acceptable cost; stopping in the kill zone is not.**

## 

---

**4.0 CONTROL ARCHITECTURE & AUTONOMY**

### **4.1 Flight Controller (Low-Level)**

Ground robots have standardized on aerial drone controllers due to the maturity of the ArduPilot ecosystem.

- **Hardware:** **Cube Orange+** (STM32H7) or **SpeedyBee F405 V3**.

- **Firmware:** **ArduPilot (ArduRover)**.

- **Tuning Note:** The ATC_STR_RAT (Steering Rate) P and I gains must be set aggressively high to overcome the static friction of mud.

### **4.2 Navigation in GPS-Denied Environments**

Russian EW systems (Pole-21, Zhitel) spoof or jam GNSS.

- **Visual Odometry (VO):** The robot estimates position by tracking feature points in video frames.


- *Hardware:* **Intel RealSense** or **Luxonis OAK-D** cameras.

- *Software:* **ROS 2** nodes running **VINS-Fusion** or **ORB-SLAM3** on an **Nvidia Jetson Orin Nano**.


- **Optical Flow:** Downward-facing sensors (ThoneFlow) provide "velocity hold" to prevent drift when GPS lock is lost.

## 

---

**5.0 SIGNALS & ELECTRONIC WARFARE (EW)**

### **5.1 The "Fiber Optic" Revolution**

For the "Zero Line" (direct contact zone), radio control is obsolete.

- **System:** A lightweight spool (5km–10km) of single-mode fiber dispenses from the *rear* of the UGV.

- **Advantages:**

1. **Spectral Invisibility:** Cannot be detected by SIGINT.

2. **Jamming Immunity:** 100% physically secure link.

3. **Bandwidth:** Uncompressed HD video with &lt;5ms latency.

### **5.2 RF Fallback (ExpressLRS)**

When wireless is necessary, **ExpressLRS (ELRS)** is the standard.

- **Frequency:** **915 MHz** (or custom 750MHz to avoid standard jamming bands).

- **Configuration:** **Gemini Mode** (Dual-frequency diversity) transmits packets on two frequencies simultaneously to defeat comb filters.

- **Video:** **1.2 GHz Analog**. Digital (5.8GHz) fails in foliage; 1.2GHz diffracts (bends) better over terrain and trenches.

## 

---

**6.0 REFERENCE DESIGN: "BADGER-M" (Logistics/Kamikaze)**

<table style="min-width: 441px;">
<colgroup><col style="min-width: 25px;"><col style="width: 208px;"><col style="width: 208px;"></colgroup><tbody><tr><td colspan="1" rowspan="1"><p><strong>Subsystem</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p><strong>Specification</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p><strong>Rationale</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Chassis</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>Welded 25x25mm Steel Box Section</p></td><td colspan="1" rowspan="1" colwidth="208"><p>Field repairable, cheap, heavy for traction.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Drive</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>4WD Skid Steer</p></td><td colspan="1" rowspan="1" colwidth="208"><p>Simple, zero turn radius.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Motors</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>4x 10" Hoverboard Motors (Rewound)</p></td><td colspan="1" rowspan="1" colwidth="208"><p>Sealed against mud. Cheap ($30/ea).</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>ESC</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>2x Dual VESC 75100</p></td><td colspan="1" rowspan="1" colwidth="208"><p>FOC Silent Mode.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Brain</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>SpeedyBee F405 V3</p></td><td colspan="1" rowspan="1" colwidth="208"><p>Running ArduRover.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Control Link</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>ELRS 915MHz Diversity (Radiomaster RP3)</p></td><td colspan="1" rowspan="1" colwidth="208"><p>High penetration, low latency.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Video</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>1.3GHz 1.5W VTX + Caddx Ratel 2</p></td><td colspan="1" rowspan="1" colwidth="208"><p>"Night Eagle" version for low-light ops.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Payload</strong></p></td><td colspan="1" rowspan="1" colwidth="208"><p>Galvanic Release Mechanism</p></td><td colspan="1" rowspan="1" colwidth="208"><p>Solenoid releases latch; gravity drops mine.</p></td></tr></tbody>
</table>

## **7.0 CRITICAL ENGINEERING FIELD NOTES**

1. **Potting:** Conformal coating is insufficient. ESCs and receivers must be "potted" (encased) in **Neutral-Cure Silicone** or thermally conductive epoxy. *Warning:* Acetic cure silicone (smells like vinegar) releases acid that corrodes electronics.

2. **Thermal Bridging:** Bolting ESCs directly to the chassis frame uses the entire robot body as a heatsink.

3. **Failsafe Logic:** Set FS_ACTION to **"Hold"** or **"Smart_RTL"**. Standard "RTL" (Return to Launch) can trigger fly-aways in spoofed GPS environments. "Hold" allows the operator to regain control via a directional antenna.

4. **Low Profile:** Height is death. The robot should be no taller than the tall grass of the Steppe (\~40cm).