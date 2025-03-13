import pytest
import qmsolve


def test_imports():
    """Test that qmsolve package imports correctly."""
    assert hasattr(qmsolve, "Hamiltonian")
    assert hasattr(qmsolve, "Eigenstates")
    assert hasattr(qmsolve, "VisualizationSingleParticle1D")
    assert hasattr(qmsolve, "VisualizationSingleParticle2D")
    assert hasattr(qmsolve, "VisualizationIdenticalParticles1D")

@pytest.mark.parametrize("attr", qmsolve.__all__)
def test_all_attributes_exist(attr):
    """Ensure all items in __all__ are present in qmsolve."""
    assert hasattr(qmsolve, attr)
