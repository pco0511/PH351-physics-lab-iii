#!/usr/bin/env python3
"""
Export publication-quality figures for the Hall effect report.

Figures (matching manual section 10 requirements):
  1. fig_calibration.pdf     — Coil current vs B-field calibration + linear fit
  2. fig_UH_vs_I_p.pdf       — U_H vs I_s at several B values (Ge-p)
  3. fig_UH_vs_I_n.pdf       — U_H vs I_s at several B values (Ge-n)
  4. fig_UH_vs_B.pdf         — U_H vs B at constant I (Ge-p, Ge-n)
  5. fig_3d_fit_p.pdf        — 3D scatter + surface fit (Ge-p)
  6. fig_3d_fit_n.pdf        — 3D scatter + surface fit (Ge-n)
  7. fig_longitudinal_vs_B.pdf — Longitudinal voltage vs B
"""

from pathlib import Path

import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

plt.rcParams.update({
    "font.size": 9,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "legend.fontsize": 7,
    "figure.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "hdf5"
FIG_DIR = ROOT / "tex" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

CALIB_H5 = DATA_DIR / "calibration.h5"
VOLTAGE_H5 = DATA_DIR / "voltage_measurements.h5"

DOPED_SAMPLES = ["Ge-n", "Ge-p"]

# ---------------------------------------------------------------------------
# Physical constants & sample dimensions
# ---------------------------------------------------------------------------
e0 = 1.602e-19        # elementary charge [C]
d_m = 1.0e-3          # sample thickness [m]
b_m = 10.0e-3         # sample height [m]
w_m = 20.0e-3         # sample length [m]

# Measurement uncertainties on sample dimensions
# (LD Didactic board specification tolerances)
sigma_d = 0.0         # [m]  (exact, no uncertainty assumed)
sigma_b = 0.5e-3      # [m]
sigma_w = 0.5e-3      # [m]

# Analysis cut: maximum sample current
I_MAX_A = 30e-3       # [A]  (clip ramp data to 0–30 mA)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def smooth_signal(signal, win=20):
    clean = np.nan_to_num(signal, nan=0.0)
    win = min(win, len(clean) // 5)
    if win > 1:
        kernel = np.ones(win) / win
        return np.convolve(clean, kernel, mode="same")
    return clean


def find_ramp_bounds(signal, start_frac=0.05, end_frac=0.90):
    sm = smooth_signal(signal)
    peak = np.max(sm)
    if peak <= 0:
        return 0, 0
    return int(np.argmax(sm > start_frac * peak)), int(np.argmax(sm > end_frac * peak))


# ---------------------------------------------------------------------------
# Load calibration
# ---------------------------------------------------------------------------
print("Loading calibration...")
with h5py.File(CALIB_H5, "r") as hf:
    calib = {}
    for direction in ["increasing", "decreasing"]:
        grp = hf[f"current_field/{direction}"]
        calib[direction] = {
            "I": grp["coil_current_A"][:],
            "B": grp["B_field_mT"][:],
        }

slopes, intercepts, calib_covs = [], [], []
for direction in ["increasing", "decreasing"]:
    c, cov = np.polyfit(calib[direction]["I"], calib[direction]["B"], 1, cov=True)
    slopes.append(c[0])
    intercepts.append(c[1])
    calib_covs.append(cov)

calib_slope = np.mean(slopes)
calib_intercept = np.mean(intercepts)

# Combined calibration covariance:
# mean of per-direction fit covariances + inter-direction spread
calib_cov = np.mean(calib_covs, axis=0)
calib_cov[0, 0] += np.var(slopes, ddof=0)
calib_cov[1, 1] += np.var(intercepts, ddof=0)

sigma_a_cal = np.sqrt(calib_cov[0, 0])    # slope uncertainty [mT/A]
sigma_b_cal = np.sqrt(calib_cov[1, 1])    # intercept uncertainty [mT]
cov_ab_cal = calib_cov[0, 1]              # covariance [mT^2/A]

print(f"  Calibration: B = ({calib_slope:.4f} +/- {sigma_a_cal:.4f}) * I"
      f" + ({calib_intercept:.4f} +/- {sigma_b_cal:.4f})  [mT]")


def I_coil_to_B(I_coil_A):
    """Convert coil current to magnetic field [mT].

    The calibration intercept b is attributed to the Hall probe zero offset
    and is intentionally excluded from the conversion.
    """
    return calib_slope * I_coil_A


def sigma_B_mT(I_coil_A):
    """Uncertainty in B [mT] from calibration slope uncertainty only.

    Since the intercept is excluded, only the slope uncertainty propagates.
    """
    return np.abs(I_coil_A) * sigma_a_cal


# ---------------------------------------------------------------------------
# Load ramp data
# ---------------------------------------------------------------------------
print("Loading voltage data & detecting ramps...")
ramp_info = {}

with h5py.File(VOLTAGE_H5, "r") as hf:
    for mtype in ["transverse", "longitudinal"]:
        for sample in DOPED_SAMPLES:
            sample_grp = hf[f"{mtype}/{sample}"]
            for coil_key in sorted(sample_grp.keys(), key=lambda k: int(k.split("_")[1])):
                grp = sample_grp[coil_key]
                t = grp["time_s"][:]
                I = grp["sample_current_A"][:]
                V = grp["voltage_V"][:]
                I_coil = grp.attrs["coil_current_A"]

                # Correct for reversed sensor polarity on transverse channel
                if mtype == "transverse":
                    V = -V

                rs, re = find_ramp_bounds(I)

                # Clip plateau: detect where current drops after ramp
                I_post = I[re:]
                I_sm = smooth_signal(I_post)
                I_peak = np.max(I_sm) if len(I_sm) else 0
                if I_peak > 0:
                    threshold = 0.90 * I_peak
                    # Find first point above threshold (skip smoothing edge)
                    first_above = int(np.argmax(I_sm >= threshold))
                    # From there, find first sustained drop below threshold
                    rest = I_sm[first_above:]
                    below_idx = np.where(rest < threshold)[0]
                    plat_end = first_above + int(below_idx[0]) if len(below_idx) else len(I_post)
                else:
                    plat_end = len(I_post)
                plat_end = max(plat_end, 1)  # at least 1 point

                V_ss = V[re:re + plat_end]
                I_ss = I[re:re + plat_end]
                V_valid = V_ss[~np.isnan(V_ss)]
                I_valid = I_ss[~np.isnan(I_ss)]

                ramp_info[(mtype, sample, coil_key)] = {
                    "I_coil_A": I_coil,
                    "rs": rs, "re": re, "plat_end": plat_end,
                    "V_mean": np.mean(V_valid) if len(V_valid) else np.nan,
                    "V_std": np.std(V_valid) if len(V_valid) else np.nan,
                    "I_mean": np.mean(I_valid) if len(I_valid) else np.nan,
                    "n_ss": len(V_valid),
                }


# ===================================================================
# Fig 1: Calibration curve with linear fit
# ===================================================================
print("Fig 1: Calibration...")
fig, ax = plt.subplots(figsize=(3.4, 2.6))
for direction, marker in [("increasing", "^"), ("decreasing", "v")]:
    I_c, B_c = calib[direction]["I"], calib[direction]["B"]
    ax.plot(I_c, B_c, marker, markersize=3, label=direction)

I_fit = np.linspace(
    min(calib["increasing"]["I"].min(), calib["decreasing"]["I"].min()),
    max(calib["increasing"]["I"].max(), calib["decreasing"]["I"].max()),
    100,
)
ax.plot(I_fit, calib_slope * I_fit + calib_intercept, "r-", lw=1,
        label=f"fit: $B = {calib_slope:.1f} I + ({calib_intercept:.1f})$ mT")
ax.set_xlabel("Coil current (A)")
ax.set_ylabel("$B$ (mT)")
ax.legend()
ax.grid(True, alpha=0.3)
fig.savefig(FIG_DIR / "fig_calibration.pdf")
plt.close(fig)
print(f"  -> {FIG_DIR / 'fig_calibration.pdf'}")


# ===================================================================
# Fig 2 & 3: U_H vs I_s at several B (Ge-p, Ge-n)
# ===================================================================
with h5py.File(VOLTAGE_H5, "r") as hf:
    for sample in DOPED_SAMPLES:
        tag = "p" if sample == "Ge-p" else "n"
        print(f"Fig U_H vs I ({sample})...")

        sample_grp = hf[f"transverse/{sample}"]
        coil_keys = sorted(sample_grp.keys(), key=lambda k: int(k.split("_")[1]))

        # B-field range for colorbar
        B_all = [I_coil_to_B(sample_grp[ck].attrs["coil_current_A"])
                 for ck in coil_keys]
        cmap = plt.cm.viridis
        norm = Normalize(vmin=min(B_all), vmax=max(B_all))

        fig, ax = plt.subplots(figsize=(3.4, 2.8))

        for coil_key in coil_keys:
            grp = sample_grp[coil_key]
            I_s = grp["sample_current_A"][:]
            V_h = -grp["voltage_V"][:]  # correct reversed sensor polarity
            I_coil = grp.attrs["coil_current_A"]
            B = I_coil_to_B(I_coil)

            rd = ramp_info[("transverse", sample, coil_key)]
            rs, re = rd["rs"], rd["re"]

            I_r = I_s[rs:re]
            V_r = V_h[rs:re]
            mask = ~(np.isnan(I_r) | np.isnan(V_r)) & (I_r <= I_MAX_A)
            ax.plot(I_r[mask] * 1e3, V_r[mask] * 1e3,
                    lw=0.6, color=cmap(norm(B)))

        ax.set_xlabel("Sample current $I_s$ (mA)")
        ax.set_ylabel("Hall voltage $U_H$ (mV)")
        ax.set_xlim(0, I_MAX_A * 1e3)
        ax.set_title(sample)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        fig.colorbar(sm, ax=ax, label="$B$ (mT)")
        ax.grid(True, alpha=0.3)
        fig.savefig(FIG_DIR / f"fig_UH_vs_I_{tag}.pdf")
        plt.close(fig)
        print(f"  -> fig_UH_vs_I_{tag}.pdf")


# ===================================================================
# Fig 4: U_H vs B (steady-state mean, both samples)
# ===================================================================
print("Fig 4: U_H vs B...")
fig, ax = plt.subplots(figsize=(3.4, 2.6))

for sample in DOPED_SAMPLES:
    B_vals, V_means, V_stds = [], [], []
    for key, d in sorted(ramp_info.items(), key=lambda x: x[1]["I_coil_A"]):
        mt, smp, ck = key
        if mt != "transverse" or smp != sample:
            continue
        B_vals.append(I_coil_to_B(d["I_coil_A"]))
        V_means.append(d["V_mean"] * 1e3)
        V_stds.append(d["V_std"] * 1e3)

    B_vals = np.array(B_vals)
    V_means = np.array(V_means)
    V_stds = np.array(V_stds)

    ax.errorbar(B_vals, V_means, yerr=V_stds, fmt="o-", markersize=3,
                capsize=1.5, lw=0.8, label=sample)

ax.set_xlabel("$B$ (mT)")
ax.set_ylabel("Hall voltage $U_H$ (mV)")
ax.legend()
ax.grid(True, alpha=0.3)
fig.savefig(FIG_DIR / "fig_UH_vs_B.pdf")
plt.close(fig)
print(f"  -> fig_UH_vs_B.pdf")


# ===================================================================
# Fig 5 & 6: 3D scatter + fit surface (Ge-p, Ge-n)
# ===================================================================
hall_results = {}

with h5py.File(VOLTAGE_H5, "r") as hf:
    for sample in DOPED_SAMPLES:
        tag = "p" if sample == "Ge-p" else "n"
        print(f"Fig 3D fit ({sample})...")

        all_Is, all_B, all_UH, all_Icoil = [], [], [], []
        sample_grp = hf[f"transverse/{sample}"]
        coil_keys = sorted(sample_grp.keys(), key=lambda k: int(k.split("_")[1]))

        for coil_key in coil_keys:
            grp = sample_grp[coil_key]
            I_s = grp["sample_current_A"][:]
            V_h = -grp["voltage_V"][:]  # correct reversed sensor polarity
            I_coil = grp.attrs["coil_current_A"]
            B = I_coil_to_B(I_coil)

            rd = ramp_info[("transverse", sample, coil_key)]
            rs, re = rd["rs"], rd["re"]
            I_r, V_r = I_s[rs:re], V_h[rs:re]
            mask = ~(np.isnan(I_r) | np.isnan(V_r)) & (I_r <= I_MAX_A)
            n_valid = mask.sum()
            all_Is.extend(I_r[mask])
            all_B.extend(np.full(n_valid, B))
            all_UH.extend(V_r[mask])
            all_Icoil.extend(np.full(n_valid, I_coil))

        Is = np.array(all_Is)
        B_arr = np.array(all_B)
        UH = np.array(all_UH)
        Icoil_arr = np.array(all_Icoil)
        N = len(Is)

        # --- Fit: U_H = alpha * I_s * B,  alpha = R_H / d ---
        B_T = B_arr * 1e-3  # mT -> T
        IB = Is * B_T       # A * T
        sum_IB2 = np.sum(IB**2)
        alpha = np.sum(UH * IB) / sum_IB2

        # (1) Statistical uncertainty from fit residuals
        residuals = UH - alpha * IB
        sigma_alpha_stat = np.sqrt(np.sum(residuals**2) / ((N - 1) * sum_IB2))

        # (2) Calibration uncertainty via numerical partial derivative
        #     B = a*I_coil (intercept ignored)  →  perturb a to get ∂alpha/∂a
        def _alpha_with_B(B_mT):
            bt = B_mT * 1e-3
            ib = Is * bt
            return np.sum(UH * ib) / np.sum(ib**2)

        eps_a = max(sigma_a_cal * 1e-3, 1e-8)

        dalpha_da = (_alpha_with_B(B_arr + eps_a * Icoil_arr)
                     - _alpha_with_B(B_arr - eps_a * Icoil_arr)) / (2 * eps_a)

        sigma_alpha_cal = abs(dalpha_da) * sigma_a_cal

        # (3) Combined R_H = alpha * d  →  three independent sources
        R_H = alpha * d_m
        sigma_RH_stat = sigma_alpha_stat * d_m
        sigma_RH_cal = sigma_alpha_cal * d_m
        sigma_RH_d = abs(alpha) * sigma_d
        sigma_RH = np.sqrt(sigma_RH_stat**2 + sigma_RH_cal**2 + sigma_RH_d**2)

        hall_results[sample] = {
            "alpha": alpha, "R_H": R_H, "N": N,
            "sigma_RH_stat": sigma_RH_stat,
            "sigma_RH_cal": sigma_RH_cal,
            "sigma_RH_d": sigma_RH_d,
            "sigma_RH": sigma_RH,
            "residual_std": np.std(residuals),
        }

        # --- Figure ---
        fig = plt.figure(figsize=(4.5, 3.5))
        ax3 = fig.add_subplot(111, projection="3d")

        sc = ax3.scatter(Is * 1e3, B_arr, UH * 1e3,
                         c=B_arr, cmap="viridis", s=0.5, alpha=0.3)

        Is_g = np.linspace(Is.min(), Is.max(), 25)
        B_g = np.linspace(B_arr.min(), B_arr.max(), 25)
        Ism, Bm = np.meshgrid(Is_g, B_g)
        UHm = alpha * Ism * (Bm * 1e-3)
        ax3.plot_surface(Ism * 1e3, Bm, UHm * 1e3, alpha=0.25, color="red")

        ax3.set_xlabel("$I_s$ (mA)", fontsize=8)
        ax3.set_ylabel("$B$ (mT)", fontsize=8)
        ax3.set_zlabel("$U_H$ (mV)", fontsize=8)
        ax3.set_title(
            f"{sample}: $R_H$ = ({R_H*1e6:.2f} $\\pm$ {sigma_RH*1e6:.2f}) cm$^3$/C",
            fontsize=8,
        )
        ax3.tick_params(labelsize=6)
        fig.colorbar(sc, ax=ax3, label="$B$ (mT)", shrink=0.5, pad=0.12)
        fig.savefig(FIG_DIR / f"fig_3d_fit_{tag}.pdf")
        plt.close(fig)

        print(f"  -> fig_3d_fit_{tag}.pdf")
        print(f"     R_H = {R_H:+.6e} m^3/C  ({R_H*1e6:+.2f} cm^3/C)")
        print(f"     sigma_RH: stat={sigma_RH_stat:.2e}  cal={sigma_RH_cal:.2e}"
              f"  d={sigma_RH_d:.2e}  total={sigma_RH:.2e} m^3/C")


# ===================================================================
# Fig 7: Longitudinal voltage vs B
# ===================================================================
print("Fig 7: Longitudinal voltage vs B...")
fig, ax = plt.subplots(figsize=(3.4, 2.6))

for sample in DOPED_SAMPLES:
    B_vals, V_means, V_stds = [], [], []
    for key, d in sorted(ramp_info.items(), key=lambda x: x[1]["I_coil_A"]):
        mt, smp, ck = key
        if mt != "longitudinal" or smp != sample:
            continue
        B_vals.append(I_coil_to_B(d["I_coil_A"]))
        V_means.append(d["V_mean"])
        V_stds.append(d["V_std"])

    B_vals = np.array(B_vals)
    V_means = np.array(V_means)
    V_stds = np.array(V_stds)

    ax.errorbar(B_vals, V_means, yerr=V_stds, fmt="o-", markersize=3,
                capsize=1.5, lw=0.8, label=sample)

    # Print mean and sigma across all B settings
    print(f"  {sample}: V_long mean = {np.mean(V_means):.4f} V, "
          f"std = {np.std(V_means):.4f} V, "
          f"avg meas. sigma = {np.mean(V_stds):.4f} V")

ax.set_xlabel("$B$ (mT)")
ax.set_ylabel("Longitudinal voltage (V)")
ax.legend()
ax.grid(True, alpha=0.3)
fig.savefig(FIG_DIR / "fig_longitudinal_vs_B.pdf")
plt.close(fig)
print(f"  -> fig_longitudinal_vs_B.pdf")


# ===================================================================
# Helper: bin ramp data by sample current
# ===================================================================

def bin_ramp_data(I_ramp, V_ramp, n_bins=30, I_max=I_MAX_A, min_count=2):
    """Bin ramp data by I_s and return (centres, means, stds)."""
    I_bins = np.linspace(0, I_max, n_bins + 1)
    centres = (I_bins[:-1] + I_bins[1:]) / 2
    means = np.full(n_bins, np.nan)
    stds = np.full(n_bins, np.nan)
    for i in range(n_bins):
        sel = (I_ramp >= I_bins[i]) & (I_ramp < I_bins[i + 1])
        vals = V_ramp[sel]
        vals = vals[~np.isnan(vals)]
        if len(vals) >= min_count:
            means[i] = np.mean(vals)
            stds[i] = np.std(vals) if len(vals) > 1 else 0.0
    return centres, means, stds


# ===================================================================
# Appendix Fig A1: U_H vs I_s  linear fits (constant B)
# ===================================================================
print("\nAppendix Fig A1: U_H vs I_s linear fits (constant B)...")

with h5py.File(VOLTAGE_H5, "r") as hf:
    for sample in DOPED_SAMPLES:
        tag = "p" if sample == "Ge-p" else "n"
        sample_grp = hf[f"transverse/{sample}"]
        coil_keys = sorted(sample_grp.keys(), key=lambda k: int(k.split("_")[1]))

        B_all = [I_coil_to_B(sample_grp[ck].attrs["coil_current_A"])
                 for ck in coil_keys]
        cmap = plt.cm.viridis
        norm = Normalize(vmin=min(B_all), vmax=max(B_all))

        fig, ax = plt.subplots(figsize=(3.4, 2.8))

        slopes_a = []
        for coil_key in coil_keys:
            grp = sample_grp[coil_key]
            I_s = grp["sample_current_A"][:]
            V_h = -grp["voltage_V"][:]  # correct reversed sensor polarity
            I_coil = grp.attrs["coil_current_A"]
            B = I_coil_to_B(I_coil)

            rd = ramp_info[("transverse", sample, coil_key)]
            rs, re = rd["rs"], rd["re"]
            I_r, V_r = I_s[rs:re], V_h[rs:re]
            cut = ~(np.isnan(I_r) | np.isnan(V_r)) & (I_r <= I_MAX_A)
            I_r, V_r = I_r[cut], V_r[cut]

            # Bin
            Ic, Vm, Vs = bin_ramp_data(I_r, V_r)
            ok = ~np.isnan(Vm)
            color = cmap(norm(B))

            # Scatter binned data
            ax.scatter(Ic[ok] * 1e3, Vm[ok] * 1e3,
                       s=3, color=color, alpha=0.6, edgecolors="none")

            # Linear fit through origin
            if ok.sum() >= 3:
                slope = np.sum(Ic[ok] * Vm[ok]) / np.sum(Ic[ok] ** 2)
                slopes_a.append((B, slope))
                I_line = np.array([0, Ic[ok].max()])
                ax.plot(I_line * 1e3, (slope * I_line) * 1e3,
                        lw=0.7, color=color, alpha=0.8)

        ax.set_xlabel("Sample current $I_s$ (mA)")
        ax.set_ylabel("Hall voltage $U_H$ (mV)")
        ax.set_xlim(0, I_MAX_A * 1e3)
        ax.set_title(sample)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        fig.colorbar(sm, ax=ax, label="$B$ (mT)")
        ax.grid(True, alpha=0.3)
        fig.savefig(FIG_DIR / f"fig_appendix_UH_vs_I_linear_{tag}.pdf")
        plt.close(fig)
        print(f"  -> fig_appendix_UH_vs_I_linear_{tag}.pdf"
              f"  ({len(slopes_a)} slopes extracted)")


# ===================================================================
# Appendix Fig A2: U_H vs B  linear fits (constant I_s)
# ===================================================================
print("\nAppendix Fig A2: U_H vs B linear fits (constant I_s)...")

I_FIXED_mA = np.array([5, 10, 15, 20, 25])  # mA
I_FIXED_A = I_FIXED_mA * 1e-3

with h5py.File(VOLTAGE_H5, "r") as hf:
    for sample in DOPED_SAMPLES:
        tag = "p" if sample == "Ge-p" else "n"
        sample_grp = hf[f"transverse/{sample}"]
        coil_keys = sorted(sample_grp.keys(), key=lambda k: int(k.split("_")[1]))

        cmap_I = plt.cm.plasma
        norm_I = Normalize(vmin=I_FIXED_mA.min(), vmax=I_FIXED_mA.max())

        fig, ax = plt.subplots(figsize=(3.4, 2.8))

        # For each coil key, build smoothed curve, then interpolate
        interp_table = {If: ([], []) for If in I_FIXED_A}

        for coil_key in coil_keys:
            grp = sample_grp[coil_key]
            I_s = grp["sample_current_A"][:]
            V_h = -grp["voltage_V"][:]  # correct reversed sensor polarity
            I_coil = grp.attrs["coil_current_A"]
            B = I_coil_to_B(I_coil)

            rd = ramp_info[("transverse", sample, coil_key)]
            rs, re = rd["rs"], rd["re"]
            I_r, V_r = I_s[rs:re], V_h[rs:re]
            cut = ~(np.isnan(I_r) | np.isnan(V_r)) & (I_r <= I_MAX_A)
            I_r, V_r = I_r[cut], V_r[cut]

            # Bin to get smooth curve
            Ic, Vm, _ = bin_ramp_data(I_r, V_r)
            ok = ~np.isnan(Vm)
            if ok.sum() < 3:
                continue

            # Interpolate at each fixed I_s
            for If in I_FIXED_A:
                if Ic[ok].min() <= If <= Ic[ok].max():
                    UH_interp = np.interp(If, Ic[ok], Vm[ok])
                    interp_table[If][0].append(B)
                    interp_table[If][1].append(UH_interp)

        # Plot and fit for each fixed I_s
        for If in I_FIXED_A:
            B_pts = np.array(interp_table[If][0])
            UH_pts = np.array(interp_table[If][1])
            if len(B_pts) < 3:
                continue

            color = cmap_I(norm_I(If * 1e3))
            ax.scatter(B_pts, UH_pts * 1e3,
                       s=10, color=color, edgecolors="none", alpha=0.7)

            # Linear fit through origin: U_H = slope * B
            B_T = B_pts * 1e-3  # mT -> T
            slope = np.sum(UH_pts * B_T) / np.sum(B_T ** 2)
            B_line = np.array([0, B_pts.max()])
            ax.plot(B_line, slope * (B_line * 1e-3) * 1e3,
                    lw=0.8, color=color, alpha=0.8)

        ax.set_xlabel("$B$ (mT)")
        ax.set_ylabel("Hall voltage $U_H$ (mV)")
        ax.set_title(sample)
        sm_I = plt.cm.ScalarMappable(cmap=cmap_I, norm=norm_I)
        fig.colorbar(sm_I, ax=ax, label="$I_s$ (mA)")
        ax.grid(True, alpha=0.3)
        fig.savefig(FIG_DIR / f"fig_appendix_UH_vs_B_linear_{tag}.pdf")
        plt.close(fig)
        print(f"  -> fig_appendix_UH_vs_B_linear_{tag}.pdf")


# ===================================================================
# Derived physical quantities with full error propagation
# ===================================================================
print("\n" + "=" * 70)
print("DERIVED PHYSICAL QUANTITIES WITH ERROR PROPAGATION")
print("=" * 70)

for sample in DOPED_SAMPLES:
    hr = hall_results[sample]
    R_H = hr["R_H"]
    sigma_RH = hr["sigma_RH"]

    print(f"\n--- {sample} ---")
    print(f"  R_H           = {R_H:+.6e} +/- {sigma_RH:.2e} m^3/C"
          f"  ({R_H*1e6:+.2f} +/- {sigma_RH*1e6:.2f} cm^3/C)")
    print(f"    breakdown:  stat={hr['sigma_RH_stat']:.2e}"
          f"  cal={hr['sigma_RH_cal']:.2e}"
          f"  d={hr['sigma_RH_d']:.2e}")

    # --- Carrier density: n = 1 / (e0 * |R_H|) ---
    n_carrier = 1.0 / (e0 * abs(R_H))
    # sigma_n / n = sigma_RH / |R_H|
    sigma_n = n_carrier * (sigma_RH / abs(R_H))
    carrier_type = "holes (p)" if R_H > 0 else "electrons (n)"

    print(f"  Carrier dens. = {n_carrier:.4e} +/- {sigma_n:.2e} m^-3  ({carrier_type})")

    # --- Mobility: mu = U_H * w / (b * B * U_long) per coil current ---
    mu_vals, sigma_mu_vals = [], []
    vd_vals, sigma_vd_vals = [], []

    for key, d_tr in sorted(ramp_info.items(), key=lambda x: x[1]["I_coil_A"]):
        mt, smp, ck = key
        if mt != "transverse" or smp != sample:
            continue
        key_long = ("longitudinal", smp, ck)
        if key_long not in ramp_info:
            continue

        d_lo = ramp_info[key_long]
        I_coil = d_tr["I_coil_A"]
        B_mT = I_coil_to_B(I_coil)
        B_val = B_mT * 1e-3          # T
        sB = sigma_B_mT(I_coil) * 1e-3  # T

        U_H = d_tr["V_mean"]         # V
        sU_H = d_tr["V_std"]         # V
        U_long = d_lo["V_mean"]      # V
        sU_long = d_lo["V_std"]      # V

        if abs(U_H) < 1e-9 or abs(U_long) < 1e-9 or abs(B_val) < 1e-9:
            continue

        # Drift velocity: v_d = U_H / (b * B)
        vd = abs(U_H) / (b_m * B_val)
        rel_vd2 = (sU_H / U_H)**2 + (sB / B_val)**2 + (sigma_b / b_m)**2
        sigma_vd = abs(vd) * np.sqrt(rel_vd2)
        vd_vals.append(vd)
        sigma_vd_vals.append(sigma_vd)

        # Mobility: mu = U_H * w / (b * B * U_long)
        mu = abs(U_H) * w_m / (b_m * B_val * abs(U_long))
        rel_mu2 = ((sU_H / U_H)**2
                    + (sigma_w / w_m)**2
                    + (sigma_b / b_m)**2
                    + (sB / B_val)**2
                    + (sU_long / U_long)**2)
        sigma_mu = mu * np.sqrt(rel_mu2)
        mu_vals.append(mu)
        sigma_mu_vals.append(sigma_mu)

    if mu_vals:
        mu_arr = np.array(mu_vals)
        sigma_mu_arr = np.array(sigma_mu_vals)
        vd_arr = np.array(vd_vals)
        sigma_vd_arr = np.array(sigma_vd_vals)

        # Weighted mean of mobility
        w_mu = 1.0 / sigma_mu_arr**2
        mu_wmean = np.sum(w_mu * mu_arr) / np.sum(w_mu)
        sigma_mu_wmean = 1.0 / np.sqrt(np.sum(w_mu))

        # Weighted mean of drift velocity
        w_vd = 1.0 / sigma_vd_arr**2
        vd_wmean = np.sum(w_vd * vd_arr) / np.sum(w_vd)
        sigma_vd_wmean = 1.0 / np.sqrt(np.sum(w_vd))

        print(f"  Drift vel.    = {vd_wmean:.2f} +/- {sigma_vd_wmean:.2f} m/s"
              f"  (weighted mean, {len(vd_vals)} points)")
        print(f"  Mobility      = {mu_wmean*1e4:.1f} +/- {sigma_mu_wmean*1e4:.1f}"
              f" cm^2/(V*s)  (weighted mean, {len(mu_vals)} points)")

        hall_results[sample]["n_carrier"] = n_carrier
        hall_results[sample]["sigma_n"] = sigma_n
        hall_results[sample]["mu_wmean"] = mu_wmean
        hall_results[sample]["sigma_mu_wmean"] = sigma_mu_wmean
        hall_results[sample]["vd_wmean"] = vd_wmean
        hall_results[sample]["sigma_vd_wmean"] = sigma_vd_wmean
    else:
        print("  [WARN] No paired transverse/longitudinal data for mobility")


# --- Final summary table ---
print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print(f"{'Quantity':<25s} {'Ge-p':>25s} {'Ge-n':>25s}")
print("-" * 75)

for label, key, unit, scale in [
    ("R_H", "R_H", "m^3/C", 1),
    ("sigma_R_H", "sigma_RH", "m^3/C", 1),
    ("Carrier density", "n_carrier", "m^-3", 1),
    ("sigma_n", "sigma_n", "m^-3", 1),
    ("Mobility", "mu_wmean", "cm^2/(V*s)", 1e4),
    ("sigma_mu", "sigma_mu_wmean", "cm^2/(V*s)", 1e4),
    ("Drift velocity", "vd_wmean", "m/s", 1),
    ("sigma_vd", "sigma_vd_wmean", "m/s", 1),
]:
    vals = []
    for s in ["Ge-p", "Ge-n"]:
        v = hall_results.get(s, {}).get(key, np.nan)
        vals.append(f"{v * scale:+.4e}" if not np.isnan(v) else "N/A")
    print(f"  {label:<23s} {vals[0]:>25s} {vals[1]:>25s}  [{unit}]")

print("=" * 70)


# ===================================================================
# Weak-field check: mu * B << 1
# ===================================================================
print("\n" + "=" * 70)
print("WEAK-FIELD APPROXIMATION CHECK: mu * B")
print("=" * 70)

B_min_T = calib_slope * 1.0 * 1e-3   # I_coil = 1.0 A -> T
B_max_T = calib_slope * 5.2 * 1e-3   # I_coil = 5.2 A -> T
print(f"  B range: {B_min_T*1e3:.1f} - {B_max_T*1e3:.1f} mT")

for sample in DOPED_SAMPLES:
    hr = hall_results.get(sample, {})
    mu_si = hr.get("mu_wmean", np.nan)  # m^2/(V*s)
    if np.isnan(mu_si):
        continue
    muB_min = mu_si * B_min_T
    muB_max = mu_si * B_max_T
    print(f"  {sample}: mu = {mu_si*1e4:.0f} cm^2/(V*s)")
    print(f"    mu*B_min = {muB_min:.4f},  mu*B_max = {muB_max:.4f}")
    print(f"    (mu*B)^2 at B_max = {muB_max**2:.6f}")

print("=" * 70)


# ===================================================================
# Discussion helpers: sample resistance, power dissipation, time const
# ===================================================================
print("\n" + "=" * 70)
print("DISCUSSION: SAMPLE RESISTANCE, JOULE HEATING, TIME CONSTANT")
print("=" * 70)

for sample in DOPED_SAMPLES:
    hr = hall_results.get(sample, {})
    # Collect longitudinal V_mean and transverse I_mean at max B
    V_long_vals, I_mean_vals = [], []
    for key, d in ramp_info.items():
        mt, smp, ck = key
        if mt == "longitudinal" and smp == sample:
            V_long_vals.append(d["V_mean"])
        if mt == "transverse" and smp == sample:
            I_mean_vals.append(d["I_mean"])

    V_long_avg = np.nanmean(V_long_vals)
    I_mean_avg = np.nanmean(I_mean_vals)  # average plateau current

    R_sample = V_long_avg / I_mean_avg if I_mean_avg > 0 else np.nan
    P_joule = I_mean_avg * V_long_avg  # P = I * V
    I_max = I_MAX_A

    print(f"\n  {sample}:")
    print(f"    V_long (mean)  = {V_long_avg:.2f} V")
    print(f"    I_mean (plat.) = {I_mean_avg*1e3:.1f} mA")
    print(f"    R_sample       = {R_sample:.0f} Ohm")
    print(f"    P_joule (avg)  = {P_joule*1e3:.0f} mW")
    print(f"    P_joule (max)  = {I_max**2 * R_sample * 1e3:.0f} mW"
          f"  (at I = {I_max*1e3:.0f} mA)")

    # RL time constant estimate for sample circuit
    # Inductance of short wire loop ~ 1 uH (conservative upper bound)
    L_est = 1e-6  # H (order of magnitude for ~10 cm wire loop)
    tau_RL = L_est / R_sample if R_sample > 0 else np.nan
    print(f"    tau_RL (est.)   = {tau_RL*1e9:.0f} ns"
          f"  (L ~ {L_est*1e6:.0f} uH, R = {R_sample:.0f} Ohm)")

    # Sweep time estimate: ramp region duration
    # Pick a representative coil key
    for key, d in ramp_info.items():
        mt, smp, ck = key
        if mt == "transverse" and smp == sample:
            rs, re = d["rs"], d["re"]
            # Estimate from data sampling rate
            break
    print(f"    Ramp region: index {rs} to {re} ({re - rs} samples)")

# Coil inductance estimate from calibration slope
# B = a * I_coil;  B = mu0 * N * I / l_gap for electromagnet
# a = 29.9 mT/A
# Two coils of 250 turns each = 500 turns
# But for inductance we need core geometry. Rough estimate:
# L_coil ~ B * A_core * N / I = a[T/A] * A_core * N
# Assuming pole piece area ~ 4 cm x 4 cm = 16 cm^2 = 16e-4 m^2
N_coil = 500  # 2 x 250
A_core_est = 16e-4  # m^2 (rough estimate)
a_T_per_A = calib_slope * 1e-3  # T/A
L_coil_est = a_T_per_A * A_core_est * N_coil
R_coil_est = 5.0  # rough: ~15V supply / ~3A typical
tau_coil = L_coil_est / R_coil_est

print(f"\n  Coil circuit (rough estimate):")
print(f"    a = {a_T_per_A:.4f} T/A, N = {N_coil}, A_core ~ {A_core_est*1e4:.0f} cm^2")
print(f"    L_coil ~ {L_coil_est:.3f} H")
print(f"    R_coil ~ {R_coil_est:.0f} Ohm (est.)")
print(f"    tau_coil = L/R ~ {tau_coil*1e3:.0f} ms")

print("=" * 70)


print("\n=== Done. All figures saved to", FIG_DIR)
