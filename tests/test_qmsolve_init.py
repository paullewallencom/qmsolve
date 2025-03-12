import pytest
import qmsolve

def test_imports():
    """Test that all required modules can be accessed via qmsolve."""
    assert hasattr(qmsolve, "Hamiltonian")
    assert hasattr(qmsolve, "Eigenstates")
    assert hasattr(qmsolve, "SingleParticle")
    assert hasattr(qmsolve, "TwoFermions")
    assert hasattr(qmsolve, "TwoBosons")
    assert hasattr(qmsolve, "TwoDistinguishableParticles")
    assert hasattr(qmsolve, "save_eigenstates")
    assert hasattr(qmsolve, "load_eigenstates")
    assert hasattr(qmsolve, "init_visualization")
    assert hasattr(qmsolve, "TimeSimulation")

@pytest.mark.parametrize("attr", qmsolve.__all__)
def test_all_attributes_exist(attr):
    """Ensure all items in __all__ are present in qmsolve."""
    assert hasattr(qmsolve, attr)
