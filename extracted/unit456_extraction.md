# Unit 4-6 Extraction Snapshot (2026-04-28)
- Tesseract available: True

## UNIT 6/1 Portfolio revision.ppt
- Type: conversion
- Conversion status: conversion-command-ran-no-output

## UNIT 4/1 Naïve Diversification.pptx
- Type: pptx
- Slides extracted: 22
- Images extracted: 9
- Slide 1 text: Naïve Diversification
- Slide 2 text: Naïve Diversification (1/N Rule) is a simple investment strategy where an investor divides their money equally among all available assets in a portfolio.
Meaning
If there are N assets, the investor allocates 1/N of the total investment to each asset, without analyzing risk, return, or correlation.
S
- Slide 3 text: ‹#› | Formula
Weight of each asset=1/N
Where:
N = Total number of assets in the portfolio
- Slide 4 text: ‹#› | Example
Suppose an investor has ₹1,00,000 and wants to invest in 5 stocks.
Using the 1/N rule: 1/5=20% | Each stock gets equal allocation.
- Slide 5 text: ‹#› | Why it is called "Naïve"
It is called naïve because:
It does not consider risk
It does not consider expected returns
It does not consider correlations between assets
It simply splits money equally.
- Slide 6 text: Key Takeaways
Naive diversification is dividing an investment portfolio simply and by instinct rather than relying on complex mathematical models.
Optimized, or sophisticated, diversification, on the other hand, utilizes complex mathematical formulas to diversify a portfolio.
Sophisticated diversifi
- Slide 7 text: When to Use the 1/N Rule
Despite its name, the 1/N rule is not "stupid." It is a highly effective strategy in specific contexts:
Asset Allocation: When deciding between broad asset classes (e.g., US Stocks, International Stocks, Bonds, Real Estate), 1/N is often superior to trying to time the market
- Slide 8 text: Advantages of the 1/N Rule
Simplicity: It is easy to understand and implement without complex financial models. This reduces the barrier to entry for novice investors.
Low Cost: It requires less frequent rebalancing than complex strategies that demand constant monitoring. This saves time and reduces
- Slide 9 text: Disadvantages of the 1/N Rule
Ignores Risk Profiles: It treats a stable utility stock the same as a volatile tech startup. A risk-averse investor might prefer a weighted approach that aligns with their tolerance.
Scalability Issues: If you have 1,000 assets available, putting 0.1% into each is impra
- Slide 10 text: Role of Behavioural Biases in Naïve Diversification

Naïve diversification (1/N rule) occurs when investors divide their investment equally among all available assets instead of analyzing risk, return, or correlation. This behavior is often influenced by behavioural biases, which are psychological t

## UNIT 4/10 Rolling Covariance Windows.pptx
- Type: pptx
- Slides extracted: 27
- Images extracted: 14
- Slide 1 text: Rolling Covariance Windows
- Slide 2 text: Meaning | Rolling covariance windows refer to calculating covariance between two assets using a fixed-size moving time window (e.g., last 30 days, 60 days, etc.).
👉 Instead of using all historical data, we:
Take a subset (window) of recent data
Calculate covariance
Move the window forward (rolling) 
- Slide 3 text: 
- Slide 4 text: Importance in Portfolio Management | 1. Captures Time-Varying Relationships
Asset relationships are not constant over time. Rolling windows help track how covariance changes with market conditions. This leads to more realistic portfolio analysis.
2. Focus on Recent Data
It gives importance to recent
- Slide 5 text: Applications in Portfolio | 1. Portfolio Variance Calculation
Used to compute portfolio risk
Updated covariance → updated variance 
🔸 2. Portfolio Optimization
Helps in Mean-Variance Optimization
Adjusts asset weights dynamically
- Slide 6 text: Applications in Portfolio | 3. Risk Management
Identifies when diversification benefits reduce
Useful in volatile markets
🔸 4. Hedging Strategies
Helps determine hedge ratios
Adjusts hedging as relationships change
🔸 5. Algorithmic Trading
Used in trading models
Detects short-term relationships betw
- Slide 7 text: Advantages of Rolling Covariance Windows | 1. Easy to Understand and Implement
Rolling covariance uses a simple moving window concept, making it easy to apply. It does not require complex mathematical models or assumptions. This simplicity makes it suitable for both students and practitioners.

2. R
- Slide 8 text: Advantages of Rolling Covariance Windows | 4. Flexible Window Size
The window size can be adjusted based on the investor’s needs. A shorter window captures short-term trends, while a longer window captures smoother patterns. This flexibility allows customization for different strategies.

5. Useful 
- Slide 9 text: Limitations of Rolling Covariance Windows | 1. Choice of Window Size is Subjective
There is no universally correct window size for all situations. Different window lengths can produce different covariance results. This subjectivity can affect consistency and comparability of analysis.

2. Sudden Cha
- Slide 10 text: Limitations of Rolling Covariance Windows | 4. Can be Unstable with Small Window
A small window uses fewer observations, making estimates more volatile. Minor changes in data can significantly affect covariance values. This instability may lead to unreliable portfolio decisions.

5. Equal Weight to 

