# qmsolve/__init__.py

from .hamiltonian import Hamiltonian
from .eigenstates import Eigenstates
from .time_dependent_solver import crank_nicolson
from .visualization import (
    VisualizationSingleParticle1D,
    VisualizationSingleParticle2D,
    VisualizationIdenticalParticles1D,
    TimeVisualizationTwoIdenticalParticles1D,
    ComplexSliderWidget
)

__all__ = [
    "Hamiltonian",
    "Eigenstates",
    "crank_nicolson",
    "VisualizationSingleParticle1D",
    "VisualizationSingleParticle2D",
    "VisualizationIdenticalParticles1D",
    "TimeVisualizationTwoIdenticalParticles1D",
    "ComplexSliderWidget",
]
