import numpy as np
from scipy.sparse import diags
import time


class Hamiltonian:
    def __init__(self, particles, potential, N, extent, spatial_ndim, potential_type="grid"):
        """
        Initializes the Hamiltonian for quantum simulations.

        Args:
            particles: A particle system providing kinetic and potential energy operators.
            potential: A function defining the potential energy.
            N: Number of grid points per dimension.
            extent: Spatial extent in atomic units.
            spatial_ndim: Number of spatial dimensions.
            potential_type: "grid" or "matrix" representation.
        """

        self.N = N
        self.extent = extent
        self.spatial_ndim = spatial_ndim
        self.potential_type = potential_type
        self.particle_system = particles  # Ensure the particle system is assigned
        self.potential = potential  # Ensure potential function is assigned

        self.Vgrid = np.zeros(N)  # Ensure Vgrid exists to prevent AttributeError
        self.V = self.get_potential_matrix()
        self.T = self.get_kinetic_matrix()

    def get_kinetic_matrix(self):
        """
        Retrieves the kinetic energy matrix from the particle system.

        Returns:
            Sparse kinetic energy matrix.
        """
        if not hasattr(self.particle_system, 'get_kinetic_matrix'):
            raise AttributeError("Particle system must define 'get_kinetic_matrix' method.")
        return self.particle_system.get_kinetic_matrix(self)

    def get_potential_matrix(self):
        """
        Computes the potential energy matrix.

        Returns:
            Sparse diagonal potential matrix.
        """
        if self.potential is None:
            return diags([np.zeros(self.N)], [0])  # Ensure correct shape

        V = self.potential(self.particle_system)

        # Ensure potential is reshaped correctly before conversion
        expected_size = self.N
        if V.size != expected_size:
            raise ValueError(f"Potential shape {V.shape} does not match expected size {expected_size}.")

        return diags([V], [0])  # Corrected shape for sparse matrix

    def solve(self, max_states=5, method="eigsh", verbose=False):
        """
        Solves the Hamiltonian for eigenstates using the specified method.

        Args:
            max_states: Number of eigenstates to compute.
            method: Solver method ("eigsh" or "lobpcg").
            verbose: Whether to print execution time.

        Returns:
            Eigenvalues and eigenvectors.
        """
        from scipy.sparse.linalg import eigsh, lobpcg

        H = self.T + self.V
        if verbose:
            print("Computing...")

        t0 = time.time()

        if method == "eigsh":
            eigenvalues, eigenvectors = eigsh(H, k=max_states, which='LM')

        elif method == "lobpcg":
            eigenvectors_guess = np.random.rand(H.shape[0], max_states)
            eigenvalues, eigenvectors = lobpcg(H, eigenvectors_guess, largest=False)

        else:
            raise ValueError(f"Invalid solver method: {method}")

        if verbose:
            print(f"Solved in {time.time() - t0:.2f} seconds")

        return eigenvalues, eigenvectors
