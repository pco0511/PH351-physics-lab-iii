# Error Propagation for Hall Effect Measurements

This document derives the uncertainty formulas used in the analysis code (`scripts/export_figures.py`).
All formulas follow from the general error propagation rule for a quantity $f(x_1, x_2, \ldots)$:

$$\sigma_f^2 = \sum_{i} \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2 + 2 \sum_{i<j} \frac{\partial f}{\partial x_i} \frac{\partial f}{\partial x_j} \operatorname{cov}(x_i, x_j)$$

---

## 1. Calibration: Coil Current to Magnetic Field

### 1.1 Model

The magnetic field $B$ (mT) at the sample position is a linear function of the coil current $I_\mathrm{coil}$ (A):

$$B = a \cdot I_\mathrm{coil} + b$$

The parameters $a$ (slope, mT/A) and $b$ (intercept, mT) are obtained by ordinary least-squares (OLS) fitting to calibration data.

### 1.2 Fit Covariance

For $N$ calibration data points $(I_k, B_k)$, `numpy.polyfit(..., cov=True)` returns the $2 \times 2$ covariance matrix of the fit parameters:

$$\mathbf{C}_\mathrm{fit} = \begin{pmatrix} \sigma_a^2 & \operatorname{cov}(a,b) \\ \operatorname{cov}(a,b) & \sigma_b^2 \end{pmatrix}$$

Since the calibration is performed in both **increasing** and **decreasing** sweep directions (to characterise hysteresis), we compute a combined covariance:

$$\mathbf{C} = \frac{1}{2}(\mathbf{C}_\mathrm{inc} + \mathbf{C}_\mathrm{dec}) + \begin{pmatrix} \mathrm{Var}(a_\mathrm{inc}, a_\mathrm{dec}) & 0 \\ 0 & \mathrm{Var}(b_\mathrm{inc}, b_\mathrm{dec}) \end{pmatrix}$$

The first term is the average statistical uncertainty from both fits; the second term accounts for the systematic spread (hysteresis) between the two sweep directions. The final slope and intercept are taken as the mean of both directions: $\bar{a} = (a_\mathrm{inc} + a_\mathrm{dec})/2$, $\bar{b} = (b_\mathrm{inc} + b_\mathrm{dec})/2$.

### 1.3 Magnetic Field Uncertainty

For a given coil current $I_\mathrm{coil}$, the uncertainty in $B$ is:

$$\sigma_B^2(I_\mathrm{coil}) = I_\mathrm{coil}^2 \, \sigma_a^2 + \sigma_b^2 + 2 \, I_\mathrm{coil} \, \operatorname{cov}(a, b)$$

This formula accounts for the full covariance structure and shows that the $B$-field uncertainty depends on the operating point $I_\mathrm{coil}$: it is smallest near the centroid of the calibration data and grows towards the edges.

---

## 2. Hall Coefficient

### 2.1 Fit Model

The Hall voltage is modelled as:

$$U_H = \alpha \cdot I_s \cdot B, \qquad \alpha \equiv \frac{R_H}{d}$$

where $I_s$ is the sample current, $B$ the magnetic field (in T), and $d$ the sample thickness. This is a one-parameter origin-constrained fit.

Given $N$ data points $(I_{s,i}, B_i, U_{H,i})$, define $x_i \equiv I_{s,i} \cdot B_i$. The OLS estimator for $\alpha$ is:

$$\hat{\alpha} = \frac{\sum_i U_{H,i} \, x_i}{\sum_i x_i^2}$$

### 2.2 Statistical Uncertainty

From the fit residuals $r_i = U_{H,i} - \hat{\alpha} \, x_i$:

$$\sigma_{\alpha,\mathrm{stat}}^2 = \frac{\sum_i r_i^2}{(N - 1) \sum_i x_i^2}$$

The factor $(N - 1)$ in the denominator accounts for the single fitted parameter.

### 2.3 Calibration Uncertainty

