import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# ----------------------------
# STEP 1: PROCESS RAW DATA
# ----------------------------
raw_df = pd.read_csv("1_1_DATA.csv")
raw_df.columns = raw_df.columns.str.strip()

# Initialize lists
frequencies = []    
phases = []
amplitudes_in = []
amplitudes_out = []
transmitancje = []

i = 0
while i < len(raw_df):
    row = raw_df.iloc[i]
    if row["Measurement"] == "AMPLITUDE" and row["Source 1"] == "CH1":
        try:
            # CH1 = wyjście, CH2 = wejście
            u_wy = float(raw_df.iloc[i]["Value"]) / 1000  # mV → V
            u_we = float(raw_df.iloc[i+1]["Value"]) / 1000
            faza = float(raw_df.iloc[i+2]["Value"])
            czest = float(raw_df.iloc[i+3]["Value"])

            frequencies.append(czest)
            phases.append(faza)
            amplitudes_out.append(u_wy)
            amplitudes_in.append(u_we)
            transmitancje.append(u_wy / u_we if u_we != 0 else 0)

            i += 4  # Skip to next block
        except:
            i += 1  # Skip faulty rows just in case
    else:
        i += 1

# Create processed DataFrame
df = pd.DataFrame({
    "Częstotliwość (Hz)": frequencies,
    "Przesunięcie fazowe (°)": phases,
    "Transmitancja H(f)": transmitancje
})

# ----------------------------
# STEP 2: PLOT DATA
# ----------------------------

# Sortowanie danych
freq = np.array(df["Częstotliwość (Hz)"])
H = np.array(df["Transmitancja H(f)"])
phase = np.array(df["Przesunięcie fazowe (°)"])

sorted_indices = np.argsort(freq)
freq = freq[sorted_indices]
H = H[sorted_indices]
phase = phase[sorted_indices]

# Interpolacja amplitudy (Tylko jeśli ilość punktów >= 4)
if len(freq) >= 4:
    freq_smooth = np.logspace(np.log10(freq.min()), np.log10(freq.max()), 500)
    H_spline = make_interp_spline(np.log(freq), H, k=3)  # log-scale interpolation
    H_smooth = H_spline(np.log(freq_smooth))
else:
    freq_smooth = freq
    H_smooth = H

# Wykres amplitudowy
plt.figure(figsize=(10, 6))
plt.plot(freq_smooth, H_smooth, 'r-', label='Interpolacja')
plt.plot(freq, H, 'o', color='black', label='Punkty pomiarowe')
plt.axhline(0.70713, color='gray', linestyle='--', linewidth=1, label='-3 dB (1/√2)')
plt.xscale("log")
plt.title("Charakterystyka amplitudowa")
plt.xlabel("Częstotliwość (Hz)")
plt.ylabel("Transmitancja H(f)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

# ----------------------------
# Wykres fazowy
# ----------------------------

# Faza może skakać (np. z 359° do 1°), więc "unwrap"
phase_unwrapped_rad = np.unwrap(np.radians(phase))  # radiany
phase_unwrapped_deg = np.degrees(phase_unwrapped_rad)

# Interpolacja fazy
if len(freq) >= 4:
    phase_spline = make_interp_spline(np.log(freq), phase_unwrapped_deg, k=3)
    phase_smooth_unwrapped = phase_spline(np.log(freq_smooth))
else:
    phase_smooth_unwrapped = phase_unwrapped_deg
    freq_smooth = freq

# Wykres fazowy
plt.figure(figsize=(10, 6))
plt.plot(freq_smooth, phase_smooth_unwrapped, 'r-', label='Interpolacja (unwrap)')
plt.plot(freq, phase, 'o', color='black', label='Punkty pomiarowe (wrap)')
plt.xscale("log")
plt.title("Charakterystyka fazowa")
plt.xlabel("Częstotliwość (Hz)")
plt.ylabel("Przesunięcie fazowe (°)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()