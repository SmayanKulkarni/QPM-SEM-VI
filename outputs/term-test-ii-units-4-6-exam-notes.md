# Quantitative Portfolio Management - Term Test II Exam Notes

Syllabus coverage target: Unit 4, Unit 5, Unit 6 (as provided).
Source base: Files present in UNIT 4, UNIT 5, UNIT 6 folders.
Generated on: 2026-04-28.

## Sources Used
- UNIT 4/1 Naïve Diversification.pptx
- UNIT 4/2 Scientific Diversification.pptx
- UNIT 4/3 Measuring_risk_contributions.pptx
- UNIT 4/4 What is a Risk Budget.docx
- UNIT 4/5 Risk Budgeting Numericals.pptx
- UNIT 4/6 Simplified Risk Parity Portfolios.pptx
- UNIT 4/7 Full Risk Parity Portfolios.pptx
- UNIT 4/8 Shrinkage Estimators.pptx
- UNIT 4/9 EWMA (Exponentially Weighted Moving Average).pptx
- UNIT 4/10 Rolling Covariance Windows.pptx
- UNIT 4/11 Comparing optimization & diversification approaches_ Empirical comparison.pptx
- UNIT 5/1 Limits of Diversification.pptx
- UNIT 5/2 CPPI.pptx
- UNIT 5/2.1 CPPI_Numericals.pptx
- UNIT 5/_3 Analysis_ Simulating CPPI using GBM, Monte Carlo evaluation, Analyzing performance, drawdowns, floor violations, Designing and calibrating CPPI strategies (light, conceptual).pptx
- UNIT 6/1 Portfolio revision.ppt (image-based deck OCR)
- UNIT 6/2 Sharpe, Treynor and Jensen.docx
- UNIT 6/2.1 sharpe-treynor-and-jenson-sum.pdf
- UNIT 6/2.2 Numericals Sharpe, Treynor, Jensen.pdf
- UNIT 6/3 Foreign Exchange Risk.pdf
- UNIT 6/4 Bond Strategy.pptx
- UNIT 6/4 Hedging.pptx
- UNIT 6/5 Active vs passive bond portfolio management.docx

---

## Unit 4: Portfolio Optimization in Practice

### 4.1 Diversification and Optimization Methods

#### Naive Diversification (1/N Rule)
Definition:
- Equal capital allocation across all selected assets, without explicit risk-return-correlation modeling.

Core formula:
- Weight per asset = 1 / N.

Worked examples from slides:
- Example shown with 5 stocks and INR 1,00,000 gives 20 percent each. (Source: UNIT 4/1 Naïve Diversification.pptx, Slide 4)
- OCR numerical: 4-stock equal-weight return computation shown as 11 percent. (Source: UNIT 4/1 Naïve Diversification.pptx, Image OCR from slides 16-18)
- OCR numerical: INR 3,00,000 in 5 securities gives INR 60,000 each; portfolio return shown as 11 percent and total return INR 33,000. (Source: UNIT 4/1 Naïve Diversification.pptx, Image OCR from slides 19-21)

Advantages highlighted:
- Simple implementation, low complexity, robust under estimation uncertainty, behavioral comfort for beginners. (Source: UNIT 4/1 Naïve Diversification.pptx, Slides 6-8)

Limitations highlighted:
- Ignores risk heterogeneity and correlations, possible scalability and transaction-cost issues, may not match investor-specific risk profile. (Source: UNIT 4/1 Naïve Diversification.pptx, Slide 9)

Behavioral-bias linkage:
- Simplicity bias, 1/N heuristic bias, overconfidence, regret aversion, choice overload are explicitly tied to naive diversification decisions. (Source: UNIT 4/1 Naïve Diversification.pptx, Slides 10-12)

#### Scientific Diversification
Definition:
- Analytical diversification based on expected return, variance or standard deviation, covariance, and correlation.

Key principles:
- Prefer low or negative correlation combinations to reduce portfolio risk.
- Construct efficient combinations rather than random equal splits.

Conceptual mapping:
- Linked to Modern Portfolio Theory and efficient portfolio construction. (Source: UNIT 4/2 Scientific Diversification.pptx, Slides 2-8)

Advantages:
- Better risk-return tradeoff, reduced unsystematic risk, more stable long-run construction logic.

Limitations:
- Data and model dependence, sensitivity to changing market regimes, computational and skill burden for small investors.

