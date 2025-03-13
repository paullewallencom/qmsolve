import pytest
from qmsolve.visualization import VisualizationSingleParticle3D
from unittest.mock import MagicMock

@pytest.fixture
def visualization():
    eigenstates_mock = MagicMock()
    eigenstates_mock.array = MagicMock()
    eigenstates_mock.extent = 10
    eigenstates_mock.N = 100
    eigenstates_mock.type = "SingleParticle3D"
    return VisualizationSingleParticle3D(eigenstates_mock)

def test_visualization_instance(visualization):
    assert visualization is not None
    assert isinstance(visualization, VisualizationSingleParticle3D)
