import numpy as np
import sys, os

# Get path to mcdc (not necessary if mcdc is installed)
sys.path.append('../../../')

import mcdc

# =============================================================================
# Set materials
# =============================================================================

M1 = mcdc.Material(capture=np.array([0.1]), scatter=np.array([[0.9]]))
M2 = mcdc.Material(capture=np.array([0.5]), scatter=np.array([[0.5]]))

# =============================================================================
# Set cells
# =============================================================================

# Set surfaces
S0 = mcdc.SurfacePlaneX(0.0, "vacuum")
S1 = mcdc.MovingSurfacePlaneX(10.0, -0.15, "transmission")
S2 = mcdc.SurfacePlaneX(11.0, "vacuum")

# Set cells
C1 = mcdc.Cell([+S0, -S1], M1)
C2 = mcdc.Cell([+S1, -S2], M2)
cells = [C1, C2]

# =============================================================================
# Set source
# =============================================================================

# Position distribution
pos = mcdc.DistPoint(mcdc.DistUniform(0.0,10.0), mcdc.DistDelta(0.0), 
                             mcdc.DistDelta(0.0))
# Direction distribution
dir = mcdc.DistPointIsotropic()

# Energy group distribution
g = mcdc.DistDelta(0)

# Time distribution
time= mcdc.DistUniform(0.0, 40.0)

# Create the source
Src = mcdc.SourceSimple(pos,dir,g,time)
sources = [Src]

# =============================================================================
# Set filters and tallies
# =============================================================================

spatial_filter = mcdc.FilterPlaneX(np.linspace(0.0, 11.0, 111))
time_filter = mcdc.FilterTime(np.linspace(0.0, 40.0, 41))

T = mcdc.Tally('tally', scores=['flux-edge'], 
               spatial_filter=spatial_filter, time_filter=time_filter)

tallies = [T]

# =============================================================================
# Set and run simulator
# =============================================================================

# Set simulator
simulator = mcdc.Simulator(cells=cells, sources=sources, tallies=tallies, 
                           N_hist=1E5, speed=np.array([1.0]))

# Run
simulator.run()