Applications:
- Sector diversification, asset-class diversification, international diversification, long-term planning, performance optimization. (Source: UNIT 4/2 Scientific Diversification.pptx, Slides 18-20)

### 4.2 Risk-Based Approaches

#### Measuring Risk Contributions
Purpose:
- Identify each asset's contribution to total portfolio risk for rebalancing and diversification control.

Measures and formulas:
- Marginal Contribution to Risk, MCR_i = Cov(R_i, R_p) / sigma_p.
- Total Risk Contribution, TRC_i = w_i x MCR_i.
- Proportional Risk Contribution, PRC_i = TRC_i / sigma_p.

Numerical patterns in slides:
- Asset A and B examples compute MCR, TRC, PRC with interpretation that higher covariance and weight generally raise risk contribution.
- Case study with Equity, Bond, Commodity fund computes contributions and percentage shares to diagnose concentration.

Important exam note:
- Slide examples include PRC values that do not always sum neatly to 100 percent in displayed arithmetic; use the formula sequence consistently in exam calculations.

(Source: UNIT 4/3 Measuring_risk_contributions.pptx, Slides 9-23)

#### Risk Budgeting
Concept:
- Allocate total risk budget across assets or strategies rather than allocating only capital.

Operational components from document:
- Risk appetite, risk tolerance, risk capacity, periodic review, resource allocation, and risk identification-assessment workflow.

Risk-budgeting process steps:
- Risk identification.
- Risk assessment (qualitative and quantitative).
- Set tolerance and appetite.
- Allocate resources.
- Review and adjust.

(Source: UNIT 4/4 What is a Risk Budget.docx, Paras 35-47)

Finance-specific applications:
- Portfolio construction, performance attribution, dynamic asset allocation, sovereign and pension contexts.

(Source: UNIT 4/4 What is a Risk Budget.docx, Paras 48-58)

Numericals covered:
- Risk contribution = Weight x Volatility.
- Total risk = sum of risk contributions.
- Percentage risk budget = contribution / total risk x 100.
- Example set includes equity-bond-commodity decomposition and target-vs-actual risk budget comparison with rebalance recommendation.

(Source: UNIT 4/5 Risk Budgeting Numericals.pptx, Slides 2-16)

#### Simplified Risk Parity Portfolios
Definition:
- Approximate equal-risk allocation using inverse volatility weights.

Core method:
- Compute 1/sigma_i for each asset.
- Normalize by total inverse-volatility sum.

Observed allocation behavior:
- Lower-volatility assets receive higher capital weights.

OCR case outputs include:
- 3-asset, 4-asset, and investment-amount conversion examples.
- Comparative case versus equal-weight portfolio showing risk-parity weighted toward lower-volatility assets.

(Source: UNIT 4/6 Simplified Risk Parity Portfolios.pptx, Slides 7-12 and OCR slides 13-27)

#### Full Risk Parity Portfolios
Definition:
- Equalize exact risk contributions by considering both volatility and cross-asset correlations.

Key equations from OCR content:
- Portfolio variance = w^T Sigma w.
- Asset risk contribution = w_i (Sigma w)_i.
- Full risk parity condition aims for equal risk contributions across assets.

Case-study structure:
- Variance decomposition into variance terms plus covariance terms.
- Portfolio standard deviation computed from variance.
- Interpretation emphasizes diversification from imperfect correlations.

(Source: UNIT 4/7 Full Risk Parity Portfolios.pptx, Slides 2-8 and OCR slides 9-18)

### 4.3 Covariance Estimation (Brief)

#### Shrinkage Estimators
Definition:
- Blend sample estimate and stable target estimate.

Formula:
- Sigma_shrink = lambda T + (1-lambda) S.

Interpretation of lambda:
- lambda closer to 1 gives more target weight and greater stability.
- lambda closer to 0 stays closer to sample and data-driven estimate.

Applications stated:
- Portfolio optimization, VaR and risk management, factor covariance estimation, high-dimensional settings with many assets and limited observations.

Numerical OCR examples:
- S=0.10, T=0.06 gives 0.092 at lambda=0.2 and 0.068 at lambda=0.8.
- S=0.12, T=0.05, lambda=0.3 gives 0.099.

(Source: UNIT 4/8 Shrinkage Estimators.pptx, Slides 3-10 and OCR slides 12, 14, 16)

