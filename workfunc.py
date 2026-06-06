import numpy as np
import matplotlib

# Headless server fix
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

# 1. Define Physical Constants
h = 4.136e-15  # Planck's constant in eV*s
phi = 2.27     # Work function in eV (Sodium)
f_0 = phi / h  # Threshold frequency (Hz)

# 2. Generate Frequency Data (Starting from 0)
frequencies = np.linspace(0, 1.5e15, 1000)

# Full linear equation (K = hf - phi) to allow negative values
k_quantum_full = h * frequencies - phi

# 3. Setting up the Portrait Plot
plt.figure(figsize=(6, 9)) # Portrait aspect ratio (Width=6, Height=9)

# Plot the real, physical quantum emission (above threshold)
physical_mask = frequencies >= f_0
plt.plot(frequencies[physical_mask], k_quantum_full[physical_mask], 
         label="Physical Emission ($K_{max} \geq 0$)", color="#1f77b4", linewidth=2.5)

# Plot the negative mathematical extrapolation (below threshold to y-intercept)
extrapolation_mask = frequencies <= f_0
plt.plot(frequencies[extrapolation_mask], k_quantum_full[extrapolation_mask], 
         label="Extrapolation to $-\\Phi$", color="#1f77b4", linestyle=":", linewidth=2)

# 4. Creating the "Slight Border" and Internal Axes
# Clean x=0 and y=0 reference crosshairs inside the plot
plt.axhline(0, color='black', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='black', linewidth=0.8, alpha=0.5)

# Highlight the Threshold Frequency
plt.axvline(x=f_0, color='gray', linestyle='--', alpha=0.5, label=f'Threshold ($f_0 = {f_0:.2e}$ Hz)')

# Explicitly mark and label the Y-Intercept point (0, -phi)
plt.plot(0, -phi, 'ko', markersize=6)
plt.text(0.04e15, -phi, f'$-\\Phi = -{phi}$ eV', va='center', ha='left', color='black', fontweight='bold')

# 5. Framing and Padding (The Border effect)
# Small negative offsets give the axes and y-intercept breathing room from the outer frame
plt.xlim(-0.15e15, 1.5e15) 
plt.ylim(-3.0, 4.5)        

# 6. Labels and Polish
plt.title("Photoelectric Effect: $K_{max}$ vs. Freq", fontsize=11, fontweight='bold', pad=15)
plt.xlabel("Frequency (Hz)", fontsize=11)
plt.ylabel("Maximum Kinetic Energy (eV)", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.4)
plt.legend(fontsize=9, loc="upper left")

plt.tight_layout()

# Save the clean portrait image with negatives
plt.savefig("photoelectric_negatives.png", dpi=300)
print("Portrait plot with negatives successfully saved to 'photoelectric_negatives.png'")