##########################################################################
############################2D WAVE SIMULATION############################
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the wave
A = 0.5                           # Amplitude of the wave
λ = 2 * np.pi                     # Wavelength
N = 5                             # No of Wavelets
L = N * (λ)                       # Length of the domain
n = 300                           # Number of grid points
φdφ = np.linspace(0,8*λ,n)          # Phase shift variable

#Resolution Limits
R = 10

# Create the grid for the domain
x = np.linspace(0, L, n)

# Compute the wave function values
for i in range(n):
    y = A * np.sin((2 * np.pi / λ) * x - φdφ[i])

    # Plot the wave
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=".")
    
    # Fill the area below the wave
    plt.fill_between(x, y, -R, color='blue', alpha=0.8)

    # Set x and y limits
    plt.xlim(0, L)
    plt.ylim(-R, R)

    # Add labels, title, legend, and grid
    plt.title("2D Wave simulation in a Domain")
    plt.xlabel("x")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(False)

    # Show the plot
    plt.show()
