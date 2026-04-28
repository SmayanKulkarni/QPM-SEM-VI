from pathlib import Path

tex_path = Path('/home/smayan/Desktop/QPM/outputs/term-test-ii-units-4-6-complete-study-source.tex')
text = tex_path.read_text(encoding='utf-8')

insertion = r'''
\section{Equation Compendium (Professional Typesetting)}

This section standardizes major formulas in display math form.

\subsection{Naive Diversification}
\[
w_i = \frac{1}{N}
\]
\[
R_p = \sum_{i=1}^{N} w_i R_i
\]

\subsection{Risk Contribution Framework}
\[
\mathrm{MCR}_i = \frac{\operatorname{Cov}(R_i, R_p)}{\sigma_p}
\]
\[
\mathrm{TRC}_i = w_i \cdot \mathrm{MCR}_i
\]
\[
\mathrm{PRC}_i = \frac{\mathrm{TRC}_i}{\sigma_p}
\]

\subsection{Risk Budgeting}
\[
\text{Risk Contribution}_i = w_i\,\sigma_i
\]
\[
\text{Risk Share}_i = \frac{\text{Risk Contribution}_i}{\sum_j \text{Risk Contribution}_j}
\]

\subsection{Simplified Risk Parity}
\[
q_i = \frac{1}{\sigma_i}, \qquad
w_i = \frac{q_i}{\sum_{j=1}^{N} q_j}
\]

\subsection{Full Risk Parity}
\[
\sigma_p^2 = \mathbf{w}^\top \Sigma \mathbf{w}
\]
\[
\mathrm{RC}_i = w_i\,(\Sigma\mathbf{w})_i
\]
\[
\mathrm{RC}_1 = \mathrm{RC}_2 = \cdots = \mathrm{RC}_N
\]

\subsection{Shrinkage Estimator}
\[
\Sigma_{\text{shrink}} = \lambda T + (1-\lambda)S,
\qquad 0 \le \lambda \le 1
\]

\subsection{EWMA Updates}
\[
\sigma_t^2 = \lambda\sigma_{t-1}^2 + (1-\lambda)r_{t-1}^2
\]
\[
\operatorname{Cov}_t(A,B)=\lambda\operatorname{Cov}_{t-1}(A,B)
+ (1-\lambda)r_{A,t-1}r_{B,t-1}
\]

\subsection{Rolling Covariance (Window $k$)}
\[
\operatorname{Cov}_{t}^{(k)}(A,B)=
\frac{1}{k}\sum_{j=t-k+1}^{t}
\left(r_{A,j}-\bar r_A\right)
\left(r_{B,j}-\bar r_B\right)
\]

\subsection{CPPI}
\[
C_t = V_t - F_t
\]
\[
E_t = m\,C_t, \qquad B_t = V_t - E_t
\]
\[
F_t^{\text{drawdown}} = (1-d)\,\max_{\tau\le t}V_\tau
\]

\subsection{Performance Evaluation}
\[
\text{Sharpe} = \frac{R_p - R_f}{\sigma_p}
\]
\[
\text{Treynor} = \frac{R_p - R_f}{\beta_p}
\]
\[
\alpha_p = R_p - \left[R_f + \beta_p\left(R_m-R_f\right)\right]
\]
'''

marker = '\\tableofcontents'
if marker in text and 'Equation Compendium (Professional Typesetting)' not in text:
    text = text.replace(marker, marker + '\n' + insertion, 1)

tex_path.write_text(text, encoding='utf-8')
print(f'Updated {tex_path}')
