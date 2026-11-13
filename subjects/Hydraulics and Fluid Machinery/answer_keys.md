# Hydraulics and Fluid Machinery: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper d5f7d6370cc8

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_Civil_7005/Hydraulics and Fluid Machinery/ANS_Hydraulics and Fluid Machinery(702CI0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY(CIVIL ENGINEERING)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Hydraulics and Fluid Machinery
Date: 28 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q.N   Par   Question (brief)   Synoptic Answer   Given / Data (if   Solution & Final
o   t   (concise)   numerical)   Answer (concise
steps + result)
Q1   a   Most economical   Optimum when b=2y   -   dP/dy at constant
rectangular section   for free rectangular   A => b=2y.
section (derive by
minimizing perimeter P
for constant area A).
Q1   b   Buckingham vs   Buckingham π is   -   Buckingham: n−k
Rayleigh   systematic and   π groups;
general; Rayleigh is   Rayleigh: quick
quicker for simple   heuristic.
single relation
problems.
Q1   c   Force by jet on   Use momentum: F =   -   ṁ=ρAV, F=ṁV (if
inclined plate   ṁ*(V_n - V_n2). If jet   stopped). For
brought to rest   inclined plates
normal: F=ρAV^2.   use normal
components.
Q1   d   Compare turbines   Pelton: impulse, high-   -   Use selection by
(Kaplan/Francis/Pelto   head; Francis: mixed   specific speed; list
n)   flow, medium-head;   speed and flow
Kaplan: axial, low-head   characteristics.
high-flow.
Q2   a   Radial vs Dead-end   Radial: central supply   -   Mention water
layouts   feeders, good for   quality, pressure
planned networks;   control,
Dead-end:   extensions and
branch/simple, cheap   costs.
but low redundancy.
Q2   b   Hardy-Cross (4-pipe   ΣkQ|Q|=0, ΔQ = -   AB:L=120,D=0.15,Q=0.0   Iter1 ΔQ=-
loop) - 2 iterations   ΣkQ|Q|/Σ2k|Q|;   6;   1.865499e-02
update flows   BC:L=180,D=0.12,Q=0.0   m³/s ->
4;   Qs=['0.041345',
CD:L=150,D=0.15,Q=0.0   '0.021345',
5;   '0.031345',
DA:L=200,D=0.10,Q=0.0   '0.011345']
********** 1 **********
--- page 2 ---
3   Iter2 ΔQ=-
k=L/D^4.87, h=kQ|Q|   1.044242e-02
m³/s ->
Qs=['0.030903',
'0.010903',
'0.020903',
'0.000903']
Final:
AB=0.030903,
BC=0.010903,
CD=0.020903,
DA=0.000903
Q2   c   Three-reservoir   Apply loop balancing   H1=120,H2=110,H3=100   Iter1 ΔQ=-
Hardy-Cross (2   as in 2(b)   ; R1-   8.333029e-02 ->
iterations)   R2:500,0.25,Q=0.25; R2- Qs=['0.166670',
R3:400,0.20,Q=0.15; R3-   '0.066670',
R1:600,0.22,Q=0.10   '0.016670']
Iter2 ΔQ=-
5.377732e-02 ->
Qs=['0.112892',
'0.012892', '-
0.037108']
Final:
Q12=0.112892,
Q23=0.012892,
Q31=-0.037108
Q3   a   Re, Fr, St definitions   Re=ρVL/μ   -   State formulas,
and significance   (inertial/viscous);   meanings, and
Fr=V/√(gL)   example
(inertial/gravity);   thresholds.
St=fL/V (unsteady
shedding). Examples:
Re controls
laminar/turbulent; Fr
controls surface
waves; St for vortex
shedding.
Q3   b   Rayleigh for laminar   Dimensional reasoning   Variables: D, μ, ρ, Δp/L   Final: Q =
pipe flow (Δp/L   yields Q ∝ D^4   (π/128μ)(Δp/L)D^
included)   (Δp/L)/μ. Exact   4 (show
Poiseuille:   derivation or
Q=(π/128μ)(Δp/L)D^4.   quote Poiseuille
law).
Q3   c   Buckingham π for   Form π groups: e.g., F,   -   Explain selection
drag/resistance   V, D, μ, ρ ->   of repeating
π1=F/(ρV^2D^2)=Cd,   variables and
π2=μ/(ρVD)=1/Re. For   present final Cd=
ships include g and L to   f(Re) or Cd =
include Fr.   f(Re,Fr).
Q4   a   Compare Pipe flow   Pipe: closed, pressure   -   List equations,
and Open Channel   flow; Open channel:   BCs and typical
flow   free surface, gravity-   phenomena
driven. Governing eqns   (critical flow,
and BC differ; Froude
********** 2 **********
--- page 3 ---
important for   backwater
channels.   profiles).
Q4   b   Trapezoidal channel:   Maximize R=A/P   b=4 m, m=0.5, Q=18   Optimal y ≈
b=4 m, m=0.5, Q=18 -   numerically over y.   m³/s   10.0000 m; A ≈
> most economical y   90.0000 m²; R ≈
3.4142 m
Q4   c   Triangular channel   Compute A,P,R then Q   Angle=60°, y=6 m, C=50, A = 62.354 m²; P ≈
flow (angle 60°), C=50, = A C √(R S).   S=1/1500   44.785 m; R ≈
S=1/1500, y=6m   1.3923 m; Q ≈
94.985 m³/s
Q5   a   Derive force on series   Apply momentum   -   Show vector
of vanes   theorem: F = ṁ (V_t1 -   momentum
V_t2) per vane;   balance and final
account for relative   expression for
velocities and blade   tangential force
angles for curved   and work.
vanes.
Q5   b   Jet d=80mm at 20 m/s ṁ=ρAV, Force=ṁ(V-   d=0.08 m, V=20 m/s,   ṁ=100.531 kg/s;
on plate moving at 6   Vp), Power=F*Vp   Vp=6 m/s, ρ=1000   Force=1407.434
m/s   kg/m³   N;
Power=8444.601
W
Q5   c   Radial curved vanes   Use inlet/outlet   Given in Q5(c): V=30   Compute mean u,
problem   velocity triangles;   m/s, n=300 rpm,   resolve V_t
work/kg = u(V_t1 -   rin=0.3, rout=0.6,   components, then
V_t2); efficiency =   inlet/outlet angles   work/kg and
work/(V^2/2).   provided   efficiency. Show
full steps in
answer sheet.
Q6   a   Specific speed & NPSH   Specific speed (Ns)   -   Give formula and
characterizes   practical guidance
turbine/pump type;   for machine
NPSH indicates suction   selection and
head margin to avoid   cavitation checks.
cavitation.
Q6   b   Compute Ns and   Ns = n √P_kW /   P=900 kW, H=9 m,   Ns = 230.940. For
suggest turbine for   H^(5/4). Lower Ns with n=120 rpm   double head
double head   higher head; selection   (same Q) choose
accordingly.   lower Ns turbine
(Francis/Pelton
depending on
head magnitude).
Q6   c   Pelton design: P=900   Compute P_hyd,   P_shaft=900 kW, H=250   P_hyd=1000000.0
kW, H=250 m,   Q_total, V, Qj, dj,   m, eta=0.9, n=720 rpm,   0 W;
eta=0.9, n=720 rpm, 3   D_runner, z, bucket   jets=3   Q_total=0.407747
jets   width   m³/s; V=70.036
m/s; d_j=0.0497
m; D=0.9289 m;
z≈326;
bucket_w=0.0348
m
Q7   a   Ideal indicator   Indicator diagram: p-V   -   Describe each
diagram   plot showing   process and
admission,   compute
********** 3 **********
--- page 4 ---
compression/expansio   indicated work
n, delivery. Area =   from area.
indicated work.   Include sketch in
answer.
Q7   b   Pump Q=0.06 m³/s,   Phyd=ρgQH;   Q=0.06 m³/s, H=30 m,   P_hyd=17658.00
H=30 m, n=1450 rpm,   Efficiency=Phyd/Pin;   n=1450 rpm, Pin=30 kW W;
Pin=30 kW   Ns_SI = n √Q / H^(3/4)   Efficiency=58.86%
; Ns=27.708
Q7   c   Reciprocating pump:   Q_theo = stroke vol *   D=0.160 m,   Q_theo=0.004222
D=160 mm,   strokes/s; a_max =   stroke=0.350 m, n=36   m³/s;
stroke=350 mm, n=36   (ω^2)(stroke/2); H_acc   rpm, Ls=5 m, Ld=20 m   H_acc_s=1.2677
rpm   = a_max L / g; Power =   m;
ρ g Q H_total   H_acc_d=5.0706
m;
Power≈1173.79
W
For every numerical: 2 marks for figure, 3 marks for step by step solution
snd 2 marks for final answer
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper e68e9a8bae8f

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Civil_7005/Hydraulics and Fluid Machinery/ANS_Hydraulics and Fluid Machinery(702CI0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY(CIVIL ENGINEERING)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Hydraulics and Fluid Machinery
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1.   a. Compare pipe flow   Pipe flow: flow completely fills conduit; pressure-driven; BC: no-
and open channel flow   slip at walls and specified pressure/flow at ends. Open channel: free
surface present; gravity-driven; governed by shallow-water (Saint-
Venant) BC; free-surface atmospheric pressure. Flow
characteristics: pipe—pressurized; open channel—
subcritical/supercritical (Fr<1 or >1).
b. Rayleigh vs   Rayleigh: quick dimensional balancing using assumed repeating
Buckingham π   variable; good for simple relations. Buckingham π: systematic
algorithm to form independent π groups (π = n − k), general and
rigorous for many variables.
c. Hydropower   Dam/reservoir (store potential energy), penstock (conveys
components   pressurized water), surge tank (transient control), turbine
(hydraulic→mechanical), governor (speed control), generator
(mechanical→electrical), tailrace (discharge).
d. Centrifugal pump   H–Q curve: H decreases with Q. Efficiency–Q: peaks at BEP.
curves   Power–Q: increases. NPSHr increases with Q. Sketch: H-Q
downward, η-Q bell-shaped.
Q2.   a. Types of pipe   Dead-end: simple, low cost, limited redundancy. Grid: looped mains
networks (dead-end,   with redundancy and better hydraulics. Circular/ring: distribution
grid, circular, radial)   with balanced pressures. Radial: feeders from central source,
suitable for small towns.
b. Hardy Cross   Pipe   k = L/D^4.87   Initial Q   Q after 2
method - Example (2   (m³/s)   iterations
iterations max)   (m³/s)
Example problem   P1   2.535e+05   0.05000   0.01979
(illustrative): Three-   P2   1.544e+06   0.04000   0.00979
pipe single loop. Data:   P3   5.082e+05   0.03000   -0.00021
L1=100 m, D1=0.20
m; L2=150 m,
D2=0.15 m; L3=120
m, D3=0.18 m. Initial
flows (clockwise):
Q1=0.05, Q2=0.04,
Q3=0.03 m³/s. Use h ∝
k Q|Q| and perform 2
iterations.
********** 1 **********
--- page 2 ---
Three-reservoir problem: Method outline - write loop head
losses, assume flows, apply Hardy Cross to loops,
compute ΔQ for each loop and update. (Numerical
depends on supplied reservoir heads).
Q3.   a. Derivations:
Re = ρ V L / μ (for pipe Re = V D / ν). Fr = V / sqrt(g L) (in open channels Fr = V/√(g
D)). Ma = V / c (c = speed of sound).
b. Rayleigh method (example): Seek Q ∝ D^a μ^b ρ^c. Dimensions: Q(L^3 T^-1), D(L),
μ(M L^-1 T^-1), ρ(M L^-3). Equate exponents:
M: 0 = b + c
T: -1 = -b => b = 1
→ c = -1
L: 3 = a - b - 3c = a -1 +3 ⇒ a = 1
Hence Q ∝ (D μ)/ρ (simple form).
c. Buckingham π (drag on sphere): Variables F, V, D, μ, ρ. Choose repeating V,D,ρ. π1
= F/(ρ V^2 D^2) = Cd, π2 = μ/(ρ V D) = 1/Re ⇒ Cd = f(1/Re) and F = ρ V^2 D^2
f(1/Re).
Q4.   a. For trapezoidal channel, derive condition by minimizing wetted perimeter P for a
given area A. For rectangular, optimum width-depth relation for minimum perimeter
at fixed area gives b = 2y (rectangular optimum). For trapezoidal derivation follow
calculus of variations or differentiate P at constant A.
b. Rectangular channel: b=4 m, Q=16 m³/s. For most economical rectangular section
with fixed width the theoretical optimum depth y = b/2 = 2 m (when free to choose
depth for area efficiency; if width fixed this yields hydraulic radius maximum for that
constraint). Compute A,R,V:
Depth y = 2.000 m; Area A = 8.000 m²; Hydraulic radius R = 1.000 m; Velocity V = 2.000
m/s.
c. Trapezoidal channel: side slope m=1 (1H:1V), bed width b=5 m, Q=20 m³/s.
Numerically find depth y that maximizes hydraulic radius R = A/P.
Optimal depth y ≈ 10.0000 m; Area A ≈ 150.0000 m²; Hydraulic radius R ≈ 4.5066 m.
To get discharge compatibility Q = A * V, one would use Manning or energy considerations
to find V; here geometry optimization shown for hydraulic radius (economy).
Q5.   a. Jet on fixed plate (centered): Force F = ṁ V = ρ A V^2 (if jet brought to rest).
b. d = 0.06 m; Jet V = 25.0 m/s; Plate speed = 10.0 m/s.
Mass flow ṁ = ρ A V = 70.686 kg/s.
Relative speed V_rel = 15.000 m/s.
Force on plate F = ṁ * V_rel = 1060.288 N.
Work done per second (power) = F * plate speed = 10602.875 W.
c. d = 0.05 m, V = 30.0 m/s, u = 12.0 m/s.
Mass flow ṁ = 58.905 kg/s.
Extracted power (ideal impulse approx) = 31808.626 W.
Jet kinetic power = 26507.188 W.
Efficiency ≈ 120.00%.
(Equivalent simple formula gives efficiency = 2*(V-u)/V = 1.200.)
Q6.   a. Unit speed and NPSH:
- Specific speed Ns (metric) for turbines: Ns = n * sqrt(P_kW) / H^(5/4) (common
form). It helps select turbine type: low Ns → Pelton; medium → Francis; high →
Kaplan.
********** 2 **********
--- page 3 ---
- NPSH (Net Positive Suction Head) is for pumps: margin of suction pressure to avoid
cavitation; for turbines, avoid vortexing and cavitation at runner inlet.
b. Given 1500 kW, H=6 m, n=90 rpm.
Specific speed Ns = 371.19 (metric). Interpretation: High Ns (order of few thousands)
indicates Kaplan (low head, high flow). For double head (H=12 m) at same discharge,
turbine type shifts toward Francis.
c. Pelton design results:
1. Hydraulic power required = 1363636.36 W. Total discharge Q = 0.46335 m³/s.
2. Ideal jet velocity V = 76.720 m/s. Q per jet = 0.231675 m³/s.
3. Jet diameter per jet = 0.0620 m.
4. Runner diameter ≈ 1.2210 m.
5. Estimated number of buckets ≈ 309.3 (round to nearest integer).
6. Suggested bucket width ≈ 0.0434 m.
Q7.   a. Ideal indicator diagram: shows p-V diagram of pump/engine with distinct processes;
area under curve = indicated work.
b. Given Q=0.04 m³/s, H=25.0 m, n=1500.0 rpm.
Hydraulic power = 9810.00 W.
Specific speed Ns = 26.83 (SI form).
Efficiency = 65.40% (0.654).
c. Given piston dia 0.15 m, stroke 0.3 m, speed 40.0 rpm.
1. Theoretical discharge Q = 0.003534 m³/s.
2. Peak piston acceleration a_max = 2.632 m/s².
Acceleration head (approx): suction = 1.6097 m, delivery = 4.8292 m.
3. Total head (neglecting friction) = 22.4389 m.
Power required ≈ 777.99 W.
For every numerical- 2 marks for diagram, 3 marks for steps, 2 marks for final answer
********** 3 **********
````
