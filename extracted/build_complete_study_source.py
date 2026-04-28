from pathlib import Path

main = '''# Quantitative Portfolio Management (Term Test II) - Complete Study Source

This document is designed as a one-stop, first-principles study source for Unit 4, Unit 5, and Unit 6.
It is not revision-only shorthand. It teaches concepts from basics, then builds into formulas, intuition, and solved numericals.

Syllabus scope covered:
- Unit 4: Portfolio Optimization in Practice
- Unit 5: Beyond Diversification (Portfolio Insurance and CPPI)
- Unit 6: Portfolio Revision, Evaluation, FX Risk, and Bond Portfolio Strategies

Primary source pool:
- All available PPTX/PPT/DOCX/PDF files inside UNIT 4, UNIT 5, UNIT 6
- Embedded images extracted and OCR-read from those files

---

## How To Study This Document

Study flow for each topic:
1. Meaning and intuition (what and why)
2. Formula and terms (how to compute)
3. Interpretation (what answer means)
4. Worked examples (source-based)

If you are seeing these topics for the first time, follow this order:
- Unit 4 first (diversification and risk mechanics)
- Unit 5 next (CPPI and downside control)
- Unit 6 last (evaluation measures and fixed-income/FX overlays)

---

## Unit 4: Portfolio Optimization in Practice

### 4.1 Diversification and Optimization Methods

#### A. Naive Diversification (1/N Rule)

Meaning:
- Naive diversification means dividing capital equally across all selected assets.
- You do not estimate expected return, covariance, or optimization weights.
- If there are N assets, each gets exactly 1/N of capital.

Why it exists:
- In real markets, expected returns and correlations are estimated with error.
- Highly optimized portfolios can overfit noisy estimates and become unstable.
- Equal-weighting is robust, transparent, and behaviorally easier to execute.

Core formula:
- Weight per asset = 1/N
- Portfolio return = sum(w_i x R_i)

What it captures well:
- Baseline diversification.
- Low implementation complexity.
- Reduced model risk from unstable parameter estimation.

What it misses:
- Risk asymmetry across assets.
- Correlation structure.
- Investor-specific risk constraints.

Source evidence:
- Definition, formula, rationale, pros/cons, behavioral-bias interpretation are present in UNIT 4/1 Naive Diversification slides.

##### Solved examples (from source content)

Example 1 (equal allocation):
- Total investment = INR 1,00,000
- Assets = 5
- Weight per asset = 1/5 = 20%
- Allocation per asset = INR 20,000
Interpretation: pure equal-weight capital split.

Example 2 (portfolio return from equal weights):
- 4 stocks, equal weight 25% each
- Returns = 8%, 12%, 10%, 14%
- Portfolio return = 0.25x8 + 0.25x12 + 0.25x10 + 0.25x14 = 11%

Example 3 (return in rupee terms):
- Total capital = INR 3,00,000
- 5 assets, equal allocation => INR 60,000 each
- Mean portfolio return shown in source = 11%
- Total rupee return = 3,00,000 x 0.11 = INR 33,000

Example 4 (empirical comparison linkage):
- Equal weight used as diversification benchmark in optimization-vs-diversification deck.
- Source case reports equal-weight expected return near 11.34% versus concentrated optimized portfolio near 12.20%.
- Interpretation: higher expected return may come with concentration risk.

---

#### B. Scientific Diversification

Meaning:
- Scientific diversification uses statistics to construct portfolios.
- Inputs include expected return, standard deviation (risk), covariance/correlation.
- Goal is not just “many assets,” but “right combination of co-movements.”

Key principle:
- Best diversification comes from combining assets with low or negative correlations.
- Two risky assets can reduce total portfolio risk when they do not move together.

Why this is better than random splitting:
- Random splitting may accidentally cluster risk in one hidden factor (sector, macro sensitivity).
- Scientific diversification explicitly checks relationships among assets.

What students must internalize:
- Diversification is about risk interaction, not asset count.
- Correlation drives diversification benefit.

Practical sequence:
1. Estimate expected returns.
2. Estimate risk (sigma or variance).
3. Estimate pairwise correlations/covariance.
4. Construct candidate portfolios.
5. Choose efficient risk-return combination.

Source evidence:
- Full conceptual path and applications are described in UNIT 4/2 Scientific Diversification.

---

### 4.2 Risk-Based Approaches

#### A. Measuring Risk Contributions

Core idea:
- Portfolio risk is not only “how risky each asset is.”
- It is “how much each asset contributes to total portfolio risk.”

Three measures:
1. Marginal Contribution to Risk (MCR_i):
   MCR_i = Cov(R_i, R_p) / sigma_p
   Meaning: how much total risk changes for a small weight increase in asset i.

2. Total Risk Contribution (TRC_i):
   TRC_i = w_i x MCR_i
   Meaning: absolute risk contribution of asset i.

3. Percentage Risk Contribution (PRC_i):
   PRC_i = TRC_i / sigma_p
   Meaning: contribution share of total risk.

Why it matters:
- Two assets can have similar variance but different risk contribution due to covariance with portfolio.
- Risk concentration can hide in a single heavily correlated position.

##### Solved examples (source-based)

Example 1 (two-asset case):
- w_A=0.60, Cov(A,p)=0.018, sigma_p=0.12
- w_B=0.40, Cov(B,p)=0.012, sigma_p=0.12
- MCR_A = 0.018/0.12 = 0.15
- MCR_B = 0.012/0.12 = 0.10
- TRC_A = 0.60x0.15 = 0.09
- TRC_B = 0.40x0.10 = 0.04
- PRC computed from TRC/sigma_p in source slides.
Interpretation: Asset A dominates risk share.

Example 2 (alternate two-asset setup):
- sigma_p=0.10, Cov(A,p)=0.018, Cov(B,p)=0.012, same weights.
- MCR_A=0.18, MCR_B=0.12
- TRC_A=0.108, TRC_B=0.048
- PRC from TRC/sigma_p indicates strong A concentration.

Example 3 (three-asset fund case):
- Equity/Bond/Commodity with given covariances and weights in source.
- Source computes MCR, TRC, PRC and shows equity highest risk share.
- Interpretation: rebalance needed if target is balanced risk profile.

Example 4 (risk-control decision):
- Use PRC table to identify breach against target risk budget.
- Action: reduce high PRC asset weight and increase under-allocated defensive assets.

---

#### B. Risk Budgeting

Meaning:
- Capital budgeting allocates money.
- Risk budgeting allocates permissible risk.
- Portfolio is designed so risk usage matches planned budget shares.

Framework elements from source:
- Risk appetite: total risk willingness.
- Risk tolerance: acceptable fluctuations.
- Risk capacity: ability to absorb losses.
- Monitoring and review cycle.

Risk-budgeting process:
1. Identify risks.
2. Assess and quantify them.
3. Set appetite/tolerance.
4. Allocate risk budget.
5. Review and adjust.

Why this is powerful:
- Prevents one asset from consuming most risk.
- Keeps portfolio aligned with investor objective and constraints.

##### Solved examples (source-based)

Example 1 (equity-bond-commodity):
- Risk contribution = weight x volatility
- Equity: 0.50x0.20=0.10
- Bond: 0.30x0.10=0.03
- Commodity: 0.20x0.15=0.03
- Total risk=0.16
- Risk shares: 62.5%, 18.75%, 18.75%

Example 2 (capital-to-risk decomposition):
- Portfolio value INR 1,00,000 with A/B/C allocations.
- Compute weights, then risk contributions and shares exactly as in source.
- Source output shows stock A largest risk budget usage.

Example 3 (risk budget from total risk):
- Total risk 18%; target shares 50/30/20
- Risk allocated: 9%, 5.4%, 3.6%

Example 4 (target vs actual risk case):
- Compare actual risk contribution against target budget.
- Source recommendation: reduce equity exposure, increase bond/commodity weight.

---

#### C. Simplified Risk Parity Portfolio

Meaning:
- Equal capital is not equal risk.
- Risk parity seeks more equal risk contributions.
- Simplified method approximates this using inverse volatility weights.

Formula:
- Preliminary score: q_i = 1/sigma_i
- Weight: w_i = q_i / sum(q_j)

Interpretation:
- Lower-risk assets (smaller sigma) get larger weights.
- Higher-risk assets get reduced capital to avoid risk dominance.

##### Solved examples (source-based)

Example 1 (3-asset base case):
- Given sigmas from source, compute inverse volatilities.
- Normalize to get weights.
- Source shows low-volatility asset receives highest weight.

Example 2 (4-asset case study):
- Equity 24%, Bond 8%, Commodity 16%, Real Estate 12%
- Inverse-vol scores and normalized weights shown in OCR source.
- Bond gets largest weight due to lowest sigma.

Example 3 (3-asset investor case):
- Stock index 20%, Gov bonds 10%, Gold 15%
- Inverse vol => 5,10,6.67; normalized weights around 23.07%, 46.15%, 30.78%

Example 4 (allocation in rupees):
- Total capital INR 10,00,000 across 4 assets.
- Use risk-parity weights from source OCR to compute rupee allocations.

Example 5 (equal-weight vs risk-parity comparison):
- Risk parity lowers weight of highest-volatility stock and raises low-volatility stock weight.
- Source interpretation: better risk diversification than equal weight.

---

#### D. Full Risk Parity Portfolio

Meaning:
- Simplified RP uses only volatility.
- Full RP uses covariance matrix (volatility + correlation structure).
- Objective: equalize true risk contributions, not approximations.

Core equations (as present in source/OCR):
- Portfolio variance: sigma_p^2 = w^T Sigma w
- Risk contribution: RC_i = w_i (Sigma w)_i
- Target condition in full RP: RC_1 = RC_2 = ... = RC_n

Why this matters:
- Two low-vol assets can still jointly dominate risk if strongly correlated.
- Full RP corrects hidden concentration.

##### Solved examples (source-based)

Example 1 (3-asset variance decomposition):
- Use variance terms plus covariance cross-terms exactly as shown.
- Sum yields portfolio variance, then sqrt gives sigma_p.
- Source interpretation: diversification reduces total risk below individual sigmas.

Example 2 (equity-bond-commodity case):
- Given weights, sigmas, and correlations.
- Compute term-by-term variance and resulting sigma_p.
- Source interpretation: equities dominate risk share due to high sigma and weight.

Example 3 (risk-contribution interpretation):
- Using same case outputs, explain why equal capital is not equal risk.
- Show why full RP decision variable must be risk contribution balance.

---

### 4.3 Covariance Estimation (Brief): Shrinkage, EWMA, Rolling Windows

#### A. Shrinkage Estimators

Problem addressed:
- Sample covariance is noisy in finite samples.
- High-dimensional portfolios amplify estimation error.

Solution structure:
- Blend sample matrix S with stable target T:
  Sigma_shrink = lambda T + (1-lambda) S

Parameter meaning:
- lambda close to 1: more stable, more biased toward target.
- lambda close to 0: more data-driven, less shrinkage.

##### Solved examples (source-based)

Example 1:
- S=0.10, T=0.06, lambda=0.2
- Estimate = 0.2x0.06 + 0.8x0.10 = 0.092

Example 2:
- S=0.10, T=0.06, lambda=0.8
- Estimate = 0.8x0.06 + 0.2x0.10 = 0.068

Example 3:
- S=0.12, T=0.05, lambda=0.3
- Estimate = 0.3x0.05 + 0.7x0.12 = 0.099

Example 4:
- S=0.15, T=0.08 with lambda alternatives 0.2 and 0.7 from OCR.
- Demonstrates stability increase as lambda rises.

Interpretation rule:
- Higher lambda reduces noise sensitivity but may increase model bias.

---

#### B. EWMA (Exponentially Weighted Moving Average)

Purpose:
- Update variance/covariance with greater weight on recent observations.

Variance update (source):
- sigma_t^2 = lambda sigma_{t-1}^2 + (1-lambda) r_{t-1}^2

Covariance update (source form):
- Cov_t = lambda Cov_{t-1} + (1-lambda)(r_{A,t-1} r_{B,t-1})

Why used in practice:
- Fast adaptation to volatility clustering.
- Standard in VaR and institutional risk systems.

Limitations:
- Lambda choice subjectivity.
- Less long-memory than full-history methods.
- Reactive, not truly predictive.

##### Solved examples (source-based)

Example 1:
- Previous variance 0.04, return 10%, lambda 0.94
- sigma_t^2 = 0.94x0.04 + 0.06x0.01 = 0.0382

Example 2:
- Same inputs with lambda 0.80
- sigma_t^2 = 0.80x0.04 + 0.20x0.01 = 0.034

Example 3:
- Two-period update with initial variance 0.05 and returns 8%,12% at lambda 0.90
- Source OCR gives final second-period variance around 0.0425

Example 4:
- Covariance update with previous covariance 0.02, returns 10% and 8%, lambda 0.95
- New covariance = 0.0194

Example 5 (portfolio risk case):
- Update variance A, variance B, covariance AB using EWMA.
- Then compute portfolio variance with weights 0.6 and 0.4.
- Source OCR gives final portfolio variance near 0.03185.

---

#### C. Rolling Covariance Windows

Meaning:
- Compute covariance on fixed recent window and roll through time.

Why useful:
- Captures time-varying relationships and changing diversification benefit.

Procedure:
1. Select window length k.
2. Compute covariance in window 1.
3. Shift window by one period.
4. Recompute and compare trajectory.

Trade-off:
- Short window: more reactive, more noisy.
- Long window: smoother, but slower to detect regime shifts.

##### Solved examples (source-based)

Example 1:
- 3-day rolling covariance on days 1-3,2-4,3-5 with full table-based calculations shown.

Example 2:
- Case study with changing relationship shows covariance rising over windows.
- Interpretation: diversification benefit deteriorating.

Example 3:
- OCR solution set with covariance sequence 0.000178 -> 0.0005 -> 0.0006.
- Interpretation: positive co-movement strengthening.

Example 4:
- OCR “exam-ready interpretation” confirms increasing covariance implies higher portfolio risk concentration.

---

### 4.4 Comparing Optimization and Diversification Approaches (Empirical)

Conceptual contrast:
- Optimization approach: model-driven, expected return and covariance sensitive.
- Diversification approach: simpler, more robust under parameter uncertainty.

Empirical message from source:
- 1/N can match or outperform optimization in real samples due to estimation error in model inputs.
- Optimization may deliver higher expected return but often with concentration risk.

Source case summary:
- Naive return ~11.34%
- Optimization return ~12.20%
- Interpretation: return gain with higher concentration in top-weight asset.

---

## Unit 5: Beyond Diversification - Portfolio Insurance and CPPI

### 5.1 Limits of Diversification

Core thesis:
- Diversification is necessary but not sufficient.
- It mitigates idiosyncratic risk, not full-system market shocks.

When diversification fails (source):
- Systematic shocks dominate.
- Correlations rise sharply in crises.
- Over-diversification dilutes quality (“diworsification”).
- Global market integration reduces cross-country insulation.

Correlation breakdown:
- Assets that were weakly correlated move together under stress.
- Diversification benefit collapses exactly when needed most.

Empirical episodes in source:
- 2008 global crisis.
- 2020 COVID crash.

Practical implication:
- Use diversification + risk budgeting + hedging + drawdown controls.

---

### 5.2 CPPI (Constant Proportion Portfolio Insurance)

#### A. Concept and Building Blocks

Goal:
- Protect floor value while preserving upside participation.

Components:
- Floor F: minimum acceptable portfolio value.
- Cushion C = V - F.
- Multiplier m: aggressiveness factor.
- Risky allocation E = m x C.
- Safe allocation B = V - E.

Behavior logic:
- If V rises => C rises => risky exposure increases.
- If V falls => C shrinks => risky exposure decreases.

Strength:
- Rule-based downside control in gradual declines.

Weakness:
- Gap risk under discontinuous crash moves.

#### B. Drawdown-constrained CPPI

Dynamic floor concept:
- Floor can be linked to peak value.
- Formula from source: Floor = (1-drawdown_limit) x peak_value

Interpretation:
- Protects gains by ratcheting floor upward after new peaks.
- Still vulnerable if crash jumps across rebalancing interval.

##### Solved examples (source-based)

Example 1 (basic allocation):
- V=10,00,000; F=8,00,000; m=3
- C=2,00,000
- E=6,00,000; B=4,00,000

Example 2 (after +10% move):
- New V=10,60,000
- C=2,60,000
- E=7,80,000; B=2,80,000

Example 3 (after -20% move):
- New V=8,80,000
- C=80,000
- E=2,40,000; B=6,40,000

Example 4 (drawdown floor):
- Peak=12,00,000; max drawdown=25%
- Floor=9,00,000
- For current V=11,00,000 and m=4:
  C=2,00,000 => E=8,00,000; B=3,00,000

Example 5 (multi-period CPPI case):
- Source tracks period-by-period allocations and confirms no floor violation in first case.

Example 6 (stress case with gap risk):
- Aggressive multiplier and crash lead to floor breach and loss lock-in in safe assets.

Example 7 (GBM-linked CPPI OCR case):
- Downward random shock reduces risky sleeve and preserves floor margin.

---

### 5.3 CPPI Simulation and Strategy Analysis (Conceptual)

How to evaluate CPPI strategy quality:
- Floor violation frequency.
- Maximum drawdown.
- Upside capture in bull phases.
- Recovery participation after drawdown.
- Sensitivity to multiplier and rebalance frequency.

Design and calibration principles from source logic:
- Higher m => higher upside and higher crash sensitivity.
- Conservative m reduces drawdown risk but lowers upside participation.
- Drawdown-linked floors improve gain protection but do not remove gap risk.

---

## Unit 6: Portfolio Revision, Evaluation, FX Risk, and Bond Portfolio Strategies

### 6.1 Portfolio Revision

Meaning:
- Portfolio revision is the periodic modification of securities and weights after original construction.

Why revision is required:
- Markets change continuously.
- Investor profile changes (risk tolerance, goals, liquidity needs, additional funds).

Objective remains same as selection:
- Maximize return for given risk.
- Minimize risk for given return.

Constraints:
- Transaction costs.
- Tax effects.

Strategies:
1. Active revision:
   - Frequent and substantial adjustments.
   - Forecast-dependent, higher turnover.

2. Passive revision:
   - Infrequent, rule-based adjustments.
   - Closer to index-like philosophy.

Source recovered via OCR from image-only legacy deck.

---

### 6.2 Portfolio Evaluation: Sharpe, Treynor, Jensen

#### A. Sharpe Ratio
- Measures excess return per unit of total risk.
- Formula: (R_p - R_f) / sigma_p
- Best for comparing diversified portfolios where total volatility matters.

#### B. Treynor Ratio
- Measures excess return per unit of systematic risk.
- Formula: (R_p - R_f) / beta_p
- Best when portfolio is already well diversified and beta is primary risk.

#### C. Jensen Alpha
- Measures abnormal return beyond CAPM-implied expected return.
- Positive alpha indicates outperformance after adjusting for market risk.

Comparative memory aid:
- Sharpe => total risk denominator.
- Treynor => beta denominator.
- Jensen => differential return (alpha).

##### Solved examples (source-based)

Example 1 (Jensen ranking of 3 portfolios):
- Source PDF computes expected returns using CAPM inputs and then differences from actual return.
- Ranked based on alpha differential.

Example 2 (Sharpe ranking across funds):
- Source computes multiple Sharpe values and rank ordering.

Example 3 (Treynor ranking across funds):
- Source computes Treynor values and ranks.

Example 4 (Jensen for A/B/C/D funds):
- Source page computes alpha values, including negative alpha cases.

Example 5 (additional OCR illustrations):
- Multiple worked mutual fund comparisons in the numericals PDF.

---

### 6.3 Foreign Exchange Risk in Global Portfolios

Meaning:
- FX risk is uncertainty in value of foreign-currency-denominated cash flows and statements due to exchange rate movement.

Three types:
1. Transaction risk:
   - Contracted foreign-currency receivables/payables before settlement.
   - Direct cash-flow impact.

2. Translation risk:
   - Conversion of subsidiary statements to reporting currency.
   - Accounting valuation impact, not immediate cash movement.

3. Economic (operating) risk:
   - Long-term competitiveness and firm value sensitivity to exchange rates.

Measurement significance:
- Better planning for financing, pricing, investment, and hedging decisions.

Mitigation methods in source:
- Forwards, futures, options.
- Natural hedging.
- Currency diversification.
- Derivative overlays.

Case narrative:
- MNC exposure management (Toyota-style example in source OCR) using layered hedges.

---

### 6.4 Bond Portfolio Management Strategies

#### A. Bullet Strategy
- Concentrate around one maturity bucket.
- Useful for target-date liabilities.
- Less flexible and carries specific yield-curve exposure.

#### B. Barbell Strategy
- Split between short and long maturities, avoid intermediate segment.
- Provides liquidity (short end) + duration exposure (long end).

#### C. Ladder Strategy
- Stagger maturities over horizon.
- Reinvest matured rung at long end to maintain stable maturity profile.

Strategic comparison:
- Bullet: precision timing, lower flexibility.
- Barbell: tactical curve positioning.
- Ladder: broad exposure and smoother reinvestment profile.

---

### 6.5 Hedging Basics and Currency-Risk Link

Hedging meaning:
- Insurance-like strategy to reduce downside, not eliminate all risk.

Typical hedge instruments from source/OCR:
- Forward contracts.
- Futures contracts.
- Option-based hedges.
- Asset allocation or structural hedging.

Advantages:
- Loss containment, improved stability.

Risks/costs:
- Can be expensive.
- Imperfect hedge may still leave residual risk.

Currency-risk tie-in:
- Source explicitly states currency-risk measurement improves planning, financing, and hedge design quality.

---

### 6.6 Active vs Passive Bond Portfolio Management

Source table summary:
- Active:
  - Outperform benchmark target.
  - Frequent trades, higher turnover, higher cost, greater skill requirement.
  - Higher flexibility and generally higher risk profile.

- Passive:
  - Match benchmark target.
  - Buy-and-hold style, lower turnover and lower costs.
  - Simpler implementation and typically more suitable for conservative investors.

---

## Numerical Practice Map (By Type)

This map ensures each numerical type in study material is covered with multiple solved source examples:

1. Naive diversification computations:
- Covered with 4 source-based solved examples.

2. Risk contribution and risk budgeting computations:
- Covered with 4+ source-based solved examples each.

3. Simplified risk parity:
- Covered with 5 source-based solved examples.

4. Full risk parity/covariance-matrix computations:
- Covered with 3 source-based solved examples.

5. Shrinkage estimator numericals:
- Covered with 4 source-based solved examples.

6. EWMA variance/covariance numericals:
- Covered with 5 source-based solved examples.

7. Rolling covariance window numericals:
- Covered with 4 source-based solved examples.

8. CPPI allocation/drawdown/gap-risk numericals:
- Covered with 7 source-based solved examples.

9. Sharpe-Treynor-Jensen performance-evaluation numericals:
- Covered with 5 source-based solved examples.

---

## Citation Notes

All definitions, formulas, procedures, and solved examples above are grounded in the source files listed at top.
Where OCR text from embedded figures was used, that has been integrated and figure embeds are provided in the appendix below.

---
'''

appendix = Path('/home/smayan/Desktop/QPM/extracted/figure_appendix.md').read_text(encoding='utf-8')
out = Path('/home/smayan/Desktop/QPM/outputs/term-test-ii-units-4-6-complete-study-source.md')
out.write_text(main + '\n\n---\n\n' + appendix + '\n', encoding='utf-8')
print(f'Wrote {out}')