The magnetic field values $B_i$ entering the fit are not exact; they carry calibration uncertainty.
Since $B_i = a \cdot I_{\mathrm{coil},i} + b$, the fitted $\hat{\alpha}$ depends implicitly on $a$ and $b$:

$$\sigma_{\alpha,\mathrm{cal}}^2 = \left(\frac{\partial \hat{\alpha}}{\partial a}\right)^2 \sigma_a^2 + \left(\frac{\partial \hat{\alpha}}{\partial b}\right)^2 \sigma_b^2 + 2 \frac{\partial \hat{\alpha}}{\partial a} \frac{\partial \hat{\alpha}}{\partial b} \operatorname{cov}(a,b)$$

The partial derivatives $\partial \hat{\alpha}/\partial a$ and $\partial \hat{\alpha}/\partial b$ are evaluated **numerically** via central finite differences:

$$\frac{\partial \hat{\alpha}}{\partial a} \approx \frac{\hat{\alpha}(B_i + \epsilon_a I_{\mathrm{coil},i}) - \hat{\alpha}(B_i - \epsilon_a I_{\mathrm{coil},i})}{2 \epsilon_a}$$

$$\frac{\partial \hat{\alpha}}{\partial b} \approx \frac{\hat{\alpha}(B_i + \epsilon_b) - \hat{\alpha}(B_i - \epsilon_b)}{2 \epsilon_b}$$

where $\hat{\alpha}(\tilde{B})$ denotes re-evaluation of the OLS estimator with perturbed $B$ values, and $\epsilon_a$, $\epsilon_b$ are small perturbations ($\sim 10^{-3} \sigma_a$, $10^{-3} \sigma_b$).

**Analytic form** (for reference): defining $S_{xx} \equiv \sum_i x_i^2$ and $S_{xU} \equiv \sum_i U_{H,i} x_i$,

$$\frac{\partial \hat{\alpha}}{\partial a} = \frac{1}{S_{xx}} \sum_i I_{\mathrm{coil},i} \left[ U_{H,i} I_{s,i} - 2 \hat{\alpha} \, x_i I_{s,i} B_i^{-1} \cdot I_{\mathrm{coil},i} \right] \cdot \frac{\partial B_i}{\partial a}$$

The expression is complex because $a$ affects both the numerator and denominator of $\hat{\alpha}$ (since $x_i = I_{s,i} B_i$ and $B_i$ depends on $a$). The numerical approach avoids algebraic errors and gives identical results to machine precision.

### 2.4 Combined $R_H$ Uncertainty

Since $R_H = \alpha \cdot d$:

$$\sigma_{R_H}^2 = d^2 \, \sigma_{\alpha,\mathrm{stat}}^2 + d^2 \, \sigma_{\alpha,\mathrm{cal}}^2 + \alpha^2 \, \sigma_d^2$$

Or equivalently, with three independent components:

| Component | Formula | Origin |
|-----------|---------|--------|
| $\sigma_{R_H,\mathrm{stat}}$ | $d \cdot \sigma_{\alpha,\mathrm{stat}}$ | Fit residual scatter |
| $\sigma_{R_H,\mathrm{cal}}$ | $d \cdot \sigma_{\alpha,\mathrm{cal}}$ | Calibration $B(I_\mathrm{coil})$ uncertainty |
| $\sigma_{R_H,d}$ | $\lvert\alpha\rvert \cdot \sigma_d$ | Sample thickness uncertainty |

$$\boxed{\sigma_{R_H} = \sqrt{\sigma_{R_H,\mathrm{stat}}^2 + \sigma_{R_H,\mathrm{cal}}^2 + \sigma_{R_H,d}^2}}$$

---

## 3. Charge Carrier Density

### 3.1 Formula

In the extrinsic regime where dopant carriers dominate:

$$n = \frac{1}{e_0 \lvert R_H \rvert}$$

where $e_0 = 1.602 \times 10^{-19}$ C is the elementary charge (exact by definition since 2019 SI redefinition).

### 3.2 Uncertainty

Since $e_0$ is exact, the only error source is $R_H$:

