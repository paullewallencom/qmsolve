import pytest
from qmsolve.visualization import Visualization, init_visualization
from unittest.mock import MagicMock


def test_imports():
    assert Visualization is not None
    assert callable(init_visualization)


def test_init_visualization():
    eigenstates_mock = MagicMock()
    eigenstates_mock.type = "SingleParticle3D"
    vis_instance = init_visualization(eigenstates_mock)
    assert vis_instance is not None
    assert isinstance(vis_instance, Visualization)
