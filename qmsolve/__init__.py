# qmsolve/__init__.py

from .hamiltonian import Hamiltonian
from .eigenstates import Eigenstates
from .time_dependent_solver import crank_nicolson
from . import visualization
from .visualization import (
    Visualization,
    TimeVisualization,
    VisualizationSingleParticle1D,
    VisualizationSingleParticle2D,
    VisualizationIdenticalParticles1D,
    TimeVisualizationTwoIdenticalParticles1D,
    ComplexSliderWidget,
)

__all__ = [
    "Hamiltonian",
    "Eigenstates",
    "crank_nicolson",
    "visualization",
    "Visualization",
    "TimeVisualization",
    "VisualizationSingleParticle1D",
    "VisualizationSingleParticle2D",
    "VisualizationIdenticalParticles1D",
    "TimeVisualizationTwoIdenticalParticles1D",
    "ComplexSliderWidget",
]
