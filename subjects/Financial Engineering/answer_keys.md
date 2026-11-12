# Financial Engineering: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 599835db5194

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/MBATech_AI_7051/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 09 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: V/Semester X(Exam Year: 2025-2026)
Subject: Financial Engineering
Date: 09 May 2026   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No. _1_is compulsory.
3. Out of remaining questions, attempt any_4_questions.
4. In all_5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary
9. Use of Scientific Calculator allowed
Q1   Answer briefly:   [10
]
CO1; SO-   a. Definition: A Forward Rate Agreement (FRA) is an over-the-counter (OTC) derivative contract
1;   between two parties — a buyer and a seller — that fixes (locks in) an interest rate for a future
BL-   borrowing or lending transaction for a specified notional principal over an agreed future period.
Understan
d   Keywords: FRA, OTC, Notional Principal, Settlement Date, Reference Rate (LIBOR/MIBOR),
Contract Rate
•   Participants: Buyer (borrower, who wants to LOCK IN a rate) and Seller (lender / bank)
•   Key Milestones: Trade Date → Setting Date → Settlement Date → Maturity Date
•   Settlement Mechanism: Cash-settled on Settlement Date; difference between Reference Rate
[03
and Contract Rate is paid on discounted basis
]
•   Settlement Formula: Payment = [(Reference Rate – Contract Rate) × Notional × Days/360] /
[1 + (Reference Rate × Days/360)]
Example: Co. A anticipates borrowing ₹10 Cr at MIBOR after 3 months for 6 months. Enters 3×9
FRA at 7% (contract rate). If MIBOR settles at 8%, settlement receipt compensates for the extra
cost.
•   Benefit: Eliminates interest rate uncertainty; hedger knows exact future cost
Mark Distribution: Definition (1) + Participants/Milestones (1) + Settlement mechanism
with formula (1)
CO1; SO-   b Hedging Definition: Hedging is the process of taking an offsetting position in a financial
1;   .   instrument to reduce or eliminate the risk of adverse price movements in an existing position.
BL-
Arbitrage Definition: Arbitrage is the simultaneous purchase and sale of the same or equivalent
Understan
asset in different markets to profit from price discrepancies, with zero risk and zero net   [03
d
investment.   ]
Comparison Table — Keywords: Risk, Objective, Cost, Duration
Parameter   Hedging   Arbitrage
********** 1 **********
--- page 2 ---
Objective   Risk reduction / protection   Risk-free profit
Risk   Residual risk may remain   Zero risk (riskless)
Cost   Premium / opportunity cost   Zero net investment
Duration   Ongoing, long-term   Instantaneous
Example   Exporter buys USD put option   Buy low on NSE, sell high on
BSE
Mark Distribution: Hedging definition with example (1) + Arbitrage definition with
example (1) + Comparison: objective/risk/cost (1)
CO1; SO-   c. Statement Interpretation: The 95%, 1-day VaR of INR 1.75 Crores means: with 95% confidence,
1;   the portfolio will NOT lose more than ₹1.75 Crores in a single trading day under normal market
BL-   conditions.
Remember
Key Keywords: Confidence Level, Holding Period, Loss Threshold, Tail Risk, Normal
Distribution
•   Significance: Quantifies downside risk; aids in capital allocation and setting risk limits   [02
•   Limitation 1: Assumes normal distribution — fails during tail events (Black Swan events)   ]
•   Limitation 2: Does not reveal the magnitude of losses BEYOND the VaR threshold
•   Limitation 3: Backward-looking — based on historical data; not predictive in structural
breaks
Mark Distribution: Correct interpretation of statement (1) + Significance + 2 limitations
(1)
CO1; SO-   d. Definition: A Credit Default Swap (CDS) is an OTC derivative contract that acts like insurance
1;   against credit default. The Protection Buyer pays a periodic premium (CDS Spread) to the
BL-   Protection Seller, who compensates the buyer if the Reference Entity defaults.
Understan
d   Keywords: Protection Buyer, Protection Seller, Reference Entity, CDS Spread, Credit Event
•   Participants: (i) Protection Buyer — hedges credit risk; (ii) Protection Seller — earns
premium; (iii) Reference Entity — underlying borrower
•   Settlement: Physical (delivery of defaulted bond) or Cash (face value minus recovery value)   [02
•   Role in 2008 Crisis: CDSs were sold massively on subprime mortgage-backed securities   ]
(MBS). When MBS defaulted, protection sellers (like AIG) faced unmanageable payouts →
systemic collapse
•   Key Issue: Lack of regulation, naked CDS positions, and excessive leverage amplified
contagion
Mark Distribution: CDS definition with participants/example (1) + Role in   2
2008 crisis: naked positions/AIG/contagion (1)
Q2   Answer the following:   [10]
CO2; SO- A Given Data: 5 Equal-Weighted Stocks (20% each) | Portfolio: Rs. 5 Crores (assumed) | Prices
1;   Year 0-5:
BL-Apply
Year   Stock A   Stock B   Stock C   Stock D   Stock E
0   317   281   400   437   277
[05]
1   350   300   370   478   310
2   300   277   457   526   347
3   280   256   415   564   386
4   325   310   460   612   423
********** 2 **********
--- page 3 ---
5   380   396   510   644   458
Step 1: Calculate Annual Returns for Each Stock (Year-on-Year %)
Formula: Return(t) = [Price(t) / Price(t-1)] − 1
Year   A (%)   B (%)   C (%)   D (%)   E (%)   Portfolio Ret (%)
Yr1   10.41   6.76   -7.50   9.38   11.91   6.19
Yr2   -14.29   -7.67   23.51   10.04   11.94   4.71
Yr3   -6.67   -7.58   -9.19   7.22   11.24   -0.99
Yr4   16.07   21.09   10.84   8.51   9.59   13.22
Yr5   16.92   27.74   10.87   5.23   8.27   13.81
Note: Portfolio Return = Equal-weighted average of 5 stock returns (20% × each)
Step 2: Sort Portfolio Returns in Ascending Order
Step   Working / Calculation   Marks
2a   Sort all 5 portfolio annual returns from worst to best:   ½
Rank 1 (Worst): −0.99% (Year 3) Rank 2: 4.71% (Year 2) Rank   ½
3: 6.19% (Year 1) Rank 4: 13.22% (Year 4) Rank 5 (Best):
13.81% (Year 5)
Step 3: Identify the 95% VaR Observation
Step   Working / Calculation   Marks
For 95% CL with 5 observations: VaR = 5% worst observation =   1
worst 5% of returns 5% × 5 = 0.25 → Round up to 1st
3a   observation (most conservative)
Formula: VaR percentile: (1 − CL) × N = 0.05 × 5 = 0.25 → 1st
observation
1-Day VaR basis: worst annual return = −0.99% First, convert: 1-   ½
3b   Day Return = −0.99% / √252 = −0.0624% per day
Formula: 1-Day σ = Annual Return / √252
Step 4: Calculate Portfolio VaR
Assuming Portfolio Value = Rs. 5 Crores (standard assumption when not specified):
Step   Working / Calculation   Marks
1-Day VaR (absolute) = Portfolio Value × |Worst 1-Day   1
Return| = 5,00,00,000 × 0.000624 = Rs. 31,200 (1-day
4a
VaR)
Formula: VaR = P × |r|
10-Day VaR = 1-Day VaR × √10 = 31,200 × 3.1623 = Rs.   1
4b   98,665
Formula: N-Day VaR = 1-Day VaR × √N
ALTERNATE: Using worst annual portfolio return   ½
directly: 95% 1-Year VaR = 5 Cr × 0.0099 = Rs. 4.95
4c
Lakhs 10-Day VaR = 4.95L × √(10/252) = Rs. 98,646 ≈
Rs. 98,700
********** 3 **********
--- page 4 ---
Step 5: Inference & Rebalancing Recommendation
Step   Working / Calculation   Marks
The 95%, 10-Day VaR ≈ Rs. 98,700 means with 95% confidence,   ½
5a   maximum loss in 10 days ≤ Rs. 98,700 Single worst year was Year 3
(−0.99% portfolio). Stocks A & B showed negative returns.
Recommendation: YES — rebalance. Stock B shows persistent   ½
5b   underperformance (−7.67%). Consider reducing exposure to A & B
and increasing D & E which show consistent positive returns.
Final Answer: 95% 10-Day Portfolio VaR ≈ Rs. 98,700 | Rebalance: Reduce B &   5
A; increase D & E   Marks
Total
CO2; SO- B Concept: A Synthetic Short Position is created using options to replicate the payoff of actually
1;   short-selling a stock, WITHOUT borrowing and selling the stock.
BL-Apply
Strategy: BUY PUT + SELL CALL at the SAME Strike Price
Numerical Example: Reliance CMP = Rs. 2,500 | Strike = Rs. 2,500 | Put Premium (Buy) = Rs. 80 |
Call Premium (Receive) = Rs. 70 | Net Cost = Rs. 10 per share
Step   Working / Calculation   Marks
1   Buy 1 ATM Put @ Strike 2500, Pay Premium = Rs. 80   ½
2   Sell 1 ATM Call @ Strike 2500, Receive Premium = Rs. 70   ½
Net Premium Paid = 80 − 70 = Rs. 10 (net debit)   ½
3
Formula: Net Cost = Put Premium − Call Premium
Payoff at Expiry: • If Market = 2300 (falls): Put profit = 200; Call   1
expires worthless → Net = 200 − 10 = +Rs. 190 • If Market =
4   2500: Both expire worthless → Net Loss = −Rs. 10 • If Market =
2700 (rises): Put worthless; Call loss = 200 → Net = −200 − 10 =
−Rs. 210   [05]
Break-even = Strike − Net Premium = 2500 − 10 = Rs. 2,490   ½
5
Formula: BE = K − Net Premium
Part (ii): Synthetic Short vs Actual Short — Comparison
Parameter   Synthetic Short   Actual Short Sell
Risk   Defined (put premium paid)   Unlimited upside = unlimited loss
Margin   No SEBI margin needed (just   SEBI prescribed VaR + ELM margin
premium)
Cost   Net premium (small)   Borrowing cost + margin cost
Dividend Risk   No dividend risk   Short seller must pay dividend
Regulatory   No stock borrowing needed   Subject to SEBI short-sell rules
Mark Distribution: Strategy construction (1.5) +
Payoff table (2) + Comparison table (1.5)
********** 4 **********
--- page 5 ---
Q3   Answer the following:   [10]
CO3; SO- A Given: EPS₀ = Rs.18 | DPR = 65% | D₀ = 18 × 0.65 = Rs. 11.70 | Rf = 5.25% | Rm = 14% | β = 1.90
8;   | CMP = Rs. 320
BL-Apply   Growth Phases: Phase 1: g = 22% for 6 years | Phase 2: g declines from 22% to 8% over 3 years |
Phase 3: g = 5% (perpetuity)
Step   Working / Calculation   Marks
Calculate Ke using CAPM: Ke = Rf + β(Rm − Rf) = 5.25% +   1
1.90 × (14% − 5.25%) = 5.25% + 1.90 × 8.75% = 5.25% +
1
16.625% = 21.875% ≈ 21.88%
Formula: Ke = Rf + β(Rm − Rf)
Phase 2: Growth declines linearly from 22% to 8% over 3 years:   ½
Year 7: g = 22% − (22%−8%)/3 × 1 = 22% − 4.67% = 17.33%
2
Year 8: g = 22% − (22%−8%)/3 × 2 = 22% − 9.33% = 12.67%
Year 9: g = 22% − (22%−8%)/3 × 3 = 8.00%
Phase 1 Dividends (Years 1-6): D₀ = 11.70; g = 22% each year   1
D1=14.27 | D2=17.41 | D3=21.24 | D4=25.91 | D5=31.61 |
3
D6=38.57
Formula: Dt = D(t-1) × (1+g)
Phase 2 Dividends (Years 7-9): D7 = 38.57 × 1.1733 = 45.25 | D8   ½
4
= 45.25 × 1.1267 = 51.01 | D9 = 51.01 × 1.08 = 55.09
[05]
Terminal Value at end of Year 9: TV9 = D10 / (Ke − g∞) = 55.09   1
5   × 1.05 / (0.2188 − 0.05) = 57.84 / 0.1688 = Rs. 342.65
Formula: TV = D(n+1)/(Ke − gL)
PV of Phase 1 (Ke=21.88%): Sum of PV of D1-D6 PV =   ½
14.27/1.2188 + 17.41/1.2188² + ... ≈ 11.71 + 11.72 + 11.74 +
6
11.77 + 11.78 + 11.80 = Rs. 70.52
Formula: PV = Dt/(1+Ke)^t
PV of Phase 2 (D7-D9): PV = 45.25/1.2188⁷ + 51.01/1.2188⁸ +   ½
7
55.09/1.2188⁹ ≈ 10.04 + 9.28 + 8.22 = Rs. 27.54
PV of Terminal Value: PV(TV9) = 342.65/1.2188⁹ =   ½
8   342.65/5.371 = Rs. 63.80
Formula: PV(TV) = TV/(1+Ke)^n
Intrinsic Value = PV(Ph1) + PV(Ph2) + PV(TV) = 70.52 + 27.54   ½
+ 63.80 = Rs. 161.86 Valuation: CMP = Rs. 320 >> IV = Rs.
9
161.86 → Stock is OVERVALUED → SELL
Formula: IV = ΣPV(Dt) + PV(TV)
Final Answer: Intrinsic Value ≈ Rs. 161.86 | CMP Rs. 320 >> IV → Stock   5 Marks Total
OVERVALUED → Recommendation: SELL/SHORT
CO3; SO- B Given: FV = Rs. 1,000 | Coupon = 7% p.a. → Annual Coupon = Rs. 70 | YTM = 9% | Maturity = 5
8;   Years
BL-Apply   [05]
Step 1: Bond Pricing using DCF Tabular Method
Step   Working / Calculation   Marks
********** 5 **********
--- page 6 ---
PV Factor at 9%: 1/(1.09)^t for t = 1 to 5 t=1: 0.9174 | t=2:   ½
1   0.8417 | t=3: 0.7722 | t=4: 0.7084 | t=5: 0.6499
Formula: PV Factor = 1/(1+r)^t
PV of Coupons: t=1: 70×0.9174=64.22 | t=2: 70×0.8417=58.92 |   ½
2   t=3: 70×0.7722=54.05 t=4: 70×0.7084=49.59 | t=5:
70×0.6499=45.49 Total PV Coupons = 272.27
3   PV of Face Value: 1000 × 0.6499 = Rs. 649.93   ½
Bond Price = 272.27 + 649.93 = Rs. 922.20 (Coupon 7% < YTM   ½
4   9% → Bond trades at DISCOUNT — confirmed)
Formula: P = Σ[C/(1+r)^t] + FV/(1+r)^n
Step 2: Macaulay Duration
Step   Working / Calculation   Marks
Duration = Σ[t × PV(CFt)] / P Numerator = 1×64.22 + 2×58.92 +   1
3×54.05 + 4×49.59 + 5×(45.49+649.93) = 64.22 + 117.84 +
5   162.15 + 198.36 + 3,477.10 = 4,019.67 Macaulay Duration =
4,019.67 / 922.20 = 4.359 Years
Formula: D = Σ[t × PV(CFt)] / Bond Price
Step 3: Modified Duration
Step   Working / Calculation   Marks
Modified Duration = Macaulay Duration / (1 + YTM) = 4.359 /   ½
1.09 = 3.998 ≈ 4.00 Years Interpretation: 1% rise in YTM →
6
Bond Price falls by ≈ 4.00%
Formula: MD = D/(1+r)
Step 4: Convexity
Step   Working / Calculation   Marks
Convexity = [1/(P×(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t] Numerator =   1
1(2)×70/1.09 + 2(3)×70/1.09² + 3(4)×70/1.09³ + 4(5)×70/1.09⁴ +
5(6)×1070/1.09⁵ = 128.44 + 353.36 + 648.46 + 994.92 +
7
17,587.82 = 19,713.00 Convexity = 19,713 / (922.20 × 1.09²) =
19,713 / 1,095.19 = 18.00
Formula: Conv = [1/(P(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t]
Price Change Approximation using MD & Convexity: ΔP/P ≈   ½
−MD × Δy + ½ × Conv × (Δy)² MD captures linear, Convexity
8
corrects for curvature of price-yield relationship
Formula: ΔP/P ≈ −MD·Δy + ½·Conv·(Δy)²
Final Answers: Bond Price = Rs. 922.20 | Mac. Duration = 4.36 yrs |   5 Marks Total
Modified Duration = 4.00 | Convexity = 18.00
********** 6 **********
--- page 7 ---
Q4   Answer the following:   [10]
CO2;   A Repricing Buckets: 1-6m (A=80L, L=70L) | 6-12m (A=40L, L=50L) | 1-3yr (A=20L, L=25L) |
SO-1;   3-5yr (A=15L, L=10L)
BL-
Step   Working / Calculation   Marks
Apply
Calculate Gap for each bucket: Gap = Rate Sensitive Assets   ½
1   (RSA) − Rate Sensitive Liabilities (RSL)
Formula: Gap = RSA − RSL
1-6m: Gap = 80 − 70 = +Rs. 10 Lakh (Positive/Asset-Sensitive)   ½
6-12m: Gap = 40 − 50 = −Rs. 10 Lakh (Negative/Liability-
Sensitive) 1-3yr: Gap = 20 − 25 = −Rs. 5 Lakh (Negative) 3-5yr:
Gap = 15 − 10 = +Rs. 5 Lakh (Positive)
Scenario (i): Rates ↑ 50 bps (+0.50%) in 1-6 month bucket ΔNII   1½
= Gap × Δr × Time Fraction = 10 Lakh × 0.005 × (6/12) =
2   10,00,000 × 0.005 × 0.5 = Rs. 2,500 Annualized ΔNII = Rs. 5,000   [05]
or use: ΔNII = Gap × Δr = 10L × 0.005 = Rs. 5,000 p.a.
Formula: ΔNII = Gap × Δr
Scenario (ii): Rates ↓ 25 bps (−0.25%) in 1-3 year bucket ΔNII =   1½
Gap × Δr = −5,00,000 × (−0.0025) = +Rs. 1,250 p.a. Negative
3
gap + rate decrease → NII INCREASES (beneficial scenario)
Formula: ΔNII = Gap × Δr
ALM Concept: Asset-Liability Management (ALM) involves   1
managing the balance sheet to optimize NII while controlling
4
interest rate risk. Gap Analysis identifies mismatches between
RSA and RSL to assess NII sensitivity to rate changes.
Final Answers: Scenario(i) +50bps: ΔNII = +Rs. 5,000 | Scenario(ii)   5 Marks Total
−25bps in 1-3yr: ΔNII = +Rs. 1,250 | Positive Gap → Rate ↑ beneficial
CO2;   B JP Bank | Asset A: EAD=40m, PD=0.25%, LGD=20%, σPD=5%, σLGD=15% | Asset B:
SO-1;   EAD=60m, PD=0.50%, LGD=35%, σPD=7%, σLGD=10% | ρ=0.20
BL-
Step   Working / Calculation   Marks
Apply
Expected Loss (EL) for each asset: EL_A = EAD_A × PD_A   1
× LGD_A = 40m × 0.0025 × 0.20 = Rs. 20,000 EL_B =
1   EAD_B × PD_B × LGD_B = 60m × 0.005 × 0.35 = Rs.
1,05,000
Formula: EL = EAD × PD × LGD
Unexpected Loss (UL) for each asset: UL_i = EAD_i ×   ½
2   √(LGD²×σPD² + PD²×σLGD²)   [05]
Formula: UL = EAD × √(LGD²·σPD² + PD²·σLGD²)
UL_A = 40m × √[(0.20²×0.05²) + (0.0025²×0.15²)] = 40m ×   ½
√[(0.04×0.0025) + (0.00000625×0.0225)] = 40m × √[0.0001
+ 0.000000140625] = 40m × √0.000100140625 = 40m ×
0.010007 = Rs. 4,00,281 ≈ Rs. 4.00 Lakh
UL_B = 60m × √[(0.35²×0.07²) + (0.005²×0.10²)] = 60m ×   ½
√[(0.1225×0.0049) + (0.000025×0.01)] = 60m ×
√[0.00060025 + 0.00000025] = 60m × √0.0006005 = 60m ×
0.02451 = Rs. 14,70,488 ≈ Rs. 14.70 Lakh
********** 7 **********
--- page 8 ---
Portfolio Unexpected Loss (ρ = 0.20): UL_P = √(UL_A² +   1
UL_B² + 2ρ×UL_A×UL_B) = √[(4.00)² + (14.70)² +
3   2×0.20×4.00×14.70] All in Lakh: = √[16.00 + 216.09 +
23.52] = √255.61 = Rs. 15.99 Lakh
Formula: UL_P = √(UL_A² + UL_B² + 2ρ·UL_A·UL_B)
Risk Contribution of each asset to Portfolio UL: RC_A =   1
UL_A × (UL_A + ρ×UL_B) / UL_P = 4.00 × (4.00 +
0.20×14.70) / 15.99 = 4.00 × 6.94 / 15.99 = Rs. 1.736 Lakh
4   RC_B = UL_B × (UL_B + ρ×UL_A) / UL_P = 14.70 × (14.70
+ 0.20×4.00) / 15.99 = 14.70 × 15.50 / 15.99 = Rs. 14.26
Lakh
Formula: RC_i = UL_i(UL_i + ρ·UL_j)/UL_P
Impact of ρ increasing to 0.35: New UL_P = √[16 + 216.09 +   1
2×0.35×4.00×14.70] = √[16+216.09+41.16] = √273.25 = Rs.
5   16.53 Lakh ↑ Correlation → ↑ Portfolio UL → Concentration
Risk increases
Formula: Higher ρ → less diversification benefit
Final Answers: EL_A=Rs.20,000 | EL_B=Rs.1,05,000 |   5 Marks Total
UL_A=Rs.4.00L | UL_B=Rs.14.70L | UL_Portfolio(ρ=0.20)=Rs.15.99L |
UL_Portfolio(ρ=0.35)=Rs.16.53L
Q5   Answer the following:   [10]
CO3; SO-   A   Given: Borrow USD 100m @ 3.6% | Sell Spot USD @ Rs. 93.70 | Buy 1-yr Fwd
8;   USD @ Rs. 97.50 | Invest INR @ 8% | Spot after 1yr = Rs. 97.80
BL-Apply
Step   Working / Calculation   Marks
Zero-Arbitrage Forward Rate (IRP): F* = S × (1 + r_INR)   1
/ (1 + r_USD) = 93.70 × (1.08) / (1.036) = 93.70 ×
1
1.04247 = Rs. 97.68
Formula: F* = S × (1+r_d)/(1+r_f)
Actual Forward = Rs. 97.50 | IRP Forward = Rs. 97.68   ½
Since Actual Fwd (97.50) < IRP Fwd (97.68) → USD is
2   underpriced forward → Arbitrage EXISTS: Strategy:
Borrow USD, Convert Spot, Invest in INR, Buy USD
Forward
[05]
Flow Diagram: Today: Borrow USD 100m → Sell @   1
93.70 → Receive INR 9,370m → Invest @ 8% After 1yr:
3   INR receipt = 9,370m × 1.08 = INR 10,119.60m Buy USD
Forward: Pay Rs. 97.50/USD → Pay INR to buy USD
100m × 1.036 = USD 103.6m fwd
USD Repayment at maturity: 100m × 1.036 = USD   ½
4   103.60m INR needed to buy USD 103.60m @ fwd 97.50:
103.60m × 97.50 = INR 10,101m
Arbitrage Gain = INR Receipts − INR paid for Fwd USD   1
= 10,119.60m − 10,101m = INR 18.60m = Rs. 18.6
5
Crores (Alternatively: (F* − Actual Fwd) × Loan Amount
= (97.68 − 97.50) × 103.6m ≈ Rs. 18.65m)
********** 8 **********
--- page 9 ---
Formula: Gain = INR receipts − INR forward
payment
Spot rate after 1yr = Rs. 97.80 (not used in CIA —   1
covered by forward contract)
6
Formula: CIA locks in via Forward → not exposed
to spot rate risk
Final Answer: IRP Forward = Rs. 97.68 | Arbitrage Gain ≈ Rs.   5 Marks
18.60 Crores | Strategy: Borrow USD → Convert INR → Invest   Total
→ Buy USD Forward
CO3; SO-   B   Indian Exporter: £6 per garment | Cost = Rs. 600 | 2-Month settlement | Spot:
8;   £=112.50, $=93.70 | 2m Fwd: £=112.79, $=93.96
BL-Apply
Interest Rates: £=3.75%, $=3.6%, Rs.=5.25%
Step   Working / Calculation   Marks
Option 1: Invoice in Sterling (£6) Sell £ at 2-month Forward   1
Rate = Rs. 112.79/£ INR Receipt per garment = £6 ×
1
112.79 = Rs. 676.74
Formula: INR = FC amount × Forward Rate
Option 2: Invoice in USD Convert £6 to USD at Spot: 6 ×   1½
112.50 / 93.70 = USD 7.202 Sell USD at 2-month Forward =
2   Rs. 93.96/USD INR Receipt = 7.202 × 93.96 = Rs. 676.50
Formula: USD = £ × (Spot £/Rs) / (Spot $/Rs); INR
= USD × Fwd $/Rs
Comparison: Sterling Invoice: Rs. 676.74 per garment →   1   [05]
3   Profit = 676.74 − 600 = Rs. 76.74 USD Invoice: Rs. 676.50
per garment → Profit = 676.50 − 600 = Rs. 76.50
Decision: INVOICE IN STERLING (£) Reason: Higher INR   1½
realization (Rs. 676.74 > Rs. 676.50) by Rs. 0.24 per
garment Additionally, Sterling forward (£=112.79) reflects
4
higher premium vs spot (112.50) = Rs. 0.29 appreciation
Both options lock in via forward contracts, eliminating
currency risk
Final Answer: Invoice in STERLING | INR/garment: £ option = Rs.   5 Marks T
676.74 vs $ option = Rs. 676.50 | Difference = Rs. 0.24 | Recommend
GBP
********** 9 **********
--- page 10 ---
Q6   Answer the following:   [10]
CO A Company A (British): Wants USD; can borrow GBP@8.5%, USD@5.8% | Company B (US):
1;   Wants GBP; can borrow GBP@8.1%, USD@5.2% | Bank earns 15bps; each Co. gains
SO-
20bps
1;
BL-   Step   Working / Calculation   Marks
App
ly   Comparative Advantage Analysis: GBP Differential: 8.5% − 8.1% =   1
0.4% (B has advantage in GBP) USD Differential: 5.8% − 5.2% =
0.6% (B has advantage in USD too) QSD = Larger diff − Smaller diff
= 0.6% − 0.4% = 0.2% = 20bps (Total gain to split) Bank earns 15bps
1
→ Each company gets 20bps (since total = bank 15bps + both cos
20bps each = 55bps > 20bps) Note: Total QSD = 20bps → Bank
15bps + 2×20bps = 55bps → structure adjusted
Formula: QSD = |Diff_currency1 − Diff_currency2|
Wait — Re-check: Total QSD = 20bps to share Bank gets 15bps;   ½
each company gets (20 − 15)/2 = 2.5bps each — that's too small
Alternative reading: Bank earns 15bps from each company (30bps
2
total); each co gains 20bps Total benefit needed = 30 + 20 + 20 =
70bps → QSD must be at least 70bps. With QSD = 0.20% = 20bps
total, the standard split: each gains (20bps − 15bps)/2 = 2.5bps each.
[05]
Swap Structure (standard interpretation): • Co. A: Borrows GBP @   1
8.5% (comparative advantage) → swaps to pay USD • Co. B:
3
Borrows USD @ 5.2% (comparative advantage) → swaps to pay GBP
• Bank acts as intermediary, earns spread
Effective Costs after swap: • Co. A wants USD: Effective rate = 5.8%   1½
− 0.20% gain = 5.60% • Co. B wants GBP: Effective rate = 8.1% −
4
0.20% gain = 7.90% • Bank net spread = 0.15% = 15bps
Formula: Effective Cost = Direct Market Rate − Gain
Cash Flow Structure: → Co.A pays GBP 8.5% to GBP market;   1
receives GBP from Bank; pays USD to Bank → Co.B pays USD 5.2%
5
to USD market; receives USD from Bank; pays GBP to Bank → Bank
nets GBP and USD flows, earning 15bps
Final Answer: QSD = 20bps | A: USD effective = 5.60% | B: GBP effective   5 Marks
= 7.90% | Bank: 15bps   Total
CO B Long Nifty 22,500 CE @ Premium Rs. 350 | Short Nifty 22,500 PE @ Premium Rs. 280 | Net
1;   Cost = 350 − 280 = Rs. 70 (debit)
SO-
1;   Synthetic Long: Buying a Call + Selling a Put at the SAME strike creates a Synthetic Long
BL-   Futures position — replicating the payoff of buying the index outright.
App   Payoff Calculation: Long CE Payoff = max(S−K,0)−Premium; Short PE Payoff =
ly   Premium−max(K−S,0)   [05]
Expiry   Long Call 22500 P/L   Short Put 22500 P/L   Net Option   Net P/L
Level   P/L   (after
Rs.70
cost)
22,800   300−350 = −50   280 (PE expires) = +280   −50+280 =   230−70
+230   = +160
********** 10 **********
--- page 11 ---
22,200   CE expires: −350   (22500−22200)−280=300−280=+20… Actual:   −350+(−20) −370+70
Put exercised against: −(22500−22200)+280   = −370   = −300
= −20
22,500   CE expires: −350   PE expires: +280   −70   −70+70
= 0
23,500   (23500−22500)−350=1000−35   PE expires: +280   +930   930−70
0=+650   = +860
Step   Working / Calculation   Marks
Payoff at 22,800 (Rs. +160) → Market above strike: net positive [1] Payoff   5
at 22,200 (Rs. −300) → Market below strike: net negative [1] Payoff at
Marks 22,500 (Rs. 0) → At-the-money: break-even [1] Payoff at 23,500 (Rs.
+860) → Far above strike: maximum upside [1] Nature: SYNTHETIC
LONG FUTURES — unlimited upside, unlimited downside [1]
When to use: When bullish on index; want long exposure without actual futures margin;
cheaper than outright futures
Mark Distribution: 4 payoffs × 1 mark each + Nature identification (1)   5 Marks Total
Q7   Answer the following:   [10]
CO1; SO- A   Step Working / Calculation   Marks
1;
BL-Analyze   Put-Call Parity (for European options): C + K×e^(−rT) = P +   1
S LHS = C + PV(K) = 130 + 500×e^(−0.0525×0.25) = 130
1   + 500×e^(−0.013125) = 130 + 500×0.9870 = 130 + 493.48
= Rs. 623.48
Formula: C + Ke^{-rT} = P + S
2   RHS = P + S = 105 + 492 = Rs. 597.00   ½
Compare: LHS (623.48) > RHS (597.00) Mismatch = Rs.   ½
26.48 → ARBITRAGE OPPORTUNITY EXISTS (LHS
3
overpriced relative to RHS: Call is overpriced or Put is
underpriced)
Arbitrage Strategy — SELL overpriced side (LHS), BUY   1
underpriced side (RHS): • SELL the Call (C) for Rs. 130 •   [05]
4
BORROW PV(K) = Rs. 493.48 at 5.25% for 0.25yr • BUY
the Put (P) for Rs. 105 • BUY the Stock (S) for Rs. 492
Cash Flows TODAY: Inflows: +130 (sell C) + 493.48   1
5   (borrow) Outflows: −105 (buy P) − 492 (buy S) Net =
623.48 − 597 = +Rs. 26.48 → RISK-FREE PROFIT upfront
At Expiry: All positions offset → No net cash flow needed   ½
6   The Rs. 26.48 locked in today is the arbitrage profit (PV
terms)
Factors affecting European Call/Put prices: • Stock Price   ½
(S) ↑ → C ↑, P ↓ | Strike (K) ↑ → C ↓, P ↑ • Time (T) ↑ →
7
Both C & P ↑ | Volatility (σ) ↑ → Both ↑ • Interest Rate (r) ↑
→ C ↑, P ↓ | Dividend → C ↓, P ↑
********** 11 **********
--- page 12 ---
Final Answer: LHS=623.48 > RHS=597.00 → Arbitrage profit =   5 Marks
Rs. 26.48 | Strategy: Sell Call + Borrow + Buy Put + Buy Stock   Total
CO1; SO- B Definition: Operational Risk is the risk of loss resulting from inadequate or failed
1;   internal processes, people, systems, or from external events. It includes legal risk but
BL-Analyze
excludes strategic and reputational risk (Basel III definition).
Keywords: Basel III, Pillar 2, AMA, BIA, Fraud, Cyber Risk, RBI Guidelines
• Sub-Category 1: Internal Fraud — unauthorized transactions, embezzlement (e.g.,
Satyam accounting fraud)
• Sub-Category 2: External Fraud — phishing, cyber-attacks (e.g., Cosmos Bank
SWIFT hack Rs. 94.42 Cr)
• Sub-Category 3: Employment Practices — employee misconduct, HR failures
• Sub-Category 4: Clients/Products — mis-selling, KYC failures
• Sub-Category 5: Business Disruption — IT failures, data breaches
Recent Indian Banking Frauds (mapped to Op-Risk categories):
• Punjab National Bank (PNB) Scam 2018: Nirav Modi/Mehul Choksi — fraudulent
LoUs via SWIFT bypass. Category: Internal Fraud + System/Process failure. Loss:
~Rs. 13,000 Cr
• Cosmos Bank SWIFT Hack 2018: External attack bypassed SWIFT → Rs. 94.42
Cr siphoned. Category: External Fraud + Technology failure
Mitigation Tools & Regulatory Framework:   [05]
• Basel III: Pillar 1 — Operational Risk Capital under BIA/STA/AMA approaches |
Pillar 2 — ICAAP
• RBI Guidelines: Cyber Security Framework, Fraud Risk Management, Risk
Governance at Board level
•   Internal Controls: SOD (Segregation of Duties), maker-checker systems, forensic
audit, whistleblower policies
Hybrid Securities:
Definition: Hybrid Securities combine features of both equity and debt instruments.
Examples: AT1 Bonds (Perpetual Bonds), Convertible Debentures (CCDs),
Preference Shares.
• Role in Financial Engineering: Used to optimize capital structure, fulfill Basel III
Tier 1/Tier 2 capital requirements, and offer risk-return flexibility
Mark Distribution: Op-Risk definition (1) + Sub-categories with
examples (1) + 2 fraud cases mapped (1) + Mitigation/Basel III (1)
+ Hybrid Securities (1)
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper ac65b0e16e29

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/MBATech_Computer_7047/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 09 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: V/Semester X(Exam Year: 2025-2026)
Subject: Financial Engineering
Date: 09 May 2026   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No. _1_is compulsory.
3. Out of remaining questions, attempt any_4_questions.
4. In all_5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary
9. Use of Scientific Calculator allowed
Q1   Answer briefly:   [10
]
CO1; SO-   a. Definition: A Forward Rate Agreement (FRA) is an over-the-counter (OTC) derivative contract
1;   between two parties — a buyer and a seller — that fixes (locks in) an interest rate for a future
BL-   borrowing or lending transaction for a specified notional principal over an agreed future period.
Understan
d   Keywords: FRA, OTC, Notional Principal, Settlement Date, Reference Rate (LIBOR/MIBOR),
Contract Rate
•   Participants: Buyer (borrower, who wants to LOCK IN a rate) and Seller (lender / bank)
•   Key Milestones: Trade Date → Setting Date → Settlement Date → Maturity Date
•   Settlement Mechanism: Cash-settled on Settlement Date; difference between Reference Rate
[03
and Contract Rate is paid on discounted basis
]
•   Settlement Formula: Payment = [(Reference Rate – Contract Rate) × Notional × Days/360] /
[1 + (Reference Rate × Days/360)]
Example: Co. A anticipates borrowing ₹10 Cr at MIBOR after 3 months for 6 months. Enters 3×9
FRA at 7% (contract rate). If MIBOR settles at 8%, settlement receipt compensates for the extra
cost.
•   Benefit: Eliminates interest rate uncertainty; hedger knows exact future cost
Mark Distribution: Definition (1) + Participants/Milestones (1) + Settlement mechanism
with formula (1)
CO1; SO-   b Hedging Definition: Hedging is the process of taking an offsetting position in a financial
1;   .   instrument to reduce or eliminate the risk of adverse price movements in an existing position.
BL-
Arbitrage Definition: Arbitrage is the simultaneous purchase and sale of the same or equivalent
Understan
asset in different markets to profit from price discrepancies, with zero risk and zero net   [03
d
investment.   ]
Comparison Table — Keywords: Risk, Objective, Cost, Duration
Parameter   Hedging   Arbitrage
********** 1 **********
--- page 2 ---
Objective   Risk reduction / protection   Risk-free profit
Risk   Residual risk may remain   Zero risk (riskless)
Cost   Premium / opportunity cost   Zero net investment
Duration   Ongoing, long-term   Instantaneous
Example   Exporter buys USD put option   Buy low on NSE, sell high on
BSE
Mark Distribution: Hedging definition with example (1) + Arbitrage definition with
example (1) + Comparison: objective/risk/cost (1)
CO1; SO-   c. Statement Interpretation: The 95%, 1-day VaR of INR 1.75 Crores means: with 95% confidence,
1;   the portfolio will NOT lose more than ₹1.75 Crores in a single trading day under normal market
BL-   conditions.
Remember
Key Keywords: Confidence Level, Holding Period, Loss Threshold, Tail Risk, Normal
Distribution
•   Significance: Quantifies downside risk; aids in capital allocation and setting risk limits   [02
•   Limitation 1: Assumes normal distribution — fails during tail events (Black Swan events)   ]
•   Limitation 2: Does not reveal the magnitude of losses BEYOND the VaR threshold
•   Limitation 3: Backward-looking — based on historical data; not predictive in structural
breaks
Mark Distribution: Correct interpretation of statement (1) + Significance + 2 limitations
(1)
CO1; SO-   d. Definition: A Credit Default Swap (CDS) is an OTC derivative contract that acts like insurance
1;   against credit default. The Protection Buyer pays a periodic premium (CDS Spread) to the
BL-   Protection Seller, who compensates the buyer if the Reference Entity defaults.
Understan
d   Keywords: Protection Buyer, Protection Seller, Reference Entity, CDS Spread, Credit Event
•   Participants: (i) Protection Buyer — hedges credit risk; (ii) Protection Seller — earns
premium; (iii) Reference Entity — underlying borrower
•   Settlement: Physical (delivery of defaulted bond) or Cash (face value minus recovery value)   [02
•   Role in 2008 Crisis: CDSs were sold massively on subprime mortgage-backed securities   ]
(MBS). When MBS defaulted, protection sellers (like AIG) faced unmanageable payouts →
systemic collapse
•   Key Issue: Lack of regulation, naked CDS positions, and excessive leverage amplified
contagion
Mark Distribution: CDS definition with participants/example (1) + Role in   2
2008 crisis: naked positions/AIG/contagion (1)
Q2   Answer the following:   [10]
CO2; SO- A Given Data: 5 Equal-Weighted Stocks (20% each) | Portfolio: Rs. 5 Crores (assumed) | Prices
1;   Year 0-5:
BL-Apply
Year   Stock A   Stock B   Stock C   Stock D   Stock E
0   317   281   400   437   277
[05]
1   350   300   370   478   310
2   300   277   457   526   347
3   280   256   415   564   386
4   325   310   460   612   423
********** 2 **********
--- page 3 ---
5   380   396   510   644   458
Step 1: Calculate Annual Returns for Each Stock (Year-on-Year %)
Formula: Return(t) = [Price(t) / Price(t-1)] − 1
Year   A (%)   B (%)   C (%)   D (%)   E (%)   Portfolio Ret (%)
Yr1   10.41   6.76   -7.50   9.38   11.91   6.19
Yr2   -14.29   -7.67   23.51   10.04   11.94   4.71
Yr3   -6.67   -7.58   -9.19   7.22   11.24   -0.99
Yr4   16.07   21.09   10.84   8.51   9.59   13.22
Yr5   16.92   27.74   10.87   5.23   8.27   13.81
Note: Portfolio Return = Equal-weighted average of 5 stock returns (20% × each)
Step 2: Sort Portfolio Returns in Ascending Order
Step   Working / Calculation   Marks
2a   Sort all 5 portfolio annual returns from worst to best:   ½
Rank 1 (Worst): −0.99% (Year 3) Rank 2: 4.71% (Year 2) Rank   ½
3: 6.19% (Year 1) Rank 4: 13.22% (Year 4) Rank 5 (Best):
13.81% (Year 5)
Step 3: Identify the 95% VaR Observation
Step   Working / Calculation   Marks
For 95% CL with 5 observations: VaR = 5% worst observation =   1
worst 5% of returns 5% × 5 = 0.25 → Round up to 1st
3a   observation (most conservative)
Formula: VaR percentile: (1 − CL) × N = 0.05 × 5 = 0.25 → 1st
observation
1-Day VaR basis: worst annual return = −0.99% First, convert: 1-   ½
3b   Day Return = −0.99% / √252 = −0.0624% per day
Formula: 1-Day σ = Annual Return / √252
Step 4: Calculate Portfolio VaR
Assuming Portfolio Value = Rs. 5 Crores (standard assumption when not specified):
Step   Working / Calculation   Marks
1-Day VaR (absolute) = Portfolio Value × |Worst 1-Day   1
Return| = 5,00,00,000 × 0.000624 = Rs. 31,200 (1-day
4a
VaR)
Formula: VaR = P × |r|
10-Day VaR = 1-Day VaR × √10 = 31,200 × 3.1623 = Rs.   1
4b   98,665
Formula: N-Day VaR = 1-Day VaR × √N
ALTERNATE: Using worst annual portfolio return   ½
directly: 95% 1-Year VaR = 5 Cr × 0.0099 = Rs. 4.95
4c
Lakhs 10-Day VaR = 4.95L × √(10/252) = Rs. 98,646 ≈
Rs. 98,700
********** 3 **********
--- page 4 ---
Step 5: Inference & Rebalancing Recommendation
Step   Working / Calculation   Marks
The 95%, 10-Day VaR ≈ Rs. 98,700 means with 95% confidence,   ½
5a   maximum loss in 10 days ≤ Rs. 98,700 Single worst year was Year 3
(−0.99% portfolio). Stocks A & B showed negative returns.
Recommendation: YES — rebalance. Stock B shows persistent   ½
5b   underperformance (−7.67%). Consider reducing exposure to A & B
and increasing D & E which show consistent positive returns.
Final Answer: 95% 10-Day Portfolio VaR ≈ Rs. 98,700 | Rebalance: Reduce B &   5
A; increase D & E   Marks
Total
CO2; SO- B Concept: A Synthetic Short Position is created using options to replicate the payoff of actually
1;   short-selling a stock, WITHOUT borrowing and selling the stock.
BL-Apply
Strategy: BUY PUT + SELL CALL at the SAME Strike Price
Numerical Example: Reliance CMP = Rs. 2,500 | Strike = Rs. 2,500 | Put Premium (Buy) = Rs. 80 |
Call Premium (Receive) = Rs. 70 | Net Cost = Rs. 10 per share
Step   Working / Calculation   Marks
1   Buy 1 ATM Put @ Strike 2500, Pay Premium = Rs. 80   ½
2   Sell 1 ATM Call @ Strike 2500, Receive Premium = Rs. 70   ½
Net Premium Paid = 80 − 70 = Rs. 10 (net debit)   ½
3
Formula: Net Cost = Put Premium − Call Premium
Payoff at Expiry: • If Market = 2300 (falls): Put profit = 200; Call   1
expires worthless → Net = 200 − 10 = +Rs. 190 • If Market =
4   2500: Both expire worthless → Net Loss = −Rs. 10 • If Market =
2700 (rises): Put worthless; Call loss = 200 → Net = −200 − 10 =
−Rs. 210   [05]
Break-even = Strike − Net Premium = 2500 − 10 = Rs. 2,490   ½
5
Formula: BE = K − Net Premium
Part (ii): Synthetic Short vs Actual Short — Comparison
Parameter   Synthetic Short   Actual Short Sell
Risk   Defined (put premium paid)   Unlimited upside = unlimited loss
Margin   No SEBI margin needed (just   SEBI prescribed VaR + ELM margin
premium)
Cost   Net premium (small)   Borrowing cost + margin cost
Dividend Risk   No dividend risk   Short seller must pay dividend
Regulatory   No stock borrowing needed   Subject to SEBI short-sell rules
Mark Distribution: Strategy construction (1.5) +
Payoff table (2) + Comparison table (1.5)
********** 4 **********
--- page 5 ---
Q3   Answer the following:   [10]
CO3; SO- A Given: EPS₀ = Rs.18 | DPR = 65% | D₀ = 18 × 0.65 = Rs. 11.70 | Rf = 5.25% | Rm = 14% | β = 1.90
8;   | CMP = Rs. 320
BL-Apply   Growth Phases: Phase 1: g = 22% for 6 years | Phase 2: g declines from 22% to 8% over 3 years |
Phase 3: g = 5% (perpetuity)
Step   Working / Calculation   Marks
Calculate Ke using CAPM: Ke = Rf + β(Rm − Rf) = 5.25% +   1
1.90 × (14% − 5.25%) = 5.25% + 1.90 × 8.75% = 5.25% +
1
16.625% = 21.875% ≈ 21.88%
Formula: Ke = Rf + β(Rm − Rf)
Phase 2: Growth declines linearly from 22% to 8% over 3 years:   ½
Year 7: g = 22% − (22%−8%)/3 × 1 = 22% − 4.67% = 17.33%
2
Year 8: g = 22% − (22%−8%)/3 × 2 = 22% − 9.33% = 12.67%
Year 9: g = 22% − (22%−8%)/3 × 3 = 8.00%
Phase 1 Dividends (Years 1-6): D₀ = 11.70; g = 22% each year   1
D1=14.27 | D2=17.41 | D3=21.24 | D4=25.91 | D5=31.61 |
3
D6=38.57
Formula: Dt = D(t-1) × (1+g)
Phase 2 Dividends (Years 7-9): D7 = 38.57 × 1.1733 = 45.25 | D8   ½
4
= 45.25 × 1.1267 = 51.01 | D9 = 51.01 × 1.08 = 55.09
[05]
Terminal Value at end of Year 9: TV9 = D10 / (Ke − g∞) = 55.09   1
5   × 1.05 / (0.2188 − 0.05) = 57.84 / 0.1688 = Rs. 342.65
Formula: TV = D(n+1)/(Ke − gL)
PV of Phase 1 (Ke=21.88%): Sum of PV of D1-D6 PV =   ½
14.27/1.2188 + 17.41/1.2188² + ... ≈ 11.71 + 11.72 + 11.74 +
6
11.77 + 11.78 + 11.80 = Rs. 70.52
Formula: PV = Dt/(1+Ke)^t
PV of Phase 2 (D7-D9): PV = 45.25/1.2188⁷ + 51.01/1.2188⁸ +   ½
7
55.09/1.2188⁹ ≈ 10.04 + 9.28 + 8.22 = Rs. 27.54
PV of Terminal Value: PV(TV9) = 342.65/1.2188⁹ =   ½
8   342.65/5.371 = Rs. 63.80
Formula: PV(TV) = TV/(1+Ke)^n
Intrinsic Value = PV(Ph1) + PV(Ph2) + PV(TV) = 70.52 + 27.54   ½
+ 63.80 = Rs. 161.86 Valuation: CMP = Rs. 320 >> IV = Rs.
9
161.86 → Stock is OVERVALUED → SELL
Formula: IV = ΣPV(Dt) + PV(TV)
Final Answer: Intrinsic Value ≈ Rs. 161.86 | CMP Rs. 320 >> IV → Stock   5 Marks Total
OVERVALUED → Recommendation: SELL/SHORT
CO3; SO- B Given: FV = Rs. 1,000 | Coupon = 7% p.a. → Annual Coupon = Rs. 70 | YTM = 9% | Maturity = 5
8;   Years
BL-Apply   [05]
Step 1: Bond Pricing using DCF Tabular Method
Step   Working / Calculation   Marks
********** 5 **********
--- page 6 ---
PV Factor at 9%: 1/(1.09)^t for t = 1 to 5 t=1: 0.9174 | t=2:   ½
1   0.8417 | t=3: 0.7722 | t=4: 0.7084 | t=5: 0.6499
Formula: PV Factor = 1/(1+r)^t
PV of Coupons: t=1: 70×0.9174=64.22 | t=2: 70×0.8417=58.92 |   ½
2   t=3: 70×0.7722=54.05 t=4: 70×0.7084=49.59 | t=5:
70×0.6499=45.49 Total PV Coupons = 272.27
3   PV of Face Value: 1000 × 0.6499 = Rs. 649.93   ½
Bond Price = 272.27 + 649.93 = Rs. 922.20 (Coupon 7% < YTM   ½
4   9% → Bond trades at DISCOUNT — confirmed)
Formula: P = Σ[C/(1+r)^t] + FV/(1+r)^n
Step 2: Macaulay Duration
Step   Working / Calculation   Marks
Duration = Σ[t × PV(CFt)] / P Numerator = 1×64.22 + 2×58.92 +   1
3×54.05 + 4×49.59 + 5×(45.49+649.93) = 64.22 + 117.84 +
5   162.15 + 198.36 + 3,477.10 = 4,019.67 Macaulay Duration =
4,019.67 / 922.20 = 4.359 Years
Formula: D = Σ[t × PV(CFt)] / Bond Price
Step 3: Modified Duration
Step   Working / Calculation   Marks
Modified Duration = Macaulay Duration / (1 + YTM) = 4.359 /   ½
1.09 = 3.998 ≈ 4.00 Years Interpretation: 1% rise in YTM →
6
Bond Price falls by ≈ 4.00%
Formula: MD = D/(1+r)
Step 4: Convexity
Step   Working / Calculation   Marks
Convexity = [1/(P×(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t] Numerator =   1
1(2)×70/1.09 + 2(3)×70/1.09² + 3(4)×70/1.09³ + 4(5)×70/1.09⁴ +
5(6)×1070/1.09⁵ = 128.44 + 353.36 + 648.46 + 994.92 +
7
17,587.82 = 19,713.00 Convexity = 19,713 / (922.20 × 1.09²) =
19,713 / 1,095.19 = 18.00
Formula: Conv = [1/(P(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t]
Price Change Approximation using MD & Convexity: ΔP/P ≈   ½
−MD × Δy + ½ × Conv × (Δy)² MD captures linear, Convexity
8
corrects for curvature of price-yield relationship
Formula: ΔP/P ≈ −MD·Δy + ½·Conv·(Δy)²
Final Answers: Bond Price = Rs. 922.20 | Mac. Duration = 4.36 yrs |   5 Marks Total
Modified Duration = 4.00 | Convexity = 18.00
********** 6 **********
--- page 7 ---
Q4   Answer the following:   [10]
CO2;   A Repricing Buckets: 1-6m (A=80L, L=70L) | 6-12m (A=40L, L=50L) | 1-3yr (A=20L, L=25L) |
SO-1;   3-5yr (A=15L, L=10L)
BL-
Step   Working / Calculation   Marks
Apply
Calculate Gap for each bucket: Gap = Rate Sensitive Assets   ½
1   (RSA) − Rate Sensitive Liabilities (RSL)
Formula: Gap = RSA − RSL
1-6m: Gap = 80 − 70 = +Rs. 10 Lakh (Positive/Asset-Sensitive)   ½
6-12m: Gap = 40 − 50 = −Rs. 10 Lakh (Negative/Liability-
Sensitive) 1-3yr: Gap = 20 − 25 = −Rs. 5 Lakh (Negative) 3-5yr:
Gap = 15 − 10 = +Rs. 5 Lakh (Positive)
Scenario (i): Rates ↑ 50 bps (+0.50%) in 1-6 month bucket ΔNII   1½
= Gap × Δr × Time Fraction = 10 Lakh × 0.005 × (6/12) =
2   10,00,000 × 0.005 × 0.5 = Rs. 2,500 Annualized ΔNII = Rs. 5,000   [05]
or use: ΔNII = Gap × Δr = 10L × 0.005 = Rs. 5,000 p.a.
Formula: ΔNII = Gap × Δr
Scenario (ii): Rates ↓ 25 bps (−0.25%) in 1-3 year bucket ΔNII =   1½
Gap × Δr = −5,00,000 × (−0.0025) = +Rs. 1,250 p.a. Negative
3
gap + rate decrease → NII INCREASES (beneficial scenario)
Formula: ΔNII = Gap × Δr
ALM Concept: Asset-Liability Management (ALM) involves   1
managing the balance sheet to optimize NII while controlling
4
interest rate risk. Gap Analysis identifies mismatches between
RSA and RSL to assess NII sensitivity to rate changes.
Final Answers: Scenario(i) +50bps: ΔNII = +Rs. 5,000 | Scenario(ii)   5 Marks Total
−25bps in 1-3yr: ΔNII = +Rs. 1,250 | Positive Gap → Rate ↑ beneficial
CO2;   B JP Bank | Asset A: EAD=40m, PD=0.25%, LGD=20%, σPD=5%, σLGD=15% | Asset B:
SO-1;   EAD=60m, PD=0.50%, LGD=35%, σPD=7%, σLGD=10% | ρ=0.20
BL-
Step   Working / Calculation   Marks
Apply
Expected Loss (EL) for each asset: EL_A = EAD_A × PD_A   1
× LGD_A = 40m × 0.0025 × 0.20 = Rs. 20,000 EL_B =
1   EAD_B × PD_B × LGD_B = 60m × 0.005 × 0.35 = Rs.
1,05,000
Formula: EL = EAD × PD × LGD
Unexpected Loss (UL) for each asset: UL_i = EAD_i ×   ½
2   √(LGD²×σPD² + PD²×σLGD²)   [05]
Formula: UL = EAD × √(LGD²·σPD² + PD²·σLGD²)
UL_A = 40m × √[(0.20²×0.05²) + (0.0025²×0.15²)] = 40m ×   ½
√[(0.04×0.0025) + (0.00000625×0.0225)] = 40m × √[0.0001
+ 0.000000140625] = 40m × √0.000100140625 = 40m ×
0.010007 = Rs. 4,00,281 ≈ Rs. 4.00 Lakh
UL_B = 60m × √[(0.35²×0.07²) + (0.005²×0.10²)] = 60m ×   ½
√[(0.1225×0.0049) + (0.000025×0.01)] = 60m ×
√[0.00060025 + 0.00000025] = 60m × √0.0006005 = 60m ×
0.02451 = Rs. 14,70,488 ≈ Rs. 14.70 Lakh
********** 7 **********
--- page 8 ---
Portfolio Unexpected Loss (ρ = 0.20): UL_P = √(UL_A² +   1
UL_B² + 2ρ×UL_A×UL_B) = √[(4.00)² + (14.70)² +
3   2×0.20×4.00×14.70] All in Lakh: = √[16.00 + 216.09 +
23.52] = √255.61 = Rs. 15.99 Lakh
Formula: UL_P = √(UL_A² + UL_B² + 2ρ·UL_A·UL_B)
Risk Contribution of each asset to Portfolio UL: RC_A =   1
UL_A × (UL_A + ρ×UL_B) / UL_P = 4.00 × (4.00 +
0.20×14.70) / 15.99 = 4.00 × 6.94 / 15.99 = Rs. 1.736 Lakh
4   RC_B = UL_B × (UL_B + ρ×UL_A) / UL_P = 14.70 × (14.70
+ 0.20×4.00) / 15.99 = 14.70 × 15.50 / 15.99 = Rs. 14.26
Lakh
Formula: RC_i = UL_i(UL_i + ρ·UL_j)/UL_P
Impact of ρ increasing to 0.35: New UL_P = √[16 + 216.09 +   1
2×0.35×4.00×14.70] = √[16+216.09+41.16] = √273.25 = Rs.
5   16.53 Lakh ↑ Correlation → ↑ Portfolio UL → Concentration
Risk increases
Formula: Higher ρ → less diversification benefit
Final Answers: EL_A=Rs.20,000 | EL_B=Rs.1,05,000 |   5 Marks Total
UL_A=Rs.4.00L | UL_B=Rs.14.70L | UL_Portfolio(ρ=0.20)=Rs.15.99L |
UL_Portfolio(ρ=0.35)=Rs.16.53L
Q5   Answer the following:   [10]
CO3; SO-   A   Given: Borrow USD 100m @ 3.6% | Sell Spot USD @ Rs. 93.70 | Buy 1-yr Fwd
8;   USD @ Rs. 97.50 | Invest INR @ 8% | Spot after 1yr = Rs. 97.80
BL-Apply
Step   Working / Calculation   Marks
Zero-Arbitrage Forward Rate (IRP): F* = S × (1 + r_INR)   1
/ (1 + r_USD) = 93.70 × (1.08) / (1.036) = 93.70 ×
1
1.04247 = Rs. 97.68
Formula: F* = S × (1+r_d)/(1+r_f)
Actual Forward = Rs. 97.50 | IRP Forward = Rs. 97.68   ½
Since Actual Fwd (97.50) < IRP Fwd (97.68) → USD is
2   underpriced forward → Arbitrage EXISTS: Strategy:
Borrow USD, Convert Spot, Invest in INR, Buy USD
Forward
[05]
Flow Diagram: Today: Borrow USD 100m → Sell @   1
93.70 → Receive INR 9,370m → Invest @ 8% After 1yr:
3   INR receipt = 9,370m × 1.08 = INR 10,119.60m Buy USD
Forward: Pay Rs. 97.50/USD → Pay INR to buy USD
100m × 1.036 = USD 103.6m fwd
USD Repayment at maturity: 100m × 1.036 = USD   ½
4   103.60m INR needed to buy USD 103.60m @ fwd 97.50:
103.60m × 97.50 = INR 10,101m
Arbitrage Gain = INR Receipts − INR paid for Fwd USD   1
= 10,119.60m − 10,101m = INR 18.60m = Rs. 18.6
5
Crores (Alternatively: (F* − Actual Fwd) × Loan Amount
= (97.68 − 97.50) × 103.6m ≈ Rs. 18.65m)
********** 8 **********
--- page 9 ---
Formula: Gain = INR receipts − INR forward
payment
Spot rate after 1yr = Rs. 97.80 (not used in CIA —   1
covered by forward contract)
6
Formula: CIA locks in via Forward → not exposed
to spot rate risk
Final Answer: IRP Forward = Rs. 97.68 | Arbitrage Gain ≈ Rs.   5 Marks
18.60 Crores | Strategy: Borrow USD → Convert INR → Invest   Total
→ Buy USD Forward
CO3; SO-   B   Indian Exporter: £6 per garment | Cost = Rs. 600 | 2-Month settlement | Spot:
8;   £=112.50, $=93.70 | 2m Fwd: £=112.79, $=93.96
BL-Apply
Interest Rates: £=3.75%, $=3.6%, Rs.=5.25%
Step   Working / Calculation   Marks
Option 1: Invoice in Sterling (£6) Sell £ at 2-month Forward   1
Rate = Rs. 112.79/£ INR Receipt per garment = £6 ×
1
112.79 = Rs. 676.74
Formula: INR = FC amount × Forward Rate
Option 2: Invoice in USD Convert £6 to USD at Spot: 6 ×   1½
112.50 / 93.70 = USD 7.202 Sell USD at 2-month Forward =
2   Rs. 93.96/USD INR Receipt = 7.202 × 93.96 = Rs. 676.50
Formula: USD = £ × (Spot £/Rs) / (Spot $/Rs); INR
= USD × Fwd $/Rs
Comparison: Sterling Invoice: Rs. 676.74 per garment →   1   [05]
3   Profit = 676.74 − 600 = Rs. 76.74 USD Invoice: Rs. 676.50
per garment → Profit = 676.50 − 600 = Rs. 76.50
Decision: INVOICE IN STERLING (£) Reason: Higher INR   1½
realization (Rs. 676.74 > Rs. 676.50) by Rs. 0.24 per
garment Additionally, Sterling forward (£=112.79) reflects
4
higher premium vs spot (112.50) = Rs. 0.29 appreciation
Both options lock in via forward contracts, eliminating
currency risk
Final Answer: Invoice in STERLING | INR/garment: £ option = Rs.   5 Marks T
676.74 vs $ option = Rs. 676.50 | Difference = Rs. 0.24 | Recommend
GBP
********** 9 **********
--- page 10 ---
Q6   Answer the following:   [10]
CO A Company A (British): Wants USD; can borrow GBP@8.5%, USD@5.8% | Company B (US):
1;   Wants GBP; can borrow GBP@8.1%, USD@5.2% | Bank earns 15bps; each Co. gains
SO-
20bps
1;
BL-   Step   Working / Calculation   Marks
App
ly   Comparative Advantage Analysis: GBP Differential: 8.5% − 8.1% =   1
0.4% (B has advantage in GBP) USD Differential: 5.8% − 5.2% =
0.6% (B has advantage in USD too) QSD = Larger diff − Smaller diff
= 0.6% − 0.4% = 0.2% = 20bps (Total gain to split) Bank earns 15bps
1
→ Each company gets 20bps (since total = bank 15bps + both cos
20bps each = 55bps > 20bps) Note: Total QSD = 20bps → Bank
15bps + 2×20bps = 55bps → structure adjusted
Formula: QSD = |Diff_currency1 − Diff_currency2|
Wait — Re-check: Total QSD = 20bps to share Bank gets 15bps;   ½
each company gets (20 − 15)/2 = 2.5bps each — that's too small
Alternative reading: Bank earns 15bps from each company (30bps
2
total); each co gains 20bps Total benefit needed = 30 + 20 + 20 =
70bps → QSD must be at least 70bps. With QSD = 0.20% = 20bps
total, the standard split: each gains (20bps − 15bps)/2 = 2.5bps each.
[05]
Swap Structure (standard interpretation): • Co. A: Borrows GBP @   1
8.5% (comparative advantage) → swaps to pay USD • Co. B:
3
Borrows USD @ 5.2% (comparative advantage) → swaps to pay GBP
• Bank acts as intermediary, earns spread
Effective Costs after swap: • Co. A wants USD: Effective rate = 5.8%   1½
− 0.20% gain = 5.60% • Co. B wants GBP: Effective rate = 8.1% −
4
0.20% gain = 7.90% • Bank net spread = 0.15% = 15bps
Formula: Effective Cost = Direct Market Rate − Gain
Cash Flow Structure: → Co.A pays GBP 8.5% to GBP market;   1
receives GBP from Bank; pays USD to Bank → Co.B pays USD 5.2%
5
to USD market; receives USD from Bank; pays GBP to Bank → Bank
nets GBP and USD flows, earning 15bps
Final Answer: QSD = 20bps | A: USD effective = 5.60% | B: GBP effective   5 Marks
= 7.90% | Bank: 15bps   Total
CO B Long Nifty 22,500 CE @ Premium Rs. 350 | Short Nifty 22,500 PE @ Premium Rs. 280 | Net
1;   Cost = 350 − 280 = Rs. 70 (debit)
SO-
1;   Synthetic Long: Buying a Call + Selling a Put at the SAME strike creates a Synthetic Long
BL-   Futures position — replicating the payoff of buying the index outright.
App   Payoff Calculation: Long CE Payoff = max(S−K,0)−Premium; Short PE Payoff =
ly   Premium−max(K−S,0)   [05]
Expiry   Long Call 22500 P/L   Short Put 22500 P/L   Net Option   Net P/L
Level   P/L   (after
Rs.70
cost)
22,800   300−350 = −50   280 (PE expires) = +280   −50+280 =   230−70
+230   = +160
********** 10 **********
--- page 11 ---
22,200   CE expires: −350   (22500−22200)−280=300−280=+20… Actual:   −350+(−20) −370+70
Put exercised against: −(22500−22200)+280   = −370   = −300
= −20
22,500   CE expires: −350   PE expires: +280   −70   −70+70
= 0
23,500   (23500−22500)−350=1000−35   PE expires: +280   +930   930−70
0=+650   = +860
Step   Working / Calculation   Marks
Payoff at 22,800 (Rs. +160) → Market above strike: net positive [1] Payoff   5
at 22,200 (Rs. −300) → Market below strike: net negative [1] Payoff at
Marks 22,500 (Rs. 0) → At-the-money: break-even [1] Payoff at 23,500 (Rs.
+860) → Far above strike: maximum upside [1] Nature: SYNTHETIC
LONG FUTURES — unlimited upside, unlimited downside [1]
When to use: When bullish on index; want long exposure without actual futures margin;
cheaper than outright futures
Mark Distribution: 4 payoffs × 1 mark each + Nature identification (1)   5 Marks Total
Q7   Answer the following:   [10]
CO1; SO- A   Step Working / Calculation   Marks
1;
BL-Analyze   Put-Call Parity (for European options): C + K×e^(−rT) = P +   1
S LHS = C + PV(K) = 130 + 500×e^(−0.0525×0.25) = 130
1   + 500×e^(−0.013125) = 130 + 500×0.9870 = 130 + 493.48
= Rs. 623.48
Formula: C + Ke^{-rT} = P + S
2   RHS = P + S = 105 + 492 = Rs. 597.00   ½
Compare: LHS (623.48) > RHS (597.00) Mismatch = Rs.   ½
26.48 → ARBITRAGE OPPORTUNITY EXISTS (LHS
3
overpriced relative to RHS: Call is overpriced or Put is
underpriced)
Arbitrage Strategy — SELL overpriced side (LHS), BUY   1
underpriced side (RHS): • SELL the Call (C) for Rs. 130 •   [05]
4
BORROW PV(K) = Rs. 493.48 at 5.25% for 0.25yr • BUY
the Put (P) for Rs. 105 • BUY the Stock (S) for Rs. 492
Cash Flows TODAY: Inflows: +130 (sell C) + 493.48   1
5   (borrow) Outflows: −105 (buy P) − 492 (buy S) Net =
623.48 − 597 = +Rs. 26.48 → RISK-FREE PROFIT upfront
At Expiry: All positions offset → No net cash flow needed   ½
6   The Rs. 26.48 locked in today is the arbitrage profit (PV
terms)
Factors affecting European Call/Put prices: • Stock Price   ½
(S) ↑ → C ↑, P ↓ | Strike (K) ↑ → C ↓, P ↑ • Time (T) ↑ →
7
Both C & P ↑ | Volatility (σ) ↑ → Both ↑ • Interest Rate (r) ↑
→ C ↑, P ↓ | Dividend → C ↓, P ↑
********** 11 **********
--- page 12 ---
Final Answer: LHS=623.48 > RHS=597.00 → Arbitrage profit =   5 Marks
Rs. 26.48 | Strategy: Sell Call + Borrow + Buy Put + Buy Stock   Total
CO1; SO- B Definition: Operational Risk is the risk of loss resulting from inadequate or failed
1;   internal processes, people, systems, or from external events. It includes legal risk but
BL-Analyze
excludes strategic and reputational risk (Basel III definition).
Keywords: Basel III, Pillar 2, AMA, BIA, Fraud, Cyber Risk, RBI Guidelines
• Sub-Category 1: Internal Fraud — unauthorized transactions, embezzlement (e.g.,
Satyam accounting fraud)
• Sub-Category 2: External Fraud — phishing, cyber-attacks (e.g., Cosmos Bank
SWIFT hack Rs. 94.42 Cr)
• Sub-Category 3: Employment Practices — employee misconduct, HR failures
• Sub-Category 4: Clients/Products — mis-selling, KYC failures
• Sub-Category 5: Business Disruption — IT failures, data breaches
Recent Indian Banking Frauds (mapped to Op-Risk categories):
• Punjab National Bank (PNB) Scam 2018: Nirav Modi/Mehul Choksi — fraudulent
LoUs via SWIFT bypass. Category: Internal Fraud + System/Process failure. Loss:
~Rs. 13,000 Cr
• Cosmos Bank SWIFT Hack 2018: External attack bypassed SWIFT → Rs. 94.42
Cr siphoned. Category: External Fraud + Technology failure
Mitigation Tools & Regulatory Framework:   [05]
• Basel III: Pillar 1 — Operational Risk Capital under BIA/STA/AMA approaches |
Pillar 2 — ICAAP
• RBI Guidelines: Cyber Security Framework, Fraud Risk Management, Risk
Governance at Board level
•   Internal Controls: SOD (Segregation of Duties), maker-checker systems, forensic
audit, whistleblower policies
Hybrid Securities:
Definition: Hybrid Securities combine features of both equity and debt instruments.
Examples: AT1 Bonds (Perpetual Bonds), Convertible Debentures (CCDs),
Preference Shares.
• Role in Financial Engineering: Used to optimize capital structure, fulfill Basel III
Tier 1/Tier 2 capital requirements, and offer risk-return flexibility
Mark Distribution: Op-Risk definition (1) + Sub-categories with
examples (1) + 2 fraud cases mapped (1) + Mitigation/Basel III (1)
+ Hybrid Securities (1)
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper c49dde311bdb

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/MBATech_DS_7052/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 09 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: V/Semester X(Exam Year: 2025-2026)
Subject: Financial Engineering
Date: 09 May 2026   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No. _1_is compulsory.
3. Out of remaining questions, attempt any_4_questions.
4. In all_5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary
9. Use of Scientific Calculator allowed
Q1   Answer briefly:   [10
]
CO1; SO-   a. Definition: A Forward Rate Agreement (FRA) is an over-the-counter (OTC) derivative contract
1;   between two parties — a buyer and a seller — that fixes (locks in) an interest rate for a future
BL-   borrowing or lending transaction for a specified notional principal over an agreed future period.
Understan
d   Keywords: FRA, OTC, Notional Principal, Settlement Date, Reference Rate (LIBOR/MIBOR),
Contract Rate
•   Participants: Buyer (borrower, who wants to LOCK IN a rate) and Seller (lender / bank)
•   Key Milestones: Trade Date → Setting Date → Settlement Date → Maturity Date
•   Settlement Mechanism: Cash-settled on Settlement Date; difference between Reference Rate
[03
and Contract Rate is paid on discounted basis
]
•   Settlement Formula: Payment = [(Reference Rate – Contract Rate) × Notional × Days/360] /
[1 + (Reference Rate × Days/360)]
Example: Co. A anticipates borrowing ₹10 Cr at MIBOR after 3 months for 6 months. Enters 3×9
FRA at 7% (contract rate). If MIBOR settles at 8%, settlement receipt compensates for the extra
cost.
•   Benefit: Eliminates interest rate uncertainty; hedger knows exact future cost
Mark Distribution: Definition (1) + Participants/Milestones (1) + Settlement mechanism
with formula (1)
CO1; SO-   b Hedging Definition: Hedging is the process of taking an offsetting position in a financial
1;   .   instrument to reduce or eliminate the risk of adverse price movements in an existing position.
BL-
Arbitrage Definition: Arbitrage is the simultaneous purchase and sale of the same or equivalent
Understan
asset in different markets to profit from price discrepancies, with zero risk and zero net   [03
d
investment.   ]
Comparison Table — Keywords: Risk, Objective, Cost, Duration
Parameter   Hedging   Arbitrage
********** 1 **********
--- page 2 ---
Objective   Risk reduction / protection   Risk-free profit
Risk   Residual risk may remain   Zero risk (riskless)
Cost   Premium / opportunity cost   Zero net investment
Duration   Ongoing, long-term   Instantaneous
Example   Exporter buys USD put option   Buy low on NSE, sell high on
BSE
Mark Distribution: Hedging definition with example (1) + Arbitrage definition with
example (1) + Comparison: objective/risk/cost (1)
CO1; SO-   c. Statement Interpretation: The 95%, 1-day VaR of INR 1.75 Crores means: with 95% confidence,
1;   the portfolio will NOT lose more than ₹1.75 Crores in a single trading day under normal market
BL-   conditions.
Remember
Key Keywords: Confidence Level, Holding Period, Loss Threshold, Tail Risk, Normal
Distribution
•   Significance: Quantifies downside risk; aids in capital allocation and setting risk limits   [02
•   Limitation 1: Assumes normal distribution — fails during tail events (Black Swan events)   ]
•   Limitation 2: Does not reveal the magnitude of losses BEYOND the VaR threshold
•   Limitation 3: Backward-looking — based on historical data; not predictive in structural
breaks
Mark Distribution: Correct interpretation of statement (1) + Significance + 2 limitations
(1)
CO1; SO-   d. Definition: A Credit Default Swap (CDS) is an OTC derivative contract that acts like insurance
1;   against credit default. The Protection Buyer pays a periodic premium (CDS Spread) to the
BL-   Protection Seller, who compensates the buyer if the Reference Entity defaults.
Understan
d   Keywords: Protection Buyer, Protection Seller, Reference Entity, CDS Spread, Credit Event
•   Participants: (i) Protection Buyer — hedges credit risk; (ii) Protection Seller — earns
premium; (iii) Reference Entity — underlying borrower
•   Settlement: Physical (delivery of defaulted bond) or Cash (face value minus recovery value)   [02
•   Role in 2008 Crisis: CDSs were sold massively on subprime mortgage-backed securities   ]
(MBS). When MBS defaulted, protection sellers (like AIG) faced unmanageable payouts →
systemic collapse
•   Key Issue: Lack of regulation, naked CDS positions, and excessive leverage amplified
contagion
Mark Distribution: CDS definition with participants/example (1) + Role in   2
2008 crisis: naked positions/AIG/contagion (1)
Q2   Answer the following:   [10]
CO2; SO- A Given Data: 5 Equal-Weighted Stocks (20% each) | Portfolio: Rs. 5 Crores (assumed) | Prices
1;   Year 0-5:
BL-Apply
Year   Stock A   Stock B   Stock C   Stock D   Stock E
0   317   281   400   437   277
[05]
1   350   300   370   478   310
2   300   277   457   526   347
3   280   256   415   564   386
4   325   310   460   612   423
********** 2 **********
--- page 3 ---
5   380   396   510   644   458
Step 1: Calculate Annual Returns for Each Stock (Year-on-Year %)
Formula: Return(t) = [Price(t) / Price(t-1)] − 1
Year   A (%)   B (%)   C (%)   D (%)   E (%)   Portfolio Ret (%)
Yr1   10.41   6.76   -7.50   9.38   11.91   6.19
Yr2   -14.29   -7.67   23.51   10.04   11.94   4.71
Yr3   -6.67   -7.58   -9.19   7.22   11.24   -0.99
Yr4   16.07   21.09   10.84   8.51   9.59   13.22
Yr5   16.92   27.74   10.87   5.23   8.27   13.81
Note: Portfolio Return = Equal-weighted average of 5 stock returns (20% × each)
Step 2: Sort Portfolio Returns in Ascending Order
Step   Working / Calculation   Marks
2a   Sort all 5 portfolio annual returns from worst to best:   ½
Rank 1 (Worst): −0.99% (Year 3) Rank 2: 4.71% (Year 2) Rank   ½
3: 6.19% (Year 1) Rank 4: 13.22% (Year 4) Rank 5 (Best):
13.81% (Year 5)
Step 3: Identify the 95% VaR Observation
Step   Working / Calculation   Marks
For 95% CL with 5 observations: VaR = 5% worst observation =   1
worst 5% of returns 5% × 5 = 0.25 → Round up to 1st
3a   observation (most conservative)
Formula: VaR percentile: (1 − CL) × N = 0.05 × 5 = 0.25 → 1st
observation
1-Day VaR basis: worst annual return = −0.99% First, convert: 1-   ½
3b   Day Return = −0.99% / √252 = −0.0624% per day
Formula: 1-Day σ = Annual Return / √252
Step 4: Calculate Portfolio VaR
Assuming Portfolio Value = Rs. 5 Crores (standard assumption when not specified):
Step   Working / Calculation   Marks
1-Day VaR (absolute) = Portfolio Value × |Worst 1-Day   1
Return| = 5,00,00,000 × 0.000624 = Rs. 31,200 (1-day
4a
VaR)
Formula: VaR = P × |r|
10-Day VaR = 1-Day VaR × √10 = 31,200 × 3.1623 = Rs.   1
4b   98,665
Formula: N-Day VaR = 1-Day VaR × √N
ALTERNATE: Using worst annual portfolio return   ½
directly: 95% 1-Year VaR = 5 Cr × 0.0099 = Rs. 4.95
4c
Lakhs 10-Day VaR = 4.95L × √(10/252) = Rs. 98,646 ≈
Rs. 98,700
********** 3 **********
--- page 4 ---
Step 5: Inference & Rebalancing Recommendation
Step   Working / Calculation   Marks
The 95%, 10-Day VaR ≈ Rs. 98,700 means with 95% confidence,   ½
5a   maximum loss in 10 days ≤ Rs. 98,700 Single worst year was Year 3
(−0.99% portfolio). Stocks A & B showed negative returns.
Recommendation: YES — rebalance. Stock B shows persistent   ½
5b   underperformance (−7.67%). Consider reducing exposure to A & B
and increasing D & E which show consistent positive returns.
Final Answer: 95% 10-Day Portfolio VaR ≈ Rs. 98,700 | Rebalance: Reduce B &   5
A; increase D & E   Marks
Total
CO2; SO- B Concept: A Synthetic Short Position is created using options to replicate the payoff of actually
1;   short-selling a stock, WITHOUT borrowing and selling the stock.
BL-Apply
Strategy: BUY PUT + SELL CALL at the SAME Strike Price
Numerical Example: Reliance CMP = Rs. 2,500 | Strike = Rs. 2,500 | Put Premium (Buy) = Rs. 80 |
Call Premium (Receive) = Rs. 70 | Net Cost = Rs. 10 per share
Step   Working / Calculation   Marks
1   Buy 1 ATM Put @ Strike 2500, Pay Premium = Rs. 80   ½
2   Sell 1 ATM Call @ Strike 2500, Receive Premium = Rs. 70   ½
Net Premium Paid = 80 − 70 = Rs. 10 (net debit)   ½
3
Formula: Net Cost = Put Premium − Call Premium
Payoff at Expiry: • If Market = 2300 (falls): Put profit = 200; Call   1
expires worthless → Net = 200 − 10 = +Rs. 190 • If Market =
4   2500: Both expire worthless → Net Loss = −Rs. 10 • If Market =
2700 (rises): Put worthless; Call loss = 200 → Net = −200 − 10 =
−Rs. 210   [05]
Break-even = Strike − Net Premium = 2500 − 10 = Rs. 2,490   ½
5
Formula: BE = K − Net Premium
Part (ii): Synthetic Short vs Actual Short — Comparison
Parameter   Synthetic Short   Actual Short Sell
Risk   Defined (put premium paid)   Unlimited upside = unlimited loss
Margin   No SEBI margin needed (just   SEBI prescribed VaR + ELM margin
premium)
Cost   Net premium (small)   Borrowing cost + margin cost
Dividend Risk   No dividend risk   Short seller must pay dividend
Regulatory   No stock borrowing needed   Subject to SEBI short-sell rules
Mark Distribution: Strategy construction (1.5) +
Payoff table (2) + Comparison table (1.5)
********** 4 **********
--- page 5 ---
Q3   Answer the following:   [10]
CO3; SO- A Given: EPS₀ = Rs.18 | DPR = 65% | D₀ = 18 × 0.65 = Rs. 11.70 | Rf = 5.25% | Rm = 14% | β = 1.90
8;   | CMP = Rs. 320
BL-Apply   Growth Phases: Phase 1: g = 22% for 6 years | Phase 2: g declines from 22% to 8% over 3 years |
Phase 3: g = 5% (perpetuity)
Step   Working / Calculation   Marks
Calculate Ke using CAPM: Ke = Rf + β(Rm − Rf) = 5.25% +   1
1.90 × (14% − 5.25%) = 5.25% + 1.90 × 8.75% = 5.25% +
1
16.625% = 21.875% ≈ 21.88%
Formula: Ke = Rf + β(Rm − Rf)
Phase 2: Growth declines linearly from 22% to 8% over 3 years:   ½
Year 7: g = 22% − (22%−8%)/3 × 1 = 22% − 4.67% = 17.33%
2
Year 8: g = 22% − (22%−8%)/3 × 2 = 22% − 9.33% = 12.67%
Year 9: g = 22% − (22%−8%)/3 × 3 = 8.00%
Phase 1 Dividends (Years 1-6): D₀ = 11.70; g = 22% each year   1
D1=14.27 | D2=17.41 | D3=21.24 | D4=25.91 | D5=31.61 |
3
D6=38.57
Formula: Dt = D(t-1) × (1+g)
Phase 2 Dividends (Years 7-9): D7 = 38.57 × 1.1733 = 45.25 | D8   ½
4
= 45.25 × 1.1267 = 51.01 | D9 = 51.01 × 1.08 = 55.09
[05]
Terminal Value at end of Year 9: TV9 = D10 / (Ke − g∞) = 55.09   1
5   × 1.05 / (0.2188 − 0.05) = 57.84 / 0.1688 = Rs. 342.65
Formula: TV = D(n+1)/(Ke − gL)
PV of Phase 1 (Ke=21.88%): Sum of PV of D1-D6 PV =   ½
14.27/1.2188 + 17.41/1.2188² + ... ≈ 11.71 + 11.72 + 11.74 +
6
11.77 + 11.78 + 11.80 = Rs. 70.52
Formula: PV = Dt/(1+Ke)^t
PV of Phase 2 (D7-D9): PV = 45.25/1.2188⁷ + 51.01/1.2188⁸ +   ½
7
55.09/1.2188⁹ ≈ 10.04 + 9.28 + 8.22 = Rs. 27.54
PV of Terminal Value: PV(TV9) = 342.65/1.2188⁹ =   ½
8   342.65/5.371 = Rs. 63.80
Formula: PV(TV) = TV/(1+Ke)^n
Intrinsic Value = PV(Ph1) + PV(Ph2) + PV(TV) = 70.52 + 27.54   ½
+ 63.80 = Rs. 161.86 Valuation: CMP = Rs. 320 >> IV = Rs.
9
161.86 → Stock is OVERVALUED → SELL
Formula: IV = ΣPV(Dt) + PV(TV)
Final Answer: Intrinsic Value ≈ Rs. 161.86 | CMP Rs. 320 >> IV → Stock   5 Marks Total
OVERVALUED → Recommendation: SELL/SHORT
CO3; SO- B Given: FV = Rs. 1,000 | Coupon = 7% p.a. → Annual Coupon = Rs. 70 | YTM = 9% | Maturity = 5
8;   Years
BL-Apply   [05]
Step 1: Bond Pricing using DCF Tabular Method
Step   Working / Calculation   Marks
********** 5 **********
--- page 6 ---
PV Factor at 9%: 1/(1.09)^t for t = 1 to 5 t=1: 0.9174 | t=2:   ½
1   0.8417 | t=3: 0.7722 | t=4: 0.7084 | t=5: 0.6499
Formula: PV Factor = 1/(1+r)^t
PV of Coupons: t=1: 70×0.9174=64.22 | t=2: 70×0.8417=58.92 |   ½
2   t=3: 70×0.7722=54.05 t=4: 70×0.7084=49.59 | t=5:
70×0.6499=45.49 Total PV Coupons = 272.27
3   PV of Face Value: 1000 × 0.6499 = Rs. 649.93   ½
Bond Price = 272.27 + 649.93 = Rs. 922.20 (Coupon 7% < YTM   ½
4   9% → Bond trades at DISCOUNT — confirmed)
Formula: P = Σ[C/(1+r)^t] + FV/(1+r)^n
Step 2: Macaulay Duration
Step   Working / Calculation   Marks
Duration = Σ[t × PV(CFt)] / P Numerator = 1×64.22 + 2×58.92 +   1
3×54.05 + 4×49.59 + 5×(45.49+649.93) = 64.22 + 117.84 +
5   162.15 + 198.36 + 3,477.10 = 4,019.67 Macaulay Duration =
4,019.67 / 922.20 = 4.359 Years
Formula: D = Σ[t × PV(CFt)] / Bond Price
Step 3: Modified Duration
Step   Working / Calculation   Marks
Modified Duration = Macaulay Duration / (1 + YTM) = 4.359 /   ½
1.09 = 3.998 ≈ 4.00 Years Interpretation: 1% rise in YTM →
6
Bond Price falls by ≈ 4.00%
Formula: MD = D/(1+r)
Step 4: Convexity
Step   Working / Calculation   Marks
Convexity = [1/(P×(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t] Numerator =   1
1(2)×70/1.09 + 2(3)×70/1.09² + 3(4)×70/1.09³ + 4(5)×70/1.09⁴ +
5(6)×1070/1.09⁵ = 128.44 + 353.36 + 648.46 + 994.92 +
7
17,587.82 = 19,713.00 Convexity = 19,713 / (922.20 × 1.09²) =
19,713 / 1,095.19 = 18.00
Formula: Conv = [1/(P(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t]
Price Change Approximation using MD & Convexity: ΔP/P ≈   ½
−MD × Δy + ½ × Conv × (Δy)² MD captures linear, Convexity
8
corrects for curvature of price-yield relationship
Formula: ΔP/P ≈ −MD·Δy + ½·Conv·(Δy)²
Final Answers: Bond Price = Rs. 922.20 | Mac. Duration = 4.36 yrs |   5 Marks Total
Modified Duration = 4.00 | Convexity = 18.00
********** 6 **********
--- page 7 ---
Q4   Answer the following:   [10]
CO2;   A Repricing Buckets: 1-6m (A=80L, L=70L) | 6-12m (A=40L, L=50L) | 1-3yr (A=20L, L=25L) |
SO-1;   3-5yr (A=15L, L=10L)
BL-
Step   Working / Calculation   Marks
Apply
Calculate Gap for each bucket: Gap = Rate Sensitive Assets   ½
1   (RSA) − Rate Sensitive Liabilities (RSL)
Formula: Gap = RSA − RSL
1-6m: Gap = 80 − 70 = +Rs. 10 Lakh (Positive/Asset-Sensitive)   ½
6-12m: Gap = 40 − 50 = −Rs. 10 Lakh (Negative/Liability-
Sensitive) 1-3yr: Gap = 20 − 25 = −Rs. 5 Lakh (Negative) 3-5yr:
Gap = 15 − 10 = +Rs. 5 Lakh (Positive)
Scenario (i): Rates ↑ 50 bps (+0.50%) in 1-6 month bucket ΔNII   1½
= Gap × Δr × Time Fraction = 10 Lakh × 0.005 × (6/12) =
2   10,00,000 × 0.005 × 0.5 = Rs. 2,500 Annualized ΔNII = Rs. 5,000   [05]
or use: ΔNII = Gap × Δr = 10L × 0.005 = Rs. 5,000 p.a.
Formula: ΔNII = Gap × Δr
Scenario (ii): Rates ↓ 25 bps (−0.25%) in 1-3 year bucket ΔNII =   1½
Gap × Δr = −5,00,000 × (−0.0025) = +Rs. 1,250 p.a. Negative
3
gap + rate decrease → NII INCREASES (beneficial scenario)
Formula: ΔNII = Gap × Δr
ALM Concept: Asset-Liability Management (ALM) involves   1
managing the balance sheet to optimize NII while controlling
4
interest rate risk. Gap Analysis identifies mismatches between
RSA and RSL to assess NII sensitivity to rate changes.
Final Answers: Scenario(i) +50bps: ΔNII = +Rs. 5,000 | Scenario(ii)   5 Marks Total
−25bps in 1-3yr: ΔNII = +Rs. 1,250 | Positive Gap → Rate ↑ beneficial
CO2;   B JP Bank | Asset A: EAD=40m, PD=0.25%, LGD=20%, σPD=5%, σLGD=15% | Asset B:
SO-1;   EAD=60m, PD=0.50%, LGD=35%, σPD=7%, σLGD=10% | ρ=0.20
BL-
Step   Working / Calculation   Marks
Apply
Expected Loss (EL) for each asset: EL_A = EAD_A × PD_A   1
× LGD_A = 40m × 0.0025 × 0.20 = Rs. 20,000 EL_B =
1   EAD_B × PD_B × LGD_B = 60m × 0.005 × 0.35 = Rs.
1,05,000
Formula: EL = EAD × PD × LGD
Unexpected Loss (UL) for each asset: UL_i = EAD_i ×   ½
2   √(LGD²×σPD² + PD²×σLGD²)   [05]
Formula: UL = EAD × √(LGD²·σPD² + PD²·σLGD²)
UL_A = 40m × √[(0.20²×0.05²) + (0.0025²×0.15²)] = 40m ×   ½
√[(0.04×0.0025) + (0.00000625×0.0225)] = 40m × √[0.0001
+ 0.000000140625] = 40m × √0.000100140625 = 40m ×
0.010007 = Rs. 4,00,281 ≈ Rs. 4.00 Lakh
UL_B = 60m × √[(0.35²×0.07²) + (0.005²×0.10²)] = 60m ×   ½
√[(0.1225×0.0049) + (0.000025×0.01)] = 60m ×
√[0.00060025 + 0.00000025] = 60m × √0.0006005 = 60m ×
0.02451 = Rs. 14,70,488 ≈ Rs. 14.70 Lakh
********** 7 **********
--- page 8 ---
Portfolio Unexpected Loss (ρ = 0.20): UL_P = √(UL_A² +   1
UL_B² + 2ρ×UL_A×UL_B) = √[(4.00)² + (14.70)² +
3   2×0.20×4.00×14.70] All in Lakh: = √[16.00 + 216.09 +
23.52] = √255.61 = Rs. 15.99 Lakh
Formula: UL_P = √(UL_A² + UL_B² + 2ρ·UL_A·UL_B)
Risk Contribution of each asset to Portfolio UL: RC_A =   1
UL_A × (UL_A + ρ×UL_B) / UL_P = 4.00 × (4.00 +
0.20×14.70) / 15.99 = 4.00 × 6.94 / 15.99 = Rs. 1.736 Lakh
4   RC_B = UL_B × (UL_B + ρ×UL_A) / UL_P = 14.70 × (14.70
+ 0.20×4.00) / 15.99 = 14.70 × 15.50 / 15.99 = Rs. 14.26
Lakh
Formula: RC_i = UL_i(UL_i + ρ·UL_j)/UL_P
Impact of ρ increasing to 0.35: New UL_P = √[16 + 216.09 +   1
2×0.35×4.00×14.70] = √[16+216.09+41.16] = √273.25 = Rs.
5   16.53 Lakh ↑ Correlation → ↑ Portfolio UL → Concentration
Risk increases
Formula: Higher ρ → less diversification benefit
Final Answers: EL_A=Rs.20,000 | EL_B=Rs.1,05,000 |   5 Marks Total
UL_A=Rs.4.00L | UL_B=Rs.14.70L | UL_Portfolio(ρ=0.20)=Rs.15.99L |
UL_Portfolio(ρ=0.35)=Rs.16.53L
Q5   Answer the following:   [10]
CO3; SO-   A   Given: Borrow USD 100m @ 3.6% | Sell Spot USD @ Rs. 93.70 | Buy 1-yr Fwd
8;   USD @ Rs. 97.50 | Invest INR @ 8% | Spot after 1yr = Rs. 97.80
BL-Apply
Step   Working / Calculation   Marks
Zero-Arbitrage Forward Rate (IRP): F* = S × (1 + r_INR)   1
/ (1 + r_USD) = 93.70 × (1.08) / (1.036) = 93.70 ×
1
1.04247 = Rs. 97.68
Formula: F* = S × (1+r_d)/(1+r_f)
Actual Forward = Rs. 97.50 | IRP Forward = Rs. 97.68   ½
Since Actual Fwd (97.50) < IRP Fwd (97.68) → USD is
2   underpriced forward → Arbitrage EXISTS: Strategy:
Borrow USD, Convert Spot, Invest in INR, Buy USD
Forward
[05]
Flow Diagram: Today: Borrow USD 100m → Sell @   1
93.70 → Receive INR 9,370m → Invest @ 8% After 1yr:
3   INR receipt = 9,370m × 1.08 = INR 10,119.60m Buy USD
Forward: Pay Rs. 97.50/USD → Pay INR to buy USD
100m × 1.036 = USD 103.6m fwd
USD Repayment at maturity: 100m × 1.036 = USD   ½
4   103.60m INR needed to buy USD 103.60m @ fwd 97.50:
103.60m × 97.50 = INR 10,101m
Arbitrage Gain = INR Receipts − INR paid for Fwd USD   1
= 10,119.60m − 10,101m = INR 18.60m = Rs. 18.6
5
Crores (Alternatively: (F* − Actual Fwd) × Loan Amount
= (97.68 − 97.50) × 103.6m ≈ Rs. 18.65m)
********** 8 **********
--- page 9 ---
Formula: Gain = INR receipts − INR forward
payment
Spot rate after 1yr = Rs. 97.80 (not used in CIA —   1
covered by forward contract)
6
Formula: CIA locks in via Forward → not exposed
to spot rate risk
Final Answer: IRP Forward = Rs. 97.68 | Arbitrage Gain ≈ Rs.   5 Marks
18.60 Crores | Strategy: Borrow USD → Convert INR → Invest   Total
→ Buy USD Forward
CO3; SO-   B   Indian Exporter: £6 per garment | Cost = Rs. 600 | 2-Month settlement | Spot:
8;   £=112.50, $=93.70 | 2m Fwd: £=112.79, $=93.96
BL-Apply
Interest Rates: £=3.75%, $=3.6%, Rs.=5.25%
Step   Working / Calculation   Marks
Option 1: Invoice in Sterling (£6) Sell £ at 2-month Forward   1
Rate = Rs. 112.79/£ INR Receipt per garment = £6 ×
1
112.79 = Rs. 676.74
Formula: INR = FC amount × Forward Rate
Option 2: Invoice in USD Convert £6 to USD at Spot: 6 ×   1½
112.50 / 93.70 = USD 7.202 Sell USD at 2-month Forward =
2   Rs. 93.96/USD INR Receipt = 7.202 × 93.96 = Rs. 676.50
Formula: USD = £ × (Spot £/Rs) / (Spot $/Rs); INR
= USD × Fwd $/Rs
Comparison: Sterling Invoice: Rs. 676.74 per garment →   1   [05]
3   Profit = 676.74 − 600 = Rs. 76.74 USD Invoice: Rs. 676.50
per garment → Profit = 676.50 − 600 = Rs. 76.50
Decision: INVOICE IN STERLING (£) Reason: Higher INR   1½
realization (Rs. 676.74 > Rs. 676.50) by Rs. 0.24 per
garment Additionally, Sterling forward (£=112.79) reflects
4
higher premium vs spot (112.50) = Rs. 0.29 appreciation
Both options lock in via forward contracts, eliminating
currency risk
Final Answer: Invoice in STERLING | INR/garment: £ option = Rs.   5 Marks T
676.74 vs $ option = Rs. 676.50 | Difference = Rs. 0.24 | Recommend
GBP
********** 9 **********
--- page 10 ---
Q6   Answer the following:   [10]
CO A Company A (British): Wants USD; can borrow GBP@8.5%, USD@5.8% | Company B (US):
1;   Wants GBP; can borrow GBP@8.1%, USD@5.2% | Bank earns 15bps; each Co. gains
SO-
20bps
1;
BL-   Step   Working / Calculation   Marks
App
ly   Comparative Advantage Analysis: GBP Differential: 8.5% − 8.1% =   1
0.4% (B has advantage in GBP) USD Differential: 5.8% − 5.2% =
0.6% (B has advantage in USD too) QSD = Larger diff − Smaller diff
= 0.6% − 0.4% = 0.2% = 20bps (Total gain to split) Bank earns 15bps
1
→ Each company gets 20bps (since total = bank 15bps + both cos
20bps each = 55bps > 20bps) Note: Total QSD = 20bps → Bank
15bps + 2×20bps = 55bps → structure adjusted
Formula: QSD = |Diff_currency1 − Diff_currency2|
Wait — Re-check: Total QSD = 20bps to share Bank gets 15bps;   ½
each company gets (20 − 15)/2 = 2.5bps each — that's too small
Alternative reading: Bank earns 15bps from each company (30bps
2
total); each co gains 20bps Total benefit needed = 30 + 20 + 20 =
70bps → QSD must be at least 70bps. With QSD = 0.20% = 20bps
total, the standard split: each gains (20bps − 15bps)/2 = 2.5bps each.
[05]
Swap Structure (standard interpretation): • Co. A: Borrows GBP @   1
8.5% (comparative advantage) → swaps to pay USD • Co. B:
3
Borrows USD @ 5.2% (comparative advantage) → swaps to pay GBP
• Bank acts as intermediary, earns spread
Effective Costs after swap: • Co. A wants USD: Effective rate = 5.8%   1½
− 0.20% gain = 5.60% • Co. B wants GBP: Effective rate = 8.1% −
4
0.20% gain = 7.90% • Bank net spread = 0.15% = 15bps
Formula: Effective Cost = Direct Market Rate − Gain
Cash Flow Structure: → Co.A pays GBP 8.5% to GBP market;   1
receives GBP from Bank; pays USD to Bank → Co.B pays USD 5.2%
5
to USD market; receives USD from Bank; pays GBP to Bank → Bank
nets GBP and USD flows, earning 15bps
Final Answer: QSD = 20bps | A: USD effective = 5.60% | B: GBP effective   5 Marks
= 7.90% | Bank: 15bps   Total
CO B Long Nifty 22,500 CE @ Premium Rs. 350 | Short Nifty 22,500 PE @ Premium Rs. 280 | Net
1;   Cost = 350 − 280 = Rs. 70 (debit)
SO-
1;   Synthetic Long: Buying a Call + Selling a Put at the SAME strike creates a Synthetic Long
BL-   Futures position — replicating the payoff of buying the index outright.
App   Payoff Calculation: Long CE Payoff = max(S−K,0)−Premium; Short PE Payoff =
ly   Premium−max(K−S,0)   [05]
Expiry   Long Call 22500 P/L   Short Put 22500 P/L   Net Option   Net P/L
Level   P/L   (after
Rs.70
cost)
22,800   300−350 = −50   280 (PE expires) = +280   −50+280 =   230−70
+230   = +160
********** 10 **********
--- page 11 ---
22,200   CE expires: −350   (22500−22200)−280=300−280=+20… Actual:   −350+(−20) −370+70
Put exercised against: −(22500−22200)+280   = −370   = −300
= −20
22,500   CE expires: −350   PE expires: +280   −70   −70+70
= 0
23,500   (23500−22500)−350=1000−35   PE expires: +280   +930   930−70
0=+650   = +860
Step   Working / Calculation   Marks
Payoff at 22,800 (Rs. +160) → Market above strike: net positive [1] Payoff   5
at 22,200 (Rs. −300) → Market below strike: net negative [1] Payoff at
Marks 22,500 (Rs. 0) → At-the-money: break-even [1] Payoff at 23,500 (Rs.
+860) → Far above strike: maximum upside [1] Nature: SYNTHETIC
LONG FUTURES — unlimited upside, unlimited downside [1]
When to use: When bullish on index; want long exposure without actual futures margin;
cheaper than outright futures
Mark Distribution: 4 payoffs × 1 mark each + Nature identification (1)   5 Marks Total
Q7   Answer the following:   [10]
CO1; SO- A   Step Working / Calculation   Marks
1;
BL-Analyze   Put-Call Parity (for European options): C + K×e^(−rT) = P +   1
S LHS = C + PV(K) = 130 + 500×e^(−0.0525×0.25) = 130
1   + 500×e^(−0.013125) = 130 + 500×0.9870 = 130 + 493.48
= Rs. 623.48
Formula: C + Ke^{-rT} = P + S
2   RHS = P + S = 105 + 492 = Rs. 597.00   ½
Compare: LHS (623.48) > RHS (597.00) Mismatch = Rs.   ½
26.48 → ARBITRAGE OPPORTUNITY EXISTS (LHS
3
overpriced relative to RHS: Call is overpriced or Put is
underpriced)
Arbitrage Strategy — SELL overpriced side (LHS), BUY   1
underpriced side (RHS): • SELL the Call (C) for Rs. 130 •   [05]
4
BORROW PV(K) = Rs. 493.48 at 5.25% for 0.25yr • BUY
the Put (P) for Rs. 105 • BUY the Stock (S) for Rs. 492
Cash Flows TODAY: Inflows: +130 (sell C) + 493.48   1
5   (borrow) Outflows: −105 (buy P) − 492 (buy S) Net =
623.48 − 597 = +Rs. 26.48 → RISK-FREE PROFIT upfront
At Expiry: All positions offset → No net cash flow needed   ½
6   The Rs. 26.48 locked in today is the arbitrage profit (PV
terms)
Factors affecting European Call/Put prices: • Stock Price   ½
(S) ↑ → C ↑, P ↓ | Strike (K) ↑ → C ↓, P ↑ • Time (T) ↑ →
7
Both C & P ↑ | Volatility (σ) ↑ → Both ↑ • Interest Rate (r) ↑
→ C ↑, P ↓ | Dividend → C ↓, P ↑
********** 11 **********
--- page 12 ---
Final Answer: LHS=623.48 > RHS=597.00 → Arbitrage profit =   5 Marks
Rs. 26.48 | Strategy: Sell Call + Borrow + Buy Put + Buy Stock   Total
CO1; SO- B Definition: Operational Risk is the risk of loss resulting from inadequate or failed
1;   internal processes, people, systems, or from external events. It includes legal risk but
BL-Analyze
excludes strategic and reputational risk (Basel III definition).
Keywords: Basel III, Pillar 2, AMA, BIA, Fraud, Cyber Risk, RBI Guidelines
• Sub-Category 1: Internal Fraud — unauthorized transactions, embezzlement (e.g.,
Satyam accounting fraud)
• Sub-Category 2: External Fraud — phishing, cyber-attacks (e.g., Cosmos Bank
SWIFT hack Rs. 94.42 Cr)
• Sub-Category 3: Employment Practices — employee misconduct, HR failures
• Sub-Category 4: Clients/Products — mis-selling, KYC failures
• Sub-Category 5: Business Disruption — IT failures, data breaches
Recent Indian Banking Frauds (mapped to Op-Risk categories):
• Punjab National Bank (PNB) Scam 2018: Nirav Modi/Mehul Choksi — fraudulent
LoUs via SWIFT bypass. Category: Internal Fraud + System/Process failure. Loss:
~Rs. 13,000 Cr
• Cosmos Bank SWIFT Hack 2018: External attack bypassed SWIFT → Rs. 94.42
Cr siphoned. Category: External Fraud + Technology failure
Mitigation Tools & Regulatory Framework:   [05]
• Basel III: Pillar 1 — Operational Risk Capital under BIA/STA/AMA approaches |
Pillar 2 — ICAAP
• RBI Guidelines: Cyber Security Framework, Fraud Risk Management, Risk
Governance at Board level
•   Internal Controls: SOD (Segregation of Duties), maker-checker systems, forensic
audit, whistleblower policies
Hybrid Securities:
Definition: Hybrid Securities combine features of both equity and debt instruments.
Examples: AT1 Bonds (Perpetual Bonds), Convertible Debentures (CCDs),
Preference Shares.
• Role in Financial Engineering: Used to optimize capital structure, fulfill Basel III
Tier 1/Tier 2 capital requirements, and offer risk-return flexibility
Mark Distribution: Op-Risk definition (1) + Sub-categories with
examples (1) + 2 fraud cases mapped (1) + Mitigation/Basel III (1)
+ Hybrid Securities (1)
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 74b8c40383f8

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/MBATech_IT_7041/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 09 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: V/Semester X(Exam Year: 2025-2026)
Subject: Financial Engineering
Date: 09 May 2026   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No. _1_is compulsory.
3. Out of remaining questions, attempt any_4_questions.
4. In all_5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary
9. Use of Scientific Calculator allowed
Q1   Answer briefly:   [10
]
CO1; SO-   a. Definition: A Forward Rate Agreement (FRA) is an over-the-counter (OTC) derivative contract
1;   between two parties — a buyer and a seller — that fixes (locks in) an interest rate for a future
BL-   borrowing or lending transaction for a specified notional principal over an agreed future period.
Understan
d   Keywords: FRA, OTC, Notional Principal, Settlement Date, Reference Rate (LIBOR/MIBOR),
Contract Rate
•   Participants: Buyer (borrower, who wants to LOCK IN a rate) and Seller (lender / bank)
•   Key Milestones: Trade Date → Setting Date → Settlement Date → Maturity Date
•   Settlement Mechanism: Cash-settled on Settlement Date; difference between Reference Rate
[03
and Contract Rate is paid on discounted basis
]
•   Settlement Formula: Payment = [(Reference Rate – Contract Rate) × Notional × Days/360] /
[1 + (Reference Rate × Days/360)]
Example: Co. A anticipates borrowing ₹10 Cr at MIBOR after 3 months for 6 months. Enters 3×9
FRA at 7% (contract rate). If MIBOR settles at 8%, settlement receipt compensates for the extra
cost.
•   Benefit: Eliminates interest rate uncertainty; hedger knows exact future cost
Mark Distribution: Definition (1) + Participants/Milestones (1) + Settlement mechanism
with formula (1)
CO1; SO-   b Hedging Definition: Hedging is the process of taking an offsetting position in a financial
1;   .   instrument to reduce or eliminate the risk of adverse price movements in an existing position.
BL-
Arbitrage Definition: Arbitrage is the simultaneous purchase and sale of the same or equivalent
Understan
asset in different markets to profit from price discrepancies, with zero risk and zero net   [03
d
investment.   ]
Comparison Table — Keywords: Risk, Objective, Cost, Duration
Parameter   Hedging   Arbitrage
********** 1 **********
--- page 2 ---
Objective   Risk reduction / protection   Risk-free profit
Risk   Residual risk may remain   Zero risk (riskless)
Cost   Premium / opportunity cost   Zero net investment
Duration   Ongoing, long-term   Instantaneous
Example   Exporter buys USD put option   Buy low on NSE, sell high on
BSE
Mark Distribution: Hedging definition with example (1) + Arbitrage definition with
example (1) + Comparison: objective/risk/cost (1)
CO1; SO-   c. Statement Interpretation: The 95%, 1-day VaR of INR 1.75 Crores means: with 95% confidence,
1;   the portfolio will NOT lose more than ₹1.75 Crores in a single trading day under normal market
BL-   conditions.
Remember
Key Keywords: Confidence Level, Holding Period, Loss Threshold, Tail Risk, Normal
Distribution
•   Significance: Quantifies downside risk; aids in capital allocation and setting risk limits   [02
•   Limitation 1: Assumes normal distribution — fails during tail events (Black Swan events)   ]
•   Limitation 2: Does not reveal the magnitude of losses BEYOND the VaR threshold
•   Limitation 3: Backward-looking — based on historical data; not predictive in structural
breaks
Mark Distribution: Correct interpretation of statement (1) + Significance + 2 limitations
(1)
CO1; SO-   d. Definition: A Credit Default Swap (CDS) is an OTC derivative contract that acts like insurance
1;   against credit default. The Protection Buyer pays a periodic premium (CDS Spread) to the
BL-   Protection Seller, who compensates the buyer if the Reference Entity defaults.
Understan
d   Keywords: Protection Buyer, Protection Seller, Reference Entity, CDS Spread, Credit Event
•   Participants: (i) Protection Buyer — hedges credit risk; (ii) Protection Seller — earns
premium; (iii) Reference Entity — underlying borrower
•   Settlement: Physical (delivery of defaulted bond) or Cash (face value minus recovery value)   [02
•   Role in 2008 Crisis: CDSs were sold massively on subprime mortgage-backed securities   ]
(MBS). When MBS defaulted, protection sellers (like AIG) faced unmanageable payouts →
systemic collapse
•   Key Issue: Lack of regulation, naked CDS positions, and excessive leverage amplified
contagion
Mark Distribution: CDS definition with participants/example (1) + Role in   2
2008 crisis: naked positions/AIG/contagion (1)
Q2   Answer the following:   [10]
CO2; SO- A Given Data: 5 Equal-Weighted Stocks (20% each) | Portfolio: Rs. 5 Crores (assumed) | Prices
1;   Year 0-5:
BL-Apply
Year   Stock A   Stock B   Stock C   Stock D   Stock E
0   317   281   400   437   277
[05]
1   350   300   370   478   310
2   300   277   457   526   347
3   280   256   415   564   386
4   325   310   460   612   423
********** 2 **********
--- page 3 ---
5   380   396   510   644   458
Step 1: Calculate Annual Returns for Each Stock (Year-on-Year %)
Formula: Return(t) = [Price(t) / Price(t-1)] − 1
Year   A (%)   B (%)   C (%)   D (%)   E (%)   Portfolio Ret (%)
Yr1   10.41   6.76   -7.50   9.38   11.91   6.19
Yr2   -14.29   -7.67   23.51   10.04   11.94   4.71
Yr3   -6.67   -7.58   -9.19   7.22   11.24   -0.99
Yr4   16.07   21.09   10.84   8.51   9.59   13.22
Yr5   16.92   27.74   10.87   5.23   8.27   13.81
Note: Portfolio Return = Equal-weighted average of 5 stock returns (20% × each)
Step 2: Sort Portfolio Returns in Ascending Order
Step   Working / Calculation   Marks
2a   Sort all 5 portfolio annual returns from worst to best:   ½
Rank 1 (Worst): −0.99% (Year 3) Rank 2: 4.71% (Year 2) Rank   ½
3: 6.19% (Year 1) Rank 4: 13.22% (Year 4) Rank 5 (Best):
13.81% (Year 5)
Step 3: Identify the 95% VaR Observation
Step   Working / Calculation   Marks
For 95% CL with 5 observations: VaR = 5% worst observation =   1
worst 5% of returns 5% × 5 = 0.25 → Round up to 1st
3a   observation (most conservative)
Formula: VaR percentile: (1 − CL) × N = 0.05 × 5 = 0.25 → 1st
observation
1-Day VaR basis: worst annual return = −0.99% First, convert: 1-   ½
3b   Day Return = −0.99% / √252 = −0.0624% per day
Formula: 1-Day σ = Annual Return / √252
Step 4: Calculate Portfolio VaR
Assuming Portfolio Value = Rs. 5 Crores (standard assumption when not specified):
Step   Working / Calculation   Marks
1-Day VaR (absolute) = Portfolio Value × |Worst 1-Day   1
Return| = 5,00,00,000 × 0.000624 = Rs. 31,200 (1-day
4a
VaR)
Formula: VaR = P × |r|
10-Day VaR = 1-Day VaR × √10 = 31,200 × 3.1623 = Rs.   1
4b   98,665
Formula: N-Day VaR = 1-Day VaR × √N
ALTERNATE: Using worst annual portfolio return   ½
directly: 95% 1-Year VaR = 5 Cr × 0.0099 = Rs. 4.95
4c
Lakhs 10-Day VaR = 4.95L × √(10/252) = Rs. 98,646 ≈
Rs. 98,700
********** 3 **********
--- page 4 ---
Step 5: Inference & Rebalancing Recommendation
Step   Working / Calculation   Marks
The 95%, 10-Day VaR ≈ Rs. 98,700 means with 95% confidence,   ½
5a   maximum loss in 10 days ≤ Rs. 98,700 Single worst year was Year 3
(−0.99% portfolio). Stocks A & B showed negative returns.
Recommendation: YES — rebalance. Stock B shows persistent   ½
5b   underperformance (−7.67%). Consider reducing exposure to A & B
and increasing D & E which show consistent positive returns.
Final Answer: 95% 10-Day Portfolio VaR ≈ Rs. 98,700 | Rebalance: Reduce B &   5
A; increase D & E   Marks
Total
CO2; SO- B Concept: A Synthetic Short Position is created using options to replicate the payoff of actually
1;   short-selling a stock, WITHOUT borrowing and selling the stock.
BL-Apply
Strategy: BUY PUT + SELL CALL at the SAME Strike Price
Numerical Example: Reliance CMP = Rs. 2,500 | Strike = Rs. 2,500 | Put Premium (Buy) = Rs. 80 |
Call Premium (Receive) = Rs. 70 | Net Cost = Rs. 10 per share
Step   Working / Calculation   Marks
1   Buy 1 ATM Put @ Strike 2500, Pay Premium = Rs. 80   ½
2   Sell 1 ATM Call @ Strike 2500, Receive Premium = Rs. 70   ½
Net Premium Paid = 80 − 70 = Rs. 10 (net debit)   ½
3
Formula: Net Cost = Put Premium − Call Premium
Payoff at Expiry: • If Market = 2300 (falls): Put profit = 200; Call   1
expires worthless → Net = 200 − 10 = +Rs. 190 • If Market =
4   2500: Both expire worthless → Net Loss = −Rs. 10 • If Market =
2700 (rises): Put worthless; Call loss = 200 → Net = −200 − 10 =
−Rs. 210   [05]
Break-even = Strike − Net Premium = 2500 − 10 = Rs. 2,490   ½
5
Formula: BE = K − Net Premium
Part (ii): Synthetic Short vs Actual Short — Comparison
Parameter   Synthetic Short   Actual Short Sell
Risk   Defined (put premium paid)   Unlimited upside = unlimited loss
Margin   No SEBI margin needed (just   SEBI prescribed VaR + ELM margin
premium)
Cost   Net premium (small)   Borrowing cost + margin cost
Dividend Risk   No dividend risk   Short seller must pay dividend
Regulatory   No stock borrowing needed   Subject to SEBI short-sell rules
Mark Distribution: Strategy construction (1.5) +
Payoff table (2) + Comparison table (1.5)
********** 4 **********
--- page 5 ---
Q3   Answer the following:   [10]
CO3; SO- A Given: EPS₀ = Rs.18 | DPR = 65% | D₀ = 18 × 0.65 = Rs. 11.70 | Rf = 5.25% | Rm = 14% | β = 1.90
8;   | CMP = Rs. 320
BL-Apply   Growth Phases: Phase 1: g = 22% for 6 years | Phase 2: g declines from 22% to 8% over 3 years |
Phase 3: g = 5% (perpetuity)
Step   Working / Calculation   Marks
Calculate Ke using CAPM: Ke = Rf + β(Rm − Rf) = 5.25% +   1
1.90 × (14% − 5.25%) = 5.25% + 1.90 × 8.75% = 5.25% +
1
16.625% = 21.875% ≈ 21.88%
Formula: Ke = Rf + β(Rm − Rf)
Phase 2: Growth declines linearly from 22% to 8% over 3 years:   ½
Year 7: g = 22% − (22%−8%)/3 × 1 = 22% − 4.67% = 17.33%
2
Year 8: g = 22% − (22%−8%)/3 × 2 = 22% − 9.33% = 12.67%
Year 9: g = 22% − (22%−8%)/3 × 3 = 8.00%
Phase 1 Dividends (Years 1-6): D₀ = 11.70; g = 22% each year   1
D1=14.27 | D2=17.41 | D3=21.24 | D4=25.91 | D5=31.61 |
3
D6=38.57
Formula: Dt = D(t-1) × (1+g)
Phase 2 Dividends (Years 7-9): D7 = 38.57 × 1.1733 = 45.25 | D8   ½
4
= 45.25 × 1.1267 = 51.01 | D9 = 51.01 × 1.08 = 55.09
[05]
Terminal Value at end of Year 9: TV9 = D10 / (Ke − g∞) = 55.09   1
5   × 1.05 / (0.2188 − 0.05) = 57.84 / 0.1688 = Rs. 342.65
Formula: TV = D(n+1)/(Ke − gL)
PV of Phase 1 (Ke=21.88%): Sum of PV of D1-D6 PV =   ½
14.27/1.2188 + 17.41/1.2188² + ... ≈ 11.71 + 11.72 + 11.74 +
6
11.77 + 11.78 + 11.80 = Rs. 70.52
Formula: PV = Dt/(1+Ke)^t
PV of Phase 2 (D7-D9): PV = 45.25/1.2188⁷ + 51.01/1.2188⁸ +   ½
7
55.09/1.2188⁹ ≈ 10.04 + 9.28 + 8.22 = Rs. 27.54
PV of Terminal Value: PV(TV9) = 342.65/1.2188⁹ =   ½
8   342.65/5.371 = Rs. 63.80
Formula: PV(TV) = TV/(1+Ke)^n
Intrinsic Value = PV(Ph1) + PV(Ph2) + PV(TV) = 70.52 + 27.54   ½
+ 63.80 = Rs. 161.86 Valuation: CMP = Rs. 320 >> IV = Rs.
9
161.86 → Stock is OVERVALUED → SELL
Formula: IV = ΣPV(Dt) + PV(TV)
Final Answer: Intrinsic Value ≈ Rs. 161.86 | CMP Rs. 320 >> IV → Stock   5 Marks Total
OVERVALUED → Recommendation: SELL/SHORT
CO3; SO- B Given: FV = Rs. 1,000 | Coupon = 7% p.a. → Annual Coupon = Rs. 70 | YTM = 9% | Maturity = 5
8;   Years
BL-Apply   [05]
Step 1: Bond Pricing using DCF Tabular Method
Step   Working / Calculation   Marks
********** 5 **********
--- page 6 ---
PV Factor at 9%: 1/(1.09)^t for t = 1 to 5 t=1: 0.9174 | t=2:   ½
1   0.8417 | t=3: 0.7722 | t=4: 0.7084 | t=5: 0.6499
Formula: PV Factor = 1/(1+r)^t
PV of Coupons: t=1: 70×0.9174=64.22 | t=2: 70×0.8417=58.92 |   ½
2   t=3: 70×0.7722=54.05 t=4: 70×0.7084=49.59 | t=5:
70×0.6499=45.49 Total PV Coupons = 272.27
3   PV of Face Value: 1000 × 0.6499 = Rs. 649.93   ½
Bond Price = 272.27 + 649.93 = Rs. 922.20 (Coupon 7% < YTM   ½
4   9% → Bond trades at DISCOUNT — confirmed)
Formula: P = Σ[C/(1+r)^t] + FV/(1+r)^n
Step 2: Macaulay Duration
Step   Working / Calculation   Marks
Duration = Σ[t × PV(CFt)] / P Numerator = 1×64.22 + 2×58.92 +   1
3×54.05 + 4×49.59 + 5×(45.49+649.93) = 64.22 + 117.84 +
5   162.15 + 198.36 + 3,477.10 = 4,019.67 Macaulay Duration =
4,019.67 / 922.20 = 4.359 Years
Formula: D = Σ[t × PV(CFt)] / Bond Price
Step 3: Modified Duration
Step   Working / Calculation   Marks
Modified Duration = Macaulay Duration / (1 + YTM) = 4.359 /   ½
1.09 = 3.998 ≈ 4.00 Years Interpretation: 1% rise in YTM →
6
Bond Price falls by ≈ 4.00%
Formula: MD = D/(1+r)
Step 4: Convexity
Step   Working / Calculation   Marks
Convexity = [1/(P×(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t] Numerator =   1
1(2)×70/1.09 + 2(3)×70/1.09² + 3(4)×70/1.09³ + 4(5)×70/1.09⁴ +
5(6)×1070/1.09⁵ = 128.44 + 353.36 + 648.46 + 994.92 +
7
17,587.82 = 19,713.00 Convexity = 19,713 / (922.20 × 1.09²) =
19,713 / 1,095.19 = 18.00
Formula: Conv = [1/(P(1+r)²)] × Σ[t(t+1)×CFt/(1+r)^t]
Price Change Approximation using MD & Convexity: ΔP/P ≈   ½
−MD × Δy + ½ × Conv × (Δy)² MD captures linear, Convexity
8
corrects for curvature of price-yield relationship
Formula: ΔP/P ≈ −MD·Δy + ½·Conv·(Δy)²
Final Answers: Bond Price = Rs. 922.20 | Mac. Duration = 4.36 yrs |   5 Marks Total
Modified Duration = 4.00 | Convexity = 18.00
********** 6 **********
--- page 7 ---
Q4   Answer the following:   [10]
CO2;   A Repricing Buckets: 1-6m (A=80L, L=70L) | 6-12m (A=40L, L=50L) | 1-3yr (A=20L, L=25L) |
SO-1;   3-5yr (A=15L, L=10L)
BL-
Step   Working / Calculation   Marks
Apply
Calculate Gap for each bucket: Gap = Rate Sensitive Assets   ½
1   (RSA) − Rate Sensitive Liabilities (RSL)
Formula: Gap = RSA − RSL
1-6m: Gap = 80 − 70 = +Rs. 10 Lakh (Positive/Asset-Sensitive)   ½
6-12m: Gap = 40 − 50 = −Rs. 10 Lakh (Negative/Liability-
Sensitive) 1-3yr: Gap = 20 − 25 = −Rs. 5 Lakh (Negative) 3-5yr:
Gap = 15 − 10 = +Rs. 5 Lakh (Positive)
Scenario (i): Rates ↑ 50 bps (+0.50%) in 1-6 month bucket ΔNII   1½
= Gap × Δr × Time Fraction = 10 Lakh × 0.005 × (6/12) =
2   10,00,000 × 0.005 × 0.5 = Rs. 2,500 Annualized ΔNII = Rs. 5,000   [05]
or use: ΔNII = Gap × Δr = 10L × 0.005 = Rs. 5,000 p.a.
Formula: ΔNII = Gap × Δr
Scenario (ii): Rates ↓ 25 bps (−0.25%) in 1-3 year bucket ΔNII =   1½
Gap × Δr = −5,00,000 × (−0.0025) = +Rs. 1,250 p.a. Negative
3
gap + rate decrease → NII INCREASES (beneficial scenario)
Formula: ΔNII = Gap × Δr
ALM Concept: Asset-Liability Management (ALM) involves   1
managing the balance sheet to optimize NII while controlling
4
interest rate risk. Gap Analysis identifies mismatches between
RSA and RSL to assess NII sensitivity to rate changes.
Final Answers: Scenario(i) +50bps: ΔNII = +Rs. 5,000 | Scenario(ii)   5 Marks Total
−25bps in 1-3yr: ΔNII = +Rs. 1,250 | Positive Gap → Rate ↑ beneficial
CO2;   B JP Bank | Asset A: EAD=40m, PD=0.25%, LGD=20%, σPD=5%, σLGD=15% | Asset B:
SO-1;   EAD=60m, PD=0.50%, LGD=35%, σPD=7%, σLGD=10% | ρ=0.20
BL-
Step   Working / Calculation   Marks
Apply
Expected Loss (EL) for each asset: EL_A = EAD_A × PD_A   1
× LGD_A = 40m × 0.0025 × 0.20 = Rs. 20,000 EL_B =
1   EAD_B × PD_B × LGD_B = 60m × 0.005 × 0.35 = Rs.
1,05,000
Formula: EL = EAD × PD × LGD
Unexpected Loss (UL) for each asset: UL_i = EAD_i ×   ½
2   √(LGD²×σPD² + PD²×σLGD²)   [05]
Formula: UL = EAD × √(LGD²·σPD² + PD²·σLGD²)
UL_A = 40m × √[(0.20²×0.05²) + (0.0025²×0.15²)] = 40m ×   ½
√[(0.04×0.0025) + (0.00000625×0.0225)] = 40m × √[0.0001
+ 0.000000140625] = 40m × √0.000100140625 = 40m ×
0.010007 = Rs. 4,00,281 ≈ Rs. 4.00 Lakh
UL_B = 60m × √[(0.35²×0.07²) + (0.005²×0.10²)] = 60m ×   ½
√[(0.1225×0.0049) + (0.000025×0.01)] = 60m ×
√[0.00060025 + 0.00000025] = 60m × √0.0006005 = 60m ×
0.02451 = Rs. 14,70,488 ≈ Rs. 14.70 Lakh
********** 7 **********
--- page 8 ---
Portfolio Unexpected Loss (ρ = 0.20): UL_P = √(UL_A² +   1
UL_B² + 2ρ×UL_A×UL_B) = √[(4.00)² + (14.70)² +
3   2×0.20×4.00×14.70] All in Lakh: = √[16.00 + 216.09 +
23.52] = √255.61 = Rs. 15.99 Lakh
Formula: UL_P = √(UL_A² + UL_B² + 2ρ·UL_A·UL_B)
Risk Contribution of each asset to Portfolio UL: RC_A =   1
UL_A × (UL_A + ρ×UL_B) / UL_P = 4.00 × (4.00 +
0.20×14.70) / 15.99 = 4.00 × 6.94 / 15.99 = Rs. 1.736 Lakh
4   RC_B = UL_B × (UL_B + ρ×UL_A) / UL_P = 14.70 × (14.70
+ 0.20×4.00) / 15.99 = 14.70 × 15.50 / 15.99 = Rs. 14.26
Lakh
Formula: RC_i = UL_i(UL_i + ρ·UL_j)/UL_P
Impact of ρ increasing to 0.35: New UL_P = √[16 + 216.09 +   1
2×0.35×4.00×14.70] = √[16+216.09+41.16] = √273.25 = Rs.
5   16.53 Lakh ↑ Correlation → ↑ Portfolio UL → Concentration
Risk increases
Formula: Higher ρ → less diversification benefit
Final Answers: EL_A=Rs.20,000 | EL_B=Rs.1,05,000 |   5 Marks Total
UL_A=Rs.4.00L | UL_B=Rs.14.70L | UL_Portfolio(ρ=0.20)=Rs.15.99L |
UL_Portfolio(ρ=0.35)=Rs.16.53L
Q5   Answer the following:   [10]
CO3; SO-   A   Given: Borrow USD 100m @ 3.6% | Sell Spot USD @ Rs. 93.70 | Buy 1-yr Fwd
8;   USD @ Rs. 97.50 | Invest INR @ 8% | Spot after 1yr = Rs. 97.80
BL-Apply
Step   Working / Calculation   Marks
Zero-Arbitrage Forward Rate (IRP): F* = S × (1 + r_INR)   1
/ (1 + r_USD) = 93.70 × (1.08) / (1.036) = 93.70 ×
1
1.04247 = Rs. 97.68
Formula: F* = S × (1+r_d)/(1+r_f)
Actual Forward = Rs. 97.50 | IRP Forward = Rs. 97.68   ½
Since Actual Fwd (97.50) < IRP Fwd (97.68) → USD is
2   underpriced forward → Arbitrage EXISTS: Strategy:
Borrow USD, Convert Spot, Invest in INR, Buy USD
Forward
[05]
Flow Diagram: Today: Borrow USD 100m → Sell @   1
93.70 → Receive INR 9,370m → Invest @ 8% After 1yr:
3   INR receipt = 9,370m × 1.08 = INR 10,119.60m Buy USD
Forward: Pay Rs. 97.50/USD → Pay INR to buy USD
100m × 1.036 = USD 103.6m fwd
USD Repayment at maturity: 100m × 1.036 = USD   ½
4   103.60m INR needed to buy USD 103.60m @ fwd 97.50:
103.60m × 97.50 = INR 10,101m
Arbitrage Gain = INR Receipts − INR paid for Fwd USD   1
= 10,119.60m − 10,101m = INR 18.60m = Rs. 18.6
5
Crores (Alternatively: (F* − Actual Fwd) × Loan Amount
= (97.68 − 97.50) × 103.6m ≈ Rs. 18.65m)
********** 8 **********
--- page 9 ---
Formula: Gain = INR receipts − INR forward
payment
Spot rate after 1yr = Rs. 97.80 (not used in CIA —   1
covered by forward contract)
6
Formula: CIA locks in via Forward → not exposed
to spot rate risk
Final Answer: IRP Forward = Rs. 97.68 | Arbitrage Gain ≈ Rs.   5 Marks
18.60 Crores | Strategy: Borrow USD → Convert INR → Invest   Total
→ Buy USD Forward
CO3; SO-   B   Indian Exporter: £6 per garment | Cost = Rs. 600 | 2-Month settlement | Spot:
8;   £=112.50, $=93.70 | 2m Fwd: £=112.79, $=93.96
BL-Apply
Interest Rates: £=3.75%, $=3.6%, Rs.=5.25%
Step   Working / Calculation   Marks
Option 1: Invoice in Sterling (£6) Sell £ at 2-month Forward   1
Rate = Rs. 112.79/£ INR Receipt per garment = £6 ×
1
112.79 = Rs. 676.74
Formula: INR = FC amount × Forward Rate
Option 2: Invoice in USD Convert £6 to USD at Spot: 6 ×   1½
112.50 / 93.70 = USD 7.202 Sell USD at 2-month Forward =
2   Rs. 93.96/USD INR Receipt = 7.202 × 93.96 = Rs. 676.50
Formula: USD = £ × (Spot £/Rs) / (Spot $/Rs); INR
= USD × Fwd $/Rs
Comparison: Sterling Invoice: Rs. 676.74 per garment →   1   [05]
3   Profit = 676.74 − 600 = Rs. 76.74 USD Invoice: Rs. 676.50
per garment → Profit = 676.50 − 600 = Rs. 76.50
Decision: INVOICE IN STERLING (£) Reason: Higher INR   1½
realization (Rs. 676.74 > Rs. 676.50) by Rs. 0.24 per
garment Additionally, Sterling forward (£=112.79) reflects
4
higher premium vs spot (112.50) = Rs. 0.29 appreciation
Both options lock in via forward contracts, eliminating
currency risk
Final Answer: Invoice in STERLING | INR/garment: £ option = Rs.   5 Marks T
676.74 vs $ option = Rs. 676.50 | Difference = Rs. 0.24 | Recommend
GBP
********** 9 **********
--- page 10 ---
Q6   Answer the following:   [10]
CO A Company A (British): Wants USD; can borrow GBP@8.5%, USD@5.8% | Company B (US):
1;   Wants GBP; can borrow GBP@8.1%, USD@5.2% | Bank earns 15bps; each Co. gains
SO-
20bps
1;
BL-   Step   Working / Calculation   Marks
App
ly   Comparative Advantage Analysis: GBP Differential: 8.5% − 8.1% =   1
0.4% (B has advantage in GBP) USD Differential: 5.8% − 5.2% =
0.6% (B has advantage in USD too) QSD = Larger diff − Smaller diff
= 0.6% − 0.4% = 0.2% = 20bps (Total gain to split) Bank earns 15bps
1
→ Each company gets 20bps (since total = bank 15bps + both cos
20bps each = 55bps > 20bps) Note: Total QSD = 20bps → Bank
15bps + 2×20bps = 55bps → structure adjusted
Formula: QSD = |Diff_currency1 − Diff_currency2|
Wait — Re-check: Total QSD = 20bps to share Bank gets 15bps;   ½
each company gets (20 − 15)/2 = 2.5bps each — that's too small
Alternative reading: Bank earns 15bps from each company (30bps
2
total); each co gains 20bps Total benefit needed = 30 + 20 + 20 =
70bps → QSD must be at least 70bps. With QSD = 0.20% = 20bps
total, the standard split: each gains (20bps − 15bps)/2 = 2.5bps each.
[05]
Swap Structure (standard interpretation): • Co. A: Borrows GBP @   1
8.5% (comparative advantage) → swaps to pay USD • Co. B:
3
Borrows USD @ 5.2% (comparative advantage) → swaps to pay GBP
• Bank acts as intermediary, earns spread
Effective Costs after swap: • Co. A wants USD: Effective rate = 5.8%   1½
− 0.20% gain = 5.60% • Co. B wants GBP: Effective rate = 8.1% −
4
0.20% gain = 7.90% • Bank net spread = 0.15% = 15bps
Formula: Effective Cost = Direct Market Rate − Gain
Cash Flow Structure: → Co.A pays GBP 8.5% to GBP market;   1
receives GBP from Bank; pays USD to Bank → Co.B pays USD 5.2%
5
to USD market; receives USD from Bank; pays GBP to Bank → Bank
nets GBP and USD flows, earning 15bps
Final Answer: QSD = 20bps | A: USD effective = 5.60% | B: GBP effective   5 Marks
= 7.90% | Bank: 15bps   Total
CO B Long Nifty 22,500 CE @ Premium Rs. 350 | Short Nifty 22,500 PE @ Premium Rs. 280 | Net
1;   Cost = 350 − 280 = Rs. 70 (debit)
SO-
1;   Synthetic Long: Buying a Call + Selling a Put at the SAME strike creates a Synthetic Long
BL-   Futures position — replicating the payoff of buying the index outright.
App   Payoff Calculation: Long CE Payoff = max(S−K,0)−Premium; Short PE Payoff =
ly   Premium−max(K−S,0)   [05]
Expiry   Long Call 22500 P/L   Short Put 22500 P/L   Net Option   Net P/L
Level   P/L   (after
Rs.70
cost)
22,800   300−350 = −50   280 (PE expires) = +280   −50+280 =   230−70
+230   = +160
********** 10 **********
--- page 11 ---
22,200   CE expires: −350   (22500−22200)−280=300−280=+20… Actual:   −350+(−20) −370+70
Put exercised against: −(22500−22200)+280   = −370   = −300
= −20
22,500   CE expires: −350   PE expires: +280   −70   −70+70
= 0
23,500   (23500−22500)−350=1000−35   PE expires: +280   +930   930−70
0=+650   = +860
Step   Working / Calculation   Marks
Payoff at 22,800 (Rs. +160) → Market above strike: net positive [1] Payoff   5
at 22,200 (Rs. −300) → Market below strike: net negative [1] Payoff at
Marks 22,500 (Rs. 0) → At-the-money: break-even [1] Payoff at 23,500 (Rs.
+860) → Far above strike: maximum upside [1] Nature: SYNTHETIC
LONG FUTURES — unlimited upside, unlimited downside [1]
When to use: When bullish on index; want long exposure without actual futures margin;
cheaper than outright futures
Mark Distribution: 4 payoffs × 1 mark each + Nature identification (1)   5 Marks Total
Q7   Answer the following:   [10]
CO1; SO- A   Step Working / Calculation   Marks
1;
BL-Analyze   Put-Call Parity (for European options): C + K×e^(−rT) = P +   1
S LHS = C + PV(K) = 130 + 500×e^(−0.0525×0.25) = 130
1   + 500×e^(−0.013125) = 130 + 500×0.9870 = 130 + 493.48
= Rs. 623.48
Formula: C + Ke^{-rT} = P + S
2   RHS = P + S = 105 + 492 = Rs. 597.00   ½
Compare: LHS (623.48) > RHS (597.00) Mismatch = Rs.   ½
26.48 → ARBITRAGE OPPORTUNITY EXISTS (LHS
3
overpriced relative to RHS: Call is overpriced or Put is
underpriced)
Arbitrage Strategy — SELL overpriced side (LHS), BUY   1
underpriced side (RHS): • SELL the Call (C) for Rs. 130 •   [05]
4
BORROW PV(K) = Rs. 493.48 at 5.25% for 0.25yr • BUY
the Put (P) for Rs. 105 • BUY the Stock (S) for Rs. 492
Cash Flows TODAY: Inflows: +130 (sell C) + 493.48   1
5   (borrow) Outflows: −105 (buy P) − 492 (buy S) Net =
623.48 − 597 = +Rs. 26.48 → RISK-FREE PROFIT upfront
At Expiry: All positions offset → No net cash flow needed   ½
6   The Rs. 26.48 locked in today is the arbitrage profit (PV
terms)
Factors affecting European Call/Put prices: • Stock Price   ½
(S) ↑ → C ↑, P ↓ | Strike (K) ↑ → C ↓, P ↑ • Time (T) ↑ →
7
Both C & P ↑ | Volatility (σ) ↑ → Both ↑ • Interest Rate (r) ↑
→ C ↑, P ↓ | Dividend → C ↓, P ↑
********** 11 **********
--- page 12 ---
Final Answer: LHS=623.48 > RHS=597.00 → Arbitrage profit =   5 Marks
Rs. 26.48 | Strategy: Sell Call + Borrow + Buy Put + Buy Stock   Total
CO1; SO- B Definition: Operational Risk is the risk of loss resulting from inadequate or failed
1;   internal processes, people, systems, or from external events. It includes legal risk but
BL-Analyze
excludes strategic and reputational risk (Basel III definition).
Keywords: Basel III, Pillar 2, AMA, BIA, Fraud, Cyber Risk, RBI Guidelines
• Sub-Category 1: Internal Fraud — unauthorized transactions, embezzlement (e.g.,
Satyam accounting fraud)
• Sub-Category 2: External Fraud — phishing, cyber-attacks (e.g., Cosmos Bank
SWIFT hack Rs. 94.42 Cr)
• Sub-Category 3: Employment Practices — employee misconduct, HR failures
• Sub-Category 4: Clients/Products — mis-selling, KYC failures
• Sub-Category 5: Business Disruption — IT failures, data breaches
Recent Indian Banking Frauds (mapped to Op-Risk categories):
• Punjab National Bank (PNB) Scam 2018: Nirav Modi/Mehul Choksi — fraudulent
LoUs via SWIFT bypass. Category: Internal Fraud + System/Process failure. Loss:
~Rs. 13,000 Cr
• Cosmos Bank SWIFT Hack 2018: External attack bypassed SWIFT → Rs. 94.42
Cr siphoned. Category: External Fraud + Technology failure
Mitigation Tools & Regulatory Framework:   [05]
• Basel III: Pillar 1 — Operational Risk Capital under BIA/STA/AMA approaches |
Pillar 2 — ICAAP
• RBI Guidelines: Cyber Security Framework, Fraud Risk Management, Risk
Governance at Board level
•   Internal Controls: SOD (Segregation of Duties), maker-checker systems, forensic
audit, whistleblower policies
Hybrid Securities:
Definition: Hybrid Securities combine features of both equity and debt instruments.
Examples: AT1 Bonds (Perpetual Bonds), Convertible Debentures (CCDs),
Preference Shares.
• Role in Financial Engineering: Used to optimize capital structure, fulfill Basel III
Tier 1/Tier 2 capital requirements, and offer risk-return flexibility
Mark Distribution: Op-Risk definition (1) + Sub-categories with
examples (1) + 2 fraud cases mapped (1) + Mitigation/Basel III (1)
+ Hybrid Securities (1)
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 10 · Answer key · paper 45bd16749c57

- Departments: Electronics and Telecommunication
- Programmes: MBATech (ELECTRONICS & TELECOMMUNICATIO
- Source: `02_Question_Papers/2024/Sem_10/Final-Exam/MBATech (ELECTRONICS & TELECOMMUNICATIO_ba3ceaa3/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2024-2025.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 28 Apr 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (Comp)/MBA. Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: V/Semester X(Exam Year: 2024-2025)
Subject: Financial Engineering
Date: 28 Apr 2025   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
8. Scientific calculator/ finance calculators are allowed
Q1
a.   Profit /   Marks
Type of   Strike   spot   Exercised Loss per   Total profit
Sl.no option   price   price   / Lapse   share   /Loss
1   Sell Call   750   600 lapsed   45   27000   1
2   Sell Call   750   850 Exercised   -55   -33000   0.5
3 Buy Put   3000   2500 Exercised   500   300000   0.5
4 Buy Put   3000   3500 lapsed   -30   -18000   1
Total profit / Loss   276000   1
b.   YTM ≈ C + (M-P) / n   (1 mark)
0.5M + 0.5P
YTM = 140 + [(900 – 1000)/4]
(900+1000)/2
= 12.10 %.   (2 marks)
c.   Interest saving = 25,00,00,000 X (6.5-5.8)/100 X 90/365 = 431506.85   (1 mark)
Net settlement amount (gain) = 431506.85 / (1 + (6.5/100*90/365)) = ₹ 4,24,700. (2 marks)
Q2   In 3 month ₹100 will become 102 @ 8%p.a.
In 6 month ₹ 100 will become 105 @ 10% p.a.
Therefore, 3X6 FRA (theoretical) = (105-102) / 102 *100 * 12 / 3 = 11.76 % p.a.
Quoted FRA 3 X 6 = 9% / 10 %.
Theoretical FRA 3X6 is greater than Quoted FRA.
Hence there is arbitrage opportunity.   (3 marks)
Borrow ₹ 10,00,000 @ 8 % p.a. for 3 months and invest ₹ 10,00,000 @ 10% for 6 month as quoted
FRA is cheaper than theoretical FRA.   (1 mark)
Amount to be repaid after 6 months
= (1000000 + (100000*8%*3/12))*10/100*3/12 ) + 1000000 = ₹ 1025500.   (3 marks)
Amount received after 6 months at 10% p.a.
=1000000 + (1000000* 6/100 * 10%) = ₹ 10,30,000.   (2 marks)
Therefore, Arbitrage gain = 10,30,000 – 10,25,500 = ₹ 4,500 at the end of 6 month. (1 mark)
********** 1 **********
--- page 2 ---
Q3   Hedge for Importer.
Long Hedge.
Amount to be hedged = 8750000   1 mark
Number of contracts in future market =   972 contracts   1mark
Long hedge created in Future market
Particulars   1$ = 84   1$ = 88   1$ = 94   Marks
In future market
Long 972 *100 $ at 90 / $   -8748000   -8748000   -8748000   1
Short in the month of December 2025   8164800   8553600   9136800   1
Net gain / loss in future market   -583200   -194400   388800
Long in Spot market in December   -8164800   -8553600   -9136800   1
Total cash outflow from hedged lots   -8748000   -8748000   -8748000   1
Cash outflow from unhedged lots   -235200   -246400   -263200   2
Total cash outflow in December   -8983200   -8994400   -9011200   2
Q4   Synthetic long position is long call at the money and short put at the money. (1 mark)
CMP = 1269.15 therefore at the money strike price is 1270.
Profit and Loss from the Synthetic position for the given spot prices are as follows:
(6 marks)
Spot   Long Call   short put   strateg
prices   1270 @ 11.15   1270 @ 12.15   y
Premium   profit/
IV Premium paid   Profit / Loss   IV   received   Profit / Loss   loss
1230   0   -11.15   -11.15   -40   12.15   -27.85   -39
1240   0   -11.15   -11.15   -30   12.15   -17.85   -29
1250   0   -11.15   -11.15   -20   12.15   -7.85   -19
1260   0   -11.15   -11.15   -10   12.15   2.15   -9
1270   0   -11.15   -11.15   0   12.15   12.15   1
1
1280   0   -11.15   -1.15   0   12.15   12.15   11
2
1290   0   -11.15   8.85   0   12.15   12.15   21
3
1300   0   -11.15   18.85   0   12.15   12.15   31
Returns from Cash market:   (2 marks)
spot   CMP =
price   1269.15
1230   -39.15
1240   -29.15
********** 2 **********
--- page 3 ---
1250   -19.15
1260   -9.15
1270   0.85
1280   10.85
1290   20.85
1300   30.85
Conclusion: By observing the returns in cash market and the returns from Synthetic position, we can
see that both of them are giving equivalent returns. But, Synthetic position in derivative market
needs less capital, so we can take the benefit of leverage in synthetic market and get the similar
returns as in cash market.   (1 mark)
Q5   Cash   PVF @
Year   flows   8%   PVCF   n.pv
1   120   0.926   111.12   111.12
2   120   0.857   102.84   205.68
3   120   0.794   95.28   285.84
4   120   0.735   88.2   352.8
5   1170   0.681   796.77 3983.85
1194.21 4939.29
Intrinsic Value = 1194.21   (2.5 marks)
Sensitivity of bond = Sum(n.pv)
1+i
Sensitivity of bond = 4939.29 / 1.08 = 4573.42   (2.5 marks)
Macaulay’s duration = sum(n.pv) / IV = 4939.29 / 1194.21   = 4.14 years   (2.5 marks)
Intrinsic value of bond if the desired rate increase to 10%   (2.5 marks)
Decrease in Intrinsic value = Intrinsic value – Sensitivity X change in rate
= 1194.21 – (4573.42 * 2%) = 1102.74
Q6a An embedded option is a feature of a financial instrument that lets issuers or holders take specified
actions against the other party at some future time. Embedded options are provisions included in
.
some fixed-income securities that allow investors or the issuer to do specific actions, such as call
back (redeem) the issue early.   (1 mark)
Convertible bonds
A convertible security is an investment that can be changed from its initial form into another form.
The most common types of convertible securities are convertible bonds and convertible preferred
shares, which can be converted into common stock. With convertible bonds, an embedded option
gives bondholders the right to exchange the bond for shares in the underlying common stock. The
conversion value is similar to the value of the call option on the common stock.
(2 marks)
Callable
Embedded options give investors the power to prematurely redeem a security. For example, a call
provision is a type of embedded option that affords holders the power to redeem the bond before its
scheduled maturity. Callable bonds are a tool used by issuers, especially at times of high prevailing
interest rates, where such an agreement allows the issuer to buy back or redeem bonds at some time
in the future. In this case, the bondholder has essentially sold a call option to the company that issued
the bond, whether they realize it or not.   ( 2 marks)
Q6   Beta of the stock = Covariance of stock and market return
Variance of the market
b.
= 30/41 = 0.732 %   (1 mark)
Total risk of security = (SD of security)^2 = (9.5)^2 = 90.25%   (1 mark)
********** 3 **********
--- page 4 ---
Systematic risk = Beta X Variance of market = 0.732 X 41 = 30.012%   (1.5 marks)
Unsystematic risk = 90.25 – 30.012 = 60.238%   (1.5 marks)
Q7   i.   Gap exposure
A gap or mismatch risk arises from holding assets and liabilities and off-balance sheet items with
a.
different principal amounts, maturity dates or re-pricing dates, thereby creating exposure to
unexpected changes in the level of market interest rates.   (1 mark)
• The positive Gap indicates that banks have more interest Rate Sensitive Assets (RSAs) than
interest Rate Sensitive Liabilities (RSLs). A positive or asset sensitive Gap means that an
increase in market interest rates could cause an increase in Net Interest Income (NII).
(1 mark)
•   Conversely, a negative or liability sensitive Gap implies that the banks’ NII could increase as a
result of decrease in market interest rates. A negative gap indicates that banks have more RSLs
than RSAs. The Gap is used as a measure of interest rate sensitivity.   (1 mark)
Earnings at risk (EaR):   (2 marks)
•   Positive or Negative Gap is multiplied by the assumed interest rate changes to derive the
Earnings at Risk (EaR). The EaR method facilitates to estimate how much the earnings might
be impacted by an adverse movement in interest rates.
• The periodic gap analysis indicates the interest rate risk exposure of banks over distinct
maturities and suggests magnitude of portfolio changes necessary to alter the risk profile.
Q7   Immunization of bond is a process of creating a bond portfolio through which interest rate
risk and reinvestment risk can be either eliminated or minimized.   (1 mark)
b.
Immunization cannot be achieved through single bond and creating a bond portfolio is
necessary for immunization.   (1 mark)
Interest Rate Risk   (1.5 marks)
•   Such risk arises when interest rate prevailing in market increases
•   This will cause an increase in the expectation for the bond holder
•   As a result, the discounting rate i.e., DYR increases and the present value of bond decreases.
Reinvestment risk   (1.5 marks)
•   Such risk arises when interest rate prevailing in market decreases
•   As a result, the bond that is currently held will have increase in its value.
•   However, once the bond is redeemed, the investor gets the redemption price in hand.
• The investment of such amount cannot be made at earlier coupon rate and reinvestment will
be at a lower rate resulting into reduced income for the investor.
********** 4 **********
````

## 2024-25 · Final-Exam · Sem 10 · Answer key · paper fc5c85fa7673

- Departments: Mechanical
- Programmes: MBATech (MECHANICAL ENGINEERING) - 7046
- Source: `02_Question_Papers/2024/Sem_10/Final-Exam/MBATech (MECHANICAL ENGINEERING) - 7046/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2024-2025.pdf`
- Text: none (FileDataError: Failed to open stream)

## 2024-25 · Final-Exam · Sem 10 · Answer key · paper 4b9fb473bc48

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_10/Final-Exam/MBATech_Computer_7047/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2024-2025.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 28 Apr 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (Comp)/MBA. Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: V/Semester X(Exam Year: 2024-2025)
Subject: Financial Engineering
Date: 28 Apr 2025   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
8. Scientific calculator/ finance calculators are allowed
Q1
a.   Profit /   Marks
Type of   Strike   spot   Exercised Loss per   Total profit
Sl.no option   price   price   / Lapse   share   /Loss
1   Sell Call   750   600 lapsed   45   27000   1
2   Sell Call   750   850 Exercised   -55   -33000   0.5
3 Buy Put   3000   2500 Exercised   500   300000   0.5
4 Buy Put   3000   3500 lapsed   -30   -18000   1
Total profit / Loss   276000   1
b.   YTM ≈ C + (M-P) / n   (1 mark)
0.5M + 0.5P
YTM = 140 + [(900 – 1000)/4]
(900+1000)/2
= 12.10 %.   (2 marks)
c.   Interest saving = 25,00,00,000 X (6.5-5.8)/100 X 90/365 = 431506.85   (1 mark)
Net settlement amount (gain) = 431506.85 / (1 + (6.5/100*90/365)) = ₹ 4,24,700. (2 marks)
Q2   In 3 month ₹100 will become 102 @ 8%p.a.
In 6 month ₹ 100 will become 105 @ 10% p.a.
Therefore, 3X6 FRA (theoretical) = (105-102) / 102 *100 * 12 / 3 = 11.76 % p.a.
Quoted FRA 3 X 6 = 9% / 10 %.
Theoretical FRA 3X6 is greater than Quoted FRA.
Hence there is arbitrage opportunity.   (3 marks)
Borrow ₹ 10,00,000 @ 8 % p.a. for 3 months and invest ₹ 10,00,000 @ 10% for 6 month as quoted
FRA is cheaper than theoretical FRA.   (1 mark)
Amount to be repaid after 6 months
= (1000000 + (100000*8%*3/12))*10/100*3/12 ) + 1000000 = ₹ 1025500.   (3 marks)
Amount received after 6 months at 10% p.a.
=1000000 + (1000000* 6/100 * 10%) = ₹ 10,30,000.   (2 marks)
Therefore, Arbitrage gain = 10,30,000 – 10,25,500 = ₹ 4,500 at the end of 6 month. (1 mark)
********** 1 **********
--- page 2 ---
Q3   Hedge for Importer.
Long Hedge.
Amount to be hedged = 8750000   1 mark
Number of contracts in future market =   972 contracts   1mark
Long hedge created in Future market
Particulars   1$ = 84   1$ = 88   1$ = 94   Marks
In future market
Long 972 *100 $ at 90 / $   -8748000   -8748000   -8748000   1
Short in the month of December 2025   8164800   8553600   9136800   1
Net gain / loss in future market   -583200   -194400   388800
Long in Spot market in December   -8164800   -8553600   -9136800   1
Total cash outflow from hedged lots   -8748000   -8748000   -8748000   1
Cash outflow from unhedged lots   -235200   -246400   -263200   2
Total cash outflow in December   -8983200   -8994400   -9011200   2
Q4   Synthetic long position is long call at the money and short put at the money. (1 mark)
CMP = 1269.15 therefore at the money strike price is 1270.
Profit and Loss from the Synthetic position for the given spot prices are as follows:
(6 marks)
Spot   Long Call   short put   strateg
prices   1270 @ 11.15   1270 @ 12.15   y
Premium   profit/
IV Premium paid   Profit / Loss   IV   received   Profit / Loss   loss
1230   0   -11.15   -11.15   -40   12.15   -27.85   -39
1240   0   -11.15   -11.15   -30   12.15   -17.85   -29
1250   0   -11.15   -11.15   -20   12.15   -7.85   -19
1260   0   -11.15   -11.15   -10   12.15   2.15   -9
1270   0   -11.15   -11.15   0   12.15   12.15   1
1
1280   0   -11.15   -1.15   0   12.15   12.15   11
2
1290   0   -11.15   8.85   0   12.15   12.15   21
3
1300   0   -11.15   18.85   0   12.15   12.15   31
Returns from Cash market:   (2 marks)
spot   CMP =
price   1269.15
1230   -39.15
1240   -29.15
********** 2 **********
--- page 3 ---
1250   -19.15
1260   -9.15
1270   0.85
1280   10.85
1290   20.85
1300   30.85
Conclusion: By observing the returns in cash market and the returns from Synthetic position, we can
see that both of them are giving equivalent returns. But, Synthetic position in derivative market
needs less capital, so we can take the benefit of leverage in synthetic market and get the similar
returns as in cash market.   (1 mark)
Q5   Cash   PVF @
Year   flows   8%   PVCF   n.pv
1   120   0.926   111.12   111.12
2   120   0.857   102.84   205.68
3   120   0.794   95.28   285.84
4   120   0.735   88.2   352.8
5   1170   0.681   796.77 3983.85
1194.21 4939.29
Intrinsic Value = 1194.21   (2.5 marks)
Sensitivity of bond = Sum(n.pv)
1+i
Sensitivity of bond = 4939.29 / 1.08 = 4573.42   (2.5 marks)
Macaulay’s duration = sum(n.pv) / IV = 4939.29 / 1194.21   = 4.14 years   (2.5 marks)
Intrinsic value of bond if the desired rate increase to 10%   (2.5 marks)
Decrease in Intrinsic value = Intrinsic value – Sensitivity X change in rate
= 1194.21 – (4573.42 * 2%) = 1102.74
Q6a An embedded option is a feature of a financial instrument that lets issuers or holders take specified
actions against the other party at some future time. Embedded options are provisions included in
.
some fixed-income securities that allow investors or the issuer to do specific actions, such as call
back (redeem) the issue early.   (1 mark)
Convertible bonds
A convertible security is an investment that can be changed from its initial form into another form.
The most common types of convertible securities are convertible bonds and convertible preferred
shares, which can be converted into common stock. With convertible bonds, an embedded option
gives bondholders the right to exchange the bond for shares in the underlying common stock. The
conversion value is similar to the value of the call option on the common stock.
(2 marks)
Callable
Embedded options give investors the power to prematurely redeem a security. For example, a call
provision is a type of embedded option that affords holders the power to redeem the bond before its
scheduled maturity. Callable bonds are a tool used by issuers, especially at times of high prevailing
interest rates, where such an agreement allows the issuer to buy back or redeem bonds at some time
in the future. In this case, the bondholder has essentially sold a call option to the company that issued
the bond, whether they realize it or not.   ( 2 marks)
Q6   Beta of the stock = Covariance of stock and market return
Variance of the market
b.
= 30/41 = 0.732 %   (1 mark)
Total risk of security = (SD of security)^2 = (9.5)^2 = 90.25%   (1 mark)
********** 3 **********
--- page 4 ---
Systematic risk = Beta X Variance of market = 0.732 X 41 = 30.012%   (1.5 marks)
Unsystematic risk = 90.25 – 30.012 = 60.238%   (1.5 marks)
Q7   i.   Gap exposure
A gap or mismatch risk arises from holding assets and liabilities and off-balance sheet items with
a.
different principal amounts, maturity dates or re-pricing dates, thereby creating exposure to
unexpected changes in the level of market interest rates.   (1 mark)
• The positive Gap indicates that banks have more interest Rate Sensitive Assets (RSAs) than
interest Rate Sensitive Liabilities (RSLs). A positive or asset sensitive Gap means that an
increase in market interest rates could cause an increase in Net Interest Income (NII).
(1 mark)
•   Conversely, a negative or liability sensitive Gap implies that the banks’ NII could increase as a
result of decrease in market interest rates. A negative gap indicates that banks have more RSLs
than RSAs. The Gap is used as a measure of interest rate sensitivity.   (1 mark)
Earnings at risk (EaR):   (2 marks)
•   Positive or Negative Gap is multiplied by the assumed interest rate changes to derive the
Earnings at Risk (EaR). The EaR method facilitates to estimate how much the earnings might
be impacted by an adverse movement in interest rates.
• The periodic gap analysis indicates the interest rate risk exposure of banks over distinct
maturities and suggests magnitude of portfolio changes necessary to alter the risk profile.
Q7   Immunization of bond is a process of creating a bond portfolio through which interest rate
risk and reinvestment risk can be either eliminated or minimized.   (1 mark)
b.
Immunization cannot be achieved through single bond and creating a bond portfolio is
necessary for immunization.   (1 mark)
Interest Rate Risk   (1.5 marks)
•   Such risk arises when interest rate prevailing in market increases
•   This will cause an increase in the expectation for the bond holder
•   As a result, the discounting rate i.e., DYR increases and the present value of bond decreases.
Reinvestment risk   (1.5 marks)
•   Such risk arises when interest rate prevailing in market decreases
•   As a result, the bond that is currently held will have increase in its value.
•   However, once the bond is redeemed, the investor gets the redemption price in hand.
• The investment of such amount cannot be made at earlier coupon rate and reinvestment will
be at a lower rate resulting into reduced income for the investor.
********** 4 **********
````

## 2024-25 · Final-Exam · Sem 10 · Answer key · paper 4c0402f4254a

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_10/Final-Exam/MBATech_IT_7041/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2024-2025.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 28 Apr 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (Comp)/MBA. Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: V/Semester X(Exam Year: 2024-2025)
Subject: Financial Engineering
Date: 28 Apr 2025   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
8. Scientific calculator/ finance calculators are allowed
Q1
a.   Profit /   Marks
Type of   Strike   spot   Exercised Loss per   Total profit
Sl.no option   price   price   / Lapse   share   /Loss
1   Sell Call   750   600 lapsed   45   27000   1
2   Sell Call   750   850 Exercised   -55   -33000   0.5
3 Buy Put   3000   2500 Exercised   500   300000   0.5
4 Buy Put   3000   3500 lapsed   -30   -18000   1
Total profit / Loss   276000   1
b.   YTM ≈ C + (M-P) / n   (1 mark)
0.5M + 0.5P
YTM = 140 + [(900 – 1000)/4]
(900+1000)/2
= 12.10 %.   (2 marks)
c.   Interest saving = 25,00,00,000 X (6.5-5.8)/100 X 90/365 = 431506.85   (1 mark)
Net settlement amount (gain) = 431506.85 / (1 + (6.5/100*90/365)) = ₹ 4,24,700. (2 marks)
Q2   In 3 month ₹100 will become 102 @ 8%p.a.
In 6 month ₹ 100 will become 105 @ 10% p.a.
Therefore, 3X6 FRA (theoretical) = (105-102) / 102 *100 * 12 / 3 = 11.76 % p.a.
Quoted FRA 3 X 6 = 9% / 10 %.
Theoretical FRA 3X6 is greater than Quoted FRA.
Hence there is arbitrage opportunity.   (3 marks)
Borrow ₹ 10,00,000 @ 8 % p.a. for 3 months and invest ₹ 10,00,000 @ 10% for 6 month as quoted
FRA is cheaper than theoretical FRA.   (1 mark)
Amount to be repaid after 6 months
= (1000000 + (100000*8%*3/12))*10/100*3/12 ) + 1000000 = ₹ 1025500.   (3 marks)
Amount received after 6 months at 10% p.a.
=1000000 + (1000000* 6/100 * 10%) = ₹ 10,30,000.   (2 marks)
Therefore, Arbitrage gain = 10,30,000 – 10,25,500 = ₹ 4,500 at the end of 6 month. (1 mark)
********** 1 **********
--- page 2 ---
Q3   Hedge for Importer.
Long Hedge.
Amount to be hedged = 8750000   1 mark
Number of contracts in future market =   972 contracts   1mark
Long hedge created in Future market
Particulars   1$ = 84   1$ = 88   1$ = 94   Marks
In future market
Long 972 *100 $ at 90 / $   -8748000   -8748000   -8748000   1
Short in the month of December 2025   8164800   8553600   9136800   1
Net gain / loss in future market   -583200   -194400   388800
Long in Spot market in December   -8164800   -8553600   -9136800   1
Total cash outflow from hedged lots   -8748000   -8748000   -8748000   1
Cash outflow from unhedged lots   -235200   -246400   -263200   2
Total cash outflow in December   -8983200   -8994400   -9011200   2
Q4   Synthetic long position is long call at the money and short put at the money. (1 mark)
CMP = 1269.15 therefore at the money strike price is 1270.
Profit and Loss from the Synthetic position for the given spot prices are as follows:
(6 marks)
Spot   Long Call   short put   strateg
prices   1270 @ 11.15   1270 @ 12.15   y
Premium   profit/
IV Premium paid   Profit / Loss   IV   received   Profit / Loss   loss
1230   0   -11.15   -11.15   -40   12.15   -27.85   -39
1240   0   -11.15   -11.15   -30   12.15   -17.85   -29
1250   0   -11.15   -11.15   -20   12.15   -7.85   -19
1260   0   -11.15   -11.15   -10   12.15   2.15   -9
1270   0   -11.15   -11.15   0   12.15   12.15   1
1
1280   0   -11.15   -1.15   0   12.15   12.15   11
2
1290   0   -11.15   8.85   0   12.15   12.15   21
3
1300   0   -11.15   18.85   0   12.15   12.15   31
Returns from Cash market:   (2 marks)
spot   CMP =
price   1269.15
1230   -39.15
1240   -29.15
********** 2 **********
--- page 3 ---
1250   -19.15
1260   -9.15
1270   0.85
1280   10.85
1290   20.85
1300   30.85
Conclusion: By observing the returns in cash market and the returns from Synthetic position, we can
see that both of them are giving equivalent returns. But, Synthetic position in derivative market
needs less capital, so we can take the benefit of leverage in synthetic market and get the similar
returns as in cash market.   (1 mark)
Q5   Cash   PVF @
Year   flows   8%   PVCF   n.pv
1   120   0.926   111.12   111.12
2   120   0.857   102.84   205.68
3   120   0.794   95.28   285.84
4   120   0.735   88.2   352.8
5   1170   0.681   796.77 3983.85
1194.21 4939.29
Intrinsic Value = 1194.21   (2.5 marks)
Sensitivity of bond = Sum(n.pv)
1+i
Sensitivity of bond = 4939.29 / 1.08 = 4573.42   (2.5 marks)
Macaulay’s duration = sum(n.pv) / IV = 4939.29 / 1194.21   = 4.14 years   (2.5 marks)
Intrinsic value of bond if the desired rate increase to 10%   (2.5 marks)
Decrease in Intrinsic value = Intrinsic value – Sensitivity X change in rate
= 1194.21 – (4573.42 * 2%) = 1102.74
Q6a An embedded option is a feature of a financial instrument that lets issuers or holders take specified
actions against the other party at some future time. Embedded options are provisions included in
.
some fixed-income securities that allow investors or the issuer to do specific actions, such as call
back (redeem) the issue early.   (1 mark)
Convertible bonds
A convertible security is an investment that can be changed from its initial form into another form.
The most common types of convertible securities are convertible bonds and convertible preferred
shares, which can be converted into common stock. With convertible bonds, an embedded option
gives bondholders the right to exchange the bond for shares in the underlying common stock. The
conversion value is similar to the value of the call option on the common stock.
(2 marks)
Callable
Embedded options give investors the power to prematurely redeem a security. For example, a call
provision is a type of embedded option that affords holders the power to redeem the bond before its
scheduled maturity. Callable bonds are a tool used by issuers, especially at times of high prevailing
interest rates, where such an agreement allows the issuer to buy back or redeem bonds at some time
in the future. In this case, the bondholder has essentially sold a call option to the company that issued
the bond, whether they realize it or not.   ( 2 marks)
Q6   Beta of the stock = Covariance of stock and market return
Variance of the market
b.
= 30/41 = 0.732 %   (1 mark)
Total risk of security = (SD of security)^2 = (9.5)^2 = 90.25%   (1 mark)
********** 3 **********
--- page 4 ---
Systematic risk = Beta X Variance of market = 0.732 X 41 = 30.012%   (1.5 marks)
Unsystematic risk = 90.25 – 30.012 = 60.238%   (1.5 marks)
Q7   i.   Gap exposure
A gap or mismatch risk arises from holding assets and liabilities and off-balance sheet items with
a.
different principal amounts, maturity dates or re-pricing dates, thereby creating exposure to
unexpected changes in the level of market interest rates.   (1 mark)
• The positive Gap indicates that banks have more interest Rate Sensitive Assets (RSAs) than
interest Rate Sensitive Liabilities (RSLs). A positive or asset sensitive Gap means that an
increase in market interest rates could cause an increase in Net Interest Income (NII).
(1 mark)
•   Conversely, a negative or liability sensitive Gap implies that the banks’ NII could increase as a
result of decrease in market interest rates. A negative gap indicates that banks have more RSLs
than RSAs. The Gap is used as a measure of interest rate sensitivity.   (1 mark)
Earnings at risk (EaR):   (2 marks)
•   Positive or Negative Gap is multiplied by the assumed interest rate changes to derive the
Earnings at Risk (EaR). The EaR method facilitates to estimate how much the earnings might
be impacted by an adverse movement in interest rates.
• The periodic gap analysis indicates the interest rate risk exposure of banks over distinct
maturities and suggests magnitude of portfolio changes necessary to alter the risk profile.
Q7   Immunization of bond is a process of creating a bond portfolio through which interest rate
risk and reinvestment risk can be either eliminated or minimized.   (1 mark)
b.
Immunization cannot be achieved through single bond and creating a bond portfolio is
necessary for immunization.   (1 mark)
Interest Rate Risk   (1.5 marks)
•   Such risk arises when interest rate prevailing in market increases
•   This will cause an increase in the expectation for the bond holder
•   As a result, the discounting rate i.e., DYR increases and the present value of bond decreases.
Reinvestment risk   (1.5 marks)
•   Such risk arises when interest rate prevailing in market decreases
•   As a result, the bond that is currently held will have increase in its value.
•   However, once the bond is redeemed, the investor gets the redemption price in hand.
• The investment of such amount cannot be made at earlier coupon rate and reinvestment will
be at a lower rate resulting into reduced income for the investor.
********** 4 **********
````

## 2024-25 · Re-Exam · Sem 10 · Answer key · paper 6034b72d63d4

- Departments: Mechanical
- Programmes: MBATech (MECHANICAL ENGINEERING) - 7046
- Source: `02_Question_Papers/2024/Sem_10/Re-Exam/MBATech (MECHANICAL ENGINEERING) - 7046/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2024-2025.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 01 Jul 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (Comp)/MBA. Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: V/Sem 10 Re-exam(Exam Year: 2024-2025)
Subject: Financial Engineering
Date: 01 Jul 2025   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
8. Scientific calculator/ finance calculators are allowed
Q1
a.   Profit /
Type of   Strike spot   Exercised   Loss per   Total profit
Sl.no option   price   price   / Lapse   share   /Loss   Marks
1 Buy Call   550   600 Exercised   -15   -9000   0.5
2 Buy Call   550   500 lapsed   -65   -39000   0.5
3   Sell Put   2000   2500 lapsed   50   30000   1
4   Sell Put   2000   1500 Exercised   -550   -330000   1
Total profit / Loss   -348000   1
b.   year cashflows   PVF   PVCF
1   60   0.925926 55.55555556
2   60   0.857339 51.44032922
3   60   0.793832 47.62993446
4   60   0.73503 44.10179117
5   60   0.680583 40.83499182
6   60   0.63017 37.81017761
7   60   0.58349 35.00942372
8   1060   0.540269 572.6850176
PV of bond 885.0672211
(3 marks)
c.   Floating rate borrower has risk when the interest rate rises.
Therefor buy FRA which means borrow in FRA to hedge itself from rising interest rate risk.
Borrowing will be at ask rate – 6.7%.
Fixed rate lending @ 8%
Margin locked in % p.a = 8% - 6.7% = 1.3% p.a.   (3 marks)
Q2   In 6 months ₹ 100 @ 15% will be = 100*15%*6/12 = 7.5 + 100 = 107.5
In 10 months ₹100 @ 18% will be = 100*18%*10/12 = 15 +100 = 115.
Theoretical 6 X 10 FRA = (115-107.5) / 107.5* 12/4 *100 = 20.93%
Quoted 6 X 10 FRA = 22/23% which is higher than theoretical FRA
********** 1 **********
--- page 2 ---
Hence Arbitrage opportunity exists.   (3 marks)
Therefore, invest at 6X 10 FRA and borrow $ 1000000 for 10 months at 18% p.a
Borrow 1 million USD at 18%   (1 mark)
Amount to be repaid after 10 months = 10,00,000 * 18%*10/12 = $1,50,000+ $ 1000000 =
$11,50,000.   (2 marks)
Invest the borrowed 1 million at present for 15% for 6 months = 1000000*15%*6/12 = 75,000
Reinvest the amount received after 6 months in FRA at 22% (bid rate)
= (1000000+75000)*22%*4/12 = 78833.33$
Amount received after 10th month = 1000000+75000+78833.33 = 1153833.33 $(3 marks)
Therefore, Arbitrage gain = 1153833.33 -1150000 = $3,833.33 per 1mio $.   (1 mark)
Q3   Hedge for Exporter
Short Hedge.
1
Amount to be hedged =   88000000   marks
Number of contracts in future   1
market =   9778 marks
Long hedge created in Fututre
market
Particulars   1$ = 85   1$ = 89   1$ = 95   Marks
In future market
Short 9778 *100 $ at 90 / $   88002000 88002000 88002000   1
Long in the month of December   -   -   -
2025   83113000 87024200 92891000   1
Net gain / loss in future market   4889000   977800 -4889000   1
Short in Spot market in December   83113000 87024200 92891000   1
Total cash outflow from hedged lots 88002000 88002000 88002000   1
Cash outflow from unhedged lots   1887000   1975800   2109000   2
Total cash outflow in December   89889000 89977800 90111000   1
Q4   8 marks
Spot   Long 2 Calls   Long put
prices   1100 @ 10   1100 @ 5   strategy
Premium   Profit /   Premium   Profit /   profit/
IV   paid   Loss   IV   received   Loss   loss
800   0   -10   -20   300   -5   295   275
850   0   -10   -20   250   -5   245   225
900   0   -10   -20   200   -5   195   175
950   0   -10   -20   150   -5   145   125
1000   0   -10   -20   100   -5   95   75
1050   0   -10   -20   50   -5   45   25
********** 2 **********
--- page 3 ---
1100   0   -10   -20   0   -5   -5   -25
1150   50   -10   80   0   -5   -5   75
1200   100   -10   180   0   -5   -5   175
1075   0   -10   -20   25   -5   20   0
Break- even point = 1075.   (2 marks)
Q5   Duration of portfolio = Wa X Da + Wb X Db
5   = Wa X 6 + (1-Wa) X 3
5   = 6Wa + 3 -3Wa
2   = 3 Wa
Wa = 2/3   and Wb =1-Wa = 1/3.   (2 marks)
The amount to be invested in each bond = 1000000*2/3 = 6,66,667 in Bond A and 3,33,333
(1000000-666667) in Bond B.   (2 marks)
No of Bond A to be bought = 666667 /986.5 = 676 bonds   (3 marks)
No of Bond B to be bought = 333333/1035 =323 bonds   (3 marks).
Q6a. Loan taken on 1st Jan 2025
Interest payable on 30th June 2025, 31st December 2025, 30th June 2026 and 31st December
2026.
Interest   Interest Cap   interest   Receipt from cap
payable   rate   option   payable   option   net cost
30-Jun-25   7% lapsed   7000   0   7000
31-Dec-25   12% exercised   12000   5000   7000
30-Jun-26   5% lapsed   5000   0   5000
31-Dec-26   9% exercised   9000   2000   7000
(5 marks)
Q6   A swaption, also known as a swap option, refers to an option to enter into an interest
rate swap or some other type of swap. In exchange for an option's premium, the buyer gains the
b.
right but not the obligation to enter into a specified swap agreement with the issuer on a
specified future date.
Swaptions are over-the-counter contracts and are not standardized, like equity options or
futures contracts. Thus, the buyer and seller need to both agree to the price of the swaption, the
time until expiration of the swaption, the notional amount and the fixed/floating rates.
(1 mark)
Payer Swaption
A payer swaption gives the holder the right, but not the obligation, to enter into a swap as the
fixed-rate payer and the float and the floating rate receiver. When it comes to the payer
swaption, the entity benefits when it anticipates a rise in interest rates. By entering the swap,
the payer locks in the ability to pay a fixed rate while receiving a potentially higher floating rate
that adjusts with rising rates.   (2 marks)
Receiver Swaption
On the other hand, a receiver swaption gives the holder the right to enter into a swap as the
fixed rate receiver and the floating rate payer. The structure works well when the holder expects
interest rates to fall. The holder will receive a higher fixed interest rate while paying a lower
floating rate that decreases with the market rate. This option is often used by pension funds and
insurance companies that require stable, predictable income streams and would like to capitalize
on favorable rate adjustments.   (2 marks)
Q7   • Repo is an abbreviation for the Repurchase Option Agreement. It is a contract between the
buyer and seller of the debt instrument, promising that the seller will repurchase the
a.
instrument after the specified period of time. It requires the seller to repurchase securities
at a higher price than the price at which it was actually sold.
********** 3 **********
--- page 4 ---
•   So, the difference in the amounts paid by the buyer of securities (at the time of buying) and
the seller of securities (at the time of repurchasing) is termed the repo rate. It helps the
seller of securities to raise short-term funds.
• To influence short-term interest levels, generally, RBI conducts Repo transactions. The tool is
used to manage excess liquidity in the monetary system.
•   Further, Repo/Reverse Repo transaction takes place between parties approved by the RBI
and that too in the securities approved by RBI, such as Government of India and State
Government Securities, Treasury Bills, FI Bonds, Corporate Bonds, PSU Bonds, etc.
Q7   A synthetic position is a trading option used to simulate the features of another comparable
position. More specifically, a synthetic position is created to simulate a similar reward or risk
b.
profile as that of a comparable position.   (1 mark)
1. Synthetic Long Stock   (2 marks)
The synthetic long stock position involves emulating the potential results of owning actual stock
by using trade options. To develop one, an individual needs to buy at the stock money calls and
then record at money puts of an equivalent stock.
The price paid at the calls is earned by the money received once puts are written, meaning that if
the stock fails to increase in price, there would be no loss or gain. Ideally, it is almost the same
as holding stock.
On the other hand, if stock prices increase, the money calls would generate a profit, and if the
price decreases, then the puts would transform into a loss. The likely profit or loss is essentially
equal to owning the stock.
The benefit, in this case, comes from the accruing leverage. The capital obligation needed when
creating a synthetic position is less than when purchasing an equivalent stock.
2. Synthetic Short Stock   (2 marks)
The synthetic short stock position is equivalent to short-selling existing stock. However, the
position uses options only. Creating such a position calls for writing on relevant stocks at the
money calls. Afterward, the same stock is bought at the money puts.
In case the stock does not increase in price, the outcome is considered neutral. The capital base
needed to purchase puts is recovered once calls are written. Thus, if the price of the stock drops,
there would be a gain made through the purchased puts.
However, if the price increases, it would translate into a loss because of the written calls. The
possible profit or loss is approximately equal to what the outcome would be if an individual short
sold a stock.
The synthetic short stock offers two important advantages. One, there is a lot to be leveraged,
and two, the stock brings in a lot of dividends. Once the stock is short sold and it generates
dividend, the stakeholders are entitled to their share of the dividend. However, stocks under
synthetic short position don’t require the seller to distribute a dividend to shareholders.
********** 4 **********
````

## 2024-25 · Re-Exam · Sem 10 · Answer key · paper eec8b344c3c9

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_10/Re-Exam/MBATech_Computer_7047/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2024-2025.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 01 Jul 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (Comp)/MBA. Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: V/Sem 10 Re-exam(Exam Year: 2024-2025)
Subject: Financial Engineering
Date: 01 Jul 2025   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
8. Scientific calculator/ finance calculators are allowed
Q1
a.   Profit /
Type of   Strike spot   Exercised   Loss per   Total profit
Sl.no option   price   price   / Lapse   share   /Loss   Marks
1 Buy Call   550   600 Exercised   -15   -9000   0.5
2 Buy Call   550   500 lapsed   -65   -39000   0.5
3   Sell Put   2000   2500 lapsed   50   30000   1
4   Sell Put   2000   1500 Exercised   -550   -330000   1
Total profit / Loss   -348000   1
b.   year cashflows   PVF   PVCF
1   60   0.925926 55.55555556
2   60   0.857339 51.44032922
3   60   0.793832 47.62993446
4   60   0.73503 44.10179117
5   60   0.680583 40.83499182
6   60   0.63017 37.81017761
7   60   0.58349 35.00942372
8   1060   0.540269 572.6850176
PV of bond 885.0672211
(3 marks)
c.   Floating rate borrower has risk when the interest rate rises.
Therefor buy FRA which means borrow in FRA to hedge itself from rising interest rate risk.
Borrowing will be at ask rate – 6.7%.
Fixed rate lending @ 8%
Margin locked in % p.a = 8% - 6.7% = 1.3% p.a.   (3 marks)
Q2   In 6 months ₹ 100 @ 15% will be = 100*15%*6/12 = 7.5 + 100 = 107.5
In 10 months ₹100 @ 18% will be = 100*18%*10/12 = 15 +100 = 115.
Theoretical 6 X 10 FRA = (115-107.5) / 107.5* 12/4 *100 = 20.93%
Quoted 6 X 10 FRA = 22/23% which is higher than theoretical FRA
********** 1 **********
--- page 2 ---
Hence Arbitrage opportunity exists.   (3 marks)
Therefore, invest at 6X 10 FRA and borrow $ 1000000 for 10 months at 18% p.a
Borrow 1 million USD at 18%   (1 mark)
Amount to be repaid after 10 months = 10,00,000 * 18%*10/12 = $1,50,000+ $ 1000000 =
$11,50,000.   (2 marks)
Invest the borrowed 1 million at present for 15% for 6 months = 1000000*15%*6/12 = 75,000
Reinvest the amount received after 6 months in FRA at 22% (bid rate)
= (1000000+75000)*22%*4/12 = 78833.33$
Amount received after 10th month = 1000000+75000+78833.33 = 1153833.33 $(3 marks)
Therefore, Arbitrage gain = 1153833.33 -1150000 = $3,833.33 per 1mio $.   (1 mark)
Q3   Hedge for Exporter
Short Hedge.
1
Amount to be hedged =   88000000   marks
Number of contracts in future   1
market =   9778 marks
Long hedge created in Fututre
market
Particulars   1$ = 85   1$ = 89   1$ = 95   Marks
In future market
Short 9778 *100 $ at 90 / $   88002000 88002000 88002000   1
Long in the month of December   -   -   -
2025   83113000 87024200 92891000   1
Net gain / loss in future market   4889000   977800 -4889000   1
Short in Spot market in December   83113000 87024200 92891000   1
Total cash outflow from hedged lots 88002000 88002000 88002000   1
Cash outflow from unhedged lots   1887000   1975800   2109000   2
Total cash outflow in December   89889000 89977800 90111000   1
Q4   8 marks
Spot   Long 2 Calls   Long put
prices   1100 @ 10   1100 @ 5   strategy
Premium   Profit /   Premium   Profit /   profit/
IV   paid   Loss   IV   received   Loss   loss
800   0   -10   -20   300   -5   295   275
850   0   -10   -20   250   -5   245   225
900   0   -10   -20   200   -5   195   175
950   0   -10   -20   150   -5   145   125
1000   0   -10   -20   100   -5   95   75
1050   0   -10   -20   50   -5   45   25
********** 2 **********
--- page 3 ---
1100   0   -10   -20   0   -5   -5   -25
1150   50   -10   80   0   -5   -5   75
1200   100   -10   180   0   -5   -5   175
1075   0   -10   -20   25   -5   20   0
Break- even point = 1075.   (2 marks)
Q5   Duration of portfolio = Wa X Da + Wb X Db
5   = Wa X 6 + (1-Wa) X 3
5   = 6Wa + 3 -3Wa
2   = 3 Wa
Wa = 2/3   and Wb =1-Wa = 1/3.   (2 marks)
The amount to be invested in each bond = 1000000*2/3 = 6,66,667 in Bond A and 3,33,333
(1000000-666667) in Bond B.   (2 marks)
No of Bond A to be bought = 666667 /986.5 = 676 bonds   (3 marks)
No of Bond B to be bought = 333333/1035 =323 bonds   (3 marks).
Q6a. Loan taken on 1st Jan 2025
Interest payable on 30th June 2025, 31st December 2025, 30th June 2026 and 31st December
2026.
Interest   Interest Cap   interest   Receipt from cap
payable   rate   option   payable   option   net cost
30-Jun-25   7% lapsed   7000   0   7000
31-Dec-25   12% exercised   12000   5000   7000
30-Jun-26   5% lapsed   5000   0   5000
31-Dec-26   9% exercised   9000   2000   7000
(5 marks)
Q6   A swaption, also known as a swap option, refers to an option to enter into an interest
rate swap or some other type of swap. In exchange for an option's premium, the buyer gains the
b.
right but not the obligation to enter into a specified swap agreement with the issuer on a
specified future date.
Swaptions are over-the-counter contracts and are not standardized, like equity options or
futures contracts. Thus, the buyer and seller need to both agree to the price of the swaption, the
time until expiration of the swaption, the notional amount and the fixed/floating rates.
(1 mark)
Payer Swaption
A payer swaption gives the holder the right, but not the obligation, to enter into a swap as the
fixed-rate payer and the float and the floating rate receiver. When it comes to the payer
swaption, the entity benefits when it anticipates a rise in interest rates. By entering the swap,
the payer locks in the ability to pay a fixed rate while receiving a potentially higher floating rate
that adjusts with rising rates.   (2 marks)
Receiver Swaption
On the other hand, a receiver swaption gives the holder the right to enter into a swap as the
fixed rate receiver and the floating rate payer. The structure works well when the holder expects
interest rates to fall. The holder will receive a higher fixed interest rate while paying a lower
floating rate that decreases with the market rate. This option is often used by pension funds and
insurance companies that require stable, predictable income streams and would like to capitalize
on favorable rate adjustments.   (2 marks)
Q7   • Repo is an abbreviation for the Repurchase Option Agreement. It is a contract between the
buyer and seller of the debt instrument, promising that the seller will repurchase the
a.
instrument after the specified period of time. It requires the seller to repurchase securities
at a higher price than the price at which it was actually sold.
********** 3 **********
--- page 4 ---
•   So, the difference in the amounts paid by the buyer of securities (at the time of buying) and
the seller of securities (at the time of repurchasing) is termed the repo rate. It helps the
seller of securities to raise short-term funds.
• To influence short-term interest levels, generally, RBI conducts Repo transactions. The tool is
used to manage excess liquidity in the monetary system.
•   Further, Repo/Reverse Repo transaction takes place between parties approved by the RBI
and that too in the securities approved by RBI, such as Government of India and State
Government Securities, Treasury Bills, FI Bonds, Corporate Bonds, PSU Bonds, etc.
Q7   A synthetic position is a trading option used to simulate the features of another comparable
position. More specifically, a synthetic position is created to simulate a similar reward or risk
b.
profile as that of a comparable position.   (1 mark)
1. Synthetic Long Stock   (2 marks)
The synthetic long stock position involves emulating the potential results of owning actual stock
by using trade options. To develop one, an individual needs to buy at the stock money calls and
then record at money puts of an equivalent stock.
The price paid at the calls is earned by the money received once puts are written, meaning that if
the stock fails to increase in price, there would be no loss or gain. Ideally, it is almost the same
as holding stock.
On the other hand, if stock prices increase, the money calls would generate a profit, and if the
price decreases, then the puts would transform into a loss. The likely profit or loss is essentially
equal to owning the stock.
The benefit, in this case, comes from the accruing leverage. The capital obligation needed when
creating a synthetic position is less than when purchasing an equivalent stock.
2. Synthetic Short Stock   (2 marks)
The synthetic short stock position is equivalent to short-selling existing stock. However, the
position uses options only. Creating such a position calls for writing on relevant stocks at the
money calls. Afterward, the same stock is bought at the money puts.
In case the stock does not increase in price, the outcome is considered neutral. The capital base
needed to purchase puts is recovered once calls are written. Thus, if the price of the stock drops,
there would be a gain made through the purchased puts.
However, if the price increases, it would translate into a loss because of the written calls. The
possible profit or loss is approximately equal to what the outcome would be if an individual short
sold a stock.
The synthetic short stock offers two important advantages. One, there is a lot to be leveraged,
and two, the stock brings in a lot of dividends. Once the stock is short sold and it generates
dividend, the stakeholders are entitled to their share of the dividend. However, stocks under
synthetic short position don’t require the seller to distribute a dividend to shareholders.
********** 4 **********
````

## 2024-25 · Re-Exam · Sem 10 · Answer key · paper 6a7cef103035

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_10/Re-Exam/MBATech_IT_7041/Financial Engineering/ANS_Financial Engineering(703TF0E012)_2024-2025.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 01 Jul 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (Comp)/MBA. Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: V/Sem 10 Re-exam(Exam Year: 2024-2025)
Subject: Financial Engineering
Date: 01 Jul 2025   Time: 10:00 am to 12:00 pm (02:00 Hrs.)
Max. Marks: 50
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
8. Scientific calculator/ finance calculators are allowed
Q1
a.   Profit /
Type of   Strike spot   Exercised   Loss per   Total profit
Sl.no option   price   price   / Lapse   share   /Loss   Marks
1 Buy Call   550   600 Exercised   -15   -9000   0.5
2 Buy Call   550   500 lapsed   -65   -39000   0.5
3   Sell Put   2000   2500 lapsed   50   30000   1
4   Sell Put   2000   1500 Exercised   -550   -330000   1
Total profit / Loss   -348000   1
b.   year cashflows   PVF   PVCF
1   60   0.925926 55.55555556
2   60   0.857339 51.44032922
3   60   0.793832 47.62993446
4   60   0.73503 44.10179117
5   60   0.680583 40.83499182
6   60   0.63017 37.81017761
7   60   0.58349 35.00942372
8   1060   0.540269 572.6850176
PV of bond 885.0672211
(3 marks)
c.   Floating rate borrower has risk when the interest rate rises.
Therefor buy FRA which means borrow in FRA to hedge itself from rising interest rate risk.
Borrowing will be at ask rate – 6.7%.
Fixed rate lending @ 8%
Margin locked in % p.a = 8% - 6.7% = 1.3% p.a.   (3 marks)
Q2   In 6 months ₹ 100 @ 15% will be = 100*15%*6/12 = 7.5 + 100 = 107.5
In 10 months ₹100 @ 18% will be = 100*18%*10/12 = 15 +100 = 115.
Theoretical 6 X 10 FRA = (115-107.5) / 107.5* 12/4 *100 = 20.93%
Quoted 6 X 10 FRA = 22/23% which is higher than theoretical FRA
********** 1 **********
--- page 2 ---
Hence Arbitrage opportunity exists.   (3 marks)
Therefore, invest at 6X 10 FRA and borrow $ 1000000 for 10 months at 18% p.a
Borrow 1 million USD at 18%   (1 mark)
Amount to be repaid after 10 months = 10,00,000 * 18%*10/12 = $1,50,000+ $ 1000000 =
$11,50,000.   (2 marks)
Invest the borrowed 1 million at present for 15% for 6 months = 1000000*15%*6/12 = 75,000
Reinvest the amount received after 6 months in FRA at 22% (bid rate)
= (1000000+75000)*22%*4/12 = 78833.33$
Amount received after 10th month = 1000000+75000+78833.33 = 1153833.33 $(3 marks)
Therefore, Arbitrage gain = 1153833.33 -1150000 = $3,833.33 per 1mio $.   (1 mark)
Q3   Hedge for Exporter
Short Hedge.
1
Amount to be hedged =   88000000   marks
Number of contracts in future   1
market =   9778 marks
Long hedge created in Fututre
market
Particulars   1$ = 85   1$ = 89   1$ = 95   Marks
In future market
Short 9778 *100 $ at 90 / $   88002000 88002000 88002000   1
Long in the month of December   -   -   -
2025   83113000 87024200 92891000   1
Net gain / loss in future market   4889000   977800 -4889000   1
Short in Spot market in December   83113000 87024200 92891000   1
Total cash outflow from hedged lots 88002000 88002000 88002000   1
Cash outflow from unhedged lots   1887000   1975800   2109000   2
Total cash outflow in December   89889000 89977800 90111000   1
Q4   8 marks
Spot   Long 2 Calls   Long put
prices   1100 @ 10   1100 @ 5   strategy
Premium   Profit /   Premium   Profit /   profit/
IV   paid   Loss   IV   received   Loss   loss
800   0   -10   -20   300   -5   295   275
850   0   -10   -20   250   -5   245   225
900   0   -10   -20   200   -5   195   175
950   0   -10   -20   150   -5   145   125
1000   0   -10   -20   100   -5   95   75
1050   0   -10   -20   50   -5   45   25
********** 2 **********
--- page 3 ---
1100   0   -10   -20   0   -5   -5   -25
1150   50   -10   80   0   -5   -5   75
1200   100   -10   180   0   -5   -5   175
1075   0   -10   -20   25   -5   20   0
Break- even point = 1075.   (2 marks)
Q5   Duration of portfolio = Wa X Da + Wb X Db
5   = Wa X 6 + (1-Wa) X 3
5   = 6Wa + 3 -3Wa
2   = 3 Wa
Wa = 2/3   and Wb =1-Wa = 1/3.   (2 marks)
The amount to be invested in each bond = 1000000*2/3 = 6,66,667 in Bond A and 3,33,333
(1000000-666667) in Bond B.   (2 marks)
No of Bond A to be bought = 666667 /986.5 = 676 bonds   (3 marks)
No of Bond B to be bought = 333333/1035 =323 bonds   (3 marks).
Q6a. Loan taken on 1st Jan 2025
Interest payable on 30th June 2025, 31st December 2025, 30th June 2026 and 31st December
2026.
Interest   Interest Cap   interest   Receipt from cap
payable   rate   option   payable   option   net cost
30-Jun-25   7% lapsed   7000   0   7000
31-Dec-25   12% exercised   12000   5000   7000
30-Jun-26   5% lapsed   5000   0   5000
31-Dec-26   9% exercised   9000   2000   7000
(5 marks)
Q6   A swaption, also known as a swap option, refers to an option to enter into an interest
rate swap or some other type of swap. In exchange for an option's premium, the buyer gains the
b.
right but not the obligation to enter into a specified swap agreement with the issuer on a
specified future date.
Swaptions are over-the-counter contracts and are not standardized, like equity options or
futures contracts. Thus, the buyer and seller need to both agree to the price of the swaption, the
time until expiration of the swaption, the notional amount and the fixed/floating rates.
(1 mark)
Payer Swaption
A payer swaption gives the holder the right, but not the obligation, to enter into a swap as the
fixed-rate payer and the float and the floating rate receiver. When it comes to the payer
swaption, the entity benefits when it anticipates a rise in interest rates. By entering the swap,
the payer locks in the ability to pay a fixed rate while receiving a potentially higher floating rate
that adjusts with rising rates.   (2 marks)
Receiver Swaption
On the other hand, a receiver swaption gives the holder the right to enter into a swap as the
fixed rate receiver and the floating rate payer. The structure works well when the holder expects
interest rates to fall. The holder will receive a higher fixed interest rate while paying a lower
floating rate that decreases with the market rate. This option is often used by pension funds and
insurance companies that require stable, predictable income streams and would like to capitalize
on favorable rate adjustments.   (2 marks)
Q7   • Repo is an abbreviation for the Repurchase Option Agreement. It is a contract between the
buyer and seller of the debt instrument, promising that the seller will repurchase the
a.
instrument after the specified period of time. It requires the seller to repurchase securities
at a higher price than the price at which it was actually sold.
********** 3 **********
--- page 4 ---
•   So, the difference in the amounts paid by the buyer of securities (at the time of buying) and
the seller of securities (at the time of repurchasing) is termed the repo rate. It helps the
seller of securities to raise short-term funds.
• To influence short-term interest levels, generally, RBI conducts Repo transactions. The tool is
used to manage excess liquidity in the monetary system.
•   Further, Repo/Reverse Repo transaction takes place between parties approved by the RBI
and that too in the securities approved by RBI, such as Government of India and State
Government Securities, Treasury Bills, FI Bonds, Corporate Bonds, PSU Bonds, etc.
Q7   A synthetic position is a trading option used to simulate the features of another comparable
position. More specifically, a synthetic position is created to simulate a similar reward or risk
b.
profile as that of a comparable position.   (1 mark)
1. Synthetic Long Stock   (2 marks)
The synthetic long stock position involves emulating the potential results of owning actual stock
by using trade options. To develop one, an individual needs to buy at the stock money calls and
then record at money puts of an equivalent stock.
The price paid at the calls is earned by the money received once puts are written, meaning that if
the stock fails to increase in price, there would be no loss or gain. Ideally, it is almost the same
as holding stock.
On the other hand, if stock prices increase, the money calls would generate a profit, and if the
price decreases, then the puts would transform into a loss. The likely profit or loss is essentially
equal to owning the stock.
The benefit, in this case, comes from the accruing leverage. The capital obligation needed when
creating a synthetic position is less than when purchasing an equivalent stock.
2. Synthetic Short Stock   (2 marks)
The synthetic short stock position is equivalent to short-selling existing stock. However, the
position uses options only. Creating such a position calls for writing on relevant stocks at the
money calls. Afterward, the same stock is bought at the money puts.
In case the stock does not increase in price, the outcome is considered neutral. The capital base
needed to purchase puts is recovered once calls are written. Thus, if the price of the stock drops,
there would be a gain made through the purchased puts.
However, if the price increases, it would translate into a loss because of the written calls. The
possible profit or loss is approximately equal to what the outcome would be if an individual short
sold a stock.
The synthetic short stock offers two important advantages. One, there is a lot to be leveraged,
and two, the stock brings in a lot of dividends. Once the stock is short sold and it generates
dividend, the stakeholders are entitled to their share of the dividend. However, stocks under
synthetic short position don’t require the seller to distribute a dividend to shareholders.
********** 4 **********
````
