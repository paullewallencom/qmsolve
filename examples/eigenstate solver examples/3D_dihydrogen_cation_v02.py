import numpy as np
from qmsolve import Hamiltonian, SingleParticle, init_visualization, Å

# Interaction potential
def di_coulomb_potential(particle):
    k_c = 1  # (e*e / (4 * np.pi * epsilon_0))
    R = 1.06 * Å

    r1 = np.sqrt((particle.x - R / 2) ** 2 + (particle.y) ** 2 + (particle.z) ** 2)
    r1 = np.maximum(r1, 0.0001)  # Avoid division by zero

    r2 = np.sqrt((particle.x + R / 2) ** 2 + (particle.y) ** 2 + (particle.z) ** 2)
    r2 = np.maximum(r2, 0.0001)

    return -k_c / r1 - k_c / r2 + k_c / R

# Create Hamiltonian
H = Hamiltonian(
    particles=SingleParticle(),
    potential=di_coulomb_potential,
    spatial_ndim=3,
    N=50,  # Keeping original grid size
    extent=9 * Å,
)

# Solve eigenstates
print("Computing...")
eigenstates = H.solve(max_states=5, method='lobpcg')
print("Eigenvalues:", eigenstates.energies)

# Initialize visualization
visualization = init_visualization(eigenstates)

# --- 🔹 Corrected Optimization: Disable Rendering Before Plotting ---
visualization.figure.scene.disable_render = True  # ✅ Corrected!

# Plot the first eigenstate
visualization.plot_eigenstate(0, contrast_vals=[0.01, 0.761])

# Re-enable rendering after setup
visualization.figure.scene.disable_render = False  # ✅ Corrected!

# Animate the visualization
visualization.animate(contrast_vals=[0.01, 0.761])
