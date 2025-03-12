import numpy as np
from scipy.sparse import diags, kron, eye
from .particle_system import ParticleSystem
from ..util.constants import hbar, m_e
from ..eigenstates import Eigenstates

class SingleParticle(ParticleSystem):
    """Represents a single particle with mass and spin properties."""

    def __init__(self, mass=m_e, spin=None):
        """
        Initialize a single particle.

        Args:
            mass (float): Mass of the particle.
            spin (optional): Spin of the particle.
        """
        super().__init__()
        self.mass = mass
        self.spin = spin

    def get_observables(self, H):
        """Compute spatial observables for different dimensions."""
        extent_half = H.extent / 2
        N = H.N

        if H.spatial_ndim == 1:
            self.x = np.linspace(-extent_half, extent_half, N)
            H.ndim = 1

        elif H.spatial_ndim == 2:
            x = np.linspace(-extent_half, extent_half, N)
            y = np.linspace(-extent_half, extent_half, N)
            self.x, self.y = np.meshgrid(x, y)
            H.ndim = 2

        elif H.spatial_ndim == 3:
            self.x, self.y, self.z = np.mgrid[
                -extent_half:extent_half:N * 1j,
                -extent_half:extent_half:N * 1j,
                -extent_half:extent_half:N * 1j,
            ]
            H.ndim = 3

    def compute_momentum_space(self, H):
        """Compute momentum space representation for split-step methods."""
        k_values = np.fft.fftshift(np.fft.fftfreq(H.N, d=H.dx)) * hbar * 2 * np.pi

        if H.spatial_ndim == 1:
            self.px = k_values
            self.p2 = self.px**2

        elif H.spatial_ndim == 2:
            px, py = np.meshgrid(k_values, k_values)
            self.p2 = px**2 + py**2

        elif H.spatial_ndim == 3:
            raise NotImplementedError("Split-step method is not implemented for 3D.")

    def get_kinetic_matrix(self, H):
        """Construct the kinetic energy matrix."""
        I = eye(H.N)
        T_diag = diags([-2.0, 1.0, 1.0], [0, -1, 1], shape=(H.N, H.N)) * -hbar**2 / (
            2 * self.mass * H.dx**2
        )

        if H.spatial_ndim == 1:
            return T_diag

        elif H.spatial_ndim == 2:
            return kron(T_diag, I) + kron(I, T_diag)

        elif H.spatial_ndim == 3:
            return kron(T_diag, kron(I, I)) + kron(I, kron(T_diag, I)) + kron(I, kron(I, T_diag))

    def get_eigenstates(self, H, max_states, eigenvalues, eigenvectors):
        """Generate Eigenstates object from computed eigenvalues and eigenvectors."""
        energies = eigenvalues
        eigenstates_array = np.moveaxis(
            eigenvectors.reshape(*[H.N] * H.ndim, max_states), -1, 0
        )
        eigenstates_array /= np.sqrt(H.dx ** H.ndim)

        types = {1: "SingleParticle1D", 2: "SingleParticle2D", 3: "SingleParticle3D"}
        eigen_type = types.get(H.spatial_ndim, "Unknown")

        return Eigenstates(energies, eigenstates_array, H.extent, H.N, eigen_type)
