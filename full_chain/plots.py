from locale import normalize
import pathlib
import uproot
import numpy as np
import matplotlib.pyplot as plt

inputDir = pathlib.Path(__file__).parent / 'odd_output'
plotsDir = pathlib.Path(__file__).parent / 'plots'

plotsDir.mkdir(parents=True, exist_ok=True)

particles = uproot.open(inputDir / 'particles.root')
particles = particles['particles']
particles = particles.arrays(library='pd')

plt.scatter(particles['eta'], np.linalg.norm(particles[['px', 'py', 'pz']], axis=-1))
plt.xlabel(r'$\eta$')
plt.ylabel(r'$p$ [GeV]')
plt.savefig(plotsDir / 'gun.pdf', bbox_inches='tight')
plt.clf()

hits = uproot.open(inputDir / 'hits.root')
hits = hits['hits']
hits = hits.arrays(library='pd')

plt.scatter(hits['tx'], hits['ty'], s=0.1)
plt.xlabel(r'$x [mm]$')
plt.ylabel(r'$y [mm]$')
plt.savefig(plotsDir / 'hits_xy.pdf', bbox_inches='tight')
plt.clf()

plt.scatter(hits['tz'], np.linalg.norm(hits[['tx', 'ty']], axis=-1), s=0.1)
plt.xlabel(r'$z [mm]$')
plt.ylabel(r'$r [mm]$')
plt.savefig(plotsDir / 'hits_zr.pdf', bbox_inches='tight')
plt.clf()

vertices = uproot.open(inputDir / 'performance_vertexing.root')
vertices = vertices['vertexing']
vertices = vertices.arrays(library='pd')

plt.hist(vertices['recoZ'], bins=11, range=(-400, 400), density=True, lw=1)
plt.xlabel(r'$z [mm]$')
plt.savefig(plotsDir / 'vertices_z.pdf', bbox_inches='tight')
plt.clf()
