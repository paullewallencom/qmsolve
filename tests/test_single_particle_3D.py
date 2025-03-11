import pytest
from qmsolve.visualization.single_particle_3D import VisualizationSingleParticle3D
from qmsolve.eigenstates import Eigenstates  # Mock eigenstates if needed
import numpy as np

@pytest.fixture
def mock_eigenstates():
    """Create a mock eigenstates object for testing."""
    class MockEigenstates:
        def __init__(self):
            self.type = "SingleParticle3D"
            self.array = np.random.rand(5, 10, 10, 10)  # Fake eigenstates array
            self.extent = 10
            self.N = 10
            self.energies = np.array([-15.32, -3.39, 2.22, 2.22, 4.08])

    return MockEigenstates()

@pytest.fixture
def visualization(mock_eigenstates):
    """Initialize the VisualizationSingleParticle3D instance."""
    return VisualizationSingleParticle3D(mock_eigenstates)

def test_class_initialization(visualization):
    """Test if the class initializes correctly."""
    assert isinstance(visualization, VisualizationSingleParticle3D)

def test_scene_exposure(visualization):
    """Test that scene is set after plotting."""
    visualization.plot_eigenstate(0)
    assert visualization.scene is not None  # Ensure scene is accessible

def test_plot_eigenstate(visualization):
    """Test that eigenstate plotting runs without errors."""
    try:
        visualization.plot_eigenstate(0)
    except Exception as e:
        pytest.fail(f"plot_eigenstate() failed with error: {e}")

def test_animate(visualization):
    """Test that animation runs without crashing."""
    try:
        visualization.animate()
    except Exception as e:
        pytest.fail(f"animate() failed with error: {e}")

def test_scene_disable_render(visualization):
    """Test that scene.disable_render can be toggled."""
    visualization.plot_eigenstate(0)  # Ensure scene exists
    assert hasattr(visualization.scene, "disable_render")
    visualization.scene.disable_render = True
    assert visualization.scene.disable_render is True
    visualization.scene.disable_render = False
    assert visualization.scene.disable_render is False

if __name__ == "__main__":
    pytest.main()
