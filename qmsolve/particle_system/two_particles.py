import numpy as np
from scipy.sparse import diags, kron, eye
from .particle_system import ParticleSystem
from ..util.constants import *
from abc import ABC, abstractmethod


class TwoParticles(ParticleSystem, ABC):
    def __init__(self, m=m_e, spin=None):
        """
        Initializes the TwoParticles system.

        Args:
            m (float): Mass of each particle.
            spin (optional): Spin state of the particles.
        """
        self.m = m
        self.spin = spin

    def get_observables(self, H):
        """
        Computes observable grids based on Hamiltonian properties.

        Args:
            H (object): Hamiltonian containing spatial and extent information.
        """
        if not hasattr(H, "spatial_ndim") or not hasattr(H, "extent") or not hasattr(H, "N"):
            raise AttributeError("Hamiltonian object must have 'spatial_ndim', 'extent', and 'N' attributes.")

        if H.spatial_ndim == 1:
            x1 = np.linspace(-H.extent / 2, H.extent / 2, H.N)
            x2 = np.linspace(-H.extent / 2, H.extent / 2, H.N)
            self.x1, self.x2 = np.meshgrid(x1, x2)
            H.ndim = 2

        elif H.spatial_ndim == 2:
            x1 = np.linspace(-H.extent / 2, H.extent / 2, H.N)
            y1 = np.linspace(-H.extent / 2, H.extent / 2, H.N)
            x2 = np.linspace(-H.extent / 2, H.extent / 2, H.N)
            y2 = np.linspace(-H.extent / 2, H.extent / 2, H.N)
            self.x1, self.y1, self.x2, self.y2 = np.meshgrid(x1, y1, x2, y2)
            H.ndim = 4
        else:
            raise NotImplementedError("Only 1D and 2D two-particle systems are supported.")

    def compute_momentum_space(self, H):
        """
        Computes momentum space representation.

        Args:
            H (object): Hamiltonian containing spatial information.
        """
        if not hasattr(H, "spatial_ndim") or not hasattr(H, "N") or not hasattr(H, "dx"):
            raise AttributeError("Hamiltonian must have 'spatial_ndim', 'N', and 'dx' attributes.")

        if H.spatial_ndim == 1:
            p1 = np.fft.fftshift(np.fft.fftfreq(H.N, d=H.dx)) * hbar * 2 * np.pi
            p2 = np.fft.fftshift(np.fft.fftfreq(H.N, d=H.dx)) * hbar * 2 * np.pi
            self.p1, self.p2 = np.meshgrid(p1, p2)
            self.p_squared = self.p1**2 + self.p2**2

        elif H.spatial_ndim == 2:
            raise NotImplementedError("Momentum space representation is not implemented for 2D two-particle systems.")

    def get_kinetic_matrix(self, H):
        """
        Computes the kinetic energy matrix.

        Args:
            H (object): Hamiltonian containing spatial and grid properties.

        Returns:
            scipy.sparse matrix: Kinetic energy matrix.
        """
        if not hasattr(H, "spatial_ndim") or not hasattr(H, "N") or not hasattr(H, "dx"):
            raise AttributeError("Hamiltonian must have 'spatial_ndim', 'N', and 'dx' attributes.")

        I = eye(H.N)
        T_ = diags([-2.0, 1.0, 1.0], [0, -1, 1], shape=(H.N, H.N)) * -k / (self.m * H.dx**2)

        if H.spatial_ndim == 1:
            return kron(T_, I) + kron(I, T_)
        elif H.spatial_ndim == 2:
            return kron(T_, I, I, I) + kron(I, T_, I, I) + kron(I, I, T_, I) + kron(I, I, I, T_)
        else:
            raise NotImplementedError("Kinetic matrix is only implemented for 1D and 2D systems.")
