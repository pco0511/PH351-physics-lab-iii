# Hall Effect in p-Ge — Report Outline

## 1. Introduction

- Overview of Hall effect and its importance for determining microscopic parameters of charge transport in semiconductors
- Objectives:
  - Measure Hall voltage as a function of current at constant B → determine charge carrier density and mobility
  - Measure Hall voltage as a function of B at constant I → determine Hall coefficient
- Three sample types: p-Ge, n-Ge, undoped Ge
- Temperature-dependent measurement omitted

## 2. Theoretical Background

### 2.1 Hall Effect

- Rectangular sample in uniform B-field with current I → Hall voltage perpendicular to both B and I
- $U_H = R_H \cdot I \cdot B / d$ (Eq. I)
- Equilibrium: Lorentz force balanced by electrical force from Hall field

### 2.2 Hall Coefficient

- $R_H = \frac{1}{e_0} \cdot \frac{p\mu_p^2 - n\mu_n^2}{(p\mu_p + n\mu_n)^2}$ (Eq. II)
- $R_H > 0$: hole-dominated (p-type), $R_H < 0$: electron-dominated (n-type)
- Extrinsic regime ($n \approx 0$): $R_H \approx 1/(e_0 \cdot p_S)$

### 2.3 Charge Carrier Density

- $p_S = B / (e_0 \cdot d \cdot U_H / I)$ (Eq. III)

### 2.4 Mobility

- $\mu_p = U_H \cdot w / (b \cdot B \cdot U)$ (Eq. VIII)
- Drift velocity $v_p = U_H / (b \cdot B)$ (Eq. VII)

### 2.5 p-Doping and Band Structure

- Group III dopants create holes in valence band
- $E_A \approx 0.01$ eV $\ll$ $E_g$ (band gap)
- Three temperature regimes: freeze-out / extrinsic / intrinsic

## 3. Experimental Procedure

### 3.1 Apparatus

- Base unit for Hall effect Ge (586 850), p-Ge / n-Ge / undoped Ge plug-in boards
- Sensor CASSY + CASSY Lab, Combi B-Sensor S
- U-core + coils (250 turns × 2) + bored pole pieces → electromagnet
- DC power supplies × 3

### 3.2 Calibration

- Coil current vs B-field calibration curve
- Increasing / decreasing sweep (check hysteresis)

### 3.3 Hall Voltage Measurement

- Compensate Hall voltage offset at $B = 0$
- Experiment a): Fix B, sweep I from 0 to max → record $U_H$ vs $I$ (repeat for multiple B values)
- Experiment b): Fix I, vary B → record $U_H$ vs $B$
- Measure voltage drop $U$ separately

### 3.4 Additional Experiments

- Repeat with n-Ge and undoped Ge boards
- Current limits: undoped Ge ≤ 4 mA, doped Ge ≤ 33 mA

## 4. Results

### 4.1 Calibration Curve

- Coil current vs B-field (increasing / decreasing)
- Linear fit: $B = a \cdot I_\text{coil} + b$
- Hysteresis assessment

### 4.2 Ramp Detection & Steady-State Extraction

- Detect ramp-up start/end in time-series data (5% / 90% of peak current)
- Extract steady-state plateau for analysis

### 4.3 Experiment a) — $U_H$ vs $I_s$ (B = const.)

- $I_s$ vs $U_H$ plot for each B-field value (coil current → B via calibration)
- Linear fit through origin → slope $A = R_H \cdot B / d$
- 3D scatter ($I_s$, $B$, $U_H$) + surface fit $U_H = (R_H / d) \cdot I_s \cdot B$
- Extract $R_H$ with uncertainty

### 4.4 Experiment b) — $U_H$ vs $B$ (I = const.)

- Steady-state mean voltage vs B-field (Ge-n, Ge-p)
- Linear fit → $R_H = A \cdot d / I$

### 4.5 Derived Physical Quantities

| Quantity | Formula | Manual reference value |
|----------|---------|----------------------|
| Hole density $p_S$ | $B / (e_0 \cdot d \cdot A)$ | $1.1 \times 10^{21}$ m$^{-3}$ |
| Drift velocity $v_p$ | $U_H / (b \cdot B)$ | 21 m/s |
| Mobility $\mu_p$ | $U_H \cdot w / (b \cdot B \cdot U)$ | 2940 cm$^2$/(V·s) |
| Hall coefficient $R_H$ | $A \cdot d / I$ | $6.6 \times 10^{-3}$ m$^3$/(As) |

### 4.6 Longitudinal Voltage

- Steady-state mean longitudinal voltage vs B-field

## 5. Discussion

### 5.1 Verification of $U_H \propto I \cdot B$

- Experiment a) confirms $U_H \propto I$; experiment b) confirms $U_H \propto B$
- Combined: experimental validation of Eq. (I)

### 5.2 Magnitude of Hall Coefficient

- Measured $R_H \sim 10^{-3}$ m$^3$/C vs metals (Ag: $8.9 \times 10^{-11}$ m$^3$/C)
- ~$10^7$ times larger → explained by carrier concentration difference (metals ~$10^{28}$ vs semiconductor ~$10^{21}$ m$^{-3}$)

### 5.3 Validity of Measured $p_S$ and $\mu_p$

- Whether $p_S \sim 10^{21}$ m$^{-3}$ is consistent with typical dopant concentration for p-Ge
- Compare $\mu_p$ with literature (~1900 cm$^2$/(V·s) at 300 K for pure Ge)

### 5.4 Hall Voltage Compensation

- Origin of $U_H \neq 0$ offset at $B = 0$ (geometric asymmetry of contacts, ohmic voltage drop)
- Importance of compensation procedure

### 5.5 Error Sources

- Magnetic field uniformity across sample
- Joule heating → temperature rise → increased intrinsic carriers, breakdown of extrinsic assumption
- Contact resistance effect on voltage drop $U$ measurement
- CASSY Lab measurement range settings (digitization resolution)
- Calibration fit uncertainty propagated to B-field conversion

### 5.6 Charge Carrier Polarity

- p-Ge: $R_H > 0$ → hole-dominated
- n-Ge: $R_H < 0$ → electron-dominated
- Consistency with Lorentz force direction and Hall field direction

### 5.7 Comparison: n-Ge and Undoped Ge

- **n-Ge**: Hall voltage sign reversal, $R_H < 0$, extract electron density $n_S$, confirm $\mu_n > \mu_p$ (smaller effective mass in conduction band)
- **Undoped Ge**: $p_E \approx n_E$ so $p\mu_p^2$ and $n\mu_n^2$ partially cancel → $R_H \approx 0$, very small or unobservable Hall voltage. If $\mu_n > \mu_p$, slightly negative $R_H$ possible
- Reason for different current limits (4 mA vs 33 mA): high resistivity → more Joule heating

## 6. Conclusion

- Summary of whether objectives were achieved
- Key measured values ($R_H$, $p_S$, $\mu_p$) with uncertainties
- Comparison across three samples (p-Ge, n-Ge, undoped Ge)

## References

[1] N.W. Ashcroft and N.D. Mermin, *Solid State Physics*, Ch. 1 & 3, Harcourt (1976).
[2] C. Kittel, *Introduction to Solid State Physics*, 8th ed., Ch. 6, Wiley (2005).
[3] B.G. Streetman and S.K. Banerjee, *Solid State Electronic Devices*, 7th ed., Pearson (2015).
[4] S.M. Sze and K.K. Ng, *Physics of Semiconductor Devices*, 3rd ed., Wiley (2007).
