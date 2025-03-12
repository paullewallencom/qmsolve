import pytest
import visualization

def test_imports():
    """Test that Visualization and init_visualization can be accessed via visualization."""
    assert hasattr(visualization, "Visualization")
    assert hasattr(visualization, "init_visualization")
