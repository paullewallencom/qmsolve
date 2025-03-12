import pytest
import numpy as np
from qmsolve.particle_system.particle_system import ParticleSystem

@pytest.fixture
def particle_system():
    return ParticleSystem()

def test_add_particle(particle_system):
    particle_system.add_particle(1.0, -1.0, [0, 0, 0])
    assert particle_system.get_particle_count() == 1

def test_get_total_mass(particle_system):
    particle_system.add_particle(1.0, -1.0, [0, 0, 0])
    particle_system.add_particle(2.0, 1.0, [1, 1, 1])
    assert particle_system.get_total_mass() == 3.0

def test_apply_force(particle_system):
    particle_system.add_particle(1.0, -1.0, [0, 0, 0])
    particle_system.apply_force(0, np.array([1, 1, 1]))
    assert np.all(particle_system.particles[0]["position"] == np.array([1, 1, 1]))
