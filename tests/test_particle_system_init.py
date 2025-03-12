import pytest
import particle_system

def test_imports():
    """Test that all required modules can be accessed via particle_system."""
    assert hasattr(particle_system, "SingleParticle")
    assert hasattr(particle_system, "TwoParticles")
    assert hasattr(particle_system, "TwoFermions")
    assert hasattr(particle_system, "TwoBosons")
    assert hasattr(particle_system, "TwoDistinguishableParticles")

@pytest.mark.parametrize("attr", particle_system.__all__)
def test_all_attributes_exist(attr):
    """Ensure all items in __all__ are present in particle_system."""
    assert hasattr(particle_system, attr)