$$\frac{\partial n}{\partial R_H} = -\frac{1}{e_0 R_H^2}$$

$$\sigma_n = \frac{\sigma_{R_H}}{e_0 R_H^2} = n \cdot \frac{\sigma_{R_H}}{\lvert R_H \rvert}$$

$$\boxed{\frac{\sigma_n}{n} = \frac{\sigma_{R_H}}{\lvert R_H \rvert}}$$

The relative uncertainty in carrier density equals the relative uncertainty in the Hall coefficient.

---

## 4. Drift Velocity

### 4.1 Formula

At equilibrium, the Lorentz force balances the Hall field force:

$$v_d = \frac{\lvert U_H \rvert}{b \cdot B}$$

where $b$ is the sample height and $B$ the magnetic field (in T).

### 4.2 Uncertainty

Independent error sources: $U_H$ (measurement noise), $b$ (dimension tolerance), $B$ (calibration):

$$\frac{\sigma_{v_d}^2}{v_d^2} = \left(\frac{\sigma_{U_H}}{U_H}\right)^2 + \left(\frac{\sigma_b}{b}\right)^2 + \left(\frac{\sigma_B}{B}\right)^2$$

$$\boxed{\sigma_{v_d} = v_d \sqrt{\left(\frac{\sigma_{U_H}}{U_H}\right)^2 + \left(\frac{\sigma_b}{b}\right)^2 + \left(\frac{\sigma_B}{B}\right)^2}}$$

Here $\sigma_{U_H}$ is the standard deviation of the steady-state Hall voltage (measurement fluctuation), and $\sigma_B$ is from the calibration (Section 1.3).

---

## 5. Carrier Mobility

### 5.1 Formula

The mobility is determined from the Hall voltage, longitudinal voltage, and sample dimensions:

$$\mu = \frac{\lvert U_H \rvert \cdot w}{b \cdot B \cdot \lvert U_\mathrm{long} \rvert}$$

where $w$ is the sample length (distance between longitudinal voltage contacts), $U_\mathrm{long}$ is the longitudinal voltage drop.

### 5.2 Uncertainty

Five independent error sources:

$$\frac{\sigma_\mu^2}{\mu^2} = \left(\frac{\sigma_{U_H}}{U_H}\right)^2 + \left(\frac{\sigma_w}{w}\right)^2 + \left(\frac{\sigma_b}{b}\right)^2 + \left(\frac{\sigma_B}{B}\right)^2 + \left(\frac{\sigma_{U_\mathrm{long}}}{U_\mathrm{long}}\right)^2$$

$$\boxed{\sigma_\mu = \mu \sqrt{\left(\frac{\sigma_{U_H}}{U_H}\right)^2 + \left(\frac{\sigma_w}{w}\right)^2 + \left(\frac{\sigma_b}{b}\right)^2 + \left(\frac{\sigma_B}{B}\right)^2 + \left(\frac{\sigma_{U_\mathrm{long}}}{U_\mathrm{long}}\right)^2}}$$

### 5.3 Weighted Mean

Mobility is computed at each coil current setting $I_{\mathrm{coil},k}$ (i.e. each $B$-field value), giving a set $\{\mu_k \pm \sigma_{\mu,k}\}$.
The best estimate is the **inverse-variance weighted mean**:

$$\bar{\mu} = \frac{\sum_k w_k \mu_k}{\sum_k w_k}, \qquad w_k = \frac{1}{\sigma_{\mu,k}^2}$$

$$\boxed{\sigma_{\bar{\mu}} = \frac{1}{\sqrt{\sum_k w_k}}}$$

The same procedure applies to the drift velocity.

---

## 6. Summary of Input Uncertainties