#### EWMA (Exponentially Weighted Moving Average)
Definition:
- Volatility-covariance updating with heavier emphasis on recent observations.

EWMA update forms shown:
- Variance update: sigma_t^2 = lambda sigma_{t-1}^2 + (1-lambda) r_{t-1}^2.
- Covariance update analog uses return product term.

Use cases:
- Dynamic volatility estimation, variance-covariance updates, VaR, risk budgeting, dynamic allocation.

Limitations stated:
- Lambda selection subjectivity, weaker long-history memory, can lag structural breaks, reactive nature.

Numerical OCR examples:
- Previous variance 0.04, return 10 percent, lambda 0.94 gives 0.0382.
- Lambda comparison 0.94 versus 0.80 gives 0.0382 versus 0.034.
- Portfolio variance case computes updated variances and covariance and then portfolio variance near 0.03185.

(Source: UNIT 4/9 EWMA (Exponentially Weighted Moving Average).pptx, Slides 2-11, 20-21 and OCR slides 3, 13, 15, 17, 19, 22, 23)

#### Rolling Covariance Windows
Definition:
- Compute covariance over fixed moving windows (for example 3-day, 30-day, 60-day), then roll window forward.

Why used:
- Time-varying relationships, regime-shift detection, dynamic risk estimation and hedging updates.

Advantages:
- Simple and transparent; adaptable window length.

Limitations:
- Window-size subjectivity, lag in abrupt shocks, equal within-window weighting, potential instability in short windows.

Numerical OCR examples:
- 3-day rolling windows with explicit covariance calculations and increasing co-movement interpretation.

(Source: UNIT 4/10 Rolling Covariance Windows.pptx, Slides 2, 4-10, 11, 20-21 and OCR slides 12-26)

### 4.4 Comparing Optimization and Diversification Approaches (Empirical)
Meaning:
- Real-data performance comparison across optimization-based and diversification-based portfolio construction.

Findings highlighted in source:
- Naive 1/N often performs similarly to or better than optimization under estimation error.
- Optimization can produce concentrated or extreme weights, improving expected return but potentially increasing concentration risk.

Case OCR example:
- Naive equal-weight expected return shown as 11.34 percent.
- Optimization portfolio expected return shown as 12.20 percent.
- Interpretation notes higher return but higher concentration in top-weight asset.

(Source: UNIT 4/11 Comparing optimization & diversification approaches_ Empirical comparison.pptx, Slides 2-6 and OCR slides 7-10)

---

## Unit 5: Beyond Diversification - Portfolio Insurance and CPPI

### 5.1 Limits of Diversification
Coverage from deck:
- Diversification lowers but does not eliminate risk.
- Failure conditions include systematic-risk dominance, high correlations, over-diversification, and global integration effects.
- Correlation breakdown in stress periods (panic, liquidity crunch, herd behavior, flight to safety) can collapse diversification benefits.
- Empirical episodes cited: 2008 GFC, COVID-19 crash, emerging-market co-movement under global shocks.

Exam-ready conclusion from source:
- Diversification protects mainly against unsystematic risk; combine with risk management and hedging for stress scenarios.

(Source: UNIT 5/1 Limits of Diversification.pptx, Slides 2-8)

### 5.2 CPPI Concept, Floor, Cushion, Multiplier, and Strategy Behavior
Definition:
- Dynamic strategy that allocates between risky and safe assets to protect a floor while retaining upside participation.

Core equations:
- Cushion = Portfolio Value - Floor.
- Risky allocation = Multiplier x Cushion.

Mechanism:
- Rising market increases cushion and risky allocation.
- Falling market reduces cushion and shifts capital to safe assets.

Merits:
- Capital-protection framework, rule-based dynamic allocation, upside participation.

Demerits and constraints:
- Gap risk under sudden crashes, high rebalancing costs, multiplier dependence, inflation non-protection in real terms.

CPPI versus buy-and-hold:
- Covered as explicit comparison in slides (dynamic protection focus versus static exposure behavior).

Drawdown-constraint design:
- Floor relative to peak: Floor = (1 - drawdown percent) x Peak.
- Example in source demonstrates floor breach under overnight crash despite CPPI reallocation logic.

(Source: UNIT 5/2 CPPI.pptx, Slides 2, 4-5, 8-12, 13, 15-20 and OCR slides 1, 3, 6, 7)

