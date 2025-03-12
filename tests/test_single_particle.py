import pytest
import numpy as np
from qmsolve.particle_system.single_particle import SingleParticle
from qmsolve.particle_system.particle_system import ParticleSystem

@pytest.fixture
def test_particle():
    """Fixture to create a test single particle instance."""
    return SingleParticle(mass=1.0, spin=0.5)

def test_particle_initialization(test_particle):
    """Test that particle initializes correctly."""
    assert test_particle.mass == 1.0
    assert test_particle.spin == 0.5

def test_get_observables_1d(test_particle):
    """Test observables for a 1D Hamiltonian."""
    class MockHamiltonian:
        spatial_ndim = 1
        extent = 10.0
        N = 5

    test_particle.get_observables(MockHamiltonian())
    assert len(test_particle.x) == 5

def test_get_kinetic_matrix():
    """Test kinetic energy matrix generation."""
    class MockHamiltonian:
        spatial_ndim = 1
        extent = 10.0
        N = 5
        dx = 2.0

    particle = SingleParticle(mass=1.0)
    T = particle.get_kinetic_matrix(MockHamiltonian())
    assert T.shape == (5, 5)