| Source | Symbol | Value | Origin |
|--------|--------|-------|--------|
| Calibration slope | $\sigma_a$ | from fit covariance | OLS + hysteresis |
| Calibration intercept | $\sigma_b$ | from fit covariance | OLS + hysteresis |
| Sample thickness | $\sigma_d$ | 0.1 mm | Manufacturer tolerance |
| Sample height | $\sigma_b$ | 0.5 mm | Manufacturer tolerance |
| Sample length | $\sigma_w$ | 0.5 mm | Manufacturer tolerance |
| Hall voltage | $\sigma_{U_H}$ | std of steady-state plateau | Measurement noise |
| Longitudinal voltage | $\sigma_{U_\mathrm{long}}$ | std of steady-state plateau | Measurement noise |

---

## 7. Error Budget (Typical Dominance)

For $R_H$:

$$\sigma_{R_H,d} \gg \sigma_{R_H,\mathrm{cal}} > \sigma_{R_H,\mathrm{stat}}$$

The sample thickness uncertainty dominates because the relative uncertainty $\sigma_d/d = 0.1/1.0 = 10\%$ directly propagates as $\sigma_{R_H}/R_H$. If a more precise thickness measurement is available (e.g. micrometer caliper with $\sigma_d \sim 0.01$ mm), this would reduce the total $R_H$ uncertainty by an order of magnitude.

For $\mu$:

The dominant contributors depend on the operating point. At low $B$ (low coil current), $\sigma_B/B$ grows. At high $B$, $\sigma_{U_H}/U_H$ and $\sigma_{U_\mathrm{long}}/U_\mathrm{long}$ are typically the limiting factors.

---

## Appendix: LaTeX Snippet for Report

The following can be adapted for inclusion in the report appendix:

```latex
\subsection{Calibration Uncertainty}

The magnetic field is related to the coil current by a linear calibration
$B = a I_\mathrm{coil} + b$, where $a$ and $b$ are obtained from a
least-squares fit. The covariance matrix of the fit parameters,
$\mathbf{C} = \begin{psmallmatrix} \sigma_a^2 & \mathrm{cov}(a,b) \\
\mathrm{cov}(a,b) & \sigma_b^2 \end{psmallmatrix}$,
yields the uncertainty in $B$ at a given coil current:
\begin{equation}
  \sigma_B^2(I_\mathrm{coil})
  = I_\mathrm{coil}^2 \sigma_a^2 + \sigma_b^2
    + 2 I_\mathrm{coil} \operatorname{cov}(a,b)
\end{equation}

\subsection{Hall Coefficient Uncertainty}

The Hall coefficient $R_H = \alpha d$ is obtained from a one-parameter
origin-constrained fit $U_H = \alpha I_s B$. Its total uncertainty
combines three independent contributions:
\begin{equation}
  \sigma_{R_H}^2
  = d^2 \sigma_{\alpha,\mathrm{stat}}^2
  + d^2 \sigma_{\alpha,\mathrm{cal}}^2
  + \alpha^2 \sigma_d^2
\end{equation}
where $\sigma_{\alpha,\mathrm{stat}}$ is from the fit residuals,
$\sigma_{\alpha,\mathrm{cal}}$ is propagated from the calibration
covariance via numerical partial derivatives, and $\sigma_d$ is the
uncertainty in the sample thickness.

\subsection{Carrier Density Uncertainty}

From $n = 1/(e_0 |R_H|)$:
\begin{equation}
  \frac{\sigma_n}{n} = \frac{\sigma_{R_H}}{|R_H|}
\end{equation}

\subsection{Mobility Uncertainty}

From $\mu = |U_H| w / (b B |U_\mathrm{long}|)$:
\begin{equation}
  \frac{\sigma_\mu^2}{\mu^2}
  = \left(\frac{\sigma_{U_H}}{U_H}\right)^2
  + \left(\frac{\sigma_w}{w}\right)^2
  + \left(\frac{\sigma_b}{b}\right)^2
  + \left(\frac{\sigma_B}{B}\right)^2
  + \left(\frac{\sigma_{U_\mathrm{long}}}{U_\mathrm{long}}\right)^2
\end{equation}
The final mobility is a weighted mean over all $B$-field settings:
$\bar{\mu} = \sum w_k \mu_k / \sum w_k$, with
$\sigma_{\bar{\mu}} = 1/\sqrt{\sum w_k}$.
```