### 5.3 CPPI Simulation and Strategy Analysis
#### Numericals and path-wise updates
From CPPI_Numericals deck:
- Basic allocation at INR 10,00,000 with floor INR 8,00,000 and m=3 yields risky INR 6,00,000 and safe INR 4,00,000.
- After +10 percent risky move, risky allocation increases to INR 7,80,000.
- After -20 percent move, risky allocation drops to INR 2,40,000.
- Drawdown-constrained case with peak and drawdown limit converts to floor and updated allocation.

(Source: UNIT 5/2.1 CPPI_Numericals.pptx, Slides 2-15)

#### Simulating CPPI with GBM and Monte Carlo style evaluation concepts
From analysis deck:
- Multi-period case tracks allocation shifts, floor checks, and performance interpretation.
- Stress case with aggressive multiplier and large crash shows floor violation and post-violation loss lock-in effect.
- Drawdown analysis case computes period-wise drawdown and maximum drawdown.
- GBM-based downward scenario OCR includes shock term interpretation and resulting reduced risky allocation after loss.

Critical strategy design insight in source:
- CPPI is sensitive to multiplier calibration and crash-gap conditions.
- Better in gradual declines; vulnerable to discontinuous drops.

(Source: UNIT 5/_3 Analysis_ Simulating CPPI using GBM, Monte Carlo evaluation, Analyzing performance, drawdowns, floor violations, Designing and calibrating CPPI strategies (light, conceptual).pptx, Slides 2-6, 11-16, 21 and OCR slides 7-10, 17-20)

---

## Unit 6: Portfolio Revision, Evaluation, FX Risk, Bond Portfolio Strategies

### 6.1 Portfolio Revision
Recovered via OCR from image-based legacy deck.

Meaning:
- Portfolio revision is periodic adjustment of existing portfolio mix because market conditions and investor circumstances change.

Objective:
- Same as selection objective: maximize return for given risk or minimize risk for given return.

Need factors explicitly listed:
- Market changes since original construction.
- Investor-side changes: additional funds, changed risk tolerance, changed goals, liquidity need.

Constraints:
- Transaction costs and taxes can limit frequent revisions.

Revision strategies:
- Active revision strategy with frequent substantial adjustments based on analysis and timing.
- Passive revision strategy with infrequent adjustments via predetermined rules or formula plans.

Management framing:
- Active management linked with forecasting and timing.
- Passive management linked with index-like replication logic.

(Source: UNIT 6/1 Portfolio revision.ppt, OCR Pages 2-12)

### 6.2 Portfolio Evaluation (Sharpe, Treynor, Jensen)

Definitions and framing:
- Sharpe: reward to total risk (uses standard deviation).
- Treynor: reward to systematic risk (uses beta).
- Jensen alpha: actual return minus CAPM-implied expected return component.

Formulas present in source materials:
- Sharpe ratio: (R_p - R_f) / sigma_p.
- Treynor ratio: (R_p - R_f) / beta_p.
- Jensen framework appears in CAPM-based form with alpha as differential return.

Comparative table details:
- Developed by: William Sharpe, Jack Treynor, Michael Jensen.
- Common aliases include reward-to-variability, reward-to-volatility, and alpha.

Numerical practice included:
- Jensen ranking of 3 portfolios from given return-beta-risk-free-market inputs.
- Sharpe and Treynor rankings for multiple funds from given return, sigma, beta data.
- Additional OCR numerical practice in the 2.2 PDF (multiple illustrations).

(Source: UNIT 6/2 Sharpe, Treynor and Jensen.docx, Table and OCR images; UNIT 6/2.1 sharpe-treynor-and-jenson-sum.pdf, Pages 1-2; UNIT 6/2.2 Numericals Sharpe, Treynor, Jensen.pdf, OCR pages 1-5)

### 6.3 Foreign Exchange Risk in Global Portfolios

Definition:
- FX risk is uncertainty in foreign-currency transaction value due to exchange-rate movement.

Three core exposures covered:
- Transaction risk: contract-to-settlement exchange-rate risk affecting realized cash flows.
- Translation risk: accounting conversion effects on statements of foreign operations.
- Economic risk: long-term competitive and cash-flow impact from currency changes.

Examples in source:
- Exporter receivable value loss when invoiced currency weakens.
- Translation loss in reported net assets when subsidiary currency depreciates.
- INR appreciation reducing INR-converted earnings for USD-earning firms.