## UNIT 4/11 Comparing optimization & diversification approaches_ Empirical comparison.pptx
- Type: pptx
- Slides extracted: 11
- Images extracted: 4
- Slide 1 text: Comparing Optimization & Diversification Approaches: Empirical
Comparison
- Slide 2 text: 1. Meaning | An empirical comparison between optimization and diversification approaches involves analyzing real-world data to evaluate how different portfolio construction strategies perform in terms of risk, return, and stability.
Two common approaches compared are:
Optimization Approach (e.g., Me
- Slide 3 text: 2. Optimization Approach | The optimization approach constructs portfolios using mathematical models to achieve the best possible risk-return combination.
Example: Mean–Variance Optimization selects portfolio weights that maximize expected return for a given level of risk.
Characteristics
Uses expe
- Slide 4 text: 3. Diversification Approach | The diversification approach spreads investments across assets to reduce overall risk without complex optimization.
Examples:
Naïve Diversification (1/N rule) – Equal investment in all assets.
Risk Parity – Equal risk contribution across assets.
Characteristics
Simple
- Slide 5 text: 4. Empirical Comparison
- Slide 6 text: Empirical Findings in Studies | 1. Naïve Diversification (1/N Rule) Often Performs Similarly or Better
Empirical studies using historical market data show that the 1/N rule often performs as well as or better than optimization models.
This is because optimization models depend on estimated inputs li
- Slide 7 text: 
- Slide 8 text: 
- Slide 9 text: 
- Slide 10 text: 

## UNIT 4/2 Scientific Diversification.pptx
- Type: pptx
- Slides extracted: 22
- Images extracted: 0
- Slide 1 text: Scientific Diversification
- Slide 2 text: Scientific Diversification is a systematic and analytical method of spreading investments among different securities in order to reduce risk and maximize return. It is based on financial theories, statistical calculations, and correlation analysis, rather than simple equal allocation.
This concept 
- Slide 3 text: 1. Meaning
Scientific diversification means selecting securities based on their risk, return, and correlation with other securities so that the overall portfolio risk is minimized without reducing expected return.
Instead of randomly investing in many assets, the investor scientifically analyzes rel
- Slide 4 text: 2. Key Principle
The main idea is:
Do not put money in assets that move in the same direction.
When assets behave differently, loss in one asset can be offset by gain in another.
This depends on **Correlation between securities.
Positive correlation (+1) → securities move in the same direction
Negat
- Slide 5 text: Features of Scientific Diversification 
1. Based on Statistical Analysis (Variance, Standard Deviation, Covariance) Scientific diversification uses statistical tools to measure the risk and return of different securities. Variance and standard deviation help in understanding how much the returns of
- Slide 6 text: 3. Focuses on Optimal Portfolio Construction Scientific diversification aims to create an optimal portfolio that provides the best possible return for a given level of risk. Investors analyze different combinations of securities to find the most efficient mix. The goal is to achieve maximum return 
- Slide 7 text: Steps in Scientific Diversification 
1. Estimate Expected Returns of Securities The first step is to estimate the expected return of each security in which investment is possible. Expected return represents the average return that an investor anticipates from a particular investment in the future. 
- Slide 8 text: 3. Analyze Correlation Between Securities Correlation analysis helps determine how the returns of two securities move in relation to each other. Securities with low or negative correlation are preferred because they reduce overall portfolio risk. If one security performs poorly, another may perform
- Slide 9 text: 5. Example
Suppose an investor invests in:
IT sector stock
Pharma sector stock
Banking sector stock
If IT sector falls, pharma may rise, balancing the portfolio. Because different sectors react differently to economic conditions.
- Slide 10 text: Advantages of Scientific Diversification

1. Reduces Unsystematic Risk Scientific diversification helps in reducing unsystematic risk, which is the risk related to a particular company or industry. By investing in securities from different sectors, the negative performance of one security can be ba

## UNIT 4/3 Measuring_risk_contributions.pptx
- Type: pptx
- Slides extracted: 24
- Images extracted: 0
- Slide 1 text: Measuring Risk Contributions
- Slide 2 text: Meaning of Risk Contribution | Measuring Risk Contribution refers to the process of determining how much each asset in a portfolio contributes to the total risk of the portfolio.
It helps investors understand which investments are responsible for increasing or reducing the overall portfolio risk. By
- Slide 3 text: Why Measuring Risk Contribution is Important | 1. Risk Management Measuring risk contribution helps investors identify which assets are adding the most risk to the portfolio. This allows them to monitor and control the overall level of risk more effectively. As a result, investors can take correcti
- Slide 4 text: Why Measuring Risk Contribution is Important | 5. Performance Analysis Risk contribution analysis helps evaluate how each asset affects the overall portfolio performance. Investors can see whether an asset is contributing too much risk relative to its return. This helps in making better investment 
- Slide 5 text: Measuring Risk Contributions – Advantages and Disadvantages
- Slide 6 text: Practical Applications of Measuring Risk Contributions | 1. Portfolio Risk Management Measuring risk contributions helps investors identify which assets contribute the most to the overall portfolio risk. By understanding this, investors can control and manage the total risk level of the portfolio. 
- Slide 7 text: Practical Applications of Measuring Risk Contributions | 3. Better Diversification Risk contribution analysis shows whether the portfolio risk is concentrated in a few assets or spread across many assets. Investors can adjust the asset allocation to avoid excessive concentration of risk. This impro
- Slide 8 text: Practical Applications of Measuring Risk Contributions | 5. Strategic Asset Allocation Measuring risk contributions helps investors decide the appropriate allocation among different asset classes such as stocks, bonds, and commodities. By understanding how each asset contributes to risk, investors 
- Slide 9 text: Types of Risk Contribution Measures | 1. Marginal Contribution to Risk (MCR)
2. Total Risk Contribution (TRC)
3. Percentage Risk Contribution (PRC)
- Slide 10 text: Marginal Contribution to Risk (MCR) | Measures how portfolio risk changes when asset weight changes slightly

Formula:
MCRᵢ = Cov(Rᵢ , Rₚ) / σₚ

## UNIT 4/4 What is a Risk Budget.docx
- Type: docx
- Paragraphs extracted: 92
- Tables extracted: 0
- Images extracted: 1
- Para: What is a Risk Budget? Process, Components, Benefits
- Para: Table of Contents
- Para: What Is Risk Budgeting?
- Para: What is the Purpose of a Risk Budget?
- Para: Components of Risk Budgeting
- Para: Risk Budgeting Process
- Para: Applications of Risk Budgeting in Finance
- Para: Challenges and Limitations of Risk Budgeting
- Para: What are the benefits of risk budgeting?
- Para: Conclusion
- Para: The ever-increasing market competition, changing technologies, and multiple other factors have increased the volatility in many ways. So, no matter which domain you work in, you should always expect the unexpected. However, this should not stop you from taking risks! All it takes is a balance betwee
- Para: What Is Risk Budgeting?

## UNIT 4/5 Risk Budgeting Numericals.pptx
- Type: pptx
- Slides extracted: 17
- Images extracted: 1
- Slide 1 text: Risk Budgeting
- Slide 2 text: Risk Budgeting – Meaning | Risk Budgeting is a portfolio management approach in which the total portfolio risk is allocated among different assets or investment strategies. Instead of allocating capital only, the investor allocates a specific portion of risk to each asset in the portfolio.
The main 
- Slide 3 text: Problem 1
A portfolio manager wants to allocate the risk budget among three assets. | Calculate the risk budget (risk contribution) of each asset.
- Slide 4 text: Step 1: Calculate Risk Contribution
Risk Contribution = Weight × Volatility | Equity = 0.50 × 0.20 = 0.10
Bonds = 0.30 × 0.10 = 0.03
Commodities = 0.20 × 0.15 = 0.03
- Slide 5 text: Step 2: Total Portfolio Risk
Total Risk = 0.10 + 0.03 + 0.03 = 0.16
- Slide 6 text: Step 3: Percentage Risk Budget | Equity = 0.10 / 0.16 × 100 = 62.5%
Bonds = 0.03 / 0.16 × 100 = 18.75%
Commodities = 0.03 / 0.16 × 100 = 18.75%
Interpretation
Equity contributes the largest share of risk to the portfolio.
- Slide 7 text: Problem 2
A portfolio manager allocates investments in three assets. | Total Portfolio Value = ₹1,00,000
Find
Weight of each asset in the portfolio
Risk Contribution of each asset
Total Portfolio Risk
Percentage Risk Budget (Risk Share) of each asset
- Slide 8 text: Step 1: Calculate Portfolio Weights
Weight = Investment / Total Portfolio Value | Stock A = 40,000 / 1,00,000 = 0.40
Stock B = 35,000 / 1,00,000 = 0.35
Stock C = 25,000 / 1,00,000 = 0.25
- Slide 9 text: Step 2: Calculate Risk Contribution
Risk Contribution = Weight × Volatility | Stock A = 0.40 × 0.25 = 0.10
Stock B = 0.35 × 0.15 = 0.0525
Stock C = 0.25 × 0.10 = 0.025
- Slide 10 text: Step 3: Total Portfolio Risk | Total Risk
= 0.10 + 0.0525 + 0.025
= 0.1775

## UNIT 4/6 Simplified Risk Parity Portfolios.pptx
- Type: pptx
- Slides extracted: 29
- Images extracted: 17
- Slide 1 text: Simplified Risk Parity Portfolios
- Slide 2 text: What is Risk Parity? | Risk Parity is a portfolio allocation strategy that assigns weights such that each asset contributes equally to the total portfolio volatility, rather than simply allocating equal capital to each asset. The goal is to prevent any single asset or asset class from dominating the
- Slide 3 text: Simplified Risk Parity Portfolio | A Simplified Risk Parity Portfolio is a portfolio allocation strategy where each asset contributes roughly equal risk to the portfolio.

Instead of investing equal money in each asset, the portfolio allocates more funds to low-risk assets and less to high-risk asse
- Slide 4 text: Importance of Simplified Risk Parity Portfolios | 1. Better Diversification Risk parity portfolios spread risk evenly across different assets rather than concentrating it in high-risk investments. This improves diversification because each asset contributes a similar level of risk to the portfolio.
- Slide 5 text: Simplified Risk Parity Portfolios – Merits and Demerits
- Slide 6 text: Real-Life Examples of Simplified Risk Parity Portfolios | 1. Stock–Bond Portfolio (Individual Investors) Many investors balance their portfolios between stocks and bonds using risk parity principles. Since stocks are more volatile than bonds, investors allocate less money to stocks and more to bond
- Slide 7 text: Formula | The simplified method assigns weights inversely proportional to volatility.

Where
Wi = Weight of asset i
σi​ = Standard deviation (risk) of asset i
n = Number of assets
Steps:
Find standard deviation of each asset.
Calculate inverse of volatility (1/σ).
Add all inverse values.
Divide eac
- Slide 8 text: Example 1
A portfolio manager wants to construct a simplified risk parity portfolio using three assets. The standard deviation (risk) of each asset is given below: | Required:
Calculate the portfolio weights of each asset using the Simplified Risk Parity method (inverse volatility method).
- Slide 9 text: Step 1: Calculate Inverse of Volatility
- Slide 10 text: Step 2: Sum of Inverse Values | 5+10+6.67=21.67

## UNIT 4/7 Full Risk Parity Portfolios.pptx
- Type: pptx
- Slides extracted: 19
- Images extracted: 10
- Slide 1 text: Full Risk Parity Portfolios
- Slide 2 text: 1. Meaning | A Full Risk Parity Portfolio is an advanced portfolio allocation strategy in which each asset contributes exactly the same amount of risk to the total portfolio.

Unlike simplified risk parity (which only uses volatility), the full risk parity approach considers both volatility and corr
- Slide 3 text: 2. Importance | 1. Accurate Risk Allocation Full risk parity measures the actual contribution of each asset to total portfolio risk by considering correlations. This leads to a more accurate and balanced portfolio structure.
2. Better Diversification Since correlations are considered, the portfoli
- Slide 4 text: Full Risk Parity Portfolios – Merits and Demerits
- Slide 5 text: Real-Life Examples of Full Risk Parity Portfolios | 1. Hedge Fund Risk Parity Strategies Many hedge funds implement full risk parity strategies by balancing risk across global equities, bonds, commodities, and currencies. They consider both volatility and correlation to calculate precise risk contr
- Slide 6 text: Difference Between Simplified Risk Parity Portfolios and Full Risk Parity Portfolios
- Slide 7 text: Difference Between Simplified Risk Parity Portfolios and Full Risk Parity Portfolios
- Slide 8 text: 3. Key Concept | Total portfolio risk depends on:
Asset weights
Volatility (standard deviation)
Correlation between assets
Full risk parity ensures:
Risk Contribution of Asset 1 = Risk Contribution of Asset 2 = Risk Contribution of Asset 3
- Slide 9 text: 
- Slide 10 text: 

## UNIT 4/8 Shrinkage Estimators.pptx
- Type: pptx
- Slides extracted: 17
- Images extracted: 4
- Slide 1 text: Shrinkage Estimators
- Slide 2 text: What Are Shrinkage Estimators? | Shrinkage estimators are widely used in finance to improve the accuracy of risk measurement and portfolio optimization, especially when dealing with many assets and limited data.

Shrinkage estimators are statistical techniques widely used in finance to improve the e
- Slide 3 text: In finance, shrinkage estimators combine:
The sample estimate (based on historical data)
A structured or target estimate (simpler and more stable)
to produce a more reliable estimate.
General formula:
Σshrink=λT+(1−λ)S   or  (λ × Target) + ((1-λ) × Sample)
Where:
S = Sample covariance matrix
T = Tar
- Slide 4 text: Example: | Sample return of a stock = 25% (very high)
Target return (market average) = 10%
Shrinkage intensity = 0.7 (70% toward target)
Shrunk Estimate = (0.7 × 10%) + (0.3 × 25%)
                = 7% + 7.5%
                = 14.5%
- Slide 5 text: Importance: Why Do We Need It? | In finance, we have a big problem: we never have enough data. | Shrinkage fixes this by reducing the influence of random noise and focusing on what's likely to be true.
- Slide 6 text: Major Applications in Finance | 1. Portfolio Optimization
Used in Modern Portfolio Theory (Markowitz model).
Helps:
Estimate better covariance matrix
Avoid extreme portfolio weights
Improve diversification
2. Risk Management
Shrinkage improves estimation of:
Portfolio volatility
Value at Risk (VaR)

- Slide 7 text: Major Applications in Finance | 3. Asset Allocation
Used by:
Mutual funds
Hedge funds
Pension funds
To build more stable long-term portfolios.
4. Factor Models
Shrinkage is used when estimating:
Factor covariance matrices
Market and sector risk exposures
5. High-Dimensional Finance Problems
Importan
- Slide 8 text: Advantages of shrinkage estimators in Financial Applications | 1. Reduces Noise in Financial Data
Financial data often contains random fluctuations that do not represent true relationships between assets. Shrinkage reduces this noise by combining the sample covariance with a stable target matrix. Th
- Slide 9 text: Limitations of shrinkage estimators in Financial Applications | 1. Depends on the Choice of Target Matrix
The effectiveness of shrinkage depends on selecting an appropriate target matrix. A poor choice may lead to inaccurate covariance estimates. Therefore, careful consideration is required while ch
- Slide 10 text: Popular Shrinkage Method in Finance | Ledoit–Wolf Shrinkage Estimator
This is the most widely used method.
It:
Automatically calculates optimal shrinkage intensity
Produces stable covariance matrix
Is used in many financial software and research papers.

## UNIT 4/9 EWMA (Exponentially Weighted Moving Average).pptx
- Type: pptx
- Slides extracted: 24
- Images extracted: 9
- Slide 1 text: EWMA
(Exponentially Weighted Moving Average)
- Slide 2 text: Meaning | EWMA is a method used to estimate volatility (risk) by giving more weight to recent data and less weight to older data.
👉 Unlike simple averages, EWMA assumes:
Recent market movements are more important
Older data gradually becomes less relevant
- Slide 3 text: Formula
- Slide 4 text: Importance of EWMA in Portfolio | 1. Captures Changing Market Risk
Financial markets are not constant
EWMA adjusts quickly to new volatility
2. More Realistic Than Simple Average
Simple average treats all data equally ❌
EWMA prioritizes recent information ✔️
3. Widely Used in Risk Models
Used in Val
- Slide 5 text: Applications in Portfolio Management | 1. Volatility Estimation
Estimate risk of individual assets
Helps in portfolio risk measurement
2. Portfolio Risk (Variance–Covariance Matrix)
EWMA is used to calculate:
Variance
Covariance between assets
👉 Important for:
Portfolio optimization
Risk budgeting
- Slide 6 text: Applications in Portfolio Management | 3. Value at Risk (VaR)
EWMA improves VaR accuracy
Reacts quickly to:
Market crashes
Sudden spikes
 4. Dynamic Portfolio Allocation
Investors adjust weights based on changing volatility
Helps in:
Reducing exposure during high risk
Increasing exposure in stable m
- Slide 7 text: Applications in Portfolio Management | 5. Risk Management Systems
Used by:
Banks
Hedge funds
Mutual funds
👉 Example:
If volatility rises → reduce risky assets
- Slide 8 text: Advantages of EWMA | 1. Simple to Use
EWMA is mathematically straightforward and easy to implement. It requires only the previous variance and latest return for calculation. This makes it practical for students as well as financial analysts.
2. Responds Quickly to Market Changes
EWMA gives higher we
- Slide 9 text: Advantages of EWMA | 4. Captures Volatility Clustering
Financial markets often show periods of high and low volatility grouped together. EWMA effectively captures this clustering effect. This improves the accuracy of short-term risk estimation.
5. Widely Accepted in Finance
EWMA is used by banks, fi
- Slide 10 text: Limitations of EWMA | 1. Ignores Long-Term Historical Patterns
EWMA gives very low weight to older data, almost ignoring it over time. This can lead to loss of valuable long-term trends and insights. As a result, it may not fully reflect structural market behavior.
2. Choice of λ (Lambda) is Subject

## UNIT 5/1 Limits of Diversification.pptx
- Type: pptx
- Slides extracted: 8
- Images extracted: 0
- Slide 1 text: Limits of Diversification
- Slide 2 text: Limits of Diversification | Diversification reduces risk by combining assets whose returns are not perfectly correlated. However, it does not eliminate all risk. Its effectiveness has clear limits.
- Slide 3 text: 1. When Diversification Fails | Diversification tends to fail under certain conditions:
🔹 a) Systematic Risk Dominance
Market-wide risks (interest rates, inflation, recession) affect all assets simultaneously
Cannot be diversified away
👉 Example: During a recession, most stocks decline together

