import pytest
from qmsolve.visualization import VisualizationClass  # Replace with actual class

@pytest.fixture
def visualization():
    return VisualizationClass()

def test_visualization_instance(visualization):
    assert visualization is not None