Measurement and mitigation themes:
- Monitor exchange-rate fluctuations, market volatility, macro-political factors.
- Hedging via forwards, futures, options, natural hedging, diversification of currency exposure, derivatives.
- Case narrative includes Toyota-style multinational exposure management through layered hedges.

(Source: UNIT 6/3 Foreign Exchange Risk.pdf, Text Pages 3-5 and OCR pages 1-14)

### 6.4 Bond Portfolio Management Strategies

#### Duration-style maturity-structure strategies
From bond strategy slides:
- Bullet: concentration around a specific maturity target, simple but less flexible and more point-yield-curve exposure.
- Barbell: concentration at short and long maturities while skipping middle maturities.
- Ladder: stagger maturities across horizon with rollover to maintain broad, stable maturity exposure.

Exam interpretation:
- Bullet gives target-date focus.
- Barbell balances liquidity and duration exposure with curve-view expression.
- Ladder emphasizes smoother maturity distribution and reduced reinvestment concentration.

(Source: UNIT 6/4 Bond Strategy.pptx, Slides 2, 4, 6, 8 and OCR slides 3, 5, 7, 9)

#### Hedging basics linked to global portfolios
From hedging deck:
- Hedging as insurance-like risk reduction, not elimination.
- Instruments and approaches in OCR: forwards, futures, money market tools, asset allocation structure, options, currency-related hedges.
- Advantages include loss mitigation and flexibility; risks include cost and imperfect hedge effectiveness.
- Slide 11 directly links currency-risk measurement to improved decision quality and hedging design.

(Source: UNIT 6/4 Hedging.pptx, Slides 2-4, 11 and OCR slides 5-10)

#### Active vs Passive Bond Portfolio Management
Table-based comparison:
- Objective: outperformance versus benchmark matching.
- Strategy: frequent trading versus buy-and-hold.
- Risk and cost: generally higher for active.
- Turnover and skill requirement: higher for active, lower for passive.
- Suitability: aggressive investors versus conservative investors.

(Source: UNIT 6/5 Active vs passive bond portfolio management.docx, Table 1)

---

## Image and Document Coverage Log

Image and visual-material extraction performed for all available Unit 4-6 files.

File-level image coverage counts:
- UNIT 4/1 Naïve Diversification.pptx: 9 images extracted, OCR snippets used.
- UNIT 4/10 Rolling Covariance Windows.pptx: 14 images extracted, OCR snippets used.
- UNIT 4/11 Comparing optimization & diversification approaches_ Empirical comparison.pptx: 4 images extracted, OCR snippets used.
- UNIT 4/4 What is a Risk Budget.docx: 1 image extracted, OCR snippet used.
- UNIT 4/5 Risk Budgeting Numericals.pptx: 1 image extracted, OCR snippet used.
- UNIT 4/6 Simplified Risk Parity Portfolios.pptx: 17 images extracted, OCR snippets used.
- UNIT 4/7 Full Risk Parity Portfolios.pptx: 10 images extracted, OCR snippets used.
- UNIT 4/8 Shrinkage Estimators.pptx: 4 images extracted, OCR snippets used.
- UNIT 4/9 EWMA (Exponentially Weighted Moving Average).pptx: 9 images extracted, OCR snippets used.
- UNIT 5/2 CPPI.pptx: 4 images extracted, OCR snippets used.
- UNIT 5/_3 Analysis_ Simulating CPPI using GBM, Monte Carlo evaluation, Analyzing performance, drawdowns, floor violations, Designing and calibrating CPPI strategies (light, conceptual).pptx: 8 images extracted, OCR snippets used.
- UNIT 6/1 Portfolio revision.ppt: OCR performed page-wise on 12 page images.
- UNIT 6/2 Sharpe, Treynor and Jensen.docx: 5 images extracted, OCR snippets used.
- UNIT 6/2.2 Numericals Sharpe, Treynor, Jensen.pdf: 5 images extracted, OCR snippets used.
- UNIT 6/3 Foreign Exchange Risk.pdf: 11 images extracted, OCR snippets used.
- UNIT 6/4 Bond Strategy.pptx: 5 images extracted, OCR snippets used.
- UNIT 6/4 Hedging.pptx: 7 images extracted, OCR snippets used.

No topic from the provided Unit 4-6 syllabus was skipped in this notes set.