🔹 b
- Slide 4 text: 1. When Diversification Fails | c) Over-diversification
Adding too many assets leads to:
Marginal reduction in risk
Lower returns due to inclusion of weak assets
👉 Known as “diworsification”
🔹 d) Global Integration
Financial markets across countries are increasingly interconnected
International dive
- Slide 5 text: 2. Correlation Breakdown | Meaning:
Correlation breakdown refers to a situation where:
Assets that were previously weakly correlated suddenly move together
🔥 Why it happens:
Panic selling
Liquidity crunch
Herd behavior
Flight to safety
📊 Impact:
Correlations move towards +1
Diversification benefits 
- Slide 6 text: 3. Empirical Evidence | Real-world observations support limits of diversification:

🔻 a) Global Financial Crisis 2008
Correlations across asset classes surged
Equities worldwide declined together
Even diversified portfolios suffered heavy losses

🔻 b) COVID-19 Market Crash 2020
Initial phase saw sim
- Slide 7 text: 3. Empirical Evidence | c) Emerging Markets Evidence
During global shocks, emerging markets move closely with developed markets
Reduces international diversification benefits
🔻 d) Research Findings
Studies show:
Correlation is not constant
It increases during market stress
Diversification works best
- Slide 8 text: Conclusion | Diversification is useful but not foolproof
Its effectiveness is limited by:
Market-wide shocks
Rising correlations
Behavioral factors
Investors must combine diversification with:
Risk management strategies
Hedging tools

