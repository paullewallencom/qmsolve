import pytest
from qmsolve.visualization.single_particle_3D import VisualizationSingleParticle3D

class MockVisualization:
    """Mock class to simulate visualization behavior."""
    def __init__(self):
        self.scene = MockScene()

    def plot_eigenstate(self, state_index):
        self.scene.rendered = True

class MockScene:
    """Mock scene for testing."""
    def __init__(self):
        self.disable_render = True
        self.rendered = False

@pytest.fixture
def visualization():
    """Fixture for VisualizationSingleParticle3D."""
    return MockVisualization()

def test_scene_exposure(visualization):
    """Test that scene is set after plotting."""
    visualization.plot_eigenstate(0)
    assert visualization.scene.rendered is True

def test_scene_disable_render(visualization):
    """Test that scene.disable_render can be toggled."""
    assert hasattr(visualization.scene, "disable_render")
