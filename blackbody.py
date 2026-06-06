import numpy as np
import matplotlib.pyplot as plt

# Physical constants
h = 6.62607015e-34      # Planck constant, J s
c = 2.99792458e8        # Speed of light, m/s
k_B = 1.380649e-23      # Boltzmann constant, J/K
b = 2.897771955e-3      # Wien's displacement constant, m K


def planck_law(wavelength, temperature):
    """
    Spectral radiance of a black body using Planck's law.
    """
    numerator = 2 * h * c**2
    exponent = h * c / (wavelength * k_B * temperature)
    denominator = wavelength**5 * (np.exp(exponent) - 1)

    return numerator / denominator


def rayleigh_jeans_law(wavelength, temperature):
    """
    Classical prediction for black body radiation using the Rayleigh-Jeans law.
    """
    return (2 * c * k_B * temperature) / wavelength**4


# Wavelength range: 100 nm to 2000 nm
wavelengths = np.linspace(100e-9, 2000e-9, 2000)
wavelengths_nm = wavelengths * 1e9

# Temperatures to plot, in Kelvin
temperatures = [3000, 4000, 5000, 6000]

plt.figure(figsize=(10, 6))

for T in temperatures:
    # Planck blackbody curve
    intensity = planck_law(wavelengths, T)
    plt.plot(wavelengths_nm, intensity, label=f"{T} K Planck")

    # Only show the 6000 K classical prediction
    if T == 6000:
        rj_intensity = rayleigh_jeans_law(wavelengths, T)
        plt.plot(
            wavelengths_nm,
            rj_intensity,
            linestyle=":",
            label="6000 K classical prediction"
        )

    # Wien's law: peak wavelength
    peak_wavelength = b / T
    peak_wavelength_nm = peak_wavelength * 1e9
    peak_intensity = planck_law(peak_wavelength, T)

    # Mark the peak
    plt.scatter(peak_wavelength_nm, peak_intensity)
    plt.text(
        peak_wavelength_nm,
        peak_intensity,
        f"  {peak_wavelength_nm:.0f} nm",
        fontsize=9
    )

plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral radiance")
plt.title("Blackbody Emission Curves with 6000 K Classical Prediction")
plt.legend(title="Temperature")
plt.grid(True)

# Axis limits
plt.xlim(0, 2000)
plt.ylim(0, 4e13)

plt.tight_layout()
plt.show()