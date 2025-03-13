# qmsolve/particle_system/__init__.py

def get_particle_system():
    from .particle_system import ParticleSystem  # Delayed import
    return ParticleSystem


def get_single_particle():
    from .single_particle import SingleParticle
    return SingleParticle


def get_two_bosons():
    from .two_bosons import TwoBosons
    return TwoBosons


def get_two_particles():
    from .two_particles import TwoParticles
    return TwoParticles
