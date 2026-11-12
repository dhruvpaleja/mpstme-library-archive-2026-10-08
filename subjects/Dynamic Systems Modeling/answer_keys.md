# Dynamic Systems Modeling: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper d48d2635226a

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Mechatronics_7004/Dynamic Systems Modeling/ANS_Dynamic Systems Modeling(702MH0C025)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 May 2026
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Dynamic Systems Modeling
Date: 06 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1 (a) — Constraints & DOF [5 marks]
• Holonomic: constraints expressible as f(q₁, q₂, ..., t) = 0. Example: pendulum (L = const) [1.5]
• Non-holonomic: involve velocities, cannot be integrated. Example: rolling disk (v_contact = 0) [1.5]
• DOF = n × f − c, where n = number of bodies, f = freedom per body, c = constraints [1]
• Constraints reduce DOF: each independent constraint removes one degree of freedom [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q1 (b) — Position-Velocity-Acceleration [5 marks]
• Given: x(t) = 4t³ − 2t; y(t) = 5t² + 3; at t = 2 s
•   r(2) = (4(8) − 4)î + (5(4) + 3)ĵ = 28î + 23ĵ m; |r| = √(784 + 529) = √1313 = 36.24 m [1.5]
• v = (12t² − 2)î + 10t ĵ → v(2) = 46î + 20ĵ m/s; speed = √(2116 + 400) = √2516 = 50.16 m/s [1.5]
• a = 24t î + 10 ĵ → a(2) = 48î + 10ĵ m/s²; |a| = √(2304 + 100) = √2404 = 49.03 m/s² [2]
───────────────────────────────────────────────────────────────────────────────────────────────
Q1 (c) — Block on 40° Incline [5 marks]
• Given: m = 2 kg, θ = 40°, μ_k = 0.3, from rest
• N = mg cos 40° = 2(9.81)(0.766) = 15.03 N [1.5]
• f_k = μ_k N = 0.3(15.03) = 4.51 N [1.5]
• a = g(sin 40° − μ_k cos 40°) = 9.81(0.6428 − 0.2298) = 9.81 × 0.4130 = 4.05 m/s² [2]
───────────────────────────────────────────────────────────────────────────────────────────────
Q1 (d) — Spinning Disk [5 marks]
• Given: m = 5 kg, R = 0.2 m, α = 3.75 rad/s², starts from rest
•   I = ½mR² = ½(5)(0.04) = 0.1 kg·m² [1]
• ω(2) = αt = 3.75 × 2 = 7.5 rad/s [1]
• At rim: a_t = αR = 3.75 × 0.2 = 0.75 m/s² [1]
• a_n = ω²R = 56.25 × 0.2 = 11.25 m/s² [1]
•   |a_total| = √(0.75² + 11.25²) = √(0.5625 + 126.5625) = √127.125 = 11.27 m/s² [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q2 — Constrained Motion & Pulleys [20 marks]
Q2 (a) — Vertical Loop R = 8 m [5 marks]
• Given: R = 8 m, m = 2 kg, v_bottom = 22 m/s
• v_bottom_min = √(5gR) = √(5 × 9.81 × 8) = √392.4 = 19.81 m/s [1.5]
• At top: ½mv²_bottom = ½mv²_top + 2mgR → v²_top = 484 − 4(9.81)(8) = 484 − 313.92 = 170.08 [1.5]
********** 1 **********
--- page 2 ---
• N_top = mv²_top/R − mg = 2(170.08)/8 − 2(9.81) = 42.52 − 19.62 = 22.90 N [2]
Q2 (b) — 6-Pulley System [5 marks]
• Given: 6 pulleys, η = 0.92 each, m = 2000 kg, h = 3 m
• MA = 6; η_total = 0.92⁶ = 0.6065 [1]
• F_ideal = 2000(9.81)/6 = 3270.0 N; F_actual = 3270.0/0.6065 = 5392.4 N [1.5]
• W_out = 2000(9.81)(3) = 58860 J [0.5]
• W_in = F_actual × (6 × 3) = 5392.4 × 18 = 97063.2 J [1]
• Heat = 97063.2 − 58860.0 = 38203.2 J ≈ 38.2 kJ [1]
Q2 (c) — Atwood m₁ = 7, m₂ = 5 [5 marks]
• a = (7 − 5)(9.81)/(7 + 5) = 2(9.81)/12 = 1.635 m/s² [1.5]
• T = 2m₁m₂g/(m₁ + m₂) = 2(7)(5)(9.81)/12 = 57.225 N [1.5]
• v(2 s) = 1.635 × 2 = 3.27 m/s [1]
• Check: m₂g = 49.05 < T = 57.23 < m₁g = 68.67 ✓ [1]
Q2 (d) — CNC 3D Path [5 marks]
• Given: P₀ = (10, 20, 5), P₁ = (110, 70, 35) mm, F = 50 mm/s
• ΔP = (100, 50, 30); d = √(10000 + 2500 + 900) = √13400 = 115.76 mm [1.5]
• û = (100, 50, 30)/115.76 = (0.864, 0.432, 0.259) [1]
• Axis speeds: v_x = 43.20, v_y = 21.60, v_z = 12.96 mm/s [1.5]
•   t = 115.76/50 = 2.315 s [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q3 — Vibrations & Rolling [20 marks]
Q3 (a) — Log Decrement [5 marks]
• Given: x₁ = 20 mm, x₂ = 15 mm, T_d = 0.35 s, m = 2 kg
• δ = ln(x₁/x₂) = ln(20/15) = ln(1.333) = 0.2877 [1]
• ζ = δ/√(4π² + δ²) = 0.2877/√(39.478 + 0.0828) = 0.2877/6.290 = 0.0457 [1.5]
• ω_d = 2π/T_d = 2π/0.35 = 17.952 rad/s [0.5]
• ω_n = ω_d/√(1 − ζ²) = 17.952/0.9990 = 17.971 rad/s → f_n = 2.860 Hz [1]
• k = mω_n² = 2(17.971²) = 2(322.96) = 645.9 N/m [1]
Q3 (b) — Rolling Wheel Acceleration [5 marks]
• Given: R = 0.4 m, v_center = 3.0 m/s, a_center = 1.5 m/s²
• ω = v/R = 3.0/0.4 = 7.5 rad/s; α = a/R = 1.5/0.4 = 3.75 rad/s² [1]
• Top point: a_tang = αR = 1.5 m/s² (backward); a_cent = ω²R = 22.5 m/s² (toward center) [1.5]
• a_top = a_center + a_tang + a_cent: net = (1.5 − 1.5)î + (−22.5)ĵ → |a_top| = 22.5 m/s² (downward) [1]
• Bottom point: a_tang = 1.5 m/s² (forward); a_cent = 22.5 m/s² (upward) [0.5]
• a_bottom = (1.5 + 1.5)î + 22.5ĵ = 3.0î + 22.5ĵ → |a_bottom| = √(9 + 506.25) = 22.70 m/s² [1]
Q3 (c) — Spinning Disk with Viscous Friction [5 marks]
• Given: m = 5 kg, R = 0.3 m, τ_applied = 2 N·m, c = 0.5 N·m·s/rad
•   I = ½mR² = ½(5)(0.09) = 0.225 kg·m² [1.5]
• Time constant τ_d = I/c = 0.225/0.5 = 0.45 s [1.5]
• Steady-state: Iα = 0 → τ = cω_ss → ω_ss = 2/0.5 = 4.0 rad/s [2]
Q3 (d) — Gear Train [5 marks]
• Given: Stage 1: 15T → 45T; Stage 2: 12T → 60T; Motor: 1500 RPM, 0.5 N·m
• GR₁ = 45/15 = 3; GR₂ = 60/12 = 5; Total GR = 15 [1]
• ω_out = 1500/15 = 100 RPM = 10.47 rad/s [1]
• τ_out = 0.5 × 15 = 7.5 N·m (ideal) [1]
********** 2 **********
--- page 3 ---
• P_in = 0.5 × 2π(1500)/60 = 0.5 × 157.08 = 78.54 W [1]
• P_out = τ_out × ω_out = 7.5 × 10.47 = 78.54 W → Power conserved ✓ [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q4 — Rigid Body Kinematics [20 marks]
Q4 (a) — Rigid Body Velocity Formula [5 marks]
• v_P = v_center + ω × r_P/C [1]
• v_center: translational velocity of the body's center of mass [1]
• ω × r: rotational contribution — velocity due to angular velocity [1]
•   r is position vector from center of mass to point P [0.5]
• For rolling: v_contact = v_center + ω × (−R ĵ) = v_center − ωR = 0 → v_center = ωR [1.5]
Q4 (b) — Rotation Matrices & Gimbal Lock [5 marks]
• R_x(α): rotation about x-axis — [[1,0,0],[0,cosα,−sinα],[0,sinα,cosα]] [1]
• R_y(β): rotation about y-axis — [[cosβ,0,sinβ],[0,1,0],[−sinβ,0,cosβ]] [0.5]
• R_z(γ): rotation about z-axis — [[cosγ,−sinγ,0],[sinγ,cosγ,0],[0,0,1]] [0.5]
• Gimbal lock: at β = ±90°, the first and third axes align → loss of one DOF [1.5]
• Quaternions: q = (w, x, y, z) with |q| = 1; interpolation is smooth, no singularity [1.5]
Q4 (c) — Rolling Wheel Velocities [5 marks]
• Given: R = 0.5 m, v_center = 2.0 m/s (right), rolling without slipping
• ω = v/R = 2.0/0.5 = 4.0 rad/s [1]
• Top: v = v_center + ωR = 2.0 + 2.0 = 4.0 m/s (rightward) [1]
• Bottom (contact): v = v_center − ωR = 2.0 − 2.0 = 0 m/s [1]
• Right: v = v_center(→) + ωR(↓) = 2.0î − 2.0ĵ; |v| = 2√2 = 2.83 m/s at 45° below horizontal [2]
Q4 (d) — Rotating Rod [5 marks]
• Given: L = 1.0 m, ω = 5 rad/s, α = 2 rad/s², pivot at one end
• Free end (r = 1.0): v = ωr = 5 m/s; a_t = αr = 2 m/s²; a_n = ω²r = 25 m/s²; |a| = √(4 + 625) = 25.08 m/s² [2]
• Midpoint (r = 0.5): v = 2.5 m/s; a_t = 1.0; a_n = 12.5; |a| = √(1 + 156.25) = 12.54 m/s² [1.5]
•   r = 0.3: v = 1.5 m/s; a_t = 0.6; a_n = 7.5; |a| = √(0.36 + 56.25) = 7.52 m/s² [1.5]
───────────────────────────────────────────────────────────────────────────────────────────────
Q5 — Energy & Momentum [20 marks]
Q5 (a) — Work-Energy Theorem [5 marks]
• W_net = ΔKE = ½mv₂² − ½mv₁² [1]
• Conservative force: path-independent work; has potential energy (gravity, spring) [1]
• Non-conservative: path-dependent (friction, drag) [1]
• Modified: W_conservative + W_non-conservative = ΔKE → ΔKE + ΔPE = W_nc [2]
Q5 (b) — Impulse-Momentum [5 marks]
• Impulse: J = ∫F dt = F_avg × Δt; Momentum: p = mv [1]
• Impulse-momentum theorem: J = Δp = mv₂ − mv₁ [1]
• Coefficient of restitution: e = (v₂B − v₂A)/(v₁A − v₁B) for collision [1]
• Conservation: if ΣF_ext = 0, then Σm_i v_i = constant (isolated system) [2]
Q5 (c) — Car Acceleration [5 marks]
• Given: m = 1200 kg, v₁ = 20 m/s, v₂ = 40 m/s, t = 8 s, F_drag = 400 N
• a = (40 − 20)/8 = 2.5 m/s²; F_net = ma = 1200 × 2.5 = 3000 N [1]
• F_engine = F_net + F_drag = 3000 + 400 = 3400 N [1]
• W_engine = F_engine × 0.5(v₁ + v₂) × t = 3400 × 30 × 8 = 816000 J [0.5]
• P_avg = W/t = 816000/8 = 102000 W = 102 kW [1]
********** 3 **********
--- page 4 ---
• P_inst(40 m/s) = F_engine × v = 3400 × 40 = 136000 W = 136 kW [1.5]
Alternative: P_avg = F_engine × v_avg = 3400 × 30 = 102 kW ✓
Q5 (d) — Collision [5 marks]
• Given: m_A = m_B = 2 kg, v_A1 = 6 m/s, v_B1 = 0, e = 0.5
• Momentum: 2(6) = 2v_A2 + 2v_B2 → v_A2 + v_B2 = 6 [1]
•   Restitution: e = (v_B2 − v_A2)/(v_A1 − v_B1) → 0.5 = (v_B2 − v_A2)/6 → v_B2 − v_A2 = 3 [1]
• Solving: v_A2 = 1.5 m/s, v_B2 = 4.5 m/s [1]
• Impulse: J = m_B(v_B2) = 2(4.5) = 9 N·s [1]
• KE_loss = ½(2)(36) − ½(2)(2.25 + 20.25) = 36 − 22.5 = 13.5 J [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q6 — FBD + Difficult Numerical [20 marks]
Q6 (a) — Mobile Manipulator [10 marks]
• Given: v_AGV = 0.5 m/s, L = 1.2 m, θ = 30° from vertical, dθ/dt = −0.2 rad/s, m = 2.5 kg
FBD [4 marks]:
• Weight W = 2.5(9.81) = 24.525 N (downward) [1]
• Arm reaction force at pivot (internal force balancing) [1]
• Centripetal and Coriolis forces in rotating frame [2]
Velocity Calculation [3 marks]:
• Tip position relative to AGV: x_tip = L sin θ = 1.2 sin 30° = 0.6 m, y_tip = L cos θ = 1.2 cos 30° = 1.039 m [1]
• v_tip_x = v_AGV + L cos θ × dθ/dt = 0.5 + 1.2(0.866)(−0.2) = 0.5 − 0.2078 = 0.292 m/s [1]
• v_tip_y = −L sin θ × dθ/dt = −1.2(0.5)(−0.2) = +0.12 m/s [0.5]
•   |v_tip| = √(0.292² + 0.12²) = √(0.0853 + 0.0144) = √0.0997 = 0.316 m/s [0.5]
Vibration Isolator [3 marks]:
• ω_n = √(k/m) = √(1000/2.5) = √400 = 20 rad/s → f_n = 3.18 Hz [1.5]
• c_cr = 2√(km) = 2√(1000 × 2.5) = 2√2500 = 100 N·s/m [0.5]
• ζ = c/c_cr = 40/100 = 0.4 → underdamped [1]
Q6 (b) — CNC Trapezoidal Profile [10 marks]
• Given: d = 200 mm, v_max = 100 mm/s, a = 500 mm/s²
200 mm move (trapezoidal) [5 marks]:
• t_acc = v_max/a = 100/500 = 0.2 s; d_acc = ½ × a × t² = ½(500)(0.04) = 10 mm [1.5]
• d_cruise = 200 − 2(10) = 180 mm; t_cruise = 180/100 = 1.8 s [1.5]
•   t_total = 0.2 + 1.8 + 0.2 = 2.2 s [2]
15 mm move (triangular) [5 marks]:
• Check: d_min_trap = 2 × v_max²/(2a) = v_max²/a = 10000/500 = 20 mm > 15 mm → triangular [1.5]
• v_peak = √(a × d/2) = √(500 × 7.5) = √3750 = 61.24 mm/s [1.5]
• t_acc = v_peak/a = 61.24/500 = 0.1225 s; t_total = 2 × 0.1225 = 0.245 s [2]
───────────────────────────────────────────────────────────────────────────────────────────────
Q7 — FBD + Difficult Numerical [20 marks]
Q7 (a) — Spring-Mass-Damper Full Analysis [10 marks]
• Given: m = 2 kg, k = 500 N/m, c = 20 N·s/m, x₀ = 0.1 m, v₀ = 0
FBD [3 marks]:
• In displaced position: Spring force kx (restoring, toward equilibrium) [1]
• Damping force cẋ (opposing velocity) [1]
• Weight and normal cancel about equilibrium point [1]
EOM and classification [4 marks]:
• mẍ + cẋ + kx = 0 → 2ẍ + 20ẋ + 500x = 0 → ẍ + 10ẋ + 250x = 0 [1]
********** 4 **********
--- page 5 ---
• ω_n = √(250) = 15.81 rad/s; c_cr = 2√(km) = 63.25 N·s/m [1]
• ζ = 20/63.25 = 0.316 → Underdamped [1]
• ω_d = 15.81√(1 − 0.0999) = 15.81 × 0.9487 = 15.00 rad/s [1]
Free response [3 marks]:
•   x(t) = e^(−5t)[A cos(15t) + B sin(15t)] [1]
• IC: x(0) = 0.1 → A = 0.1; ẋ(0) = 0 → B = (ζω_n/ω_d) × A = (5/15)(0.1) = 0.0333 [1]
•   x(t) = e^(−5t)[0.1 cos(15t) + 0.0333 sin(15t)] m [1]
Q7 (b) — Double Pendulum [10 marks]
• Given: m₁ = m₂ = 1 kg, L₁ = L₂ = 1 m
Kinetic and Potential Energy [4 marks]:
• T = ½m₁L₁²θ̇₁² + ½m₂[L₁²θ̇₁² + L₂²θ̇₂² + 2L₁L₂θ̇₁θ̇₂ cos(θ₁ − θ₂)] [2]
• V = −m₁gL₁ cos θ₁ − m₂g(L₁ cos θ₁ + L₂ cos θ₂) [2]
Euler-Lagrange equations [4 marks]:
• For θ₁: (m₁ + m₂)L₁²θ̈₁ + m₂L₁L₂θ̈₂ cos(θ₁ − θ₂) + m₂L₁L₂θ̇₂² sin(θ₁ − θ₂) + (m₁ + m₂)gL₁ sin θ₁ = 0 [2]
• For θ₂: m₂L₂²θ̈₂ + m₂L₁L₂θ̈₁ cos(θ₁ − θ₂) − m₂L₁L₂θ̇₁² sin(θ₁ − θ₂) + m₂gL₂ sin θ₂ = 0 [2]
Small-angle linearization and chaos [2 marks]:
• Linearized form (sin θ ≈ θ, cos Δθ ≈ 1): 2θ̈₁ + θ̈₂ + 2g θ₁ = 0; θ̈₂ + θ̈₁ + g θ₂ = 0 [1]
• The double pendulum is a canonical example of deterministic chaos: sensitive to initial conditions, large-angle motion appears
random despite deterministic equations [1]
─────────────────────────────────────────
********** 5 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 1f306aa89a0b

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Mechatronics_7004/Dynamic Systems Modeling/ANS_Dynamic Systems Modeling(702MH0C025)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2026
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Dynamic Systems Modeling
Date: 02 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1 (a) — Definitions [5 marks]
•   (i) DOF: In 2D, a rigid body has 3 DOF (x, y, θ); in 3D, it has 6 DOF (x, y, z + three rotational angles). DOF = total coordinates −
number of constraints. [1.5]
•   (ii) Rolling without slipping: v_cm = ωR. The contact point has zero velocity relative to the surface. Example: car wheel on road.
[2]
•   (iii) Instantaneous Center of Rotation (ICR): A point on or off the body about which all points appear to rotate at that inst ant.
Example: contact point of a rolling wheel. [1.5]
───────────────────────────────────────────────────────────────────────────────────────────────
Q1 (b) — Projectile Motion [5 marks]
• Given: v_x0 = 12 m/s, v_y0 = 16 m/s, g = 9.81 m/s²
• h_max = v_y0²/(2g) = 256 / 19.62 = 13.05 m [1]
• t_peak = v_y0/g = 16/9.81 = 1.631 s; Total T = 2 × 1.631 = 3.262 s [1]
• Range R = v_x0 × T = 12 × 3.262 = 39.14 m [1]
• At t = 1 s: v_x = 12 m/s, v_y = 16 − 9.81(1) = 6.19 m/s [1]
• Speed = √(12² + 6.19²) = √(144 + 38.32) = √182.32 = 13.50 m/s [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q1 (c) — Atwood Machine [5 marks]
• Given: m₁ = 5 kg, m₂ = 3 kg, g = 9.81 m/s²
• a = (m₁ − m₂)g / (m₁ + m₂) = (2)(9.81)/8 = 2.453 m/s² [1.5]
• T = 2m₁m₂g / (m₁ + m₂) = 2(5)(3)(9.81)/8 = 36.79 N [1.5]
• v(1.5 s) = a × t = 2.453 × 1.5 = 3.68 m/s [1]
• Check: m₂g = 29.43 N < T = 36.79 N < m₁g = 49.05 N ✓ [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q1 (d) — Work-Energy on Incline [5 marks]
• Given: m = 3 kg, θ = 35°, μ_k = 0.25, s = 4 m, v₀ = 0
• N = mg cos 35° = 3(9.81)(0.8192) = 24.11 N [1]
• W_gravity = mgs sin 35° = 3(9.81)(4)(0.5736) = 67.51 J [1]
• W_friction = −μ_k N s = −0.25(24.11)(4) = −24.11 J [1]
• W_net = 67.51 − 24.11 = 43.40 J [1]
• ½mv² = W_net → v = √(2 × 43.40 / 3) = √28.93 = 5.38 m/s [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q2 — Particle Kinetics [20 marks]
********** 1 **********
--- page 2 ---
Q2 (a) — Frictionless Incline [5 marks]
• Given: m = 5 kg, θ = 30°, v₀ = 10 m/s up, frictionless
• a = −g sin 30° = −9.81 × 0.5 = −4.905 m/s² (decelerating) [1]
• d = v₀² / (2 × 4.905) = 100 / 9.81 = 10.19 m [2]
•   t = v₀ / 4.905 = 10 / 4.905 = 2.039 s [2]
Q2 (b) — Block and Tackle [5 marks]
• Given: 4 pulleys, η = 0.95 each, m_load = 200 kg, h = 2 m
• MA_ideal = 4; η_total = 0.95⁴ = 0.8145 [1]
• F_ideal = 200(9.81)/4 = 490.5 N [1]
• F_actual = F_ideal / η_total = 490.5 / 0.8145 = 602.2 N [1]
• W_in = F_actual × (4 × 2) = 602.2 × 8 = 4817.6 J [1]
• W_out = mgh = 200(9.81)(2) = 3924.0 J; Heat = 4817.6 − 3924.0 = 893.6 J [1]
Q2 (c) — Vertical Circular Loop [5 marks]
• Given: R = 2 m, m = 1 kg, v_bottom = 12 m/s
• v_top_min = √(gR) = √(9.81 × 2) = 4.43 m/s (when N_top = 0) [1]
• v_bottom_min = √(5gR) = √(5 × 9.81 × 2) = √98.1 = 9.90 m/s [1]
• Energy conservation: ½mv²_bottom = ½mv²_top + 2mgR
• v²_top = 144 − 4(9.81) = 144 − 39.24 = 104.76; v_top = 10.24 m/s [1]
• N_bottom = mv²/R + mg = 1(144)/2 + 9.81 = 72 + 9.81 = 81.81 N [2]
N_top = mv²_top/R − mg = 1(104.76)/2 − 9.81 = 52.38 − 9.81 = 42.57 N
Q2 (d) — Movable Pulley [5 marks]
• Given: m_load = 50 kg, F = 300 N applied
• For constant velocity: F = W/2 = 50(9.81)/2 = 245.25 N [2]
• For F = 300 N: Net force = 2F − mg = 600 − 490.5 = 109.5 N [1.5]
• a = 109.5 / 50 = 2.19 m/s² [1.5]
───────────────────────────────────────────────────────────────────────────────────────────────
Q3 — Rigid Body & Vibrations [20 marks]
Q3 (a) — Rolling Race [5 marks]
• For rolling objects: a = g sin θ / (1 + β), where β = I/(mR²)
• Sphere: β = 2/5 → a = 9.81 sin 30° / 1.4 = 4.905 / 1.4 = 3.504 m/s² [1]
• Disk: β = 1/2 → a = 4.905 / 1.5 = 3.270 m/s² [1]
• Cylinder (hollow): β = 1 → a = 4.905 / 2 = 2.453 m/s² [1]
• Time (t = √(2s/a)): Sphere: 1.689 s, Disk: 1.749 s, Cylinder: 2.019 s [1]
• Velocity (v = √(2as)): Sphere: 5.92 m/s, Disk: 5.72 m/s, Cylinder: 4.95 m/s [0.5]
• Winner: Solid sphere (lowest β → highest acceleration) [0.5]
Q3 (b) — Physical Pendulum [5 marks]
• Given: rod m = 2 kg, L = 1 m, pivot at end
• I_O = mL²/3 = 2(1)/3 = 0.667 kg·m² [1]
• d (pivot to CG) = L/2 = 0.5 m [0.5]
• ω_n = √(mgd/I_O) = √(2 × 9.81 × 0.5 / 0.667) = √(14.72) = 3.836 rad/s [1.5]
• T = 2π/ω_n = 2π/3.836 = 1.638 s [1]
• Simple pendulum (same L): T_s = 2π√(1/9.81) = 2.006 s → Physical is 18.4% faster [1]
Q3 (c) — Undamped Spring-Mass [5 marks]
• Given: m = 2 kg, k = 200 N/m, x₀ = 0.1 m, v₀ = 0
• ω_n = √(k/m) = √(200/2) = √100 = 10 rad/s [1]
• f_n = ω_n/(2π) = 10/6.283 = 1.592 Hz; T = 1/f_n = 0.628 s [1]
********** 2 **********
--- page 3 ---
• v_max = ω_n × x₀ = 10 × 0.1 = 1.0 m/s [1.5]
• E_total = ½kx₀² = ½(200)(0.01) = 1.0 J [1.5]
Q3 (d) — Spring-Mass-Damper Classification [5 marks]
• Given: m = 2 kg, k = 500 N/m, c = 20 N·s/m
• ω_n = √(500/2) = √250 = 15.81 rad/s [1]
• c_cr = 2√(km) = 2√(1000) = 63.25 N·s/m [1]
• ζ = c/c_cr = 20/63.25 = 0.316 → Underdamped (ζ < 1) [1]
• ω_d = ω_n √(1 − ζ²) = 15.81 × √(1 − 0.0999) = 15.81 × 0.9487 = 15.00 rad/s [1]
• Amplitude envelope: e^(−ζω_n t) = e^(−5t); For 10%: t = ln(10)/5 = 0.461 s [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q4 — Rotating Frames [20 marks]
Q4 (a) — Transport Theorem [5 marks]
• Statement: (dA/dt)_fixed = (dA/dt)_rotating + Ω × A for any vector A [2]
• Velocity relation: v_fixed = v_rel + Ω × r + v_origin
•   v_rel: velocity measured in rotating frame [1]
• Ω × r: velocity due to rotation of the frame itself [1]
• v_origin: velocity of the rotating frame's origin [1]
Q4 (b) — Acceleration in Rotating Frame [5 marks]
• a_fixed = a_rel + 2Ω × v_rel + Ω × (Ω × r) + α × r + a_origin [2]
•   Coriolis: 2Ω × v_rel — deflection of moving objects due to frame rotation [1]
•   Centripetal: Ω × (Ω × r) — always directed toward the rotation axis [1]
• Euler: α × r — present only when angular velocity is changing [1]
Q4 (c) — Rotating Platform Numerical [5 marks]
• Given: Ω = 3.0 k̂ rad/s, r = 1.0 î m, v_rel = (0.5î + 0.8ĵ) m/s, a_rel = (0.2î − 0.1ĵ), α = 0
• Coriolis = 2Ω × v_rel = 2(3k̂) × (0.5î + 0.8ĵ) = 6(0.5ĵ − 0.8î) = (−4.8î + 3.0ĵ) m/s² [1.5]
Using k̂ × î = ĵ and k̂ × ĵ = −î
• Centripetal = Ω × (Ω × r) = 3k̂ × (3k̂ × 1.0î) = 3k̂ × 3ĵ = 9(−î) = −9.0î m/s² [1.5]
• Euler = α × r = 0 (since α = 0)
• Total: a = (0.2 − 4.8 − 9.0)î + (−0.1 + 3.0)ĵ = (−13.6î + 2.9ĵ) m/s² [1]
•   |a| = √(13.6² + 2.9²) = √(184.96 + 8.41) = √193.37 = 13.91 m/s² [1]
Q4 (d) — Coriolis on Earth [5 marks]
• Given: latitude λ = 45°N, v = 500 m/s due north, Ω = 7.3 × 10⁻⁵ rad/s, t = 10 s
• Vertical component: Ω_v = Ω sin λ = 7.3 × 10⁻⁵ × sin 45° = 5.162 × 10⁻⁵ rad/s [1]
• a_Coriolis = 2Ω_v × v = 2(5.162 × 10⁻⁵)(500) = 0.05162 m/s² [2]
• Deflection d = ½ a_C t² = ½(0.05162)(100) = 2.58 m to the east (right) [2]
In Northern hemisphere, Coriolis deflects to the right of the velocity direction
───────────────────────────────────────────────────────────────────────────────────────────────
Q5 — Constitutive Laws & Energy [20 marks]
Q5 (a) — Euler-Lagrange Derivation [5 marks]
• Hamilton's Principle: δ∫(T − V)dt = 0 over t₁ to t₂ [1]
• Lagrangian: L = T − V, where T = kinetic energy, V = potential energy [1]
• Euler-Lagrange: d/dt(∂L/∂q̇) − ∂L/∂q = 0 for each generalized coordinate q [1]
• Generalized coordinates: minimum set of independent variables describing configuration [1]
• Advantage: constraint forces never appear → works naturally with complex systems [1]
Q5 (b) — Newton vs Lagrange Comparison [5 marks]
********** 3 **********
--- page 4 ---
• Newton: Force-based, requires FBD, explicitly handles constraint forces [1]
• Lagrange: Energy-based, uses scalar T and V, constraints handled automatically [1]
• Newton preferred: when forces are needed (e.g., joint reactions) [1]
• Lagrange preferred: multi-DOF, complex constraints, no need for reaction forces [1]
• Simple pendulum: Newton gives mg sin θ = mLα; Lagrange gives same via T = ½mL²θ̇², V = −mgL cos θ [1]
Q5 (c) — Ramp + Rough Surface [5 marks]
• Given: m = 4 kg, h = 3 m (frictionless), μ_k = 0.3 (horizontal)
• At bottom: mgh = ½mv² → v = √(2gh) = √(2 × 9.81 × 3) = √58.86 = 7.67 m/s [2]
• On horizontal: ½mv² = μ_k mg d → d = v²/(2μ_k g) = 58.86/(2 × 0.3 × 9.81) = 10.0 m [3]
Q5 (d) — Impulse and Ball-Bat Problem [5 marks]
• Given: m = 0.15 kg, v₁ = 40 m/s (→), v₂ = 60 m/s (←), Δt = 0.002 s
• Taking initial direction as positive: v₂ = −60 m/s
•   J = m(v₂ − v₁) = 0.15(−60 − 40) = −15 N·s; |J| = 15 N·s [1.5]
• F_avg = |J|/Δt = 15/0.002 = 7500 N [1.5]
• KE_before = ½(0.15)(40²) = 120 J; KE_after = ½(0.15)(60²) = 270 J [1]
• KE NOT conserved — the bat does positive work on the ball (external energy input) [1]
───────────────────────────────────────────────────────────────────────────────────────────────
Q6 — FBD + Difficult Numerical [20 marks]
Q6 (a) — Conveyor Belt Transfer [10 marks]
• Given: m = 2 kg, v₁ = 1.5 m/s, v₂ = 3.0 m/s, μ_s = 0.35, μ_k = 0.25
FBD [4 marks]:
• Weight W = mg = 2(9.81) = 19.62 N (downward)
• Normal N = 19.62 N (upward)
• Kinetic friction f_k = μ_k N = 0.25(19.62) = 4.905 N (forward, in belt direction) [2]
FBD shows: block on belt surface; W↓, N↑, f_k→ (direction of belt motion)
• Check: package initially slower than belt → belt drags package forward → kinetic friction acts in belt direction ✓ [2]
Calculations [6 marks]:
• a = f_k/m = 4.905/2 = 2.453 m/s² [1.5]
• Time to match: t = (v₂ − v₁)/a = 1.5/2.453 = 0.612 s [1.5]
• Package distance: s_pkg = v₁t + ½at² = 1.5(0.612) + ½(2.453)(0.612²) = 0.918 + 0.459 = 1.377 m [1]
• Belt distance: s_belt = v₂ × t = 3.0(0.612) = 1.836 m [0.5]
• Relative sliding = 1.836 − 1.377 = 0.459 m [0.5]
• Heat = f_k × relative sliding = 4.905 × 0.459 = 2.25 J [1]
Q6 (b) — Slider-Crank Mechanism [10 marks]
• Given: r = 50 mm, L = 150 mm, n = 3000 RPM, θ = 30°
• ω = 2π(3000)/60 = 314.16 rad/s [2]
•   sin φ = (r/L) sin θ = (50/150) sin 30° = 0.3333 × 0.5 = 0.1667 → φ = 9.59° [2]
• cos φ = 0.9860 [0.5]
• Piston position from crank center: x = r cos θ + L cos φ = 50(0.866) + 150(0.986) = 43.30 + 147.90 = 191.20 mm [2]
• Angular velocity of connecting rod: φ̇ = rω cos θ/(L cos φ) = 50(314.16)(0.866)/(150 × 0.986) = 13599.1/147.9 = 91.95 rad/s [1.5]
• Piston velocity: v = −rω sin θ − Lφ̇ sin φ = −50(314.16)(0.5) − 150(91.95)(0.1667) = −7854 − 2299 = −10153 mm/s = −10.15 m/s
[2]
Negative sign: piston moves toward crank (away from TDC)
───────────────────────────────────────────────────────────────────────────────────────────────
Q7 — FBD + Difficult Numerical [20 marks]
Q7 (a) — Yo-Yo Dynamics [10 marks]
• Given: m = 50 g = 0.05 kg, R = 30 mm = 0.03 m, r = 10 mm = 0.01 m (solid disk)
********** 4 **********
--- page 5 ---
FBD [3 marks]:
• Weight W = mg = 0.4905 N (downward at center)
• String tension T (upward, applied at spool radius r)
• Rolling constraint: a = αr (linear and angular acceleration linked)
Derivation [3 marks]:
•   I = ½mR² = ½(0.05)(0.03²) = 2.25 × 10⁻⁵ kg·m² [1]
• β = I/(mr²) = R²/(2r²) = 0.0009/(2 × 0.0001) = 4.5 [1]
• From ΣF = ma: mg − T = ma; From Στ = Iα: Tr = Iα = I(a/r)
• Solving: a = g/(1 + β) = 9.81/5.5 = 1.784 m/s² [1]
Calculations [4 marks]:
• T = m(g − a) = 0.05(9.81 − 1.784) = 0.05(8.026) = 0.401 N [1]
• α = a/r = 1.784/0.01 = 178.4 rad/s² [1]
• KE_rot/KE_total = β/(1 + β) = 4.5/5.5 = 0.818 = 81.8% rotational [2]
Q7 (b) — 2-DOF Mass-Spring System [10 marks]
• Given: m₁ = 1.0 kg, m₂ = 1.5 kg, k₁ = 100, k₂ = 150, k₃ = 100 N/m
Matrices [3 marks]:
• [M] = [[1.0, 0], [0, 1.5]] [1]
• [K] = [[k₁ + k₂, −k₂], [−k₂, k₂ + k₃]] = [[250, −150], [−150, 250]] [2]
Eigenvalue problem [4 marks]:
• det([K] − ω²[M]) = 0
• (250 − ω²)(250 − 1.5ω²) − (−150)² = 0 [1]
• 1.5ω⁴ − 625ω² + 40000 = 0 [1]
• ω² = (625 ± √(625² − 4(1.5)(40000))) / (2 × 1.5) = (625 ± √150625) / 3 = (625 ± 388.1) / 3 [1]
• ω₁² = 236.9/3 = 78.97 → ω₁ = 8.887 rad/s (f₁ = 1.414 Hz) [0.5]
• ω₂² = 1013.1/3 = 337.7 → ω₂ = 18.38 rad/s (f₂ = 2.925 Hz) [0.5]
Mode shapes [3 marks]:
• Mode 1 (ω₁): Both masses move in-phase (same direction) [1.5]
• Mode 2 (ω₂): Masses move out-of-phase (opposite directions) [1.5]
───────────────────────────────────────────────────────────────────────────────────────────────
********** 5 **********
````