## UNIT 5/2 CPPI.pptx
- Type: pptx
- Slides extracted: 23
- Images extracted: 4
- Slide 1 text: CPPI – Constant Proportion Portfolio Insurance
- Slide 2 text: Concept | CPPI is a dynamic portfolio strategy that:
Protects a minimum portfolio value (floor)
While allowing participation in upside market returns
👉 It allocates funds between:
Risky asset (equity)
Safe asset (bonds/cash)
- Slide 3 text: 
- Slide 4 text: Key Components of CPPI | 1️⃣ Floor (F)
Minimum value the portfolio should not fall below
Ensures capital protection
👉 Example: ₹10 lakh investment, floor = ₹8 lakh
2️⃣ Cushion (C)
Cushion = Portfolio Value – Floor
Represents risk-taking capacity
👉 Example: Portfolio = ₹10 lakh, Floor = ₹8 lakh Cus
- Slide 5 text: Key Components of CPPI | 3️⃣ Multiplier (m)
Determines aggressiveness of strategy
Higher multiplier → more exposure to risky assets
👉 Typical values: 2 to 5
4️⃣ Risky Asset Allocation
Investment in Risky Asset = m × Cushion
👉 Example: m = 3, Cushion = ₹2 lakh → Equity investment = ₹6 lakh → Remai
- Slide 6 text: 
- Slide 7 text: 
- Slide 8 text: How CPPI Works (Mechanism) | If market rises:
Portfolio value ↑ → Cushion ↑ → More investment in equity
If market falls:
Portfolio value ↓ → Cushion ↓ → Shift to safe assets
👉 Automatically adjusts risk exposure
- Slide 9 text: Merits of CPPI | 1️⃣ Capital Protection
CPPI ensures that the portfolio does not fall below a predefined floor value. It dynamically reduces exposure to risky assets when the market declines. This provides a safety net for investors.
2️⃣ Participation in Upside
The strategy allows investors to benef
- Slide 10 text: Merits of CPPI | 4️⃣ Flexibility through Multiplier
The multiplier allows customization based on investor risk appetite. A higher multiplier increases return potential but also risk. Thus, investors can tailor the strategy to their needs.
5️⃣ Simplicity of Concept
The basic CPPI formula (m × cushion

## UNIT 5/2.1 CPPI_Numericals.pptx
- Type: pptx
- Slides extracted: 16
- Images extracted: 0
- Slide 1 text: CPPI (Constant Proportion Portfolio Insurance) | Concept and Numericals

Cushion = Portfolio – Floor
Risky Investment = Multiplier × Cushion
- Slide 2 text: Numerical 1: Basic Allocation | Portfolio = ₹10,00,000
Floor = ₹8,00,000
Multiplier = 3
Find allocation in risky and safe assets.
- Slide 3 text: Numerical 1: Basic Allocation | Step 1: CushionCushion = 10,00,000 – 8,00,000 = ₹2,00,000
Step 2: Risky Asset Investment= 3 × 2,00,000 = ₹6,00,000
Step 3: Safe Asset Investment= 10,00,000 – 6,00,000 = ₹4,00,000

Final Answer:
Risky Asset = ₹6,00,000 
Safe Asset = ₹4,00,000
- Slide 4 text: Numerical 2: After Market Rise | 📌 Question:
Initial portfolio = ₹10,00,000Risky asset rises by 10%Safe asset unchangedUse same multiplier (3) and floor ₹8,00,000
Find new allocation.
- Slide 5 text: Solution: | Step 1: Initial Allocation (from previous)Risky = ₹6,00,000Safe = ₹4,00,000
Step 2: Value after riseRisky = 6,00,000 × 1.10 = ₹6,60,000Safe = ₹4,00,000
New Portfolio = ₹10,60,000

Step 3: New Cushion= 10,60,000 – 8,00,000 = ₹2,60,000

Step 4: New Risky Investment= 3 × 2,60,000 = ₹
- Slide 6 text: Numerical 3: After Market Fall | 📌 Question:
From Numerical 1, risky asset falls by 20%Find new allocation.
- Slide 7 text: Solution: | Step 1: Initial AllocationRisky = ₹6,00,000Safe = ₹4,00,000

Step 2: After fallRisky = 6,00,000 × 0.80 = ₹4,80,000Safe = ₹4,00,000
New Portfolio = ₹8,80,000
Step 3: Cushion= 8,80,000 – 8,00,000 = ₹80,000
Step 4: Risky Investment= 3 × 80,000 = ₹2,40,000
Step 5: Safe Investment= 
- Slide 8 text: Numerical 4: With Drawdown Constraint | 📌 Question:
Portfolio peak = ₹12,00,000Drawdown limit = 25%Current portfolio = ₹11,00,000Multiplier = 4
Find allocation.
- Slide 9 text: Solution: | Step 1: Floor (Drawdown based)= (1 – 0.25) × 12,00,000= 0.75 × 12,00,000 = ₹9,00,000
Step 2: Cushion= 11,00,000 – 9,00,000 = ₹2,00,000

Step 3: Risky Investment= 4 × 2,00,000 = ₹8,00,000

Step 4: Safe Investment= 11,00,000 – 8,00,000 = ₹3,00,000
✔️ Final Answer:
Risky Asset = ₹8,0
- Slide 10 text: Case Study | An investor adopts a Constant Proportion Portfolio Insurance (CPPI) strategy with an initial investment of ₹10,00,000. The investor sets a floor value of ₹8,00,000 and uses a multiplier of 3 to determine exposure to risky assets. The portfolio is divided between a risky asset (equity) a

## UNIT 5/_3 Analysis_ Simulating CPPI using GBM, Monte Carlo evaluation, Analyzing performance, drawdowns, floor violations, Designing and calibrating CPPI strategies (light, conceptual).pptx
- Type: pptx
- Slides extracted: 21
- Images extracted: 8
- Slide 1 text: Analysis: Simulating CPPI using GBM, Monte
Carlo evaluation, Analyzing performance, drawdowns, floor violations,
Designing and calibrating CPPI strategies (light, conceptual)
- Slide 2 text: Case Study: CPPI Strategy Evaluation | Case:
An investor adopts a CPPI strategy with the following details:
Initial Portfolio Value = ₹10,00,000
Floor Value = ₹8,00,000
Multiplier (m) = 3
The portfolio is reviewed over 3 periods:
- Slide 3 text: 👉 Assume safe asset gives 0% return.
Required:
Calculate allocation and portfolio value at each period
Analyze changes in risky exposure
Check if floor violation occurs
Comment on strategy performance
- Slide 4 text: Step 1: Initial Allocation
Cushion = 10,00,000 – 8,00,000 = ₹2,00,000 Risky Asset = 3 × 2,00,000 = ₹6,00,000 Safe Asset = 10,00,000 – 6,00,000 = ₹4,00,000

Step 2: Period 1 (+10%)
Risky = 6,00,000 × 1.10 = ₹6,60,000 Safe = ₹4,00,000
Total Portfolio = ₹10,60,000
New Cushion = 10,60,000 – 8,00,000 
- Slide 5 text: Step 3: Period 2 (–20%)
Risky = 7,80,000 × 0.80 = ₹6,24,000 Safe = ₹2,80,000
Total Portfolio = ₹9,04,000
Cushion = 9,04,000 – 8,00,000 = ₹1,04,000 New Risky = 3 × 1,04,000 = ₹3,12,000 Safe = 9,04,000 – 3,12,000 = ₹5,92,000
👉 Exposure reduced sharply
Step 4: Period 3 (+15%)
Risky = 3,12,000 × 1.15
- Slide 6 text: Step 5: Floor Violation Check
Lowest Portfolio Value = ₹9,04,000
Floor = ₹8,00,000
👉 No floor violation
Step 6: Analysis
CPPI increased exposure during rising markets (Period 1 & 3).
It reduced risky investment after losses (Period 2), protecting capital.
Portfolio never fell below floor → capital p
- Slide 7 text: 
- Slide 8 text: 
- Slide 9 text: 
- Slide 10 text: 

## UNIT 6/1 Portfolio revision.ppt
- Type: legacy_ppt_pdflike
- Pages extracted: 12
- Page images extracted: 12
- Page 1 text snippet: 
- Page 1 OCR snippet: Chapter 21 Portfolio Revision
- Page 2 text snippet: 
- Page 2 OCR snippet: Meaning of Portfolio Revision = In portfolio management, the maximum emphasis is placed on portfolio analysis and selection which leads to the construction of the optimal portfolio .portfolio revision is an important as 
- Page 3 text snippet: 
- Page 3 OCR snippet: LE = Portfolio revision involves changing the existing mix of securities .this may be effected either by changing the securities currently included in the portfolio or by altering the proportion of funds invested in the 
- Page 4 text snippet: 
- Page 4 OCR snippet: OO Objective of portfolio revision = The objective of portfolio revision is the same as the objective of portfolio selection, 1.e., maximization the return for a given level of risk or minimization the risk for a give fo
- Page 5 text snippet: 
- Page 5 OCR snippet: ee Need for Revision = The primary factor necessitating portfolio revision is changes in the financial markets since the creation of the portfolio . The need for portfolio revision may arise because of some investor rela
- Page 6 text snippet: 
- Page 6 OCR snippet: Constraints in Portfolio Revision 1}Transaction cost: Buying n selling of securities involve transaction costs such as commission and brokerage. Frequent buying and selling of securities for portfolio revision may push u
- Page 7 text snippet: 
- Page 7 OCR snippet: Two different strategies may be adopted for portfolio revision which are as follows: 1}Active Revision Strategy 2}Passive Revision Strategy
- Page 8 text snippet: 
- Page 8 OCR snippet: 1}Active Revision Strategy : =» Active revision strategy involves frequent and sometime substantial adjustment to the portfolio . = Active portfolio revision is essentially carrying out portfolio analysis and portfolio s

