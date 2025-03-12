import numpy as np
from scipy.sparse import diags
import time


class Hamiltonian:
    def __init__(self, particles, potential, N, extent, spatial_ndim, potential_type="grid", E_min=0):
        """
        Initializes the Hamiltonian for quantum simulations.

        Args:
            particles: A particle system providing kinetic and potential energy operators.
            potential: A function defining the potential energy.
            N: Number of grid points per dimension.
            extent: Spatial extent in atomic units.
            spatial_ndim: Number of spatial dimensions.
            potential_type: "grid" or "matrix" representation.
            E_min: Minimum energy guess for certain solvers.
        """

        self.N = N
        self.extent = extent
        self.dx = extent / N
        self.particle_system = particles
        self.spatial_ndim = spatial_ndim
        self.potential = potential
        self.potential_type = potential_type
        self.E_min = E_min

        self.T = self.get_kinetic_matrix()
        self.V = self.get_potential_matrix()

    def get_kinetic_matrix(self):
        """
        Retrieves the kinetic energy matrix from the particle system.

        Returns:
            Sparse kinetic energy matrix.
        """
        return self.particle_system.get_kinetic_matrix(self)

    def get_potential_matrix(self):
        """
        Computes the potential energy matrix.

        Returns:
            Sparse diagonal potential matrix.
        """
        if self.potential is None:
            return diags([np.zeros(self.N ** self.spatial_ndim)], [0])

        V = self.potential(self.particle_system)
        
        # Ensure potential is reshaped correctly before conversion
        expected_size = self.N ** self.spatial_ndim
        if V.size != expected_size:
            raise ValueError(f"Potential shape {V.shape} does not match expected size {expected_size}.")

        return diags([V.reshape(expected_size)], [0])

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
            eigenvalues, eigenvectors = eigsh(H, k=max_states, which='LM', sigma=self.E_min)

        elif method == "lobpcg":
            eigenvectors_guess = np.random.rand(H.shape[0], max_states)
            eigenvalues, eigenvectors = lobpcg(H, eigenvectors_guess, largest=False)

        else:
            raise ValueError(f"Invalid solver method: {method}")

        if verbose:
            print(f"Solved in {time.time() - t0:.2f} seconds")

        return eigenvalues, eigenvectors
