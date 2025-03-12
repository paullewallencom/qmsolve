import pytest
import qmsolve.particle_system as ps

def test_imports():
    """Test that all required modules can be accessed via particle_system."""
    assert hasattr(ps, "ParticleSystem")

@pytest.mark.parametrize("attr", ps.__all__)
def test_all_attributes_exist(attr):
    """Ensure all items in __all__ are present in particle_system."""
    assert hasattr(ps, attr)