## UNIT 6/2 Sharpe, Treynor and Jensen.docx
- Type: docx
- Paragraphs extracted: 0
- Tables extracted: 1
- Images extracted: 5

## UNIT 6/2.1 sharpe-treynor-and-jenson-sum.pdf
- Type: pdf
- Pages extracted: 2
- Images extracted: 0
- Page 1 snippet: Q. 9. Following table provides the details about 3 portfolios. Find out the difference between the actual and expected return using Jensen index. On the basis of your calculation rank them. Portfolio Return on Portfolio Portfolio Beta Risk Free Interest Rate 1 15 1.3 6% 2 12 0.9 6% 3 18 1.6 6% Marke
- Page 2 snippet: Risk free rate of return is 4 per cent. Market return is 10 %. R −R Solution: Sharpe = p f σ p 2−4 Fund A: = = – 0.1 …(4) 20 12−4 Fund B: = = 0.44 …(1) 18 8−4 Fund C: = = 0 .18 …(3) 22 4−4 Fund D: = = 0.21 …(2) 24 R −R p f Treyner = B p 2−4 Fund A: = = – 2.04 …(4) 0.98 12−4 Fund B: = = 8.25 …(1) .97

## UNIT 6/2.2 Numericals Sharpe, Treynor, Jensen.pdf
- Type: pdf
- Pages extracted: 5
- Images extracted: 5
- Page 1 snippet: 
- Page 2 snippet: 
- Page 3 snippet: 
- Page 4 snippet: 
- Page 5 snippet: 

## UNIT 6/3 Foreign Exchange Risk.pdf
- Type: pdf
- Pages extracted: 14
- Images extracted: 11
- Page 1 snippet: 
- Page 2 snippet: 
- Page 3 snippet: 1. Transaction Risk • Arises from already agreed foreign currency contracts (imports/exports). • Exists between invoice date and settlement date. • Caused by exchange rate fluctuations during credit period. • Directly affects cash inflows and outflows. • Impacts profit margin on foreign trade transa
- Page 4 snippet: 2. Translation Risk (Risk when financial statements of foreign subsidiaries are converted into home currency) Explanation • Occurs when a company has foreign subsidiaries. • Financial statements must be converted into reporting currency. • Affects balance sheet and income statement values. • Does no
- Page 5 snippet: Economic Risk (Long-term impact of exchange rate changes on firm value and competitiveness) Explanation • Also called operating exposure. • Affects future cash flows and competitiveness. • Arises due to long-term currency movements. • Impacts pricing strategy, demand, and cost structure. • Difficult
- Page 6 snippet: 
- Page 7 snippet: 
- Page 8 snippet: 

## UNIT 6/4 Bond Strategy.pptx
- Type: pptx
- Slides extracted: 11
- Images extracted: 5
- Slide 1 text: 
- Slide 2 text: While there are numerous ways to attain long exposure, bullet, barbell and laddered strategies are the most common. Each has a distinctly different structure that should be considered when deciding between strategies.
- Slide 3 text: 
- Slide 4 text: Bullet – Specific Maturity Target
As the name suggests, a bullet strategy involves purchasing bonds with a specific maturity target. For instance, an investor might focus exclusively on one-year bonds, or only invest in twenty-year maturities. While this is one of the simplest strategies to execute,
- Slide 5 text: 
- Slide 6 text: Barbell – Skip the Middle | While barbell strategies come in all shapes and sizes, most involve allocating capital to shorter term maturities, avoiding intermediate and investing in long. The longer end of the barbell provides duration exposure and offers more certainty around future cash flows, whi
- Slide 7 text: 
- Slide 8 text: Ladder – Broad Exposure | In a laddered strategy, investors attempt to evenly distribute maturities across their investment horizon, providing exposure to short, intermediate and long bonds. When the shortest bond in the ladder (rung) matures, proceeds are reinvested into the longest end, keeping du
- Slide 9 text: 
- Slide 10 text: 

## UNIT 6/4 Hedging.pptx
- Type: pptx
- Slides extracted: 12
- Images extracted: 7
- Slide 1 text: Hedging
- Slide 2 text: What is Hedging? | To understand the hedging meaning in the stock market, simply consider it as a type of insurance. When people opt to hedge, they are protecting themselves against the financial effect of a negative event. This does not preclude all bad occurrences from occurring. However, if a bad
- Slide 3 text: What is Hedging in the Stock Market | Hedging is the purchase of one asset with the intention of reducing the risk of loss from another asset.
In finance, hedging is a risk management technique that focuses on minimizing and eliminating the risk of uncertainty. It aids in limiting losses that may oc
- Slide 4 text: What’s a Hedge Fund? | The hedge fund manager gets money from an outside investor and then invests it according to the plan provided by the investor.
- Slide 5 text: 
- Slide 6 text: 
- Slide 7 text: 
- Slide 8 text: 
- Slide 9 text: 
- Slide 10 text: 

## UNIT 6/5 Active vs passive bond portfolio management.docx
- Type: docx
- Paragraphs extracted: 1
- Tables extracted: 1
- Images extracted: 0
- Para: Active vs passive bond portfolio management